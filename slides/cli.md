# Command Line Interface

We're going to learn a new interface to our computer.
No icons, no menus, just _text_.
It's called the **command line** or **terminal**.

The computer outputs appends new text to a history of output.
You can type and supply new text as input.

Why?

*   Efficient -
    Direct action.
    Once you know the command you want, just type it.
    Steep learning curve, though.

*   Simple -
    Our programs must communicate with a human;
    Let's use the simplest interface, so we can focus on the problem.

*   Composable -
    When text is both input and output, we can string together programs.

*   Tooling -
    Tools built for the command line over 40 years!
    Often, your problem has already been solved.

## Prompt

The **prompt** is what the terminal gives you when it's waiting for you to write out commands.
Everyone's terminal will be slightly different, but it will look like:

```bash
~ $
```

This shows you your working directory and shows you the command you're currently typing.

```bash
WORKING_DIRECTORY $ YOUR_COMMAND
```

## Working Directory

The **working directory** is the directory in the filesystem you're currently "in".
All paths you write can be relative to the working directory.

You can change you working directory so you can refer to files with less typing.

## Commands

**Commands** are instructions to the computer.
They either change or view the filesystem, move the working directory, or run another program to do so.

At the prompt, you can type out commands and press enter to run them.

Commands tend to have the format `NAME ARGUMENTS`, with spaces between each thing.
Words in `ALL_CAPS` in these notes are a placeholder.

* `pwd` - Print absolute path to the working directory
* `ls` - List the working directory
* `cd DIR_PATH` - Change the working directory to a path
* `atom FILE_PATH` - Open Atom to edit a file
* `mkdir DIR_NAME` - Create a directory with a name in the working directory
* `python FILE_PATH` - Run a file containing Python code (might need `python3`)

We will not learn commands to delete things because it's too easy to accidentally erase your computer.
Use the OS GUI Finder / Explorer to delete for now.

## Keyboard Tips

Most terminals do _not_ let you use the mouse to manipulate input text.
But they do give you a wealth of keyboard shortcuts to do fancy things.
There are a ton of them [for OS X and Linux](http://ss64.com/bash/syntax-keyboard.html) and [Windows](https://technet.microsoft.com/en-us/magazine/ff678293.aspx), but here are some super useful ones.

* `TAB` - Complete a unique path
* `ctrl-a` - Move cursor to the beginning of the line
* `ctrl-e` - Move cursor to the end of the line
* `alt-delete` - Delete backwards a whole word
