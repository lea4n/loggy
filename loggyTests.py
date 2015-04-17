#!/usr/bin/python

import unittest,json
from loggy import pickMessageByIndex, getEntriesPerOS

class LoggyTests(unittest.TestCase):

    def testPickMessageByIndex(self):
        with open('loggy.data') as data_file:
            data = json.load(data_file)
        output = pickMessageByIndex(data, "Linux", "Lin1")
        self.assertEqual(output, "Linux syslog test message one")

    def testGetEntriesPerOS(self):
        with open('loggy.data') as data_file:
            data = json.load(data_file)
        output = getEntriesPerOS(data, "Linux")
        self.assertEqual(output, 2)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
