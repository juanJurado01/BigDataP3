
from get_animals import get_animals
import requests
import unittest

class GetAnimals(unittest.TestCase):
    def test_find_animals(self):
        r = requests.get("https://misanimales.com/")
        f = open("file.html", "w", encoding="utf8")
        f.writelines(r.text)
        f.close()
        f2 = open("file.html", "r", encoding="utf8")
        self.assertEqual(len(get_animals(f2))>0, True)
        f2.close()


if __name__ == '__main__':
    unittest.main()
