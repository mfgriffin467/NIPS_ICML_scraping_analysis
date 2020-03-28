from scrapy import Spider
from NIPS.items import NipsItem
from scrapy import Request
from w3lib.html import remove_tags
import re

class ICMLSpider(Spider):
	name = 'icml_spider'
	#allowed_domains = ['https://nips.cc/Conferences']
	start_urls = ['https://icml.cc/Conferences/2017/Schedule']

    # High level pages by year
	def parse(self, response):
		result_urls = ['https://icml.cc/Conferences/{}/Schedule'.format(x) for x in range(2017,2020)]
		for url in result_urls:
			yield Request(url=url, callback=self.parse_result_page)


	def parse_result_page(self, response):
		item = NipsItem()
		#base_url = response.url
		ids = response.xpath('//div[@class="col-xs-12 col-sm-9"]/div/div/@id').re('(?<=_)[0-9]+')
		detail_urls = []
		for i in range(0,len(ids)):
#			detail_urls = detail_urls + ['https://nips.cc/Conferences/2018/Schedule?showEvent=' + ids[i]]
			detail_urls = detail_urls + [response.url + '?showEvent=' + ids[i]]

		for url in detail_urls:
			yield Request(url=url, callback=self.parse_detail_page)


	def parse_detail_page(self, response):
		item = NipsItem()
	#	item['title'] = remove_tags(response.xpath('//div[@class="maincardBody"]').extract())
	#	item['author'] = remove_tags(response.xpath('//div[@class="maincardFooter"]').extract())
	#	item['abstract'] = remove_tags(response.xpath('//div[@class="abstractContainer"]/p').extract())
	#	item['event_type'] = remove_tags(response.xpath('//div[@class="pull-right maincardHeader maincardType"]').extract())
	#	item['year'] = remove_tags(response.xpath('//span[@id="conferenceYear"]').extract())
		item['title'] = response.xpath('//div[@class="maincardBody"]').re('\>(.*?)\<')
		item['author'] = response.xpath('//div[@class="maincardFooter"]').re('\>(.*?)\<')
		item['abstract'] = response.xpath('//div[@class="abstractContainer"]').extract()
		item['event_type'] = response.xpath('//div[@class="pull-right maincardHeader maincardType"]')[0].re('\>(.*?)\<')
		item['year'] = response.xpath('//span[@id="conferenceYear"]').re(r'\d+')

		yield item


