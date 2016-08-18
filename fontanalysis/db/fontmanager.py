import argparse
import logging

from dbsettings import Session
from font import Font

import os
import shutil


def main():

    oldpath = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    logging.basicConfig(filename='logs/fontmanager.log', level=logging.INFO)

    session = Session()

    parser = argparse.ArgumentParser(description='Add font file to db')
    parser.add_argument('fpath', help='filepath to font file')

    args = vars(parser.parse_args())


    fpath = os.path.join(oldpath, args['fpath'])
    successFlag = True

    fontRow = Font(name=os.path.basename(fpath), fname='')

    session.add(fontRow)
    session.commit()
    session.refresh(fontRow)

    print 'session'
    print session.query(Font).filter_by(id=1).first()
    print 'session end'

    fext = os.path.splitext(fpath)[1] # file extension
    fname = str(fontRow.id) + fext

    try: 
        shutil.copy(fpath, os.path.join('fontdepot', fname))
    except:
        logging.error('error, could not copy file')
        successFlag = False

    print fname
    logging.info(args['fpath'])

    os.chdir(oldpath)

if __name__ == '__main__':
    main()
