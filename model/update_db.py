# -*- coding: utf-8 -*-
import logging

import brotli
import requests

logger = logging.getLogger(__name__)


def update_db(db_name: str):
    url = 'https://redive.estertion.win/db/redive_cn.db.br'
    logger.info(f'Getting Princess Connect Re:Dive CN Database at {url}')
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        logger.warning('Connection problem')
    with open(db_name, 'wb') as f:
        f.write(brotli.decompress(r.content))


if __name__ == '__main__':
    update_db('redive_cn.db')
