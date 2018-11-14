import scrapy
import re
import requests
from zukerman.items import LeilaoItem

class leilaoSpider(scrapy.Spider):
		name = "zukerman"
		allowed_domains = ["zukerman.com.br"]

		def start_requests(self):


			url_list = [
			'https://www.zukerman.com.br/?pagina=1'
			]

			return(scrapy.Request(url)
					for url in url_list )


		def parse(self,response):

			anuncios = response.xpath("""//a[@class='c-lk']/@href""").extract()

			for anuncio in anuncios:
				if not "veiculos" in anuncio:
					yield scrapy.Request(url=anuncio, callback=self.middle)


			page = response.xpath("""//a[@class='active']/text()""").extract_first()
			page = str(int(page)+1)
			next_page = response.xpath("""//ul[@class='pagination']/li/a[contains(text(),'{0}')]""".format(page))
			if next_page:
				yield scrapy.Request(url="https://www.zukerman.com.br/?pagina="+ page)
					   
		
		def middle(self, response):

			anuncios = response.xpath("""//a[@class='c-lk']/@href""").extract()
			if anuncios:
				for anuncio in anuncios:
					yield scrapy.Request(url=anuncio, callback=self.scrape)
			else:
				self.scrape(response)

		def scrape(self, response):

			self.log('GETTING URL: %s'% response.url)

			item = LeilaoItem()

			item['link'] = response.url

			r = re.search(r"\d{6}", response.url)
			if r:
				item['_id'] = r.group()

			item['comitente'] = response.xpath("""//div[@class='d-n-v']/h2/text()""").extract_first()

			item['status'] = response.xpath("""//div[@class='s-d-lb2']//text()""").extract()
			item['status'] = ''.join(item['status']).strip()
			item['maior_lance'] = response.xpath("""//div[@class='m-l-o']/text()""").extract_first()

			item['lance_minimo'] = response.xpath("""//span[@class='dvla']/text()""").extract_first()

			item['incremento_minimo'] = response.xpath("""//div[@class='s-d-lb6-2 f-d']/text()""").extract_first()

			item['encerramento'] = response.xpath("""//div[@class="s-d-lb6-3 f-d"]/text()""").extract_first()

			item['data'] = response.xpath("""//div[@class='daet']/text()""").extract_first()

			item['endereco'] = response.xpath("""//div[@class='s-d-ld-i2 f-d']//text()""").extract()
			item['endereco'] = ''.join(item['endereco']).strip()

			details = []

			detalhes = response.xpath("""//div[@class='s-d-ld-i3 f-d']//text()""").extract()
			for d in detalhes:
				if d.isspace():
					continue
				details.append(d.strip())

			item['detalhes'] = ' '.join(details)

			item['descricao'] = response.xpath("""//div[@class='s-d-ld-i1 f-d']//text()""").extract()
			item['descricao'] = ''.join(item['descricao']).strip()

			item['observacoes'] = response.xpath("""//div[@class='s-d-ld-i4']/p/text()""").extract_first()

			item['url_matricula'] = response.xpath("""//a[@class='doctos'][text()[contains(.,'Matricula')]]/@href""").extract()

			item['formas_de_pagamento'] = response.xpath("""//div[@class="s-d-fp"]//div[@class='s-d-fp-i-main f-d']//text()""").extract()
			item['formas_de_pagamento'] = ''.join(item['formas_de_pagamento']).strip()
			item['informacoes_leilao'] = response.xpath("""//div[@class="s-d-il"]//div[@class='s-d-il-i-main f-d']//text()""").extract()

			yield item

		def download(self, url, file):

			r = requests.get(url)
			with open("files\{0}.pdf".format(file),"wb") as f:
				f.write(r.content)


		