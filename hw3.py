import json

class AdvertProperty:
    pass

class Advert:
    def __init__(self, mapping: dict):


        self.title = mapping['title']
        self.price = mapping['price']
        for item, item_value in mapping.items():
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

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

if __name__ == '__main__':
    lesson_str = """{
    "title": "python", "price": 0,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad)

    # lesson_str = '{"title": "python", "price": -1}'
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson)

    # lesson_str = '{"title": "python"}'
    # lesson = json.loads(lesson_str)
    # lesson_ad = Advert(lesson) 
    # print(lesson_ad.price)
    