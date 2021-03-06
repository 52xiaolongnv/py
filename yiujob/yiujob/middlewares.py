# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

# 导入随机模块
import random
import time

from scrapy import signals

class YiujobSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyMiddleware(object):


    def process_request(self,request,spider):
        time.sleep(2)
        IPPOOL = [
            {"ip": "180.120.211.171:808"},
            {"ip": "59.51.120.198:3128"},
            {"ip": "49.81.252.81:8118"},
            {"ip": "221.211.206.162:80"},
            {"ip": "1.28.144.19:80"},
            {"ip": "183.15.138.43:808"},
            {"ip": "111.6.187.52:80"},
            {"ip": "112.114.98.248:8118"},
            {"ip": "1.28.144.14:80"},
            {"ip": "111.3.108.44:8118"},
            {"ip": "219.149.46.151:3128"},
            {"ip": "120.199.64.163:8081"},
            {"ip": "1.28.144.10:80"},
            {"ip": "58.250.168.164:9000"},
            {"ip": "219.138.58.110:3128"},
            {"ip": "112.114.96.51:8118"},
            {"ip": "1.28.144.16:80"},
            {"ip": "182.37.53.1:808"},
            {"ip": "114.228.15.112:8118"},
            {"ip": "61.187.251.235:80"},
            {"ip": "112.114.92.223:8118"},
            {"ip": "113.221.45.78:8888"},
            {"ip": "106.226.170.237:808"},
            {"ip": "120.35.12.105:3128"},
            {"ip": "101.132.146.103:8080"},
            {"ip": "183.148.93.92:808"},
            {"ip": "113.218.217.118:8888"},
            {"ip": "119.136.199.95:8118"},
            {"ip": "221.233.85.102:3128"},
            {"ip": "123.125.159.122:80"},
            {"ip": "139.209.90.50:80"},
            {"ip": "123.13.40.180:9999"},
            {"ip": "163.177.151.23:80"},
            {"ip": "112.114.96.87:8118"},
            {"ip": "218.203.56.228:80"},
            {"ip": "112.86.73.52:53281"},
            {"ip": "120.198.224.6:80"},
            {"ip": "121.228.48.234:808"},
            {"ip": "58.56.128.84:9001"},
            {"ip": "123.54.238.8:808"},
            {"ip": "112.114.98.115:8118"},
            {"ip": "223.150.48.128:8888"},
            {"ip": "49.72.210.239:8118"},
            {"ip": "112.114.95.137:8118"},
            {"ip": "112.114.96.70:8118"},
            {"ip": "101.248.64.68:80"},
            {"ip": "112.114.96.91:8118"},
            {"ip": "112.114.98.249:8118"},
            {"ip": "101.132.148.7:8080"},
            {"ip": "183.235.254.160:80"},
            {"ip": "222.209.122.193:8118"},
            {"ip": "114.101.33.151:54318"},
            {"ip": "124.165.252.72:8080"},
            {"ip": "219.138.58.185:3128"},
            {"ip": "118.114.77.47:8080"},
            {"ip": "117.34.72.251:8082"},
            {"ip": "122.96.59.102:81"},
            {"ip": "113.122.34.206:808"},
            {"ip": "112.114.98.187:8118"},
            {"ip": "218.86.80.34:808"},
            {"ip": "183.235.254.159:8080"},
            {"ip": "1.28.144.17:80"},
            {"ip": "124.232.163.39:3128"},
            {"ip": "112.114.92.124:8118"},
            {"ip": "125.72.106.174:808"},
            {"ip": "27.40.153.65:61234"},
            {"ip": "112.114.96.152:8118"},
            {"ip": "112.114.99.248:8118"},
            {"ip": "113.110.108.57:808"},
            {"ip": "113.221.50.164:8888"},
            {"ip": "27.152.6.118:808"},
            {"ip": "117.64.235.163:808"},
            {"ip": "112.114.99.210:8118"},
            {"ip": "112.114.97.250:8118"},
            {"ip": "112.114.94.247:8118"},
            {"ip": "1.28.144.12:80"},
            {"ip": "113.221.46.37:8888"},
            {"ip": "117.43.1.251:808"},
            {"ip": "222.241.14.91:8888"},
            {"ip": "1.28.144.18:80"},
            {"ip": "122.235.166.101:8118"},
            {"ip": "112.114.99.134:8118"},
            {"ip": "220.168.238.158:8888"},
            {"ip": "112.192.18.177:8118"},
            {"ip": "49.85.7.205:26100"},
            {"ip": "112.114.97.180:8118"},
            {"ip": "220.168.237.187:8888"},
            {"ip": "113.108.204.74:8888"},
            {"ip": "223.150.48.217:8888"},
            {"ip": "1.28.144.11:80"},
            {"ip": "175.23.15.143:8118"},
            {"ip": "27.40.137.129:61234"},
            {"ip": "120.236.142.103:8888"},
            {"ip": "222.89.144.134:808"},
            {"ip": "60.214.118.170:63000"},
            {"ip": "112.114.98.247:8118"},
            {"ip": "121.238.41.44:808"},
            {"ip": "120.198.224.5:8080"},
            {"ip": "112.13.93.43:8088"},
            {"ip": "112.114.99.193:8118"},
            {"ip": "111.62.243.64:80"},
            {"ip": "221.198.152.184:8118"},
            {"ip": "123.54.251.114:808"},
            {"ip": "182.88.11.84:9797"},
            {"ip": "112.114.98.118:8118"},
            {"ip": "220.168.239.115:8888"},
            {"ip": "112.114.98.66:8118"},
            {"ip": "182.108.4.46:8118"},
            {"ip": "116.17.236.36:808"},
            {"ip": "219.138.58.244:3128"},
            {"ip": "112.114.99.202:8118"},
            {"ip": "106.39.179.236:80"},
            {"ip": "139.209.90.50:80"},
            {"ip": "112.114.94.244:8118"},
            {"ip": "117.143.66.62:9999"},
            {"ip": "112.114.98.165:8118"},
            {"ip": "122.228.179.178:80"},
            {"ip": "124.232.163.56:3128"},
            {"ip": "219.138.58.84:3128"},
            {"ip": "114.245.152.189:8118"},
            {"ip": "60.214.155.243:53281"},
            {"ip": "1.28.144.14:80"},
            {"ip": "124.165.252.72:8081"},
            {"ip": "223.150.8.209:8888"},
            {"ip": "106.39.179.118:80"},
            {"ip": "123.125.159.122:80"},
            {"ip": "124.232.163.39:3128"},
            {"ip": "121.206.54.68:808"},
            {"ip": "124.202.214.26:8118"},
            {"ip": "101.248.64.68:8080"},
            {"ip": "124.232.163.4:3128"},
            {"ip": "101.132.148.7:8080"},
            {"ip": "171.35.103.37:808"},
            {"ip": "60.208.44.228:80"},
            {"ip": "223.241.119.70:8010"},
            {"ip": "121.207.1.208:808"},
            {"ip": "111.3.108.44:8118"},
            {"ip": "223.241.119.115:8010"},
            {"ip": "112.114.96.162:8118"},
            {"ip": "112.114.79.80:8118"},
            {"ip": "112.114.92.113:8118"},
            {"ip": "122.235.169.126:8118"},
            {"ip": "118.254.142.42:53281"},
            {"ip": "183.237.206.92:53281"},
            {"ip": "183.235.254.159:8080"},
            {"ip": "116.31.124.104:3128"},
            {"ip": "117.34.72.251:8082"},
            {"ip": "61.135.155.82:443"},
            {"ip": "222.169.193.162:8099"},
            {"ip": "113.221.46.4:8888"},
            {"ip": "220.168.237.187:8888"},
            {"ip": "112.114.95.32:8118"},
            {"ip": "106.39.179.86:80"},
            {"ip": "124.232.163.9:3128"},
            {"ip": "112.114.97.13:8118"},
            {"ip": "113.221.47.98:808"},
            {"ip": "220.168.237.9:8888"},
            {"ip": "111.62.245.185:80"},
            {"ip": "118.114.77.47:8080"},
            {"ip": "113.221.46.45:808"},
            {"ip": "183.64.111.243:80"},
            {"ip": "27.37.187.209:8888"},
            {"ip": "124.232.163.37:3128"},
            {"ip": "112.114.95.148:8118"},
            {"ip": "113.218.216.54:8888"},
            {"ip": "112.114.98.58:8118"},
            {"ip": "183.235.254.160:8080"},
            {"ip": "124.232.163.58:3128"},
            {"ip": "115.222.1.224:80"},
            {"ip": "112.114.93.190:8118"},
            {"ip": "27.184.139.46:8888"},
            {"ip": "113.221.45.40:8888"},
            {"ip": "112.114.93.240:8118"},
            {"ip": "112.16.9.198:81"},
            {"ip": "183.136.232.149:9999"},
            {"ip": "106.39.179.162:80"},
            {"ip": "112.114.97.102:8118"},
            {"ip": "112.114.79.125:8118"},
            {"ip": "219.149.46.151:3129"},
            {"ip": "1.28.144.19:80"},
            {"ip": "106.39.179.9:80"},
            {"ip": "117.65.39.207:54132"},
            {"ip": "115.207.36.67:808"},
            {"ip": "163.125.235.165:8118"},
            {"ip": "116.248.160.70:80"},
            {"ip": "42.85.243.99:80"},
            {"ip": "113.221.49.104:8888"},
            {"ip": "106.39.179.244:80"},
            {"ip": "110.88.127.17:23087"},
            {"ip": "220.168.239.130:8888"},
            {"ip": "112.114.94.137:8118"},
            {"ip": "112.114.99.137:8118"},
            {"ip": "124.232.163.36:3128"},
            {"ip": "112.114.96.156:8118"},
            {"ip": "118.255.22.14:808"},
            {"ip": "223.241.119.172:8010"},
            {"ip": "112.114.76.221:8118"},
            {"ip": "113.218.218.237:808"},
            {"ip": "112.114.79.134:8118"},
            {"ip": "113.218.218.18:808"},
            {"ip": "101.132.146.103:8080"},
            {"ip": "58.56.128.84:9001"},
            {"ip": "39.155.169.70:80"},
            {"ip": "112.114.98.212:8118"},
            {"ip": "183.32.89.50:6666"},
            {"ip": "101.68.73.54:53281"},
            {"ip": "218.201.98.196:3128"},
            {"ip": "183.62.202.130:3128"},
            {"ip": "124.232.163.48:3128"},
            {"ip": "218.18.35.13:3128"},
            {"ip": "112.114.97.180:8118"},
            {"ip": "183.94.164.219:808"},
            {"ip": "121.69.45.162:8118"},
            {"ip": "112.114.76.190:8118"},
            {"ip": "106.56.102.151:808"},
            {"ip": "223.150.218.211:8888"},
            {"ip": "113.221.46.43:808"},
            {"ip": "219.138.58.167:3128"},
            {"ip": "112.114.98.217:8118"},
            {"ip": "1.28.144.18:80"},
            {"ip": "116.2.230.60:8080"},
            {"ip": "219.150.189.212:9999"},
            {"ip": "106.39.179.248:80"},
            {"ip": "112.13.93.43:8088"},
            {"ip": "113.218.218.21:808"},
            {"ip": "163.125.235.196:8118"},
            {"ip": "113.140.25.4:81"},
            {"ip": "163.177.151.23:80"},
            {"ip": "183.63.101.62:55555"},
            {"ip": "112.114.98.23:8118"},
            {"ip": "112.114.94.132:8118"},
            {"ip": "219.138.58.20:3128"},
            {"ip": "1.60.150.210:8888"},
            {"ip": "112.114.93.133:8118"},
            {"ip": "122.235.162.131:8118"},
            {"ip": "222.92.19.166:8118"},
            {"ip": "112.114.96.143:8118"},
            {"ip": "116.231.42.127:808"},
            {"ip": "124.232.163.8:3128"},
            {"ip": "115.203.215.102:808"},
            {"ip": "124.202.214.26:8118"},
            {"ip": "60.214.118.170:63000"},
            {"ip": "223.241.119.57:8010"},
            {"ip": "171.37.177.226:9797"},
            {"ip": "112.114.96.143:8118"},
            {"ip": "112.114.97.93:8118"},
            {"ip": "101.132.146.103:8080"},
            {"ip": "113.105.202.197:808"},
            {"ip": "27.46.48.167:8118"},
            {"ip": "222.186.32.227:8118"},
            {"ip": "112.114.97.171:8118"},
            {"ip": "60.208.44.228:80"},
            {"ip": "114.95.117.172:8118"},
            {"ip": "58.250.168.164:9000"},
            {"ip": "112.114.92.73:8118"},
            {"ip": "182.244.206.47:8118"},
            {"ip": "223.241.117.114:8010"},
            {"ip": "112.114.96.214:8118"},
            {"ip": "39.134.161.18:80"},
            {"ip": "183.163.38.110:54318"},
            {"ip": "182.90.12.171:8888"},
            {"ip": "222.92.141.250:80"},
            {"ip": "222.186.45.58:57624"},
            {"ip": "39.134.161.17:80"},
            {"ip": "122.193.14.85:82"},
            {"ip": "27.197.102.221:8118"},
            {"ip": "120.236.142.103:8888"},
            {"ip": "183.163.38.75:54318"},
            {"ip": "112.229.242.128:8118"},
            {"ip": "112.114.93.251:8118"},
            {"ip": "106.60.38.139:80"},
            {"ip": "112.114.98.2:8118"},
            {"ip": "111.62.243.64:80"},
            {"ip": "222.246.15.217:8888"},
            {"ip": "113.221.50.164:8888"},
            {"ip": "39.134.161.16:80"},
            {"ip": "223.243.208.2:44311"},
            {"ip": "60.189.117.213:61234"},
            {"ip": "113.221.13.242:8888"},
            {"ip": "219.149.46.151:3128"},
            {"ip": "101.68.73.54:53281"},
            {"ip": "60.160.170.104:61234"},
            {"ip": "112.114.95.148:8118"},
            {"ip": "124.165.252.72:9999"},
            {"ip": "124.232.163.36:3128"},
            {"ip": "39.134.161.13:8080"},
            {"ip": "183.32.89.227:6666"},
            {"ip": "113.221.46.43:808"},
            {"ip": "124.232.163.37:3128"},
            {"ip": "121.69.45.166:8118"},
            {"ip": "101.132.148.7:8080"},
            {"ip": "223.150.48.118:8888"},
            {"ip": "112.114.92.113:8118"},
            {"ip": "39.134.161.15:80"},
            {"ip": "111.3.108.44:8118"},
            {"ip": "125.115.141.6:8118"},
            {"ip": "121.69.45.162:8118"},
            {"ip": "125.76.228.200:80"},
            {"ip": "183.64.111.243:80"},
            {"ip": "220.168.236.30:8888"},
            {"ip": "113.108.204.74:8888"},
            {"ip": "112.114.98.66:8118"},
            {"ip": "111.197.160.56:8118"},
            {"ip": "125.211.202.26:53281"},
            {"ip": "183.32.88.219:6666"},
            {"ip": "112.114.97.45:8118"},
            {"ip": "222.241.15.77:8888"},
            {"ip": "112.114.96.152:8118"},
            {"ip": "125.122.148.115:61234"},
            {"ip": "112.114.97.230:8118"},
            {"ip": "27.40.134.71:61234"},
            {"ip": "60.214.155.243:53281"},
            {"ip": "183.163.36.106:54318"},
            {"ip": "112.114.99.164:8118"},
            {"ip": "49.85.0.206:49344"},
            {"ip": "58.56.149.198:53281"},
            {"ip": "39.134.161.14:8080"},
            {"ip": "42.49.119.155:8118"},
            {"ip": "39.155.169.70:80"},
            {"ip": "163.177.151.23:80"},
            {"ip": "120.199.64.163:8081"},
            {"ip": "61.187.251.235:80"},
            {"ip": "221.233.85.95:3128"},
            {"ip": "219.138.58.82:3128"},
            {"ip": "117.65.40.218:44311"},
            {"ip": "183.32.89.140:6666"},
            {"ip": "106.57.22.116:61234"},
            {"ip": "122.235.169.126:8118"},
            {"ip": "182.88.196.251:8118"},
            {"ip": "112.114.97.233:8118"},
            {"ip": "112.114.96.178:8118"},
            {"ip": "124.31.72.26:80"},
            {"ip": "139.209.90.50:80"},
            {"ip": "211.159.171.58:80"},
            {"ip": "112.114.95.83:8118"},
            {"ip": "39.134.161.12:8080"},
            {"ip": "219.138.58.176:3128"},
            {"ip": "221.233.85.52:3128"},
            {"ip": "180.156.95.157:8118"},
            {"ip": "114.245.176.79:8118"}

        ]
        ip = random.choice(IPPOOL)
        # print('now ip is :'+ ip['ip'])
        request.meta['proxy'] = "http://"+ip['ip']
        request.meta['download_timeout'] = 10

