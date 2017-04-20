# Filesystem and Paths

Since programs are stored in files, let's learn rigorously about how the computer manages files.
You've probably dealt with files on your own computer already, but let's learn some technical terms and conventions.

Your **filesystem** is a hierarchical store of data.
**Files** are named blobs of data.
**Directories** are named containers of files and other directories.
Directories form a hierarchy because they contain each other.
Directories are sometimes written with a trailing `/` after their name to signal they are not a file, but the slash is _not part of their name_.

Every filesystem has a **root directory**, the directory that isn't contained by anything.
On OS X and Linux systems this is `/` or on Windows it is your drive letter `C:\`

An example filesystem visualized as a tree.
All files and directories that live in a directory are indented one more level.

```
/
    root_file.txt
    Users/
        david/
            resume.txt
            code/
                greeting.py
                fortune.py
    System/
        ...
```

## Paths

A **path** is a text string specifying a file or directory.
It is a series of directory names following the hierarchy, separated by `/`s, ending in a file name or directory name.

* `/Users/david/resume.txt`
* `/Users/david/code`
* `/System`
* `/root_file.txt`

There are a few special directory names:

* `~` is shorthand for your **home directory**
* `..` is the name of the **parent directory**; every directory has it inside
* `.` is the name of the **current directory**; every directory has it inside

Realize that that means paths are _not unique_.

* `/Users/david/code/..` refers to `/Users/david`
* `/Users/david/./code/.` refers to `/Users/david/code`
* `~` refers to `/Users/david`
* `~/..` refers to `/Users`

Paths can be **absolute** or **relative**.
An absolute path starts with a `/` or `~` and specifies the whole path from the root.
A relative path just shows how to navigate from one directory to another file;
you can basically append the relative path to the relative directory.

* In `/Users/david`, `code/greeting.py` is the same as `/Users/david/code/greeting.py`
* In `/Users/david`, `../../root_file.txt` is the same as `/root_file.txt`
* In `/Users/david`, `..` is the same as `/Users`
