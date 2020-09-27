# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        film_title = item['film_title']
        film_type = item['film_type']
        plan_date = item['plan_date']
        output = f'{film_title},{film_type},{plan_date}\n'
        print(output)
        with open('./HomeWork02.csv', 'a+', encoding='utf-8') as result:
            result.write(output)
            result.close()
        return item
