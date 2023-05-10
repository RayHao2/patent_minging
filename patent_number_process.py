# Description: This is a script control the patent number crawler from crawlering different patent number




from scrapy.crawler import CrawlerProcess
from test_project.turtriol.turtriol.spiders.paten_number_crawler import PatentCrawler
import csv
from datetime import datetime
import time
import random
import os


base_url = 'https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/'


# get the patent number csv
input_file = open('patentNO.csv', 'r')
csv_list = list(csv.reader(input_file))
list_len = len(csv_list)
count = 0

while(count < list_len):
    current_hour = datetime.now().hour
    # If current hour is with in 8am to 5pm, do the fetchy
    if(current_hour >= 8 and current_hour <= 17):
        patent_no = csv_list[count]
        # Join the elements of the item list and remove brackets, quotes, and commas
        patent_no = ''.join(number).replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
        # Construct the URL with the cleaned-up patent number
        url = base_url + patent_no
        # Create a new instance of the PatentCrawler spider
        crawler = CrawlerProcess()
        crawler.crawl(PatentCrawler, url=url)
        # Start the crawling process
        crawler.start()
    
    # Plus one to count
    count += 1
    # random from 30 mins to one hour 
    random_time = random.randint(30,60)
    random_time = random_time * 60 #conver to second
    time.sleep(random_time)
    
        

