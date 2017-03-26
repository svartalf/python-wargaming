import unittest
from wargaming import parser
from datetime import datetime


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser(fields=[
            {
                "name": [
                        "integer",
                ],
                "type": "numeric",
            },
            {
                "name": [
                    "timestamp",
                ],
                "type": "timestamp",
            },
            {
                "name": [
                    "list of timestamps",
                ],
                "type": "list of timestamps",
            },
            {
                "name": [
                    "list of integers",
                ],
                "type": "list of integers",
            },
            {
                "name": [
                    "list of strings",
                ],
                "type": "list of strings",
            },
            {
                "name": [
                    "section1",
                ],
                "type": "block_header",
            },
            {
                "name": [
                    "section1",
                    "timestamp",
                ],
                "type": "timestamp",
            },
            {
                "name": [
                    "section2",
                ],
                "type": "block_header",
            },
            {
                "name": [
                    "section2",
                    "string",
                ],
                "type": "string",
            },
            {
                "name": [
                    "section2",
                    "integer",
                ],
                "type": "numeric",
            },
        ])
        self.sample_record = {
            "integer": "1",
            "timestamp": 0,
            "list of timestamps": [1, 2],
            "list of integers": [1, 2, 3],
            "list of strings": [1, 2, 3],
            "section1": {"timestamp": 0},
            "section2": [{"integer": 0, "string": 0}, {"integer": 0, "string": "0"}],
        }
        self.sample_converted_record = {
            "integer": 1,
            "timestamp": datetime.fromtimestamp(0),
            "list of timestamps": [
                datetime.fromtimestamp(1),
                datetime.fromtimestamp(2),
            ],
            "list of integers": [1, 2, 3],
            "list of strings": ["1", "2", "3"],
            "section1": {"timestamp": datetime.fromtimestamp(0)},
            "section2": [{"integer": 0, "string": "0"}, {"integer": 0, "string": "0"}],
        }

    def test_parser_singe_record(self):
        data = self.parser.parse_response_data(self.sample_record)
        self.assertEqual(data, self.sample_converted_record)

    def test_parser_list_of_records(self):
        data = self.parser.parse_response_data([self.sample_record] * 2)
        self.assertEqual(data, [self.sample_converted_record] * 2)

    def test_parser_set_of_records(self):
        data = self.parser.parse_response_data({
            "123": self.sample_record,
            "321": self.sample_record,
        })
        self.assertEqual(data, {
            "123": self.sample_converted_record,
            "321": self.sample_converted_record,
        })
