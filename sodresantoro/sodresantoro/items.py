# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SodresantoroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    titulo = scrapy.Field()
    lance_inicial = scrapy.Field()
    descricao = scrapy.Field()

    leilao = scrapy.Field()
    lote = scrapy.Field()
    data = scrapy.Field()
    categorias = scrapy.Field()
    alienacao_fiduciaria = scrapy.Field()
    local_leilao = scrapy.Field()
    local_lote = scrapy.Field()

    vistoria = scrapy.Field()
    terreno = scrapy.Field()
    avaliacao = scrapy.Field()
    bairro = scrapy.Field()
    tipo = scrapy.Field()
    cidade = scrapy.Field() 
    endereco = scrapy.Field()
    privativa = scrapy.Field()
    construida = scrapy.Field()
    lance_minimo = scrapy.Field()

    forma_pagamento = scrapy.Field()
