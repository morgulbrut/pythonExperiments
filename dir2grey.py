#!/usr/bin/env python3

# # QT Buttons 1
# 
# Converts all images in a dir to greyscale adding a prefix

from PIL import Image
import os

prefix='inactive'

included_extenstions = ['jpg', 'bmp', 'png', 'gif']
file_names = [fn for fn in os.listdir() if any(fn.endswith(ext) for ext in included_extenstions)]

for f in file_names:
    img = Image.open(f).convert('LA')
    img.save(prefix+'_'+f)

