# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
from PIL import Image
import os
import cv2
import pandas as pd
import numpy as np

vis_img_root = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/frames/frame_vis/'
invis_img_root = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/frames/frame_invis/'
saved_vis_root = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/frames/Saved_frame/fig_vis/'
saved_invis_root = '/home/linlincheng/Gaze_estimation/gaze-automated-annotation/bb/frames/Saved_frame/fig_invis/'
img_name = '51007_sessie1_taskrobotEngagement.png'

vis_img = vis_img_root + img_name
invis_img = invis_img_root + img_name

# Read RGB image
# im = cv2.imread(vis_img)
im = cv2.imread(invis_img)
height, width, channels = im.shape
# print(f"({width}, {height})")   # (852,480) (1280,720)

# Draw rectangles (SP=start point, EP=End point)
tablet_SP, tablet_EP, robot_SP, robot_EP, table_SP, table_EP = \
(0, 390), (135, 480), (225, 455), (540, 480), (555, 455), (725, 480)
# Red rectangle (tablet)
tablet_invis = True
cv2.rectangle(im, tablet_SP, tablet_EP,
              (0, 0, 255), 1)

# Green rectangle (robot)
robot_invis = True
cv2.rectangle(im, robot_SP, robot_EP,
              (0, 255, 0), 1)
# Blue rectangle (table)
table_invis = False
cv2.rectangle(im, table_SP, table_EP,
              (255, 0, 0), 1)

# data = np.array(['Video_name', 'Tablet_SP', 'Tablet_EP', 'Robot_SP', 'Robot_EP', 'Table_SP', 'Table_EP', 'Invisible_obj'])

invis_obj = []
if tablet_invis == robot_invis == table_invis is False:
    invis_obj = None

while tablet_invis:
    invis_obj.append("Tablet")
    break
while robot_invis:
    invis_obj.append("Robot")
    break
while table_invis:
    invis_obj.append("Table")
    break

# Normalize
norm_tablet_SP = (round(tablet_SP[0] / width, 3), round(tablet_SP[1] / height, 3))
norm_tablet_EP = (round(tablet_EP[0] / width, 3), round(tablet_EP[1] / height, 3))
norm_robot_SP = (round(robot_SP[0] / width, 3), round(robot_SP[1] / height, 3))
norm_robot_EP = (round(robot_EP[0] / width, 3), round(robot_EP[1] / height, 3))
norm_table_SP = (round(table_SP[0] / width, 3), round(table_SP[1] / height, 3))
norm_table_EP = (round(table_EP[0] / width, 3), round(table_EP[1] / height, 3))
# print(f"{norm_tablet_SP}, {norm_tablet_EP}, {norm_robot_SP}, {norm_robot_EP}, {norm_table_SP}, {norm_table_EP}")

# Output img with window name as image_name
cv2.imshow(img_name, im)

# uncomment this part to write the image and text files
cv2.imwrite(os.path.join(saved_vis_root, img_name), im)
with open("pixel_position_invis_original.txt", "a") as file:
    file.write(f"{img_name}, {tablet_SP}, {tablet_EP}, {robot_SP}, "
               f"{robot_EP}, {table_SP}, {table_EP}, {invis_obj} \n")
with open("pixel_position_invis.txt", "a") as file:
    file.write(f"{img_name}, {norm_tablet_SP}, {norm_tablet_EP}, {norm_robot_SP}, "
               f"{norm_robot_EP}, {norm_table_SP}, {norm_table_EP}, {invis_obj} \n")

# Maintain output window until user presses a key
cv2.waitKey(5000)
# Destroying present windows on screen
cv2.destroyAllWindows()
