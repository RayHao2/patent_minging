from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exporters import CsvItemExporter
from scrapy.utils.project import get_project_settings


class staff_crawler(CrawlSpider):
    name = "test_crawler"
    # allowed_domains = ["toscrape.com"]
    start_urls = ["file:///C:/Users/haoju/OneDrive/Desktop/Faculty%20A-Z%20_%20Oregon%20State%20University.html"]
    
    rules = (
        Rule(LinkExtractor(), callback = "parse_item"),
    )
    
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'output.csv'
    }
    
    def parse_item(self, response):
        faculty_names = response.css(".faculty-item strong::text").getall()
        for name in faculty_names:
            item = {'faculty_name': name}
            yield item

        settings = get_project_settings()
        exporter = CsvItemExporter(open(settings['FEED_URI'], 'a+b'))
        exporter.start_exporting()
        for item in faculty_names:
            exporter.export_item(item)
        exporter.finish_exporting()


        
