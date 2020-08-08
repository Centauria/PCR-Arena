# -*- coding: utf-8 -*-
import brotli
import requests


def update_db():
    url = 'https://redive.estertion.win/db/redive_cn.db.br'
    r = requests.get(url)
    with open('redive_cn.db', 'wb') as f:
        f.write(brotli.decompress(r.content))


if __name__ == '__main__':
    update_db()
