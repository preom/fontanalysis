import shutil

from fontanalysis.db import imgmanager

shutil.copy(imgmanager.imgpath(1, 'c', True), './c1.png')
shutil.copy(imgmanager.imgpath(2, 'c', True), './c2.png')
