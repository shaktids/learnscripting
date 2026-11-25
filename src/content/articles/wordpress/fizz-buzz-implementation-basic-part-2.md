---
title: "Fizz Buzz Implementation Basic Part 2"
description: "The most common examples seen in imperative languages try to “tell” the machine what to do; something like: I don’t know about you, but I’m really annoyed…"
lang: other
categories: ["Questions"]
author: "Shakti Das"
pubDate: 2021-01-18T11:41:05Z
legacy: true
wpId: 2139
---

The most common examples seen in imperative languages try to “tell” the machine what to do; something like:

```
std::string fizzbuzz(int n)
{
    if(n%3 == 0 && n%5 == 0)
        return "FizzBuzz";
    else if (n%3 == 0)
        return "Fizz";
    else if (n%5 == 0)
        return "Buzz";
    else
        return std::to_string(n);
}
```

I don’t know about you, but I’m really annoyed at the implementation because you have to define the predicates for Fizz and Buzz twice. So you might output the string directly so you have control of the new line and then you can do this:

```
void fizzbuzz(int n)
{
    bool shouldPrintN = true;
    if (n%3 == 0)
    {
        std::cout << "Fizz";
        shouldPrintN = false;
    }
    if (n%5 == 0)
    {
        std::cout << "Buzz";
        shouldPrintN = false;
    }
    if(shouldPrintN)
        std::cout << n;

    std::cout << '\n';
}
```

But now we have a silly boolean in our code. This isn’t elegant! There must be a better way. Let’s look at how FizzBuzz can be done in a functional language and see if we can glean some ideas from it.

### Fizzbuzz in Haskell

Looking back at the original tweet, we can see that it captures some details in code that we’re just not capturing with our C-style way of coding up the problem. So if we take a step back, what exactly does each line in a FizzBuzz statement contain? In pseudo code it might be something like the following:

```
(Maybe "Fizz" +  Maybe "Buzz") or n
```

The “Maybe” here is an abstraction that allows 2 things.

- 1) It allows combining two “Maybe’s” together even when one of them might not be there and
- 2) If a “Maybe” doesn’t contain a value you can give a default

In Haskell, this exact abstraction exists. It’s even called Maybe. A “Maybe” can be constructed with a constructor called “Just” if it contains a value or “Nothing” if it doesn’t. So the proper code would look something like this:

```
fromMaybe (show n) (Just "Fizz" <> Just "Buzz")
```

`from Maybe` will return whatever value is in the `Maybe` (given as the second param) or will default to the first parameter if it’s a `Nothing`. `show` converts a variable to a string. `<>` is a binary operator that can combine two s so long as the value they contain can also be combined. In this example they can because strings can be concatenated!

Now that we have the basic abstraction down, we just need a way to create “Fizz” or “Buzz” inside the statement based on the value of `n`. We can call those functions `maybeFizz` and `maybeBuzz`.

```
fromMaybe (show n) (maybeFizz <> maybeBuzz) -- (actually implementing maybeFizz and maybeBuzz is left as an exercise for the reader)
```

### Back to our C++ Fizzbuzz

Wait! I hear you saying. I’m not a Haskell programmer. I need something I can use in C++. Well in C++ this is [optional](https://en.cppreference.com/w/cpp/utility/optional).

```
(maybeFizz() + maybeBuzz()).value_or(std::to_string(n));
```

The `value_or` function provides the same mechanism that `fromMaybe` did in Haskell. From our list of needs above, this is number 2. Sadly, the first item in the list, the ability to combine two `Maybe`s doesn’t exist in `std::optional`, so we have to write it ourselves.

While it’s unusual to overload operators for standard types, in this case I think it’s warranted since it’s a concept that other languages have and could have applications in other code bases.

```
template<class T>
std::optional<T> operator+(std::optional<T> first, std::optional<T> second)
{
    if(first)
        if(second)
            return std::make_optional(first.value() + second.value());
        else
            return first;
    else
        return second;
}
```

As a templated function, this allows us to combine any two `optional`s so long as the value inside it has an `operator+` defined for it. If not you’ll get an error like the following:

```
struct Foo {};
auto foo1 = std::make_optional<Foo>();
auto foo2 = std::make_optional<Foo>();
auto foo3 = foo1 + foo2;
```

```
error: no match for 'operator+' (operand types are 'Foo' and 'Foo')
    return std::make_optional(first.value() + second.value());
```

If we provide this as a helper method somewhere in our project, it might not be obvious why it’s failing.

In abstract algebra, an object that has a binary operator is called a [Magma](https://en.wikipedia.org/wiki/Magma_(algebra))and we can make this requirement explicit using C++20 Concepts.

#### Naming the concept

```
template<typename T>
concept Magma = requires(T a)
{
    { a + a } -> T; // a binary operator that returns the same Type
    // define operator+ for your Type if you get an error here
};

template<Magma T>
std::optional<T> operator+(std::optional<T> first, std::optional<T> second)
```

Compiling with `-c++=2a` and `-fconcepts` we still get some diagnostics about operator+, but we also get a new one:

```
note:   constraints not satisfied
note: within 'template<class T> concept const bool Magma<T> [with T = Foo]'
14 | concept Magma= requires(T a)
|         ^~~~~~~~~
note: with 'Foo a'
note: the required expression '(a + a)' would be ill-formed
```

It may still be a little confusing if you’re not familiar with concepts, but it at least gives you a chance to write some comments in the code that can give better direction to the user.

#### Coding up Fizzbuzz

Now that we have both requirements we can code up our maybeFizz and maybeBuzz implementations.

```
std::string fizzBuzzOrNumber(int n)
{
    auto maybeFizz = [n]() {
        return (n % 3) == 0 ? std::make_optional("Fizz"s) : std::nullopt;
    };
    auto maybeBuzz = [n]() {
        return (n % 5) == 0 ? std::make_optional("Buzz"s) : std::nullopt;
    };
    return (maybeFizz() + maybeBuzz()).value_or(std::to_string(n));
}
```

Since these functions take no arguments we can just use the return value directly and treat them as variables.

```
std::string fizzBuzzOrNumber(int n)
{
    auto maybeFizz = (n % 3) == 0 ? std::make_optional("Fizz"s) : std::nullopt;
    auto maybeBuzz = (n % 5) == 0 ? std::make_optional("Buzz"s) : std::nullopt;
    return (maybeFizz + maybeBuzz).value_or(std::to_string(n));
}
```

There’s still some code duplication we can get rid of if we want to be super concise, but it’s perhaps not as understandable

```
std::string fizzBuzzOrNumber(int n)
{
    auto ifFactor= [n](int divisor, std::string s) {
        return (n % divisor) == 0 ? std::make_optional(s) : std::nullopt;
    };
    auto maybeFizz = ifFactor (3, "Fizz");
    auto maybeBuzz = ifFactor(5, "Buzz");
    return (maybeFizz + maybeBuzz).value_or(std::to_string(n));
}
```

I’ve kept the helper function as a lamba since it really only make sense inside the fizzbuzz function and doesn’t belong in a higher scope.

The goal (I believe) for every program is to try to capture the basic abstraction of the problem you’re working on. By using optional and writing a little helper function we end up pretty close to our original pseudocode.

The last line of our function precisely describes the algorithm that we wanted to create. While this code (and the code in the original tweet) might be less readable to some, I think this is because we aren’t used to capturing the essence of the problem in code and instead focus on “telling” the machine what to do.

What do you think about this Fizzbuzz implementation with `optional`?
