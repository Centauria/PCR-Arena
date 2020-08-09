# -*- coding: utf-8 -*-
import atexit
import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)

db_name = 'redive_cn.db'
if not os.path.exists(db_name):
    from .update_db import update_db

    update_db(db_name)

logger.info('Generating model/model.py')
os.system(f'sqlacodegen sqlite:///{db_name} --outfile model/model.py')
logger.info('Creating engine')
engine = create_engine(f'sqlite:///{db_name}')
Session = sessionmaker(engine)


@atexit.register
def at_exit():
    Session.close_all()
