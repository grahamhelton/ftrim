# What is this?
fTrim is a simple tool that allows you to designate a clip and select the timestamps you want saved from that clip. For example, if you have a 1 minute clip and you want to save only between 30 and 45 seconds of it, you would input :30 seconds as the start time and :45 seconds as the end time. The resulting clip would be 15 seconds starting at 0:30 and ending at 0:45.

# Install

```bash
git clone https://github.com/grahamhelton/ftrim

pip install os io sys datetime moviepy colorama

chmod +x ftrim.py

./ftrim.py -h
```

# Usage

```bash
===============================================================
                            fTrim
===============================================================
 DESCRIPTION
    This is a simple script that allows you to trim video 
    files in your $HOME/Videos directory to whatever length 
    you desire. 

 OPTIONS
    -h,                     Print this help

    -o,                     Opens file manager to Videos 
                            folder when complete.(Linux only)
==============================================================
```
Please note that this currently only works with .mkv files

![](/fTrim.gif)

# Todo 
- [ ] Add support for multiple video formats
