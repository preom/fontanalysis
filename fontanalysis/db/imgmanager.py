import logging
import os
import string
from PIL import Image, ImageFont, ImageDraw
import sys

import pprint
import pdb

from dbsettings import Session, imgDepotPth, mainDbDirPth
from font import Font, FontImage
from fontmanager import fontpath


def gen_letter_img(char, ffpath):
    """
        Args:
         ffpath: fontfilepath
    """
    
    try:
        font = ImageFont.truetype(ffpath, size=100)
    except:
        logging.warning("Could not load font {}: {}".format(
            ffpath, sys.exc_info()[0]))

    img = Image.new('L', font.getsize(char), 'white')
    draw = ImageDraw.Draw(img)

    draw.text((0,0), char, font=font)

    return img

def imgpath(fontid, char, absPath=False):
    imgExt = '.png'
    fontid = str(fontid)

    result = os.path.join(imgDepotPth, fontid, char + imgExt)

    if absPath:
        result = (os.path.join(mainDbDirPth, result))

    return result

def main():
    logging_lvl = logging.INFO

    logging.basicConfig(file='logs/imgmanager.log', level=logging_lvl)

    # gen_letter_img('x', 'depot/fontdepot/1.otf')

    oldpath = os.getcwd()
    os.chdir(mainDbDirPth)

    session = Session()
    query = session.query(Font.id). \
            outerjoin(FontImage). \
            filter(FontImage.id == None).all()



    for (fontId,) in query: 
        imgfolder = os.path.join(imgDepotPth, str(fontId))
        try:
            os.mkdir(imgfolder)
        except:
            logging.warning("Could not create: ", imgfolder)

        for char in string.letters:
            fntImg = FontImage(fontname=fontId, character=char)
            img = gen_letter_img(char, fontpath(fontId))
            img.save(imgpath(fontId, char))
            print (imgpath(fontId, char))
            session.add(fntImg)

        session.commit()


    os.chdir(oldpath)


if __name__ == "__main__":
    main()
