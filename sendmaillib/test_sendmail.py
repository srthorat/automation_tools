#!/usr/bin/env python3
"""
Description: Test script for custom logger
Author : Sakharam Thorat
Date   : 06/06/2018
Email  : srt.2011@outlook.com

"""

import sendmail as sm
import unittest

class SendMailTestCase(unittest.TestCase):

	def setUp(self):
			self.sendmail = sm.SendEmailUtility("xxx@gmail.com", "xxxxxx",
								"smtp.gmail.com", "xxxx@gmail.com")

	def test_json_validator(self):
		self.assertNotEqual(self.sendmail.send("SmokeTestReport.html"), -1)

if __name__ == '__main__':
    unittest.main()