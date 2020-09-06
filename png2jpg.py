# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 00:25:49 2020

@author: Haijie
"""
import glob
import os
from PIL import Image
 

for file in glob.glob("*.png"):
    im = Image.open(file)
    rgb_im = im.convert('RGB')
    rgb_im.save(file.replace("png", "jpg"), quality=95)
    os.remove(file)