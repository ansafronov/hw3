import json

class AdvertProperty:
    pass

class Advert:
    def __init__(self, json_dict: dict):
        self.json_dict = json_dict
        for item, item_value in json_dict.items():
            setattr(self, item, self._parse(item_value))  
        
        self._check_price()

    def _parse(self, json_object: dict):
        if isinstance(json_object, dict):
            value = AdvertProperty()
            for item, item_value in json_object.items():
                setattr(value, item, self._parse(item_value))
        else:
            value = json_object
        return value     

    def _check_price(self):
        if hasattr(self, "price"):
            if self.price < 0:
                raise ValueError("must be >= 0")
        else:
            self.price = 0

if __name__ == '__main__':
    # lesson_str = """{
    # "title": "python", "price": 0,
    # "location": {
    #     "address": "город Москва, Лесная, 7",
    #     "metro_stations": ["Белорусская"]
    #     }
    # }"""
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)
    # print(lesson_ad.location.address)

    # lesson_str = '{"title": "python", "price": -1}'
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)

    # lesson_str = '{"title": "python"}'
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson) 
    # print(lesson_ad.price)
    