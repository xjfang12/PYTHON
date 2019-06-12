from xmlrpc.client import ServerProxy
from os.path import join, isfile
from xmlrpc.server import SimpleXMLPRCServer
from urllib.parse import urlparse
import sys

MAX_HISTORY_LENGTH=6

OK = 1
FAIL = 2
EMPTY = ''
class Node:
    def __init__(self, url, dirname, secret):
        self.url = url
        self.dirname= dirname
        self.secret = secret
        self.known= set()
    
    def query(self, query):
        pass
    
    def fetch(self, query, secret):
        pass
    
    def hello(self, other):
        pass