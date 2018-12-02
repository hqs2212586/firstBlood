# -*- coding: utf-8 -*-
import scrapy
from firstBlood.items import FirstbloodItem

class QiubaiproSpider(scrapy.Spider):
    name = 'qiubaipro'
    # allowed_domains = ['www.qiushibaike.com/text']  # 图片等信息可能不属于指定域名之下
    start_urls = ['https://www.qiushibaike.com/text/']  # 注意修改默认协议头

    def parse(self, response):
        # 建议使用xpath来执行指定内容的解析（Scrapy已经集成好了xpath解析的接口）
        # 段子的内容和作者
        div_list = response.xpath('//div[@id="content-left"]/div')

        # 存储解析到的页面数据
        data_list = []

        for div in div_list:
            # 通过xpath解析到的指定内容被存储到了selector对象中
            # 需要通过extract()方法来提取selector对象中存储的数据值
            # 方法一：
            # author = div.xpath('./div/a[2]/h2/text()').extract()[0]  # './'表示解析当前局部div; a[2]表示第二个a标签
            # 方法二：extract_first()等同于extract()[0]
            author = div.xpath('./div/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()  # './/'表示当前局部所有元素；@class匹配类属性

        # （一）基于终端指令的持久化存储
        #     dict = {
        #         'author': author,
        #         'content': content
        #     }
        #     data_list.append(dict)
        #
        # # parse方法的返回值必须是迭代器或空
        # return data_list

            # （二）基于管道的持久化存储
            # 1、将解析到的数据值(author和content)存储到items对象(存储前先声明item属性)
            item = FirstbloodItem()
            item['author'] = author
            item['content'] = content

            # 2、yield将item对象提交给管道进行持久化存储操作
            yield item








