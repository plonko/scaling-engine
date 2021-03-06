# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sys
from scrapy.exceptions import DropItem


class ContainsKeywordPipeline:
    def process_item(self, item, spider):
        if "Albert" in item["name"]:
            return item
        else:
            raise DropItem("Not in %s" % item["name"])


class SaveToDbPipeline:
    def process_item(self, item, spider):
        try:
            item["brand"] = spider.brand
            item.save()
            print("Added %s" % item["title"])
        except:
            e = sys.exc_info()[1]
            print("ERROR. Could not add %s" % item["title"])
            print(e)
        return item
