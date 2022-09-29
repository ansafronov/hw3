import unittest
import json
from Advert import Advert

class MyTestCase(unittest.TestCase):
    def test_constructor_dict(self):
        lesson_str = """{
            "title": "python", "price": 0,
            "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]
                }
            }"""
        lesson = json.loads(lesson_str)
        try:
            lesson_ad = Advert(lesson)
        except Exception as e:
            self.fail('Class not set', e)

    def test_constructor_tuple_1(self):
        try:
            lesson_ad = Advert('IPhoneX')
        except Exception as e:
            self.fail('Class not set', e)
        lesson_ad = Advert('IPhoneX')
        self.assertTrue(hasattr(lesson_ad, 'price'))

    def test_constructor_tuple_2(self):
        try:
            lesson_ad = Advert('IPhoneX', 100)
        except Exception as e:
            self.fail('Class not set', e)
        lesson_ad = Advert('IPhoneX', 100)
        self.assertTrue(hasattr(lesson_ad, 'price'))

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            Advert('IPhoneX', -100)

    def test_dot_access(self):
        lesson_str = """{
                    "title": "python", "price": 0,
                    "location": {
                        "address": "город Москва, Лесная, 7",
                        "metro_stations": ["Белорусская"]
                        }
                    }"""
        lesson = json.loads(lesson_str)
        lesson_ad = Advert(lesson)
        self.assertTrue(hasattr(lesson_ad, 'location'))
        self.assertTrue(hasattr(lesson_ad.location, 'address'))

    def test_repr(self):
        korgi = {
            "title": "Вельш-корги",
            "price": 1000,
            "class": "dogs",
            "location": {
                "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            }
        }
        korgi_ad = Advert(korgi)
        self.assertTrue(repr(korgi_ad) == 'Вельш-корги | 1000 ₽')

if __name__ == '__main__':
    unittest.main()
