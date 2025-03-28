# -*- coding: utf-8 -*-
"""Refget Service Info, used for /sequence/service-info endpoint"""


SERVICE_INFO = {
    "id": "",
    "name": "",
    "type": {
        "group": "org.ga4gh",
        "artifact": "refget",
        "version": "2.0.0"
    },
    "organization": {},
    "version": "2.0.0",
    "refget": {
       "circular_supported": False,
       "subsequence_limit": 300000,
       "algorithms":  ["md5", "ga4gh"],
       "identifier_types": ["insdc", "refseq"],
    }
}
"""Refget Service Info Dictionary"""
