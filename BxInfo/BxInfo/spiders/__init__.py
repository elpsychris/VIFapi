# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import re
from subprocess import Popen, PIPE, STDOUT
from io import StringIO


class BienxoSpider(scrapy.Spider):
    name = "bienxo"

    def log_subprocess_output(self, pipe):
        content = ''
        for line in iter(pipe.readline, b'\n'):  # b'\n'-separated lines
            content += line.decode('utf-8')
        return content

    def get_header_map(self, process):
        print("[[[[text la")
        with process.stdout:
            output = self.log_subprocess_output(process.stdout)
            m = re.search("Date:[\s\w,:\-\/.=;]+", output)

        if m is not None:
            hFields = m.group(0).split('\n')
            header = {}

    def start_requests(self):
        url = "http://www.vr.org.vn/ptpublic_web/ThongTinPTPublic.aspx"
        # output = subprocess.call(['wget','-S', url])
        process = Popen(['wget', '-r', '-S', '-np', '-k', url], stdout=PIPE, stderr=STDOUT)
        header = self.get_header_map(process)

        print(header)

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        self.log('Saved file %s' % "asas")
