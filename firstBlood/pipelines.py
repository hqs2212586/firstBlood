# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstbloodPipeline(object):
    fp = None
    def open_spider(self, spider):
        """
        该方法只会在爬虫开始爬数据的时候被调用一次
        :param spider:
        :return:
        """
        print("开始爬虫")
        # 在该方法中打开文件
        self.fp = open('./qiubai_pipe.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        """
        接收爬虫文件中提交的item对象，并对item对象中存储的页面数据进行持久化存储
        每当爬虫文件向管道提交一次item,porcess_item方法就会执行一次
        :param item: 表示接收到的item对象
        :param spider:
        :return:
        """
        # 取出Item对象中存储的数据值
        author = item['author']
        content = item['content']

        # 持久化存储
        # with open('./qiubai_pipe.txt', 'w', encoding='utf-8') as fp:
        self.fp.write(author + ":" + content+ '\n\n\n')  # 写入数据
        return item

    def close_spider(self, spider):
        """
        该方法只会在爬虫结束时被调用一次
        :param spider:
        :return:
        """
        print("爬虫结束")
        # 关闭文件
        self.fp.close()
