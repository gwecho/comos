#!/usr/bin/env python
#encoding:utf8

import requests
import json
import traceback
import time

"""
filter documents by engine and process them
param:
    query_str:lucene query str _id:fidjij2344232
    fl: filted field list: title,online...
    callback
Exception:
    retry num of requesting search api exceed the max retry num
    the return data format or content error
    Exceptions of the callback
"""
def search_and_proc(query_str, fl, callback):
    results = []
    search_api = "http://0.0.0.0/fullsearch/"    
    page = 1 
    num_found = 1
    max_retry = 10 
    retry = 0 
    while(num_found and retry < max_retry):
        ret = requests.get(search_api, params={"query":query_str,
        	"pid":31,"tid":1,"fields":fl, "page":page, "offset":100})
        ret_dct = json.loads(ret.content)
        if not ret.ok:
            print "requests api Error![{error_code}]:{error_msg}".\
                  format(error_code=ret_dct['result']['status']['code'],
                    error_msg=ret_dct['result']['status']['msg'])
            time.sleep(1)
            retry += 1
            continue
        try:
            num_found = len(ret_dct['results'])
            results.extend(ret_dct['results']) 
        except Exception, e:
            raise Exception(repr(e))
        page += 1

    if retry == max_retry:
        raise Exception("{api} Error after {retry} retries".format(api=search_api, retry=retry))
    print len(results) 
    callback(results)
