import unittest
from regex_custom_dict.regex_custom_dict import RegexCustomDict

class TestRegexCustomDict(unittest.TestCase):
    def setUp(self):
        # Create an instance of RegexCustomDict for testing
        self.custom_dict = RegexCustomDict({
            "name": "John",
            "age": 25,
            "address": {
                "city": "New York",
                "zipcode": "10001",
                "nested_address": {
                    "state": "NY",
                    "country": "USA"
                }
            },
            "start_with_s_1": {
                "item1": "value1",
                "item2": "value2",
                "nested_1": {
                    "subitem1": "subvalue1",
                    "subitem2": "subvalue2"
                }
            },
            "start_with_s_2": {
                "item3": "value3",
                "item4": "value4",
                "nested_2": {
                    "subitem3": "subvalue3",
                    "subitem4": "subvalue4"
                }
            },
            "end_with_1": {
                "item1": "value1",
                "item2": "value2",
                "nested_3": {
                    "subitem5": "subvalue5",
                    "subitem6": "subvalue6"
                }
            },
            "end_with_2": {
                "item3": "value3",
                "item4": "value4",
                "nested_4": {
                    "subitem7": "subvalue7",
                    "subitem8": "subvalue8"
                }
            },
            "contains_1": {
                "item1": "value1",
                "item2": "value2",
                "nested_5": {
                    "subitem9": "subvalue9",
                    "subitem10": "subvalue10"
                }
            },
            "contains_2": {
                "item3": "value3",
                "item4": "value4",
                "nested_6": {
                    "subitem11": "subvalue11",
                    "subitem12": "subvalue12"
                }
            },
            "another_key": "some_value"
        })

    def test_getitem_regex_key_start_with(self):
        result_dict = self.custom_dict["^start_with_s_"].flatten_dict()
        expected_dict = [
            {
                "item1": "value1",
                "item2": "value2",
                "nested_1": {
                    "subitem1": "subvalue1",
                    "subitem2": "subvalue2"
                }
            },
            {
                "item3": "value3",
                "item4": "value4",
                "nested_2": {
                    "subitem3": "subvalue3",
                    "subitem4": "subvalue4"
                }
            }
        ]
        self.assertEqual(result_dict, expected_dict)

    def test_getitem_regex_key_end_with(self):
        result_dict = self.custom_dict["end_with_\\d$"].flatten_dict()
        expected_dict = [
            {
                "item1": "value1",
                "item2": "value2",
                "nested_3": {
                    "subitem5": "subvalue5",
                    "subitem6": "subvalue6"
                }
            },
            {
                "item3": "value3",
                "item4": "value4",
                "nested_4": {
                    "subitem7": "subvalue7",
                    "subitem8": "subvalue8"
                }
            }
        ]
        self.assertEqual(result_dict, expected_dict)

    def test_getitem_regex_key_contains(self):
        result_dict = self.custom_dict["contains_\\d"].flatten_dict()
        expected_dict = [
            {
                "item1": "value1",
                "item2": "value2",
                "nested_5": {
                    "subitem9": "subvalue9",
                    "subitem10": "subvalue10"
                }
            },
            {
                "item3": "value3",
                "item4": "value4",
                "nested_6": {
                    "subitem11": "subvalue11",
                    "subitem12": "subvalue12"
                }
            }
        ]
        self.assertEqual(result_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
