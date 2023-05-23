import os
from fnmatch import fnmatch
import subprocess

root = '/home/sail/Documents/ronald/code/bb/visible'
dest = '/home/sail/Documents/ronald/code/bb/frames/'

vids = []

for path, subdirs, files in os.walk(root):
    for name in files:
        if '.mp4' not in name.lower():
            continue
        f = os.path.join(path, name)
        outname = dest+name[:-4] + '.png'
        cmd = 'input='+f+';'
        cmd += ' '.join([
            'ffmpeg',
            '-ss',
            "\"$(bc -l <<< \"$(ffprobe -loglevel error -of csv=p=0 -show_entries format=duration \"$input\")*0.5\")\"",
            '-i',
            "\"$input\"",
            "-frames:v",
            "1",
            outname
        ])
        cmd+=';'

        print(cmd)
