import pycountry
import os
import datetime
from browsepy import db, models


dirname="/mnt/UNISDR/"

def get_dir_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            p = os.path.join(dirpath, f)
            size = os.path.getsize(p)
            total_size += size
    return total_size

def update_db():
    for root, dirs, files in os.walk(dirname):
        for dir in dirs:
            p = os.path.join(root,dir)
            print p
            size = get_dir_size(p)
            try:
                meta = models.Metadata.query.filter_by(path=p).one()
            except:
                meta = models.Metadata()
                meta.path = p
            finally:
                meta.size = size
                meta.size_date = datetime.datetime.now()
                db.session.add(meta)
                db.session.commit()

def add_descriptions():
    dirname="/mnt/UNISDR/Hazard/Flood scenarios"
    for filename in os.listdir(dirname):
        meta = models.Metadata.query.filter_by(path=os.path.join(dirname, filename)).one()
        print meta.path
        print meta.size
        meta.desc = pycountry.countries.get(alpha_2=filename.split('.')[0]).name
        print meta.desc
        db.session.commit()

    dirname = "/mnt/UNISDR/Exposure"
    for root, dirs, files in os.walk(dirname):
        for name in files:
            path = (os.path.join(root, name))
            countrycode = path.split('_')[1].split('.')[0]
            desc = pycountry.countries.get(alpha_3=countrycode.upper()).name
            try:
                meta = models.Metadata.query.filter_by(path=path).one()
                meta.desc = desc
                db.session.commit()
            except:
                meta = models.Metadata()
                meta.path = path
                meta.desc = desc
                db.session.add(meta)
                db.session.commit()



    


