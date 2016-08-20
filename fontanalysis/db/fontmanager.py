import argparse
import logging

from dbsettings import Session, fntDepotPth, mainDbDirPth
from font import Font

import os
import shutil
import pdb

def add_font_db(fpath):
    fext = os.path.splitext(fpath)[1] # file extension
    successFlag = True

    fontRow = Font(name=os.path.basename(fpath), ext=fext, src=fpath)

    session = Session()
    session.add(fontRow)
    session.flush()
    session.refresh(fontRow)

    fname = str(fontRow.id) + fext

    try: 
        shutil.copy(fpath, os.path.join(fntDepotPath, fname))
    except:
        logging.error('error, could not copy file {}'.format(fpath))
        successFlag = False

    if (successFlag):
        session.commit()

    return successFlag

def isfontfile(fpath):
    valid_extensions = ['.ttf', '.otf']
    return os.path.splitext(fpath)[1] in valid_extensions

def fontpath(id):
    session = Session()
    q = session.query(Font).filter(Font.id==id).first()
    return os.path.join(fntDepotPth, str(q.id) + q.ext)

def main():

    oldpath = os.getcwd()
    os.chdir(mainDbDirPth)

    logging.basicConfig(filename='logs/fontmanager.log', level=logging.INFO)


    parser = argparse.ArgumentParser(description='Add font file to db')
    parser.add_argument('fpaths', help='filepath to font file', action='append')

    args = vars(parser.parse_args())

    fpaths = [os.path.join(oldpath, fpath) for fpath in args['fpaths']]

    error = []
    success = []
    dirFiles = []

    for fpath in fpaths:
        if os.path.isdir(fpath):
            dirlisting = [os.path.join(fpath, i) for i in os.listdir(fpath)]
            for f in dirlisting:
                if os.path.isfile(f) and isfontfile(f):
                    dirFiles.append(f)

    fpaths.extend(dirFiles)

    for fpath in fpaths: 
        if not os.path.isfile(fpath):
            error.append((fpath, 'Is not a file'))
        elif not isfontfile(fpath):
            error.append((fpath, 'Not a valid filetype'))
        else:
            if add_font_db(fpath):
                success.append(fpath)
            else:
                error.append(fpath, 'Error in db or copying operation')

    logging.info('Success - ' + str(success))
    logging.info('Error - ' + str(error))

    add_font_db(fpath)    

    os.chdir(oldpath)

if __name__ == '__main__':
    main()
