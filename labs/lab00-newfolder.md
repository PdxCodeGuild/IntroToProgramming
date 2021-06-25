<div align="center">

## *******************************************************

## This syllabus is **deprecated**.

### Intro to Programming has become Programming 101 and Programming 102. 

### **Contact your instructor** for the link to the correct syllabus. 
***
## *******************************************************
</div>

# Lab 00: Navigating the Terminal <a id="top"></a>

- [Back to Syllabus](https://github.com/PdxCodeGuild/IntroToProgramming#top)
- [Python Tutor](http://pythontutor.com/visualize.html#mode=edit)
- [Terminal Cheatsheet](https://docs.google.com/spreadsheets/d/18WWrry7RI2zzJlTsUHQLCsElNjiVVuMGjowBKZ5DPH8/edit#gid=0)

You write your code in a text editor, like Atom or PyCharm, but then what happens? How does your laptop know what to do with it?

Have no fear, the Python Interpreter is here! On your laptop, search for the program according to your system:

- macOS - Terminal
- Windows - Powershell or Command Line
- Linux - Shell or Terminal

After opening the program, you should see something like this:

![root](/resources/lab00-root.png)

The root sign, **~**, means you're in the root of your computer. For windows, it will be your username.
```
C:\Users\lisanguyen06>
```
 Doesn't make sense? Don't worry, it will soon. Follow the directions below and things should start to make more sense.

### Where am I?

To see your current directory, type the following command into your terminal and hit enter:

```bash
# mac/linux
pwd

# Windows
cd
```
This will print the path of the directory (or folder) that you're in.

![pwd](/resources/lab00-pwd.png)

### What's in this folder?

Next, type **ls** in your terminal/command line to list all the folders and files available in the current directory:

```bash
# mac/linux/ Windows
ls
```
As you can see, here are all the folders and files in the **root** directory. The one we're interested in is **Desktop**.

![ls](/resources/lab00-ls.png)

### Moving into a folder

To get to Desktop. Type **cd Desktop** into the terminal/command line. **Capitalization matters.**

```bash
# mac/linux/ Windows
cd Desktop
```

![cd Desktop](/resources/lab00-cd-desktop.png)

Notice that the path changes from **~** to **Desktop**. That's how you know what folder you're in.

Type **ls** again in your terminal/command line to list all the folders and files available on your Desktop!

```bash
ls
```
![ls](/resources/lab00-ls-2.png)

Pretty neat, right? Now we're going to make some changes to your Desktop.

### Creating a new folder

In terminal/command line, type **mkdir pdxcode**.

```bash
# mac/linux/ Windows
mkdir pdxcode
```
Type **ls** again:
```bash
ls
```
![mkdir](/resources/lab00-mkdir.png)

Do you see the difference? **pdxcode** is now on your Desktop. To double check, you can go find the folder on the your Desktop:

![mkdir](/resources/lab00-desktop.png)

Go back to terminal and let's navigate into the folder **pdxcode**.

Hint: After typing the characters, **pdx**, hit tab. The terminal will auto-complete the file name! Isn't that cool?

```bash
# mac/linux/ Windows
cd pdx # type this then hit tab

# Ad a result, you should see "cd pdxcode".
# Then hit enter.
```
Notice that the path changes from **Desktop** to **Desktop\pdxcode>**. That's how you know what folder you're in.

### Conclusion
With the terminal, we've navigated around the computer and created a new folder on the Desktop. The folder that we created will be where we save all our labs. If you had a hard time remembering all the commands, you can use this [terminal cheatsheet](https://docs.google.com/spreadsheets/d/18WWrry7RI2zzJlTsUHQLCsElNjiVVuMGjowBKZ5DPH8/edit#gid=0). It's also linked on the main page of the [syllabus](https://github.com/PdxCodeGuild/IntroToProgramming)

[Back to top](#top)
