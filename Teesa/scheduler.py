#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-11-23 10:28:04

import asyncio


class Scheduler:
    '''
    从redis取出url, 并传给crawl爬取
    '''
    def __init__(self, crawl, cache):
        self.crawl = crawl
        self.cache = cache

    async def get_url(self):
        url = await self.cache.get()
        return url

    async def push_url(self):
        await self.crawl.fetch(url)

    def run(self):
        pass
