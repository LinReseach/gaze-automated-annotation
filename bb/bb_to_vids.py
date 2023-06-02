import pandas as pd
from readbbtxt import readbbtxt

data = readbbtxt()
print(data['obj_list'])