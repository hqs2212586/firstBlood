# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstbloodItem(scrapy.Item):
    # 必须遵从如下属性声明规则
    # name = scrapy.Field()

    # 声明item属性
    author = scrapy.Field()  # 存储解析到的作者
    content = scrapy.Field()  # 存储解析到的内容信息
