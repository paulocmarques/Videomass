# **Videomass** is a cross-platform graphical interface for FFmpeg and youtube-dl.
Videomass provides a graphical interface to create presets and write profiles 
in order to use [FFmpeg](https://www.ffmpeg.org/) without limits on formats and 
codecs with wide automation capabilities. Among the various tools it also 
includes a graphical interface for the famous video downloader 
[youtube_dl](http://ytdl-org.github.io/youtube-dl/).

Check out the full list of features: https://jeanslack.github.io/Videomass/features.html

## Requirements
- [Python ~=3.7](https://www.python.org/)
- [wxPython4](https://wxpython.org/)
- [PyPubSub](https://pypi.org/project/PyPubSub/)
- [pip](https://pypi.org/project/pip/)
- [ffmpeg](https://ffmpeg.org/) >= 4.1.4
- [ffprobe](https://ffmpeg.org/ffprobe.html)
- [ffplay](http://ffmpeg.org/ffplay.html)
- [youtube-dl](https://pypi.org/project/youtube_dl/)

### Optionals
- [mpv](https://mpv.io/)
- [atomicparsley](http://atomicparsley.sourceforge.net/)

## First install basic dependencies

| **OS**          | **Dependencies**                             |
|:----------------|:---------------------------------------------|
|Linux/FreeBSD    | python3, wxpython4, pip for python3, ffmpeg  |
|MS Windows       | python3, ffmpeg                              |
|MacOs            | python3, pip for python3, ffmpeg             |

## Install Videomass using pip

`python3 -m pip install videomass`   

On Linux and FreeBSD a launcher should be even created in the application 
launcher of your desktop environment.   

On Mac-Os and MS-Windows open a console and just write `videomass` command.   

## How to start Videomass manually from source code
Videomass can be run without installing it, just download and unzip the 
[source code archive](https://github.com/jeanslack/Videomass/releases) and 
executing the "launcher" script inside the directory:   

`python3 launcher`   

Videomass can also be run in interactive mode with the Python interpreter, 
always within the same unpacked directory:   

`>>> from videomass3 import Videomass3`   
`>>> Videomass3.main()`   

## Resources
* [Videomass on PyPi](https://pypi.org/project/videomass/)
* [GitHub Page](https://github.com/jeanslack/Videomass)
* [Support Page and Documentation](http://jeanslack.github.io/Videomass)
* [Wiki page](https://github.com/jeanslack/Videomass/wiki)
* [Downloads Source Code](https://github.com/jeanslack/Videomass/releases)
* [Installers for Windows and MacOsX](https://sourceforge.net/projects/videomass2/)


