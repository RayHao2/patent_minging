import scrapy
import os

class PatentCrawler(scrapy.Spider):
    name = 'patent_crawler'

    def __init__(self, url=None, *args, **kwargs):
        super(PatentCrawler, self).__init__(*args, **kwargs)
        self.start_urls = [url]
        self.output_folder = 'C:/Users/haoju/OneDrive/Desktop/school/patent_minging/output'

    def parse(self, response):
        # Extract the file name from the URL
        if response.status == 400:
            self.logger.error('Received a 400 status code for URL: %s', response.url)
            return
        file_name = response.url.split('/')[-1] + '.pdf'
        # Create the output folder if it doesn't exist
        os.makedirs(self.output_folder, exist_ok=True)

        # Save the PDF file to the output folder
        with open(os.path.join(self.output_folder, file_name), 'wb') as f:
            f.write(response.body)
