# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import sqlite3


class ImdbPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        logging.warning(crawler.settings.get("MONGO_URI"))

    def open_spider(self, spider):
        logging.warning("SPIDER OPENED FROM PIPELINE")

    def close_spider(self, spider):
        logging.warning("SPIDER CLOSED FROM PIPELINE")

    def process_item(self, item, spider):
        return item


class SQLlitePipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect("imdb.db")
        self.curr = self.connection.cursor()
        try:
            self.curr.execute("""
                CREATE TABLE best_movies(
                    title TEXT,
                    year TEXT, 
                    duration TEXT, 
                    genre TEXT, 
                    rating TEXT, 
                    movie_url TEXT 
                )
            
            """)
        except sqlite3.OperationalError:
            pass

        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):

        self.curr.execute("""
            INSERT INTO best_movies (title, year, duration, genre, rating, movie_url) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            item.get("title"),
            item.get("year"),
            item.get("duration"),
            item.get("genre"),
            item.get("rating"),
            item.get("movie_url")
        ))

        self.connection.commit()
        return item
