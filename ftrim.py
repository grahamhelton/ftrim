#! /usr/bin/python3
# Import stuff and things
import os
import io
import sys
import datetime
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from os import listdir
from os.path import isfile, join, expanduser
from colorama import init, Fore, Style
count = 0
dic = {}
reset = Style.RESET_ALL
tick = Fore.BLUE + "[" + Fore.GREEN + "+" + Fore.BLUE + "]" + reset

# Get command line arugments
if "-h" in sys.argv:
    print('''
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
    ''')
    exit()
# Make an attempt at making this useful to other people by not hardcoding my path in
home = expanduser("~")
videos = home + "/Videos/"

# List all the files in $HOME/Videos
listFiles = [f for f in listdir(videos) if isfile(join(videos, f))]
print (tick + Fore.GREEN + " Listing Files in " + Fore.YELLOW + videos + reset)

# List key/value pair where key = file number and value is file name
for i in listFiles:
    count +=1
    dic[count]=i
for key, value in dic.items():
    print(key, ':', value)

# Get user input
selection = input(tick + Fore.GREEN + " Select the number of the file you would like to trim: " + reset)
startTime = input(tick + Fore.GREEN +  " Input start time: "+ reset)
endTime = input(tick + Fore.GREEN +  " Input end time: "+ reset)
name = input(tick + Fore.GREEN +  " Output file name?: " + reset) + ".mkv" 
selection = dic[int(selection)]
finalSelection = videos + selection 

# Fixes user input (clean this up at some point) 
if ":" in startTime or ":" in endTime:
    if startTime.count(":") == 2:
        h,m,s = startTime.split(':')
        starTime = (int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()))
    elif startTime.count(":") == 1:
        m,s = startTime.split(':')
        startTime = (int(datetime.timedelta(minutes=int(m),seconds=int(s)).total_seconds()))
    else: 
        s = startTime
        startTime = (int(datetime.timedelta(seconds=int(s)).total_seconds()))
    if endTime.count(":") >= 2:
        h,m,s = endTime.split(':')
        endTime = (int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()))
    elif endTime.count(":") == 1:
        m,s = endTime.split(':')
        endTime = (int(datetime.timedelta(minutes=int(m),seconds=int(s)).total_seconds()))
    else: 
        s = endTime 
        endTime = (int(datetime.timedelta(seconds=int(s)).total_seconds()))
else: 
    s = startTime
    startTime = (int(datetime.timedelta(seconds=int(s)).total_seconds()))
    s = endTime 
    endTime = (int(datetime.timedelta(seconds=int(s)).total_seconds()))

# Silence output from moviepy 
text_trap = io.StringIO()
sys.stdout = text_trap

# Do the thing 
ffmpeg_extract_subclip(finalSelection, startTime, endTime, targetname=name)

# Unsilence output from moviepy 
text_trap = io.StringIO()
sys.stdout = text_trap

# Unsilence output from moviepy 
sys.stdout = sys.__stdout__

print( tick + Fore.GREEN + " Created " + Fore.RED + name + Fore.GREEN + " in " + Fore.YELLOW + videos )
if "-o" in sys.argv:
    os.system('xdg-open "%s" &' % videos)

