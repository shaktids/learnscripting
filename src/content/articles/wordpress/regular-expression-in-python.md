---
title: "Regular Expression In Python"
description: "The module defines several functions, constants, and an exception. Some of the functions are simplified versions of the full featured methods for compiled…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2019-09-23T09:09:35Z
legacy: true
wpId: 951
---

The module defines several functions, constants, and an exception. Some of the functions are simplified versions of the full-featured methods for compiled regular expressions. Most non-trivial applications always use the compiled form.

### `re.compile`(*pattern*, *flags=0*)

Compile a regular expression pattern into a regular expression object, which can be used for matching using its [`match()`](https://docs.python.org/2/library/re.html#re.RegexObject.match) and [`search()`](https://docs.python.org/2/library/re.html#re.RegexObject.search) methods, described below.

The expression’s behavior can be modified by specifying a *flags* value. Values can be any of the following variables, combined using bitwise OR (the `|` operator).

The sequence

```
prog = re.compile(pattern)
result = prog.match(string)
```

is equivalent to

```
result = re.match(pattern, string)
```

but using [`re.compile()`](https://docs.python.org/2/library/re.html#re.compile) and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.

Note

The compiled versions of the most recent patterns passed to [`re.match()`](https://docs.python.org/2/library/re.html#re.match), [`re.search()`](https://docs.python.org/2/library/re.html#re.search) or [`re.compile()`](https://docs.python.org/2/library/re.html#re.compile) are cached, so programs that use only a few regular expressions at a time needn’t worry about compiling regular expressions.`re.``DEBUG`

Display debug information about compiled expression.`re.``I``re.``IGNORECASE`

Perform case-insensitive matching; expressions like `[A-Z]` will match lowercase letters, too. This is not affected by the current locale. To get this effect on non-ASCII Unicode characters such as `ü` and `Ü`, add the [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) flag.`re.``L``re.``LOCALE`

Make `\w`, `\W`, `\b`, `\B`, `\s` and `\S` dependent on the current locale.`re.``M``re.``MULTILINE`

When specified, the pattern character `'^'` matches at the beginning of the string and at the beginning of each line (immediately following each newline); and the pattern character `'$'` matches at the end of the string and at the end of each line (immediately preceding each newline). By default, `'^'` matches only at the beginning of the string, and `'$'` only at the end of the string and immediately before the newline (if any) at the end of the string.`re.``S``re.``DOTALL`

Make the `'.'` special character match any character at all, including a newline; without this flag, `'.'` will match anything *except* a newline.`re.``U``re.``UNICODE`

Make the `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s` and `\S` sequences dependent on the Unicode character properties database. Also enables non-ASCII matching for [`IGNORECASE`](https://docs.python.org/2/library/re.html#re.IGNORECASE).

*New in version 2.0.*`re.``X``re.``VERBOSE`

This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments. Whitespace within the pattern is ignored, except when in a character class, or when preceded by an unescaped backslash, or within tokens like `*?`, `(?:` or `(?P<...>`. When a line contains a `#` that is not in a character class and is not preceded by an unescaped backslash, all characters from the leftmost such `#` through the end of the line are ignored.

This means that the two following regular expression objects that match a decimal number are functionally equal:

```
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")
```

### `re.``search`(*pattern*, *string*, *flags=0*)

Scan through *string* looking for the first location where the regular expression *pattern* produces a match, and return a corresponding [`MatchObject`](https://docs.python.org/2/library/re.html#re.MatchObject) instance. Return `None` if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.

### `re.match`(*pattern*, *string*, *flags=0*)

If zero or more characters at the beginning of *string* match the regular expression *pattern*, return a corresponding [`MatchObject`](https://docs.python.org/2/library/re.html#re.MatchObject) instance. Return `None` if the string does not match the pattern; note that this is different from a zero-length match.

Note that even in [`MULTILINE`](https://docs.python.org/2/library/re.html#re.MULTILINE) mode, [`re.match()`](https://docs.python.org/2/library/re.html#re.match) will only match at the beginning of the string and not at the beginning of each line.

If you want to locate a match anywhere in *string*, use [`search()`](https://docs.python.org/2/library/re.html#re.search) instead (see also [search() vs. match()](https://docs.python.org/2/library/re.html#search-vs-match)).

### `re.split`(*pattern*, *string*, *maxsplit=0*, *flags=0*)

Split *string* by the occurrences of *pattern*. If capturing parentheses are used in *pattern*, then the text of all groups in the pattern are also returned as part of the resulting list. If *maxsplit* is nonzero, at most *maxsplit* splits occur, and the remainder of the string is returned as the final element of the list. (Incompatibility note: in the original Python 1.5 release, *maxsplit* was ignored. This has been fixed in later releases.)

```
>>> re.split('\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split('(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split('\W+', 'Words, words, words.', 1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']
```

If there are capturing groups in the separator and it matches at the start of the string, the result will start with an empty string. The same holds for the end of the string:

```
>>> re.split('(\W+)', '...words, words...')
['', '...', 'words', ', ', 'words', '...', '']
```

That way, separator components are always found at the same relative indices within the result list (e.g., if there’s one capturing group in the separator, the 0th, the 2nd and so forth).

Note that *split* will never split a string on an empty pattern match. For example:

```
>>> re.split('x*', 'foo')
['foo']
>>> re.split("(?m)^$", "foo\n\nbar\n")
['foo\n\nbar\n']
```

*Changed in version 2.7:*Added the optional flags argument.

### `re.findall`(*pattern*, *string*, *flags=0*)

Return all non-overlapping matches of *pattern* in *string*, as a list of strings. The *string* is scanned left-to-right, and matches are returned in the order found. If one or more groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group. Empty matches are included in the result.

Note

Due to the limitation of the current implementation the character following an empty match is not included in a next match, so `findall(r'^|\w+', 'two words')` returns `['', 'wo', 'words']` (note missed “t”). This is changed in Python 3.7.

*New in version 1.5.2.*

*Changed in version 2.4:*Added the optional flags argument.

### `re.finditer`(*pattern*, *string*, *flags=0*)

Return an [iterator](https://docs.python.org/2/glossary.html#term-iterator) yielding [`MatchObject`](https://docs.python.org/2/library/re.html#re.MatchObject) instances over all non-overlapping matches for the RE *pattern* in *string*. The *string* is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result. See also the note about [`findall()`](https://docs.python.org/2/library/re.html#re.findall).

*New in version 2.2.*

*Changed in version 2.4:*Added the optional flags argument.`re.``sub`(*pattern*, *repl*, *string*, *count=0*, *flags=0*)

Return the string obtained by replacing the leftmost non-overlapping occurrences of *pattern* in *string* by the replacement *repl*. If the pattern isn’t found, *string* is returned unchanged. *repl* can be a string or a function; if it is a string, any backslash escapes in it are processed. That is, `\n` is converted to a single newline character, `\r` is converted to a carriage return, and so forth. Unknown escapes such as `\j` are left alone. Backreferences, such as `\6`, are replaced with the substring matched by group 6 in the pattern. For example:

```
>>> re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
...        r'static PyObject*\npy_\1(void)\n{',
...        'def myfunc():')
'static PyObject*\npy_myfunc(void)\n{'
```

If *repl* is a function, it is called for every non-overlapping occurrence of *pattern*. The function takes a single match object argument, and returns the replacement string. For example:

```
>>> def dashrepl(matchobj):
...     if matchobj.group(0) == '-': return ' '
...     else: return '-'
>>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')
'pro--gram files'
>>> re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
'Baked Beans & Spam'
```

The pattern may be a string or an RE object.

The optional argument *count* is the maximum number of pattern occurrences to be replaced; *count* must be a non-negative integer. If omitted or zero, all occurrences will be replaced. Empty matches for the pattern are replaced only when not adjacent to a previous match, so `sub('x*', '-', 'abc')` returns `'-a-b-c-'`.

In string-type *repl* arguments, in addition to the character escapes and backreferences described above, `\g<name>` will use the substring matched by the group named `name`, as defined by the `(?P<name>...)` syntax. `\g<number>` uses the corresponding group number; `\g<2>` is therefore equivalent to `\2`, but isn’t ambiguous in a replacement such as `\g<2>0`. `\20` would be interpreted as a reference to group 20, not a reference to group 2 followed by the literal character `'0'`. The backreference `\g<0>` substitutes in the entire substring matched by the RE.

*Changed in version 2.7:*Added the optional flags argument.`re.``subn`(*pattern*, *repl*, *string*, *count=0*, *flags=0*)

Perform the same operation as [`sub()`](https://docs.python.org/2/library/re.html#re.sub), but return a tuple `(new_string, number_of_subs_made)`.

*Changed in version 2.7:*Added the optional flags argument.`re.``escape`(*pattern*)

Escape all the characters in *pattern* except ASCII letters and numbers. This is useful if you want to match an arbitrary literal string that may have regular expression metacharacters in it. For example:

```
>>> print re.escape('python.exe')
python\.exe

>>> legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
>>> print '[%s]+' % re.escape(legal_chars)
[abcdefghijklmnopqrstuvwxyz0123456789\!\#\$\%\&\'\*\+\-\.\^\_\`\|\~\:]+

>>> operators = ['+', '-', '*', '/', '**']
>>> print '|'.join(map(re.escape, sorted(operators, reverse=True)))
\/|\-|\+|\*\*|\*
```

### `re.``purge`()

Clear the regular expression cache.*exception*`re.``error`

Exception raised when a string passed to one of the functions here is not a valid regular expression (for example, it might contain unmatched parentheses) or when some other error occurs during compilation or matching. It is never an error if a string contains no match for a pattern.

#### `\number`

Matches the contents of the group of the same number. Groups are numbered starting from 1. For example, `(.+) \1` matches `'the the'` or `'55 55'`, but not `'thethe'` (note the space after the group). This special sequence can only be used to match one of the first 99 groups. If the first digit of *number* is 0, or *number* is 3 octal digits long, it will not be interpreted as a group match, but as the character with octal value *number*. Inside the `'['` and `']'` of a character class, all numeric escapes are treated as characters.

#### `\A`

Matches only at the start of the string.

#### `\b`

Matches the empty string, but only at the beginning or end of a word. A word is defined as a sequence of alphanumeric or underscore characters, so the end of a word is indicated by whitespace or a non-alphanumeric, non-underscore character. Note that formally, `\b` is defined as the boundary between a `\w` and a `\W` character (or vice versa), or between `\w` and the beginning/end of the string, so the precise set of characters deemed to be alphanumeric depends on the values of the `UNICODE` and `LOCALE` flags. For example, `r'\bfoo\b'` matches `'foo'`, `'foo.'`, `'(foo)'`, `'bar foo baz'` but not `'foobar'` or `'foo3'`. Inside a character range, `\b` represents the backspace character, for compatibility with Python’s string literals.

#### `\B`

Matches the empty string, but only when it is *not* at the beginning or end of a word. This means that `r'py\B'` matches `'python'`, `'py3'`, `'py2'`, but not `'py'`, `'py.'`, or `'py!'`. `\B` is just the opposite of `\b`, so is also subject to the settings of `LOCALE` and `UNICODE`.

#### `\d`

When the [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) flag is not specified, matches any decimal digit; this is equivalent to the set `[0-9]`. With [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE), it will match whatever is classified as a decimal digit in the Unicode character properties database.

#### `\D`

When the [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) flag is not specified, matches any non-digit character; this is equivalent to the set `[^0-9]`. With [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE), it will match anything other than character marked as digits in the Unicode character properties database.

#### `\s`

When the [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) flag is not specified, it matches any whitespace character, this is equivalent to the set `[ \t\n\r\f\v]`. The [`LOCALE`](https://docs.python.org/2/library/re.html#re.LOCALE) flag has no extra effect on matching of the space. If [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) is set, this will match the characters `[ \t\n\r\f\v]` plus whatever is classified as space in the Unicode character properties database.

#### `\S`

When the [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) flag is not specified, matches any non-whitespace character; this is equivalent to the set `[^ \t\n\r\f\v]` The [`LOCALE`](https://docs.python.org/2/library/re.html#re.LOCALE) flag has no extra effect on non-whitespace match. If [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) is set, then any character not marked as space in the Unicode character properties database is matched.

#### `\w`

When the [`LOCALE`](https://docs.python.org/2/library/re.html#re.LOCALE) and [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) flags are not specified, matches any alphanumeric character and the underscore; this is equivalent to the set `[a-zA-Z0-9_]`. With [`LOCALE`](https://docs.python.org/2/library/re.html#re.LOCALE), it will match the set `[0-9_]` plus whatever characters are defined as alphanumeric for the current locale. If [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) is set, this will match the characters `[0-9_]` plus whatever is classified as alphanumeric in the Unicode character properties database.

#### `\W`

When the [`LOCALE`](https://docs.python.org/2/library/re.html#re.LOCALE) and [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) flags are not specified, matches any non-alphanumeric character; this is equivalent to the set `[^a-zA-Z0-9_]`. With [`LOCALE`](https://docs.python.org/2/library/re.html#re.LOCALE), it will match any character not in the set `[0-9_]`, and not defined as alphanumeric for the current locale. If [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) is set, this will match anything other than `[0-9_]` plus characters classified as not alphanumeric in the Unicode character properties database.

#### `\Z`

Matches only at the end of the string.

#### `'.'`

(Dot.) In the default mode, this matches any character except a newline. If the [`DOTALL`](https://docs.python.org/2/library/re.html#re.DOTALL) flag has been specified, this matches any character including a newline.

#### `'^'`

(Caret.) Matches the start of the string, and in [`MULTILINE`](https://docs.python.org/2/library/re.html#re.MULTILINE) mode also matches immediately after each newline.

#### `'$'`

Matches the end of the string or just before the newline at the end of the string, and in [`MULTILINE`](https://docs.python.org/2/library/re.html#re.MULTILINE) mode also matches before a newline. `foo` matches both ‘foo’ and ‘foobar’, while the regular expression `foo$` matches only ‘foo’. More interestingly, searching for `foo.$` in `'foo1\nfoo2\n'` matches ‘foo2’ normally, but ‘foo1’ in [`MULTILINE`](https://docs.python.org/2/library/re.html#re.MULTILINE) mode; searching for a single `$` in `'foo\n'` will find two (empty) matches: one just before the newline, and one at the end of the string.

#### `'*'`

It causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible. `ab*` will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.

#### `'+'`

Causes the resulting RE to match 1 or more repetitions of the preceding RE. `ab+` will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.

#### `'?'`

Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. `ab?` will match either ‘a’ or ‘ab’.

#### `*?`, `+?`, `??`

The `'*'`, `'+'`, and `'?'` qualifiers are all *greedy*; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE `<.*>` is matched against `<a> b <c>`, it will match the entire string, and not just `<a>`. Adding `?` after the qualifier makes it perform the match in *non-greedy* or *minimal* fashion; as *few* characters as possible will be matched. Using the RE `<.*?>` will match only `<a>`.

#### `{m}`

Specifies that exactly *m* copies of the previous RE should be matched; fewer matches cause the entire RE not to match. For example, `a{6}` will match exactly six `'a'` characters, but not five.

#### `{m,n}`

Causes the resulting RE to match from *m* to *n* repetitions of the preceding RE, attempting to match as many repetitions as possible. For example, `a{3,5}` will match from 3 to 5 `'a'` characters. Omitting *m* specifies a lower bound of zero, and omitting *n* specifies an infinite upper bound. As an example, `a{4,}b` will match `aaaab` or a thousand `'a'` characters followed by a `b`, but not `aaab`. The comma may not be omitted or the modifier would be confused with the previously described form.

#### `{m,n}?`

Causes the resulting RE to match from *m* to *n* repetitions of the preceding RE, attempting to match as *few* repetitions as possible. This is the non-greedy version of the previous qualifier. For example, on the 6-character string `'aaaaaa'`, `a{3,5}` will match 5 `'a'` characters, while `a{3,5}?` will only match 3 characters.

#### `'\'`

Either escapes special characters (permitting you to match characters like `'*'`, `'?'`, and so forth), or signals a special sequence; special sequences are discussed below.

If you’re not using a raw string to express the pattern, remember that Python also uses the backslash as an escape sequence in string literals; if the escape sequence isn’t recognized by Python’s parser, the backslash and subsequent character are included in the resulting string. However, if Python would recognize the resulting sequence, the backslash should be repeated twice. This is complicated and hard to understand, so it’s highly recommended that you use raw strings for all but the simplest expressions.

#### `[]`

Used to indicate a set of characters. In a set:

- Characters can be listed individually, e.g. `[amk]` will match `'a'`, `'m'`, or `'k'`.
- Ranges of characters can be indicated by giving two characters and separating them by a `'-'`, for example `[a-z]` will match any lowercase ASCII letter, `[0-5][0-9]` will match all the two-digits numbers from `00` to `59`, and `[0-9A-Fa-f]` will match any hexadecimal digit. If `-` is escaped (e.g. `[a\-z]`) or if it’s placed as the first or last character (e.g. `[a-]`), it will match a literal `'-'`.
- Special characters lose their special meaning inside sets. For example, `[(+*)]` will match any of the literal characters `'('`, `'+'`, `'*'`, or `')'`.
- Character classes such as `\w` or `\S` (defined below) are also accepted inside a set, although the characters they match depends on whether [`LOCALE`](https://docs.python.org/2/library/re.html#re.LOCALE) or [`UNICODE`](https://docs.python.org/2/library/re.html#re.UNICODE) mode is in force.
- Characters that are not within a range can be matched by *complementing* the set. If the first character of the set is `'^'`, all the characters that are *not* in the set will be matched. For example, `[^5]` will match any character except `'5'`, and `[^^]` will match any character except `'^'`. `^` has no special meaning if it’s not the first character in the set.
- To match a literal `']'` inside a set, precede it with a backslash, or place it at the beginning of the set. For example, both `[()[\]{}]` and `[]()[{}]` will both match a parenthesis.

#### `'|'`

`A|B`, where A and B can be arbitrary REs, creates a regular expression that will match either A or B. An arbitrary number of REs can be separated by the `'|'` in this way. This can be used inside groups (see below) as well. As the target string is scanned, REs separated by `'|'` are tried from left to right. When one pattern completely matches, that branch is accepted. This means that once `A` matches, `B` will not be tested further, even if it would produce a longer overall match. In other words, the `'|'` operator is never greedy. To match a literal `'|'`, use `\|`, or enclose it inside a character class, as in `[|]`.

#### `(...)`

Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; the contents of a group can be retrieved after a match has been performed, and can be matched later in the string with the `\number` special sequence, described below. To match the literals `'('` or `')'`, use `\(` or `\)`, or enclose them inside a character class: `[(] [)]`.

#### `(?...)`

This is an extension notation (a `'?'` following a `'('` is not meaningful otherwise). The first character after the `'?'` determines what the meaning and further syntax of the construct is. Extensions usually do not create a new group; `(?P<name>...)` is the only exception to this rule. Following are the currently supported extensions.

#### `(?iLmsux)`

(One or more letters from the set `'i'`, `'L'`, `'m'`, `'s'`, `'u'`, `'x'`.) The group matches the empty string; the letters set the corresponding flags: [`re.I`](https://docs.python.org/2/library/re.html#re.I) (ignore case), [`re.L`](https://docs.python.org/2/library/re.html#re.L) (locale dependent), [`re.M`](https://docs.python.org/2/library/re.html#re.M) (multi-line), [`re.S`](https://docs.python.org/2/library/re.html#re.S) (dot matches all), [`re.U`](https://docs.python.org/2/library/re.html#re.U) (Unicode dependent), and [`re.X`](https://docs.python.org/2/library/re.html#re.X) (verbose), for the entire regular expression. (The flags are described in [Module Contents](https://docs.python.org/2/library/re.html#contents-of-module-re).) This is useful if you wish to include the flags as part of the regular expression, instead of passing a *flag* argument to the [`re.compile()`](https://docs.python.org/2/library/re.html#re.compile) function.

Note that the `(?x)` flag changes how the expression is parsed. It should be used first in the expression string, or after one or more whitespace characters. If there are non-whitespace characters before the flag, the results are undefined.

#### `(?:...)`

A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses, but the substring matched by the group *cannot* be retrieved after performing a match or referenced later in the pattern.

#### `(?P<name>...)`

Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name *name*. Group names must be valid Python identifiers, and each group name must be defined only once within a regular expression. A symbolic group is also a numbered group, just as if the group were not named.

Named groups can be referenced in three contexts. If the pattern is `(?P<quote>['"]).*?(?P=quote)` (i.e. matching a string quoted with either single or double quotes):

| Context of reference to group “quote” | Ways to reference it |
| --- | --- |
| in the same pattern itself | `(?P=quote)` (as shown)`\1` |
| when processing match object `m` | `m.group('quote')``m.end('quote')` (etc.) |
| in a string passed to the `repl` argument of `re.sub()` | `\g<quote>``\g<1>``\1` |

`(?P=name)`

A backreference to a named group; it matches whatever text was matched by the earlier group named *name*.`(?#...)`

A comment; the contents of the parentheses are simply ignored.`(?=...)`

Matches if `...` matches next, but doesn’t consume any of the string. This is called a lookahead assertion. For example, `Isaac (?=Asimov)` will match `'Isaac '` only if it’s followed by `'Asimov'`.`(?!...)`

Matches if `...` doesn’t match next. This is a negative lookahead assertion. For example, `Isaac (?!Asimov)` will match `'Isaac '` only if it’s *not* followed by `'Asimov'`.`(?<=...)`

Matches if the current position in the string is preceded by a match for `...` that ends at the current position. This is called a *positive lookbehind assertion*. `(?<=abc)def` will find a match in `abcdef`, since the lookbehind will back up 3 characters and check if the contained pattern matches. The contained pattern must only match strings of some fixed length, meaning that `abc` or `a|b` are allowed, but `a*` and `a{3,4}` are not. Group references are not supported even if they match strings of some fixed length. Note that patterns which start with positive lookbehind assertions will not match at the beginning of the string being searched; you will most likely want to use the [`search()`](https://docs.python.org/2/library/re.html#re.search) function rather than the [`match()`](https://docs.python.org/2/library/re.html#re.match) function:

```
>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'
```

This example looks for a word following a hyphen:

```
>>> m = re.search('(?<=-)\w+', 'spam-egg')
>>> m.group(0)
'egg'
```

#### `(?<!...)`

Matches if the current position in the string is not preceded by a match for `...`. This is called a *negative lookbehind assertion*. Similar to positive lookbehind assertions, the contained pattern must only match strings of some fixed length and shouldn’t contain group references. Patterns which start with negative lookbehind assertions may match at the beginning of the string being searched.`(?(id/name)yes-pattern|no-pattern)`

Will try to match with `yes-pattern` if the group with given *id* or *name* exists, and with `no-pattern` if it doesn’t. `no-pattern` is optional and can be omitted. For example, `(<)?(\w+@\w+(?:\.\w+)+)(?(1)>)` is a poor email matching pattern, which will match with `'<user@host.com>'` as well as `'user@host.com'`, but not with `'<user@host.com'`.
