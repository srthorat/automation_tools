#!/usr/bin/env python3
"""
Description: Reference json schema
Author : Sakharam Thorat
Date   : 06/06/2018
Email  : srt.2011@outlook.com

"""
followers_list = {
  "$id": "http://example.com/example.json",
  "type": "array",
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "items": {
    "$id": "http://example.com/example.json/items",
    "type": "object",
    "minProperties": 1,
    "properties": {
      "caid": {
        "$id": "http://example.com/example.json/items/properties/caid",
        "type": "string",
        "title": "The Caid Schema ",
        "default": "",
        "examples": [
          "CAID75C3E8E7FC9E4702B79143C04ECB4AC3"
        ]
      },
      "followed_at": {
        "$id": "http://example.com/example.json/items/properties/followed_at",
        "type": "string",
        "title": "The Followed_at Schema ",
        "default": "",
        "examples": [
          "2018-04-22T13:02:18.000Z"
        ]
      }
    },
    "required": [
      "caid",
      "followed_at"
    ]
  }
}
