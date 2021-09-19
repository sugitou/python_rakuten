import requests
import urllib
import numpy as np
import os
import pandas as pd
import pprint
import analysis

# from spreadsheet_manager import SpreadsheetManager
from dotenv import load_dotenv
# .envファイルの内容を読み込みます
load_dotenv()

RAKUTEN_API_ID = int(os.environ["RAKUTEN_API_ID"])
# SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]


def set_url(select_url):
    if select_url == 'market_search':
        url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
        api_flg = 1
    elif select_url == 'book_search':
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
        item_list = alys.extract_market()
    elif api_flg == 2:
        item_list = alys.extract_book()
    else:
        item_list = alys.extract_travel()

    return item_list


def main():
    keyword = input("検索ワードを入力してください。 >>> ")
    # TODO
    url, api_flg = set_url('book_search')
    params = set_param(keyword)
    resp = get_api(url, params)
    # pprint.pprint(resp)

    items = extract(resp, api_flg)
    pprint.pprint(items)
    # データフレームを作成
    # items_df = pd.DataFrame(items)
    # # ヘッダー変更
    # items_df.columns = ['ランキング', '商品名', '商品価格', '説明文', '商品URL', 'ジャンルID']
    # items_df.index = np.arange(1, 31)
    # # csvに出力
    # items_df = items_df.to_csv('./rakuten_ranking.csv',
    #                             columns=['ランキング', '商品名', '商品価格', '説明文', '商品URL', 'ジャンルID'])


if __name__ == "__main__":
   main()