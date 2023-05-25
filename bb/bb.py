import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

vis_img_root = 'frames/frame_vis/'
invis_img_root = 'frames/frame_invis/'
saved_vis_root = 'frames/saved_frame/fig_vis/'
saved_invis_root = 'frames/saved_frame/fig_invis/'
img_name = '33001_sessie1_taskrobotEngagement.png'

vis_img = vis_img_root + img_name
invis_img = invis_img_root + img_name

im = Image.open(vis_img)
# im = Image.open(invis_img)

# Create figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(im)	

# Create a Rectangle patch
rect = patches.Rectangle((159, 143), 350-159, 460-143, linewidth=1, edgecolor='r', facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect)

plt.draw()
# plt.show()
fig.savefig(path.join(saved_vis_root, img_name))
# fig.savefig(path.join(saved_invis_root, img_name))
plt.close()
