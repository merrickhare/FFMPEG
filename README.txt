Still adding some logic and ui upgrades (file picker)


This is a simple GUI for converting mp4 files to flv. Used currently at work to help with users not familiar with FFMPEG.

VERY Specific to the workflow I use for converting videos for hyland onbase. 

You can change any of the parameters in the class file run.py

"ffmpeg -i "  " -vcodec libx264 -preset veryslow -b:v 400k -maxrate 500k -profile:v high -level 4.1 -x264-params crf=23:bframes=0 -c:a aac -b:a 96k "  ".flv"
