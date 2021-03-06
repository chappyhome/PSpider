# _*_ coding: utf-8 _*_

"""
define WebSpider, WebSpiderAsync, and also define utilities and instances for web_spider
"""

from .utilities import *
from .insts_thread import Fetcher, Parser, Saver
from .insts_async import FetcherAsync, ParserAsync, SaverAsync
from .module_concurrent import WebSpider, WebSpiderAsync
