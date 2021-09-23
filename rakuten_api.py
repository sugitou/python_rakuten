import requests
import urllib
import numpy as np
import os
import pandas as pd
import pprint
import analysis

from dotenv import load_dotenv
# .envファイルの内容を読み込みます
load_dotenv()

RAKUTEN_API_ID = int(os.environ["RAKUTEN_API_ID"])


def set_url(select_url):
    if select_url == 'market_search':
        url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
        api_flg = 1
    elif select_url == 'books_search':
        url = 'https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404'
        api_flg = 2
    else:
        url = 'https://app.rakuten.co.jp/services/api/Travel/KeywordHotelSearch/20170426'
        api_flg = 3
    return url, api_flg

def set_param(keyword=''):
    param = {
        "format" : "json",
        "keyword" : keyword,
        "applicationId" : RAKUTEN_API_ID,
    }
    return param


def get_api(url, params):
    result = requests.get(url, params)
    return result.json()


def extract(resp, api_flg):
    alys = analysis.Analysis(resp)
    if api_flg == 1:
        list_key_head_name = alys.extract_market()
    elif api_flg == 2:
        list_key_head_name = alys.extract_book()
    else:
        list_key_head_name = alys.extract_travel()

    return list_key_head_name


def crdir(fdname):
    new_dir = f'{os.getcwd()}\\{fdname}'
    # 指定ディレクトリ作成
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    return new_dir


def main(skw, csv_name, box_name, api):
    # TODO
    url, api_flg = set_url(api)
    params = set_param(skw)
    resp = get_api(url, params)
    # pprint.pprint(resp)

    items, head_key, header, name = extract(resp, api_flg)
    # データフレームを作成
    items_df = pd.DataFrame(items)
    # csvに出力
    csv_path = f'{crdir(box_name)}/{csv_name}.csv'
    create_df = items_df.to_csv(csv_path, header=False, index=False, columns=head_key)
    # ヘッダー書き換え
    change_head_df = pd.read_csv(csv_path, encoding="utf-8_sig", names=header)
    recreate_df = change_head_df.to_csv(csv_path)

    return name
