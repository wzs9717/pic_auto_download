from __future__ import print_function
import os
import logging

from scrapy.utils.job import job_dir
from scrapy.utils.request import request_fingerprint


class RepeatFilter(object):
    def __init__(self):
        self.set=set()
    @classmethod
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):
        if request.url in self.set:
            return True
        self.set.add(request.url)
        return False
    def open(self):  # can return deferred
        print("open")

    def close(self, reason):  # can return a deferred
        print("close")

    def log(self, request, spider):  # log that a request has been filtered
        pass


