#!/usr/bin/env python3
"""
Description: Custom logger library
Author : Sakharam Thorat
Date   : 04/07/2017
Email  : srt.2011@outlook.com

"""

import logging
from datetime import datetime


def customlogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    logger = logging.getLogger(__name__)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(
    				datetime.now().strftime('%H_%M_%d_%m_%Y_')+'file.log')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
