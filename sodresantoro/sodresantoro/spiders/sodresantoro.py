import scrapy
import requests
from sodresantoro.items import SodresantoroItem
#scrapy startproject nomeprojeto
#scrapy crawl nomeprojeto 

class sodresantoroSpider(scrapy.Spider):
	name = 'sodresantoro'
	allowed_domains = ['sodresantoro.com.br']

	def start_requests(self):
		url = 'http://www.sodresantoro.com.br/imoveis/pagina/{0}/'

		for i in range(1,5):
			yield scrapy.Request(url = url.format(str(i)))

	def parse(self, response): 

		urls = response.xpath("""//a[@class="visualizacaoDiv-titulo-lote"]/@href""").extract()

		for url in urls:
			yield scrapy.Request(url = 'http://www.sodresantoro.com.br' + url, callback=self.scrape)
		
	def scrape(self, response):
		self.log('Getting URL: %s' %response.url)

		item = SodresantoroItem()

		item['url'] = (response.url)

		titulo = response.xpath("""//div[@class="online_lance-tit-esq"]//text()""").extract()
		titulo = [i.strip() for i in titulo if i.strip()]
		item['titulo'] = titulo

		lance_inicial = response.xpath("""//span[@class="valor"]//text()""").extract()
		lance_inicial = [i.strip() for i in lance_inicial if i.strip()]
		item['lance_inicial'] = lance_inicial

		descricao = response.xpath("""//p[@class="desc_titulos"]//text()""").extract()
		descricao = [i.strip() for i in descricao if i.strip()]
		item['descricao'] = descricao

		leilao = response.xpath("""//p[text()[contains(.,"Leilão:")]]//text()""").extract()
		leilao = [i.strip() for i in leilao if i.strip()]
		item['leilao'] = "".join(leilao)

		lote = response.xpath("""//p[text()[contains(.,"Lote:")]]//text()""").extract()
		lote = [i.strip() for i in lote if i.strip()]
		item['lote'] = "".join(lote)

		data = response.xpath("""//p[text()[contains(.,"Data:")]]//text()""").extract()
		data = [i.strip() for i in data if i.strip()]
		item['data'] = "".join(data)

		categorias = response.xpath("""//p[text()[contains(.,"Categorias")]]//text()""").extract()
		categorias = [i.strip() for i in categorias if i.strip()]
		item['categorias'] = "".join(categorias)

		alienacao_fid = response.xpath("""//p[text()[contains(.,"Alienação Fiduciária")]]//text()""").extract()
		alienacao_fid = [i.strip() for i in alienacao_fid if i.strip()]
		item['alienacao_fiduciaria'] = "".join(alienacao_fid)

		local_lei = response.xpath("""//p[text()[contains(.,"Local do leilão")]]//text()""").extract()
		local_lei = [i.strip() for i in local_lei if i.strip()]
		item['local_leilao'] = "".join(local_lei)

		local_lot = response.xpath("""//p[text()[contains(.,"Local do lote")]]//text()""").extract()
		local_lot = [i.strip() for i in local_lot if i.strip()]
		item['local_lote'] = "".join(local_lot)

		informacoes = response.xpath("""//ul[@class="divisao"]//text()""").extract()
		informacoes = [i.strip() for i in informacoes if i.strip()]
		
		for i, element in enumerate(informacoes):
			if (element == 'Vistoria:'):
				item['vistoria'] = informacoes[i+1]
			
			elif (element == 'Terreno:'):
				item['terreno'] = informacoes[i+1]

			elif (element == 'Avaliação:'):
				item['avaliacao'] = informacoes[i+1]
						
			elif (element == 'Bairro:'):
				item['bairro'] = informacoes[i+1]

			elif (element == 'Tipo:'):
				item['tipo'] = informacoes[i+1]

			elif (element == 'Cidade:'):
				item['cidade'] = informacoes[i+1]

			elif (element == 'Endereço:'):
				item['endereco'] = informacoes[i+1]

			elif (element == 'Privativa:'):
				item['privativa'] = informacoes[i+1]

			elif (element == 'Construída:'):
				item['construida'] = informacoes[i+1]

			elif (element == 'Lance Mínimo:'):
				item['lance_minimo'] = informacoes[i+1]
		
		forma_pagamento = response.xpath("""//*[@id="coluna4"]/div[3]/div[10]/div[2]//p//text()""").extract()
		item['forma_pagamento'] = forma_pagamento

		yield item

