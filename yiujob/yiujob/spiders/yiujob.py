from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from yiujob.items import YiujobItem
import time
import json



class yiujob(CrawlSpider):
    name = "yiujobText"
    start_urls = [
        'http://sz.58.com/job/?PGTID=0d100000-0000-4377-f16a-093541080292&ClickID=3'
    ]

    #存储区域的URL
    def __init__(self):
        self.leimu_name_url = []
        self.qy_name_url=[]
        self.jishu_58 = 0#计算url的位数
        self.allwork_58 = {0:[{1:"销售代表"},{5:"电话销售"},{3:"销售经理"},{4:"销售总监"},{7:"汽车销售"},{8:"医药销售"},{9:"器械销售"},{10:"网络销售"},{11:"区域销售"},{13:"客户经理"},{16:"销售顾问"}]}


    # 大类目首页
    def parse(self,response):
        selector = Selector(response)
        Movies = selector.xpath('//div[@id="filterJob"]/ul/li')
        for eachMovies in Movies:
            leimu_name = eachMovies.xpath('a/text()').extract()[0]
            if leimu_name == ' 全部 ':
                continue
            leimu_url = eachMovies.xpath('a/@href').extract()[0]
            yield Request(leimu_url, callback=self.smpares,meta={'leimu_name':leimu_name,'leimu_url':leimu_url,'allwork_58':self.allwork_58[self.jishu_58]})
            self.jishu_58+=1
            break

    def smpares(self,response):

        leimu_name_sm = response.meta['leimu_name']
        leimu_url_sm = response.meta['leimu_url']
        allwork_58_sm = response.meta['allwork_58']
        selector = Selector(response)
        Movies = selector.xpath('//div[@id="filterJob"]/ul/li')

        for i in allwork_58_sm:
            if list(i.keys())[0]==1:
                print('跳过销售代表')
                continue
            leimu_name= list(i.keys())[1]
            leimu_url= Movies[list(i.keys())[0]].xpath('a/@href').extract()[0]
            yield Request(leimu_url, callback=self.sxpares, meta={'leimu_name': leimu_name})
            # break
    #小类列表，如销售代表
    def sxpares(self,response):
        leimu_name_xm = response.meta['leimu_name']
        selector = Selector(response)
        Movies = selector.xpath('//div[@id="filterArea"]/ul/li')
        for eachMovies in Movies:
            quyu_name = eachMovies.xpath('a/text()').extract()[0]
            quyu_url = eachMovies.xpath('a/@href').extract()[0]
            if(quyu_name[-1]!="区"):
                quyu_name = quyu_name+"区"
            self.qy_name_url.append([quyu_name,quyu_url])
        del self.qy_name_url[0]
        del self.qy_name_url[-1]

        for i in self.qy_name_url:
            city = '深圳'
            city_quyu= i[0]
            yield Request(i[1], callback=self.parseneirong, meta={'city': city,'city_quyu':city_quyu,'leimu_name': leimu_name_xm})


    def parseneirong(self,response):
        selector = Selector(response)
        city = response.meta['city']
        city_quyu = response.meta['city_quyu']
        leimu_name_neirong = response.meta['leimu_name']
        cotent_li = selector.xpath('//div[@class="leftCon"]/ul/li')
        for each_cotent_li in cotent_li:
            item = YiujobItem()
            #左边
            item['title'] = each_cotent_li.xpath('div[@class="item_con job_title"]/div/a').xpath('string(.)').extract()[0]
            title_url = each_cotent_li.xpath('div[@class="item_con job_title"]/div/a/@href').extract()[0]
            item['pay'] = each_cotent_li.xpath('div[@class="item_con job_title"]/p').xpath('string(.)').extract()[0]
            item['welfare'] = each_cotent_li.xpath('div[@class="item_con job_title"]/div[@class="job_wel clearfix"]/span/text()').extract()
            item['name'] = each_cotent_li.xpath('div[@class="item_con job_comp"]/div/a/text()').extract()[0]
            item['jobcontent'] = leimu_name_neirong
            item['education'] = each_cotent_li.xpath('div[@class="item_con job_comp"]/p/span[@class="xueli"]/text()').extract()[0]
            item['experience'] = each_cotent_li.xpath('div[@class="item_con job_comp"]/p/span[@class="jingyan"]/text()').extract()[0]
            item['time'] = '今天'
            item['job'] = '销售'
            item['call'] = '企业未提供,请直接投递简历'
            item['whereform'] = 58
            item['title_url'] = title_url
            item['city'] = city
            item['quyu'] = city_quyu
            yield Request(title_url, callback=self.parseneirongtwo, meta={'item': item})

    def parseneirongtwo(self,response):
        selector = Selector(response)
        item = response.meta['item']

        zhiwei_cotent = selector.xpath('//div[@class="leftCon"]/div')

        dizhi = zhiwei_cotent[0].xpath('div[@class="pos-area"]').xpath('string(.)').extract()[0]
        neirong = zhiwei_cotent[1].xpath('div[@class="subitem_con pos_description"]/div[@class="posDes"]/div/text()').extract()
        item['jutidizhi'] = dizhi
        item['content'] = neirong
        yield item


    # def smpares(self,response):
    #     leimu_name2 = response.meta['leimu_name']
    #     selector = Selector(response)
    #     Movies = selector.xpath('//div[@id="filterJob"]/ul/li')
    #     self.lmjson = {"smleimu":[]}
    #     self.lmjson['leimu_name']=leimu_name2
    #     for eachMovies in Movies:
    #         leimu_name = eachMovies.xpath('a/text()').extract()[0]
    #         if leimu_name == ' 全部 ':
    #             continue
    #         self.lmjson["smleimu"].append(leimu_name)
    #     lmjson2 = json.dumps(self.lmjson, ensure_ascii=False)
    #     with open("G://chromedowm/leimu.txt", "a") as f:
    #         f.writelines(lmjson2)
    #         f.writelines('\n')
    #         print("加载入文件完成...")



    # def parse(self, response):
    #     selector = Selector(response)
    #     Movies = selector.xpath('//div[@id="filterArea"]/ul/li')
    #     for eachMovies in Movies:
    #         quyu_name = eachMovies.xpath('a/text()').extract()[0]
    #         quyu_url = eachMovies.xpath('a/@href').extract()[0]
    #         if(quyu_name[-1]!="区"):
    #             quyu_name = quyu_name+"区"
    #         self.qy_name_url.append([quyu_name,quyu_url])
    #     del self.qy_name_url[0]
    #     del self.qy_name_url[-1]
    #
    #     for i in self.qy_name_url:
    #         city = '深圳'
    #         city_quyu= i[0]
    #         yield Request(i[1], callback=self.parseneirong, meta={'city': city,'city_quyu':city_quyu})
    #
    # def parseneirong(self, response):
    #
    #     selector = Selector(response)
    #     city = response.meta['city']
    #     city_quyu = response.meta['city_quyu']
    #     cotent_li = selector.xpath('//div[@class="leftCon"]/ul/li')
    #     con = 0
    #     for each_cotent_li in cotent_li:
    #         item = YiujobItem()
    #         #左边
    #         item['title'] = each_cotent_li.xpath('div[@class="item_con job_title"]/div/a').xpath('string(.)').extract()[0]
    #         title_url = each_cotent_li.xpath('div[@class="item_con job_title"]/div/a/@href').extract()[0]
    #         item['pay'] = each_cotent_li.xpath('div[@class="item_con job_title"]/p').xpath('string(.)').extract()[0]
    #         item['welfare'] = each_cotent_li.xpath('div[@class="item_con job_title"]/div[@class="job_wel clearfix"]/span/text()').extract()
    #         item['name'] = each_cotent_li.xpath('div[@class="item_con job_comp"]/div/a/text()').extract()[0]
    #         item['jobcontent'] = each_cotent_li.xpath('div[@class="item_con job_comp"]/p/span[@class="cate"]/text()').extract()[0]
    #         item['education'] = each_cotent_li.xpath('div[@class="item_con job_comp"]/p/span[@class="xueli"]/text()').extract()[0]
    #         item['experience'] = each_cotent_li.xpath('div[@class="item_con job_comp"]/p/span[@class="jingyan"]/text()').extract()[0]
    #         item['time'] = '今天'
    #         item['job'] = '司机'
    #         item['call'] = '企业未提供,请直接投递简历'
    #         item['whereform'] = 58
    #         item['title_url'] = title_url
    #         item['city'] = city
    #         item['quyu'] = city_quyu
    #
    #
    #         yield Request(title_url, callback=self.parseneirongtwo, meta={'item': item,'con':con})
    #         con+=1
    #
    # def parseneirongtwo(self,response):
    #     selector = Selector(response)
    #     item = response.meta['item']
    #
    #     zhiwei_cotent = selector.xpath('//div[@class="leftCon"]/div')
    #
    #     dizhi = zhiwei_cotent[0].xpath('div[@class="pos-area"]').xpath('string(.)').extract()[0]
    #     neirong = zhiwei_cotent[1].xpath('div[@class="subitem_con pos_description"]/div[@class="posDes"]/div/text()').extract()
    #     item['jutidizhi'] = dizhi
    #     item['content'] = neirong
    #     yield item







        # item['job'] = '销售'
        # item['jobcontent'] = '电话销售'
        # item['pay'] = '面议'
        # item['education'] = '大专'
        # item['experience'] = '1-3年'
        # item['welfare'] = ["五险一金","包吃","包住"]
        # item['title'] = '找销售'
        # item['time'] = '12-02'
        # item['city'] = '深圳'
        # item['quyu'] = '宝安区'
        # item['name'] = '傻逼公司'
        # item['content'] = '来不来啊'
        #item['jutidizhi']=''
        # yield item
