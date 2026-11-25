---
title: "How to create a Virtual Environment in Python"
description: "To create a virtual environment in Python, you will need to use the venv module. This module is included in Python as of version 3.3, so you should have…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2022-12-27T09:03:39Z
legacy: true
wpId: 3365
---

To create a virtual environment in Python, you will need to use the `venv` module. This module is included in Python as of version 3.3, so you should have it available if you are using a relatively recent version of Python.

Here is an example of how to create a virtual environment using `venv`:

```python
python3 -m venv myenv
```

This will create a new directory called `myenv` that contains the files and directories needed for your virtual environment.

You can also specify a specific Python executable to use when creating the virtual environment, like this:

```python
python3.8 -m venv myenv
```

Once you have created your virtual environment, you can activate it by running the `activate` the script that is located in the `bin` directory of the virtual environment. For example, on Unix or Linux systems, you can activate the virtual environment like this:

```python
Copy codesource myenv/bin/activate
```

On Windows, you can activate the virtual environment by running the `activate.bat` script:

```python
codemyenv\Scripts\activate.bat
```

Once you have activated your virtual environment, any Python packages that you install using `pip` will be installed in the virtual environment, rather than in the global Python environment. This allows you to have separate package installations for different projects, which can be useful if you need to work on multiple projects that have different package requirements.

To deactivate the virtual environment, you can use the `deactivate` command:

```python
deactivate
```

I hope this helps! Let me know if you have any questions.
