# Lab 00: Python Interpreter

---
Quicklinks
- [Intro to Programming](https://github.com/PdxCodeGuild/IntroToProgramming)
- [Labs](https://github.com/PdxCodeGuild/IntroToProgramming/tree/master/labs)
- [Slack Channel](https://app.slack.com/client/TH5A28SJ0/CH6DE8QK1)
- [Python Tutor](http://pythontutor.com/visualize.html#mode=edit)
---
You write your code in a text editor, like Atom or PyCharm, but then what happens? How does your laptop know what to do with it?

Have no fear, the Python Interpreter is here! On your laptop, search for the program according to your system:

- macOS - Terminal
- Windows - Powershell or Commandline
- Linux - Shell or Terminal

After opening the program, you should see something like this:

![root](/resources/lab00-root.png)

The ~ sign means you're in the root of your computer. Doesn't make sense? Don't worry, it will soon. Do the following and things should start to make more sense:

## macOS/linux
Type **pwd** in your terminal/command line to see a working directory:

```bash
pwd
```
![pwd](/resources/lab00-pwd.png)

This will print the path of the directory (or folder) that you're in.

Next, type **ls** in your terminal/command line to list all the folders and files available in the current directory:
```bash
ls
```
![ls](/resources/lab00-ls.png)

As you can see, here are all the folders and files in the directory. The one we're interested in is **Desktop**.

To get to Desktop. Type **cd Desktop** into the terminal/command line. **Capitalization matters.**

```bash
cd Desktop
```
![cd Desktop](/resources/lab00-cd-desktop.png)

Type **ls** again in your terminal/command line to list all the folders and files available on your Desktop!
```bash
ls
```
![ls](/resources/lab00-ls-2.png)

Pretty neat, right? Now we're going to make some changes to your Desktop. In terminal/command line, type **mkdir pdxcode**

```bash
mkdir pdxcode
```
Type ls again:
```bash
ls
```
![mkdir](/resources/lab00-mkdir.png)

Do you see the difference? **pdxcode** is now on your Desktop. To double check, you can go find the folder on the your Desktop:

![mkdir](/resources/lab00-desktop.png)
