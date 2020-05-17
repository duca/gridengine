#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       mcache.py
#
#       Copyright 2020 Eduardo Martins Lopes <edumlopes@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
#

from google.appengine.api import memcache
import wsDB

class cacher:
        """ Class doc """

        def __init__(self,key):
                self.dummy = None
                self.key = key

                #db = wsDB.manager()

        def updatecache(self,data):

                if memcache.get(self.key) is None:
                        memcache.add(self.key,data)
                else:
                        memcache.replace(self.key,data)

        def update_timed(self, obj, life):

                memcache.add(self.key,obj,life)


        def retrieve(self):

                result = memcache.get(self.key)
                if result is None:
                        result=[]

                return result

        def updatelist(self, obj):

                data = self.retrieve()

                if data.__contains__(obj) is False:
                        data.append(obj)
                        self.updatecache(data)

        def updatedict(self, key,info,life):

                data = memcache.get(key)

#		if data is None:
                memcache.add(key, info,life)
#		else:
#			memcache.replace(key,info,life)

        def retrievedict(self,key):

                data = memcache.get(key)

                if data is not None:
                        return data
                else:
                        return -1

        def removeitem(self, data, item):

                for i in range(0, len(data)):
                        if data[i] == item:
                                data.pop(i)
                memcache.replace(self.key, data)

def main():

        a = []

if __name__ == '__main__':
        main()
