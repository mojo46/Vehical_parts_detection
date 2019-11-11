from icrawler.builtin import GoogleImageCrawler 

import sys, ast

colours = ["Red", "Moonlight Silver",
           "Zanskar Blue", "OUTBACK BRONZE", "Cool White"]
car_model = ["KWID STD", "KWID RXE", "KWID RXL", "KWID RXT", "KWID 1.0 RXT", "KWID 1.0 RXT Opt", "KWID Climber 1.0 MT",
             "KWID Climber 1.0 MT Opt", "KWID 1.0 RXT AMT", "KWID 1.0 RXT AMT Opt", "KWID Climber 1.0 AMT", "KWID Climber 1.0 AMT Opt"]
parts_ref=[]

for car in car_model:
    for clr in colours:
        cmb = car + " "+clr
        parts_ref.append(cmb)

# parts_ref = ['Renault Duster']
for pf in parts_ref:
    google_crawler = GoogleImageCrawler(storage={'root_dir': pf})
    print("#########################  Crawling google images for ",pf)
    google_crawler.crawl(keyword=pf, offset=0, max_num=100,
                     date_min=None, date_max=None, feeder_thr_num=1,
                     parser_thr_num=1, downloader_thr_num=4,
                     min_size=(200,200), max_size=None)
    print("########################## Image crawling is done for ",pf)
