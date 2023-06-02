import pandas as pd

datafolder = './data_fin/'
datafile = 'pixel_position_vis.txt'

# tl:topleft coordinate, br: bottom right coordinate
data = pd.read_csv(datafolder+datafile,
                   sep=', [^\']',
                   names=['file',
                          'tl_tablet_x',
                          'tl_tablet_y',
                          'br_tablet_x',
                          'br_tablet_y',
                          'tl_robot_x',
                          'tl_robot_y',
                          'br_robot_x',
                          'br_robot_y',
                          'tl_p_x',
                          'tl_pp_y',
                          'br_pp_x',
                          'br_pp_y',
                          'obj_list'],

                   engine='python')

pp = ['tl_tablet_y',
      'br_tablet_y',
      'tl_robot_y',
      'br_robot_y',
      'tl_pp_y',
      'br_pp_y']

for p in pp:
    data[p]=data[p].apply(lambda x : float(x.replace(')', '')))

data['obj_list'] = data['obj_list'].apply(lambda x: str(x))
data['obj_list'] = data['obj_list'].apply(lambda x : '[' + x if x[-1] == ']' else '[]' if x == 'one' else x)

print(len(data.columns))
for i in data.columns:
    print(i, data[i])
