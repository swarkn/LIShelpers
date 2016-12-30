# LIShelpers

[![N|Solid](https://www.python.org/static/community_logos/python-powered-w-140x56.png)](https://www.python.org)

This will be a little collection for some tools, people can use if they / or their beloved ones suffer from "locked-in" syndrom. This project is in a really early state and might not be very usefull at the moment. We want all the tools to be as easy to use as nothing else. Therefore:

  - Using the tools will be possible with at least only 1 physical body reaction to say "yes"
  - Eyerything is designed for high contrast & big sized fonts
  - Eyerything you might see on the screen, will be read out loud (if you wish so)
  - Less information on the screen is more.

The toolset of LIShelpers are written in Python Computer Language by the guys of [do-it-neat.com]. You are able to get support at the [github issues] site.

### Tech

The LIShelpers use a number of open source projects to work properly:

* [Tk] - a thin object-oriented layer on top of Tcl/Tk.
* [ImageTk] - support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images
* [gTTS] - Create an mp3 file from spoken text via the Google TTS (Text-to-Speech) API
* [pyglet] - a cross-platform windowing and multimedia library for Python
* [AVbin] - a cross-platform, thin wrapper around Libav’s video and audio decoding library

And of course LIShelpers itself are open source with a [public repository][github project]
 on GitHub.

### Installation

LIShelpers requires [Python](https://python.org/) v3.5.2 to run.

Download and extract the [latest pre-built release](https://www.python.org/downloads/release/python-352/).

##### Install LIShelpers on Windows

Install the python package the "typical" way. Please don't forget to put the Python search path into your PATH environment variable.

Open up a command prompt (by starting cmd.exe) and install the necessary Python modules:

```cmd
$ pip install imagetk
$ pip install gtts
$ pip install pyglet
```
Install the binary package of AVbin by downloading and running the [setup file][avbin download]. Please be shure to install the right flavor of AVbin (32/64bit). The right version need to be the same version of Python you are using.

To have AVbin work properly on Windows 10, copy the files AVbin.dll and/or AVbin64.dll from your Windows/system32 folder into your Windows/WinSxS folder.

### Development

Want to contribute? Great!

We truly need your help. We are no developers at all and your development skill would come in very handy for the project. :) We're only using the github toolset for developing. Just do a pull request.

### Todos

 - build more usefull tools
 - work on hardware interfaces
 - Add Code Comments
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
[pyglet]: <https://bitbucket.org/pyglet/pyglet/wiki/Home>
[AVbin]: <http://avbin.github.io/AVbin/Home/Home.html>
[avbin download]: <https://avbin.github.io/AVbin/Download.html>


