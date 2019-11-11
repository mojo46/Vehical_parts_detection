from icrawler.builtin import GoogleImageCrawler
import sys
import ast

query = "KWID STD"

google_crawler = GoogleImageCrawler(storage={'root_dir': query})
google_crawler.crawl(keyword=query, offset=0, max_num=400)
