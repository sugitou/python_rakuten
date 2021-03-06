from rakuten_api import *


RAKUTEN_API_ID = int(os.environ["RAKUTEN_API_ID"])

def test_set_param():
    test_key = "鬼滅"
    res = set_param(test_key)
    assert res

def test_get_api():
    param = {
        "format" : "json",
        "keyword" : "鬼滅",
        "applicationId" : RAKUTEN_API_ID,
    }
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
    res = get_api(url, param)

    assert len(res['Items']) >= 1
    assert res['Items'][0]['Item']['itemName']
