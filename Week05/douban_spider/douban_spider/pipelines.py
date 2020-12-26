# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
import pymysql
from datetime import datetime

class DoubanSpiderPipeline:
    def open_spider(self, spider):
        # 建立连接
        self.conn = pymysql.connect(
            host='192.168.0.57',
            user='zcat',
            password='MySQL5.7',
            database='Django-Test',
        )
        # 创建游标
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()


    def process_item(self, item, spider):
        cid = item['cid']
        #updatetime = item['updatetime']
        updatetime = 'NULL' if item['updatetime'] == None else f"'{item['updatetime']}'" 
        user = item['user']
        star = 'NULL' if item['star'] == 0 else item['star']
        #item['title']
        short = item['short']


        sql = f"INSERT INTO movies_comments(cid, updatetime, username, star, short) VALUES( \
                '{cid}', \
                {updatetime}, \
                '{user}', \
                {star}, \
                '{short}')"

        #print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print('******************PROCESS ITEM ERROR!!******************')
            print(repr(e))
            print(sql)
            self.conn.rollback()
        
        return item
