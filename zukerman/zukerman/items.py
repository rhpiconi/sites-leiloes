# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LeilaoItem(scrapy.Item):
    
	link = scrapy.Field()

	_id = scrapy.Field()

	comitente = scrapy.Field()

	status = scrapy.Field()

	maior_lance = scrapy.Field()

	lance_minimo = scrapy.Field()

	incremento_minimo = scrapy.Field()

	encerramento = scrapy.Field()

	data = scrapy.Field()

	endereco = scrapy.Field()

	detalhes = scrapy.Field()

	descricao = scrapy.Field()

	observacoes = scrapy.Field()

	url_matricula = scrapy.Field()

	formas_de_pagamento = scrapy.Field()

	informacoes_leilao = scrapy.Field()
