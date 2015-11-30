#!/usr/bin/env python
#coding:utf8

from search_and_proc import search_and_proc

def main():
    def func(data):
        with open("finance_news_1115_1121_urls.log", "w") as f:
            for news in data:
                try:
                    f.write(news['url'].decode("utf-8"))            
                    f.write("\n")
                except Exception as e:
                    print repr(e)

    search_and_proc("published:y AND deleted:n AND createtime:[2015\-11\-15T00\:00\:00Z TO 2015\-11\-22T00\:00\:00Z]", "did,url", func)

if __name__ == "__main__":
"""
  get published news urls of finance channel from 2015-11-15 to 2015-11-22
"""
    main()
