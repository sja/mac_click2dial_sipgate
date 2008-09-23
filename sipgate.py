#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple and uncomplete sipgate python api

autho: Marcel Lauhoff <ml@irq0.org>
"""


import sys,os
import getopt
import re

import xmlrpclib
from ConfigParser import ConfigParser

IDENT={'ClientName': 'irq0.org sipgate api',
       'ClientVersion': '0.1'}

PATH=sys.path[0]



class SimpleSipgateApi:
    """ simple and uncomplete si pgate api :) """
    
    def __init__(self, user, passwd):
        self.conn = xmlrpclib.ServerProxy(
            "https://%s:%s@samurai.sipgate.net/RPC2" % (user, passwd))
        
        result = self.conn.samurai.ClientIdentify(IDENT)
    
        if result['StatusCode'] != 200:
            print "connection failed :( .. exiting"
            sys.exit(23)
    def sms(self, remote_uri, text):
        result = self.conn.samurai.SessionInitiate({'RemoteUri': sip_uri,
                                                    'TOS': 'text',
                                                    'Content': text})
        return result['StatusCode'] == 200

    def call(self, local_uri, remote_uri):
        result = self.conn.samurai.SessionInitiate({'RemoteUri': remote_uri,
                                                    'LocalUri': local_uri,
                                                    'TOS': 'voice'})
        return result['StatusCode'] == 200