# Description: This is a script control the patent number crawler from crawlering different patent number




from scrapy.crawler import CrawlerProcess
from test_project.turtriol.turtriol.spiders.paten_number_crawler import PatentCrawler
import csv


base_url = 'https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/'


# get the patent number csv
input_file = open('patentNO.csv', 'r')
csv_file_reader = csv.reader(input_file)
for number in csv_file_reader:
    # Join the elements of the item list and remove brackets, quotes, and commas
    patent_no = ''.join(number).replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
    
    # Construct the URL with the cleaned-up patent number
    url = base_url + patent_no
    # Create a new instance of the PatentCrawler spider
    crawler = CrawlerProcess()
    crawler.crawl(PatentCrawler, url=url)
    # Start the crawling process
    crawler.start()

    
    