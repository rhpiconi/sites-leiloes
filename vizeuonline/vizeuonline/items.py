# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VizeuonlineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	url = scrapy.Field()
	titulo = scrapy.Field() 
	lote = scrapy.Field()

	descricao = scrapy.Field()
	lance_inicial = scrapy.Field()
	despesas = scrapy.Field()
	despesas_adm = scrapy.Field()
	despesas_log = scrapy.Field()
	incremento_minimo = scrapy.Field()
	numero_visitas = scrapy.Field()

