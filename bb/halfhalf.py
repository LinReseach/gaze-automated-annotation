import os
from fnmatch import fnmatch
import subprocess

vis_root = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/visible'
invis_root = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/invisible'
vis_dest = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/frames/frame_vis/'
invis_dest = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/frames/frame_invis/'
vis_cmd = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/visible_cmd.txt'
invis_cmd = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/invisible_cmd.txt'
root = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/new'

# file_list = ["Proefpersoon11012_sessie1.mp4", "Proefpersoon11012_sessie2.mp4", "Proefpersoon11012_Sessie3.mp4"]

vids = []
vis_cmd = []
invis_cmd = []

for path, subdirs, files in os.walk(vis_root):
    for name in files:
        if '.mp4' not in name.lower():
            continue
        f = os.path.join(path, name)
        outname = vis_dest+name[:-4] + '.png'
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
        # print(cmd)
        vis_cmd.append(cmd)

with open("visible_cmd.txt", "w") as file:
	for c in vis_cmd:
		file.write(c)
		
for path, subdirs, files in os.walk(invis_root):
    for name in files:
        if '.mp4' not in name.lower():
            continue
        f = os.path.join(path, name)
        outname = invis_dest+name[:-4] + '.png'
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
        # print(cmd)
        invis_cmd.append(cmd)

with open("invisible_cmd.txt", "w") as file:
	for c in invis_cmd:
		file.write(c)