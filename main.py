# -*- coding: utf-8 -*-
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s: %(name)s-%(levelname)s: %(message)s'
)

if __name__ == '__main__':
    from model import Session
    from model.model import *

    session = Session()
    unit = session.query(UnitDatum).filter(UnitDatum.unit_id == 100101).one()
    print(unit.unit_name)
    session.close()
