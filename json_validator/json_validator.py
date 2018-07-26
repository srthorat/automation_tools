#!/usr/bin/env python3
"""
Description: Json schema validation library
Author : Sakharam Thorat
Date   : 06/06/2018
Email  : srt.2011@outlook.com

"""
import sys
import os.path
import jsonschema

class JsonValidator(object):
	
	def validate(self,json_obj, ref_schema):
		'''
        Validate json_obj with reference schema
        Params:
            json_obj:
                received json object
            ref_schema:
            	reference schema to validate
        Return:
            0:
            	if received json schema validated sucessfully
            -1:
            	if received json schema failed to validate
        '''
		try:
			if jsonschema.validate(json_obj, ref_schema) == None:
				return 0
		except Exception as e:
			print(f"Exception {e} occured while validation schema")
			return -1
