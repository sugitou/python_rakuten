class Analysis:
    def __init__(self, rakuten_data):
        self.res_name = []
        self.res_list = []
        self.rakuten_data = rakuten_data


    def extract_market(self):
        item_key = ['itemName', 'itemPrice', 'itemCaption', 'itemUrl', 'genreId']
        item_head = ['商品名', '商品価格', '説明文', '商品URL', 'ジャンルID']
        for i in range(0, len(self.rakuten_data['Items'])):
            tmp_item = {}
            item = self.rakuten_data['Items'][i]['Item']
            for key, value in item.items():
                if key in item_key:
                    tmp_item[key] = value
                    if key == 'itemName':
                        self.res_name.append(value + '\n')
            self.res_list.append(tmp_item.copy())
    
        return self.res_list, item_key, item_head, self.res_name


    def extract_book(self):
        item_key = ['title', 'itemPrice', 'itemCaption', 'itemUrl', 'booksGenreId']
        item_head = ['商品名', '商品価格', '説明文', '商品URL', 'ブックジャンルID']
        for i in range(0, len(self.rakuten_data['Items'])):
            tmp_item = {}
            item = self.rakuten_data['Items'][i]['Item']
            for key, value in item.items():
                if key in item_key:
                    tmp_item[key] = value
                    if key == 'title':
                        self.res_name.append(value + '\n')
            self.res_list.append(tmp_item.copy())
    
        return self.res_list, item_key, item_head, self.res_name


    def extract_travel(self):
        hotel_key = ['hotelName', 'hotelMinCharge', 'hotelSpecial', 'hotelInformationUrl', 'hotelNo']
        hotel_head = ['ホテル名', '最低宿泊価格', 'ホテルの特色', 'メインページURL', 'ホテルID']
        for i in range(0, len(self.rakuten_data['hotels'])):
            tmp_hotel = {}
            item = self.rakuten_data['hotels'][i]['hotel'][0]['hotelBasicInfo']
            for key, value in item.items():
                if key in hotel_key:
                    tmp_hotel[key] = value
                    if key == 'hotelName':
                        self.res_name.append(value + '\n')
            self.res_list.append(tmp_hotel.copy())
    
        return self.res_list, hotel_key, hotel_head, self.res_name