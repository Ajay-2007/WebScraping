# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import sqlite3
import pymongo


class MongodbPipeline(object):
    collection_name = "best_movies"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://webscraping:webscraping@cluster0-st61f.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client["IMDB"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
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
