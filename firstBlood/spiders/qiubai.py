# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):  # Spider是所有爬虫的父类
    name = 'qiubai'   # 爬虫文件的名称：通过爬虫文件的名称可以指定定位到某一个具体的爬虫文件
    allowed_domains = ['www.qiushibaike.com']   # 允许的域名：只爬取指定域名下的页面数据
    start_urls = ['http://www.qiushibaike.com/']   # 起始url：当前工程将要爬取页面对应的url

    def parse(self, response):
        """
        解析方法：对获取的页面数据进行指定内容解析
        :param response: 根据起始url列表发起请求，请求成功返回的响应对象
        :return:
        """
        print(response.text)  # 获取字符串类型的响应内容
        # print(response.body)  # 获取字节类型的相应内容

        # parse方法的返回值必须是迭代器或空
        # 未指定返回值时，返回值默认为空
