import json


class AdvertProperty:
    pass


class ColorMixin:
    def __repr__(self):
        return f"\033[1;{self.repr_color_code};40m{self.title} | {self.price}\033[0m"


class Advert(ColorMixin):
    def __init__(self, *args):
        """
        Initialize the Advertisment object.
        If price was not passed, it initializes with 0.
        Supports multiple input patterns. Cloud be initialized from:
        * dict object
        * One argument -- only title will be set
        * Two arguments -- title and price
        >>> Advert({'title': 'Kite', 'price': 1000})
        'Kite | 1000 ₽'
        >>> Advert('Kite')
        'Kite | 0 ₽'
        >>> Advert('Kite', 1000)
        'Kite | 1000 ₽'
        """
        self.repr_color_code = 32
        if len(args) == 1 and isinstance(args[0], dict):
            # dictionary initialization
            for item, item_value in args[0].items():
                setattr(self, item, self._parse(item_value))
            self._check_title()
        elif len(args) == 1:
            # only title initialization
            self.title = args[0]
        elif len(args) == 2:
            # title and price initialization
            self.title = args[0]
            self.price = args[1]
        elif len(args) == 0:
            # empty initialization
            pass
        else:
            raise ValueError('Invalid input pattern')
        self._check_price()

    def _parse(self, json_object: dict):
        """
        Parse the dictionary to create intermediate objects
        """
        if isinstance(json_object, dict):
            value = AdvertProperty()
            for item, item_value in json_object.items():
                setattr(value, item, self._parse(item_value))
        else:
            value = json_object
        return value

    def _check_price(self):
        """
        check if price is valid or set price = 0
        """
        if hasattr(self, 'price'):
            if self.price < 0:
                raise ValueError("must be >= 0")
        else:
            self.price = 0

    def _check_title(self):
        if not hasattr(self, 'title'):
            raise ValueError('title attribute is not set')

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
