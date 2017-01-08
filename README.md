# LIShelpers

[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-140x56.png)](https://www.python.org)

This will be a little collection for some tools, people can use if they / or their beloved ones suffer from "locked-in" syndrom. This project is in a really early state and might not be very usefull at the moment. We want all the tools to be as easy to use as possible. Therefore:

  - Using the tools will be possible with at least only 1 physical body reaction to say "yes"
  - Eyerything is designed for high contrast & big sized fonts
  - Eyerything you might see on the screen, will be read out loud (if you wish so)
  - Less information on the screen is allways more.

The toolset of LIShelpers is written in Python computer language, hosted by the guys of [do-it-neat.com] and [GitHub][github project]. You are able to get support at the [github issues] site.

Please visit this site from time to time. It will be constantly updated, until we release a first major version.

### Table of contents
**[1. How to use the SimpleSpellMachine](#how-to-use-the-simplespellmachine)**  
**[2. Tech](#tech)**  
**[3. Installation](#installation)**  
**[3.1 Install LIShelpers on Windows](#install-lishelpers-on-windows)**  
**[3.2 Install LIShelpers on Linux](#install-lishelpers-on-linux)**  
**[3.3 Install LIShelpers on Raspberry Pi](#install-lishelpers-on-raspberry-pi)**  
**[4. FAQ](#faq)**
**[5. Development](#development)**
**[6. Todos](#todos)**

### How to use the SimpleSpellMachine

This is the keyboard layout:
[![N|Solid](http://www.do-it-neat.com/wp-content/uploads/2016/12/LIShelpers-SSM_keyboard-layout_v01.png)](https://www.do-it-neat.com/projekte/lishelpers)

This is the user interface:
[![N|Solid](http://www.do-it-neat.com/wp-content/uploads/2016/12/LIShelpers_SSM.jpg)](https://www.do-it-neat.com/projekte/lishelpers)

### Tech

The LIShelpers package uses a number of open source projects to work properly:

* [Tk] - a thin object-oriented layer on top of Tcl/Tk.
* [ImageTk] - support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
* [gTTS] - Create an mp3 file from spoken text via the Google TTS (Text-to-Speech) API
* [python-vlc] - a complete coverage of the libvlc API for Python
* [VLC Mulitmedia Player] - is a free and open source mulitmedia player

And of course the LIShelpers package itself is open source with a [public repository][github project]
 on GitHub.

### Installation

LIShelpers requires at least [Python](https://python.org/) 3.4 to run. Python 3.6 is currently not supported.

##### Install LIShelpers on Windows

Download and extract the [latest pre-built release](https://www.python.org/downloads/release/python-352/).

Install the python package the "typical" way. Please don't forget to put the Python search path into your PATH environment variable.

Download and install the [latest release](http://www.videolan.org/vlc/) of VLC player, according to your Windows version.

Open up a command prompt (by right-clicking cmd.exe and start it with administrative privileges) and install the necessary Python modules:

```cmd
C:\Users\bob> pip install pillow
C:\Users\bob> pip install gtts
C:\Users\bob> pip install python-vlc
```

Download the latest [source code](https://github.com/swarkn/LIShelpers/archive/master.zip) of the LIShelpers as a zip file and extract it onto you computer.

Go inside the folder "LIShelpers-master/SimpleSpellMachine" and double-click "LIS_SimpleSpellMachine.py" to start the SimpleSpellMachine.

The first time you'll start the SimpleSpellMachine, a cache will be build up to fasten up the application. To configure the SimpleSpellMachine, take a look at the file LISconfig.py and feel free to edit the variables to your needs.

##### Install LIShelpers on Linux

The following instructionset will help you install LIShelpers on openSUSE Leap 42.2. Support for the Raspberry Pi project will fast follow. Therefore, an instructionset to install LIShelpers on Debian flavored Linux distributions will also be available soon.

Update your current Leap 42.2 installation by refreshing your repositories and updating your packages.

```cmd
$ sudo zypper refresh
$ sudo zypper up
```

Now, install the necessary binary packages for Python 3 and VLC

```cmd
$ sudo zypper in python3
$ sudo zypper in vlc
```

Basically, you are able to install all needed Python modules by pip. However, for your convenience, openSUSE provides some Python base-packages within it's package management. You should use those:

```cmd
$ sudo zypper in python3-tk
$ sudo zypper in python3-Pillow
```

There are only some "non-standard" packages left missing. Just install them by using pip.

```cmd
$ sudo pip install gtts
$ sudo pip install python-vlc
```

Now, we need to clone the LIShelpers repository into the current users home directory.

```cmd
$ cd ~
$ git clone https://github.com/swarkn/LIShelpers.git
```

To start the LIShelpers SimpleSpellMachine, just go inside the newly generated folder and start it.

```cmd
$ cd LIShelpers/SimpleSpellMachine/
$ python3 LIS_SimpleSpellMachine.py
```

##### Install LIShelpers on Raspberry Pi

The installation of the LIShelpers are tested with Raspbian Jessie. Therefore, this part of the readme should also work with all other Debian flavors arround.

Update your current Raspbian installation by refreshing your repositories and updating your packages.

```cmd
$ sudo apt-get update
```

Now, install the necessary binary packages for Python 3 and VLC.

```cmd
$ sudo apt-get install python3
$ sudo apt-get install vlc
```

Pillow might be isntalled, but in Debian flavors, you need to install imagetk separately.

```cmd
$ sudo apt-get install python3-pil
$ sudo apt-get install python3-pil.imagetk
```

Only gtts and the Python VLC modules are left missing. Those can be installed via pip.

```cmd
sudo pip3 install gtts
sudo pip3 install python-vlc
```

Now, we need to clone the LIShelpers repository into the current users home directory.

```cmd
$ cd ~
$ git clone https://github.com/swarkn/LIShelpers.git
```

To start the LIShelpers SimpleSpellMachine, just go inside the newly generated folder and start it.

```cmd
$ cd LIShelpers/SimpleSpellMachine/
$ DISPLAY=:0 python3 LIS_SimpleSpellMachine.py
```

### FAQ

**Q: I am experiencing problems while downloading the cache from Google Translate. There are SSL exceptions inside the terminal window.**

This might be caused by an rather old version of your Pythons request module. Just uninstall/reinstall the latest version (should be 2.12.4 or above).

```cmd
$ pip list
$ pip uninstall requests
$ pip install requests
```

**Q: There is no audio output on Raspberry Pi. How do i fix that?**

This might come from some default settings of your Raspian image. Just run "sudo raspi-config". Within the advanced settings, set the audio output to 3.5mm or HDMI to your needs. You might need to restart your Raspberry Pi.

### Development

Want to contribute? Great!

We truly need your help. We are no developers at all and your development skill would come in very handy for the project. :) We're only using the github toolset for developing. Just do a pull request.

### Todos

 - finish the first tool "SimpleSpellMachine"
 - of course: build more usefull tools!
 - work on hardware interfaces
 - add more code comments
 - etc.

License
----

GNU GENERAL PUBLIC LICENSE v3




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

[do-it-neat.com]: <http://www.do-it-neat.com/projekte/LIShelpers>
[github project]: <https://github.com/swarkn/LIShelpers>
[github issues]: <https://github.com/swarkn/LIShelpers/issues>
[Tk]: <http://www.tcl.tk/>
[ImageTk]: <https://wiki.python.org/moin/TkInter>
[gTTS]: <https://pypi.python.org/pypi/gTTS>
[python-vlc]: <https://wiki.videolan.org/python_bindings>
[VLC Mulitmedia Player]: <http://www.videolan.org/vlc/>
