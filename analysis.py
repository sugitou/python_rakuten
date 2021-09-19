class Analysis:
    def __init__(self, rakuten_data):
        self.rakuten_data=rakuten_data


    def extract_market(self):
        # for文を回してdictを作る
        item_key = ['title', 'itemPrice', 'itemCaption', 'itemUrl', 'genreId']
        item_list = []
        for i in range(0, len(self.rakuten_data['Items'])):
            tmp_item = {}
            item = self.rakuten_data['Items'][i]['Item']
            for key, value in item.items():
                if key in item_key:
                    tmp_item[key] = value
            item_list.append(tmp_item.copy())
    
        return item_list


    def extract_book(self):
        # for文を回してdictを作る
        item_key = ['itemName', 'itemPrice', 'itemCaption', 'itemUrl', 'booksGenreId']
        item_list = []
        for i in range(0, len(self.rakuten_data['Items'])):
            tmp_item = {}
            item = self.rakuten_data['Items'][i]['Item']
            for key, value in item.items():
                if key in item_key:
                    tmp_item[key] = value
            item_list.append(tmp_item.copy())
    
        return item_list


    def extract_travel(self):
        # for文を回してdictを作る
        hotel_key = ['hotelName', 'hotelMinCharge', 'hotelSpecial', 'hotelInformationUrl', 'hotelNo']
        hotel_list = []
        for i in range(0, len(self.rakuten_data['hotels'])):
            tmp_hotel = {}
            item = self.rakuten_data['hotels'][i]['hotel'][0]['hotelBasicInfo']
            for key, value in item.items():
                if key in hotel_key:
                    tmp_hotel[key] = value
            hotel_list.append(tmp_hotel.copy())
    
        return hotel_list