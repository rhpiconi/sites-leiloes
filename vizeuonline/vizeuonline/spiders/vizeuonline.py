import scrapy
import re
import requests
from vizeuonline.items import VizeuonlineItem
#scrapy startproject nomeprojeto
#scrapy crawl nomeprojeto 

class vizeuonlineSpider(scrapy.Spider):
	name = 'vizeuonline'
	allowed_domains = ['vizeuonline.com.br']

	def start_requests(self):
		url_list = [
		'http://www.vizeuonline.com.br/leiloes/categorias/4',
		'http://www.vizeuonline.com.br/lotes/lista_lotes/',
		'http://www.vizeuonline.com.br/lotes/visualizar/'
		] 

		return(scrapy.Request(url)
					for url in url_list )

	def parse(self, response):
		urls = response.xpath("""//a[@title="Veja o lote"]//@href""").extract()

		print('INICIO PRIMEIRA FAZE')
		for url in urls:
			if '/lista_lotes' in url:
				yield scrapy.Request(url = url, callback=self.middle)
				print(url)
		print('FIM PRIMEIRA FAZE')

	def middle(self, response):	
		urls = response.xpath("""//a[@title="Veja o lote"]//@href""").extract()
	
		print('INICIO SEGUNDA FAZE')
		for url in urls:
			if '/visualizar' in url:
				yield scrapy.Request(url = url, callback=self.scrape)
				print(url)
		print('FIM SEGUNDA FAZE')

	def scrape(self, response):
		self.log('GETTING URL: %s'% response.url)

		item = VizeuonlineItem()

		item['url'] = (response.url)
		print(item['url'])

		titulo = response.xpath("""//*[@id="titulo"]/h1//text()""").extract()
		titulo = [i.strip() for i in titulo if i.strip()]
		item['titulo'] = "".join(titulo)
		print(item['titulo'])

		lote = response.xpath("""//*[@id="lote-info-titulo"]//text()""").extract()
		lote = [i.strip() for i in lote if i.strip()]
		item['lote'] = "".join(lote)
		print(item['lote'])

		informacoes = response.xpath("""//*[@id="lote-info"]/table//text()""").extract()
		informacoes = [i.strip() for i in informacoes if i.strip()]

		for i, element in enumerate(informacoes):
			if (element == 'Descrição'):
				item['descricao'] = informacoes[i+1]

			elif (element == 'Lance inicial'):
				item['lance_inicial'] = informacoes[i+1]

			elif (element == 'Despesas'):
				item['despesas'] = informacoes[i+1]

			elif (element == 'Despesas ADM'):
				item['despesas_adm'] = informacoes[i+1]

			elif (element == 'Despesas LOG'):
				item['despesas_log'] = informacoes[i+1]

			elif (element == 'Incremento mínimo'):
				item['incremento_minimo'] = informacoes[i+1]

			elif (element == 'Número de visitas'):
				item['numero_visitas'] = informacoes[i+1]

		yield item







