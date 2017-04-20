# Command-Line Tour

We will be working from your system’s command-line interface (CLI) throughout the course. Below are some common commands with which you should become familiar.

(These should all work on OS X and Linux. See [Introduction to the Windows Command Prompt](http://www.bleepingcomputer.com/tutorials/windows-command-prompt-introduction/) for their Windows equivalents.)

- `ls` — list files in current directory
- `cd` — change directory
- `cd ~/` — change to your home directory
- `cd Documents` — change to the Documents directory
- `cd ../` — go up one directory
- `mkdir` — make a directory, e.g., `mkdir NewFolder` to make a new directory with name NewFolder
- `rmdir` — remove a directory, e.g., `rmdir NewFolder` to delete the directory we just created (or `rmdir -R NewFolder` if the directory is not empty)
- `pwd` — list the current directory (‘pwd’ stands for ‘print working directory’)
- `touch` — create a new, empty file, e.g., `touch new_file.txt`
- `cp` — copy a file, e.g., `cp new_file.txt newer_file.txt`
- `rm` — remove a file, e.g., `rm newer_file.txt`

------

## Autocomplete

A super-handy shortcut when working with the CLI is to tab to autocomplete. Try the following (on OS X):

1. `cd ~/`
1. `ls Doc` + [tab]

The system should have autocompleted to `ls Documents/`. You can then hit [enter] to execute the command.

If the system can’t resolve the autocomplete to a single string, tab a second time to get a list of the matching options. Try the following (on OS X):

1. `cd ~/`
1. `ls D` + [tab] + [tab]

The system should have shown you `Desktop/   Documents/ Downloads/` as the possible options. Type `e` + [tab] and the system should autocomplete to `ls Desktop/`.

------

## Resources for futher reading:

1. [A very, very gentle introduction to the Linux Command Line](http://chrisyoung.net/prose/blog/posts/2009-11-28-very-very-gentle-introduction-linux-command-line/)
1. Django Girls [Introduction to the command-line interface](http://tutorial.djangogirls.org/en/intro_to_command_line/)
