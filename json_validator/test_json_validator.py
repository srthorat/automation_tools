#!/usr/bin/env python3
"""
Description: Test script for custom logger
Author : Sakharam Thorat
Date   : 06/06/2018
Email  : srt.2011@outlook.com

"""

import logging
import json_validator as jv
import unittest
from reference_schema import *


class JsonValidatorTestCase(unittest.TestCase):

	def setUp(self):
			self.jsonvalidate = jv.JsonValidator()
			self.response =[{"caid":"CAID75C3E8E7FC9E4702B79143C04ECB4AC3",
							"followed_at":"2018-04-22T13:02:18.000Z"},
							{"caid":"CAID44CA82AB9D9D42CCAEEFB66870A245F4",
							"followed_at":"2018-04-18T20:41:29.000Z"},
]

	def test_json_validator(self):
		self.assertNotEqual(self.jsonvalidate.validate(self.response,
							followers_list), -1)

if __name__ == '__main__':
    unittest.main()