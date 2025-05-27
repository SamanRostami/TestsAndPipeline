import unittest
import csv
import json

class TestDataFiles(unittest.TestCase):
    def test_always_true(self):
        self.assertTrue(1 == 1)

    def test_csv_column_count(self):
        with open('Data/profiles1.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            first_row = next(reader)
            self.assertEqual(len(first_row), 12, "CSV-filen ska innehålla 12 kolumner")

    def test_csv_row_count(self):
        with open('Data/profiles1.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertGreaterEqual(len(rows), 900, "CSV-filen ska innehålla minst 900 rader")

    def test_fail():
        assert False, "Det här testet ska alltid faila"

    def test_json_properties(self):
        expected_properties = {"Givenname", "Surname", "Streetaddress", "City", "Zipcode",
            "Country", "CountryCode", "NationalId", "TelephoneCountryCode",
            "Telephone", "Birthday", "ConsentToContact"}  
        with open('Data/profiles1.json', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            for item in data:
                self.assertTrue(expected_properties.issubset(item.keys()), "JSON-objekt saknar en eller flera properties")

    def test_json_row_count(self):
        with open('Data/profiles1.json', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            self.assertGreaterEqual(len(data), 900, "JSON-filen ska innehålla minst 900 rader")

if __name__ == '__main__':
    unittest.main()


