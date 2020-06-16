from PIL import Image
import easygui
import os
import sys

diabox = easygui.fileopenbox()
os.chdir(os.path.dirname(diabox))

try:
    img = Image.open(diabox)
    data = img.getdata()
    data_len = len(list(data))

except:
    print('Invalid file type')
    sys.exit()

red = 0
green = 0
blue = 0

for pix in data:
    r, g, b = pix
    red += r
    green += g
    blue += b

print(f'Average RGB of image: ({red/data_len}, {green/data_len}, {blue/data_len})')