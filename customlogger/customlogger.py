#!/usr/bin/env python3
"""
Description: Custom logger library
Author : Sakharam Thorat
Date   : 25/07/2018
Email  : srt.2011@outlook.com

"""

import logging
from datetime import datetime

class CustomLogger(object):
    def __init__(self,logLevel=logging.DEBUG):
        # Create the Logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logLevel)

        # Create the file Handler for logging data to a file
        fileHandler = logging.FileHandler(
                    datetime.now().strftime('%H_%M_%d_%m_%Y_')+'file.log')
        fileHandler.setLevel(logLevel)

        # Create a Formatter for formatting the log messages
        formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

        # Add the Formatter to the Handler
        fileHandler.setFormatter(formatter)

        # Add the file Handler to the Logger
        self.logger.addHandler(fileHandler)
        self.logger.info('Completed configuring logger()!')

################################################################################
    def debug(self, msg):
        self.logger.debug(msg)

################################################################################
    def info(self, msg):
        self.logger.info(msg)

################################################################################
    def warning(self, msg):
        self.logger.warning(msg)

################################################################################
    def error(self, msg):
        self.logger.error(msg)

################################################################################

