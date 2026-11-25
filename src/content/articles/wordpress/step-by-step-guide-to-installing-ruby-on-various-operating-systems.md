---
title: "Installation and Setup: Step-by-Step Guide to Installing Ruby on Various Operating Systems"
description: "Ruby is a dynamic, open source programming language with a focus on simplicity and productivity. Whether you're a seasoned developer or a beginner…"
lang: other
categories: ["Ruby"]
author: "Shakti Das"
pubDate: 2024-05-22T10:01:33Z
legacy: true
wpId: 5176
---

Ruby is a dynamic, open-source programming language with a focus on simplicity and productivity. Whether you're a seasoned developer or a beginner, setting up Ruby on your system is the first step towards building powerful applications. This guide will walk you through the installation process for Ruby on various operating systems: Windows, macOS, and Linux.

## Installing Ruby on Windows

### Using RubyInstaller

RubyInstaller is the easiest way to set up Ruby on a Windows system.

1. **Download RubyInstaller:**

- Go to the [RubyInstaller website](https://rubyinstaller.org/).
- Download the latest Ruby+Devkit version.

1. **Run the Installer:**

- Run the downloaded installer.
- Follow the prompts to complete the installation. Ensure that you check the option to add Ruby to your PATH.

1. **Run `ridk install`:**

- After the installation, a command prompt window will appear. Type `ridk install` to install the MSYS2 Devkit, which provides essential tools for building native C/C++ extensions.

1. **Verify Installation:**

- Open a new command prompt and type:
  `sh ruby -v`
- You should see the Ruby version number, confirming a successful installation.

### Using Windows Subsystem for Linux (WSL)

For a more Unix-like environment, you can use WSL to run Ruby on Windows.

1. **Enable WSL:**

- Open PowerShell as Administrator and run:
  `sh wsl --install`
- Restart your computer if prompted.

1. **Install a Linux Distribution:**

- Open the Microsoft Store, search for a Linux distribution (e.g., Ubuntu), and install it.

1. **Set Up Ruby:**

- Open the installed Linux distribution from the Start menu.
- Update package lists:
  `sh sudo apt update sudo apt upgrade`
- Install Ruby using a version manager like `rbenv` or `rvm` (see Linux instructions below).

## Installing Ruby on macOS

### Using Homebrew

Homebrew is a package manager for macOS that makes installing software a breeze.

1. **Install Homebrew:**

- Open Terminal and run:
  `sh /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

1. **Install Ruby:**

- With Homebrew installed, run:
  `sh brew install ruby`

1. **Update Your PATH:**

- Add Homebrew's Ruby to your PATH by adding the following line to your `~/.zshrc` (or `~/.bash_profile` if you're using Bash):
  `sh export PATH="/usr/local/opt/ruby/bin:$PATH"`
- Apply the changes:
  `sh source ~/.zshrc`

1. **Verify Installation:**

- Check the Ruby version:
  `sh ruby -v`

### Using rbenv

`rbenv` is a popular version manager for Ruby, allowing you to install and manage multiple Ruby versions.

1. **Install `rbenv`:**

- Run:
  `sh brew install rbenv`

1. **Set Up `rbenv`:**

- Add `rbenv` to your shell by adding the following to your `~/.zshrc`:
  `sh eval "$(rbenv init -)"`
- Apply the changes:
  `sh source ~/.zshrc`

1. **Install Ruby:**

- Find the version you want to install:
  `sh rbenv install -l`
- Install the desired version:
  `sh rbenv install 3.1.2 rbenv global 3.1.2`

1. **Verify Installation:**

- Check the Ruby version:
  `sh ruby -v`

## Installing Ruby on Linux

### Using APT (Debian/Ubuntu)

1. **Update Package Lists:**

- Open Terminal and run:
  `sh sudo apt update sudo apt upgrade`

1. **Install Ruby:**

- Install Ruby with:
  `sh sudo apt install ruby-full`

1. **Verify Installation:**

- Check the Ruby version:
  `sh ruby -v`

### Using rbenv

`rbenv` is also a great option for Linux systems.

1. **Install Dependencies:**

- Install required dependencies:
  `sh sudo apt update sudo apt install -y git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev`

1. **Install `rbenv` and `ruby-build`:**

- Clone `rbenv` and `ruby-build` repositories:
  `sh git clone https://github.com/rbenv/rbenv.git ~/.rbenv echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc echo 'eval "$(rbenv init -)"' >> ~/.bashrc source ~/.bashrc git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc source ~/.bashrc`

1. **Install Ruby:**

- List available versions and install:
  `sh rbenv install -l rbenv install 3.1.2 rbenv global 3.1.2`

1. **Verify Installation:**

- Check the Ruby version:
  `sh ruby -v`

## Conclusion

Setting up Ruby on your system is a straightforward process, whether you're using Windows, macOS, or Linux. By following these step-by-step instructions, you'll be ready to start developing Ruby applications in no time. With Ruby's elegant syntax and powerful features, you'll quickly see why it has become such a beloved language in the programming community. Happy coding!
