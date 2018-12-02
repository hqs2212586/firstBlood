## 一、Scrapy介绍
### 1、Scrapy是什么
　　Scrapy 是一个开源和协作的框架，其最初是为了页面抓取 (更确切来说, 网络抓取 )所设计的，使用它可以以快速、简单、可扩展的方式从网站中提取所需的数据。但目前Scrapy的用途十分广泛，可用于如数据挖掘、监测和自动化测试等领域，也可以应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫。

### 2、何谓框架
　　所谓框架其实就是一个已经被集成了各种功能（高性能异步下载，队列，分布式，解析，持久化等）的具有很强通用性的项目模板。对于框架的学习，重点是要学习其框架的特性、各个功能的用法即可。
　　scrapy和requests、bs4的关系，可以做如下类比：

> requests + bs4  =>  socket
> scrapy框架       =>  django

　　Scrapy 是基于twisted框架开发而来，twisted是一个流行的事件驱动的python网络框架。因此Scrapy使用了一种**非阻塞（又名异步）**的代码来实现**并发**（基于Twisted实现单线程并发下载页面）。也具备解析下载内容功能、帮助实现“递归”、帮助完成数据持久化（数据写入硬盘或数据库）、还具备一些扩展性功能（自定义组件）。

## 二、Scrapy安装
### 1、Windows平台

```bash
1、安装wheel
    pip3 install wheel   # 安装后，便支持通过wheel文件安装软件，wheel文件官网：https://www.lfd.uci.edu/~gohlke/pythonlibs
2、下载twisted（Scrapy基于twisted框架）：
    http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
    安装twisted:
    进入下载目录，执行： 
    pip3 install Twisted‑17.1.0‑cp35‑cp35m‑win_amd64.whl
3、下载并安装pywin32：    
    pip3 install pywin32
4、安装scrapy
    pip3 install scrapy
```

### 2、Linux平台

```bash
    pip3 install scrapy
```

## 三、Scrapy基础使用

### 1、使用流程
## （1）创建一个工程
　　切换到项目目录后，执行创建项目的命令，爬虫项目即创建成功。
```bash
$ scrapy startproject firstPro(工程名称)
```

- 目录结构
　　用pycharm打开创建的工程，可以看到如下目录结构。

```bash
project_name/
|--scrapy.cfg                # 项目的主配置信息。（真正爬虫相关的配置信息在settings.py文件中）
|--project_name/
    |--__init__.py
    |--items.py               # 设置数据存储模板，用于结构化数据，如Django的Model
    |--pipelines.py           # 数据持久化处理
    |--settings.py            # 配置文件(一般修改这里)，如：递归的层数、并发数，延迟下载等
    |--spiders/               # 爬虫目录，如：创建文件，编写爬虫解析规则
         |--__init__.py
```

#### （2）创建爬虫应用程序

```bash
$ pwd
/Users/hqs/ScrapyProjects/firstBlood
$ scrapy genspider qiubai www.qiushibaike.com
Created spider 'qiubai' using template 'basic' in module:
  firstBlood.spiders.qiubai
```

　　执行成功后，就可以在项目的spiders目录下找到新生成的爬虫文件了。

　　*1）创建爬虫程序语法*

    scrapy genspider 应用名称 爬取网页的起始url

　　*2）创建的爬虫文件内容模板*

```python
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
        pass
```

#### （3）编写爬虫文件

```python
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

        # 注意：parse方法的返回值必须是迭代器或空
        # 未指定返回值时，返回值默认为空
```

#### （4）修改settings.py配置文件

```python
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' # 伪装请求载体身份

# Obey robots.txt rules
ROBOTSTXT_OBEY = False   # 不遵从门户网站robots协议，避免某些信息爬取不到
```

注意：
　　（1）取消USER_AGENT注释，这里给它添加火狐浏览器身份标识，以**伪装请求载体身份**。
　　（2）将ROBOTSTXT_BOE修改为False，即**不遵守门户网站的robots协议**，避免某些信息爬取不到。（这个可视情况决定是否遵守）

