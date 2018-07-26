#!/usr/bin/env python3
"""
Description: Test script for custom logger
Author : Sakharam Thorat
Date   : 04/07/2017
Email  : srt.2011@outlook.com

"""

import logging
import customlogger as cl
import unittest


class CustomloggerTestCase(unittest.TestCase):

	def setUp(self):
			self.logger=cl.CustomLogger()

	def test_logger_info_level(self):
		self.assertNotEqual(self.logger.info('''This is a test for logger with 
							info log level'''), -1)

if __name__ == '__main__':
    unittest.main()