#### （5）执行爬虫程序：

```bash
# scrapy crawl  应用名称 --nolog(阻止日志信息输出)
$ scrapy crawl qiubai
```
　　添加 '--nolog' 参数可以阻止日志信息的输出，只输出爬取的页面数据。

### 2、指定页面数据解析操作示例

　　需求：糗百中段子的内容和作者。
　　依然使用之前创建的项目，因此省略流程第一步的工程创建操作。
#### (1)创建爬虫文件（第二步）

```bash
$ pwd
/Users/hqs/ScrapyProjects/firstBlood
$ scrapy genspider qiubaipro www.qiushibaike.com/text
Created spider 'qiubaipro' using template 'basic' in module:
  firstBlood.spiders.qiubaipro
```

#### (2)xpath指定内容解析
　　Scrapy已经集成好了xpath解析的接口，因此推荐使用xpath进行指定内容的解析。
　　Control-Shift-X开启xpath插件。

![xpath解析](https://www.cnblogs.com/images/cnblogs_com/xiugeng/1344115/o_1543666875500.jpg)

#### (3)编写代码（第三步）

```python
import scrapy

class QiubaiproSpider(scrapy.Spider):
    name = 'qiubaipro'
    # allowed_domains = ['www.qiushibaike.com/text']  # 图片等信息可能不属于指定域名之下
    start_urls = ['https://www.qiushibaike.com/text/']  # 注意修改默认协议头

    def parse(self, response):
        # 建议使用xpath来执行指定内容的解析（Scrapy已经集成好了xpath解析的接口）
        # 段子的内容和作者
        div_list = response.xpath('//div[@id="content-left"]/div')
        for div in div_list:
            # 通过xpath解析到的指定内容被存储到了selector对象中
            # 需要通过extract()方法来提取selector对象中存储的数据值
            # 方法一：
            # author = div.xpath('./div/a[2]/h2/text()').extract()[0]  # './'表示解析当前局部div; a[2]表示第二个a标签
            # 方法二：extract_first()等同于extract()[0]
            author = div.xpath('./div/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()  # './/'表示当前局部所有元素；@class匹配类属性

            print(author)
```
注意：
　　1）第四步的修改配置文件也省略，配置方法见前面一节。
　　2）xpath解析的指定内容被存储到了selector对象中。
　　3）可以通过extract()方法来提取selector对象中存储的数据值。
　　4）selector对象和extract方法

```
使用extract()方法前：
[<Selector xpath='./div/a[2]/h2/text()' data='\n南九\n'>]
[<Selector xpath='./div/a[2]/h2/text()' data='\n无书斋主\n'>]
[<Selector xpath='./div/a[2]/h2/text()' data='\n请闭上眼睛里\n'>]

使用extract()方法后：
['\n好吃的焦糖饼干～\n']
['\n艾玛*^o^*ZW…\n']
['\n嘻嘻嘻，一\n']
```

　　5）extract_first()等同于extract()\[0]

#### (4)执行代码（第五步）

```bash
$ scrapy crawl qiubaipro --nolog
```

注意：
　　1）selector对象和extract方法

```
使用extract()方法前：
[<Selector xpath='./div/a[2]/h2/text()' data='\n南九\n'>]
[<Selector xpath='./div/a[2]/h2/text()' data='\n无书斋主\n'>]
[<Selector xpath='./div/a[2]/h2/text()' data='\n请闭上眼睛里\n'>]

使用extract()方法后：
['\n好吃的焦糖饼干～\n']
['\n艾玛*^o^*ZW…\n']
['\n嘻嘻嘻，一\n']
```


## 四、更多文档参考

[Scrapy 0.25 文档](https://scrapy-chs.readthedocs.io/zh_CN/latest/index.html)
[wupeiqi的Scrapy](http://www.cnblogs.com/wupeiqi/articles/5354900.html)
[爬虫框架：scrapy](http://www.cnblogs.com/linhaifeng/articles/7811861.html)