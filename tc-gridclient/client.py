#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#       client.py
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

import data, erros, sys, time, json
import urllib.request as urllib
import multiprocessing

class cliente(multiprocessing.Process):

        def __init__(self,key):
                super(cliente,self).__init__()

                lurl = "http://localhost:8080/tick.regtick"
                self.url = lurl
                self.errors = erros.logger("erros_cliente.log");
                self.errors.calee = "cliente.py";

                self.fetcher = data.Fetcher(1,key);
                self.datalogger = True
        def run(self, timer):
                self.work(timer)

        def work(self, timer):
                import time;
                try:
                        pidf = open(".client.pid","r")
                        pid = True
                        pidf.close()
                except:
                        pidf = open(".client.pid","w")
                        pidf.close()
                        pid = True

                while pid:

                        string = self.fetcher.fetch();
                        enc = json.dumps(string)
                        enc = enc.encode('utf-8');
                        r = urllib.Request(self.url, data=enc, headers={'Content-Type': 'application/json'})
                        try:
                                res = urllib.urlopen(r);
                                #resp, content = h.request(self.url,'POST',enc,headers={'Content-Type': 'application/json'})
                                print("Tick")
                        except:
                                error = "Couldnt connect to server"
                                self.errors.reg(error,1)
                                print("Failed")
                        #checagem de existencia de arquivo
                        try:
                                pidf = open(".client.pid","r")
                                pid = True
                                pidf.close()
                        except:
                                pid = False
                                self.errors.reg("Interrompido", 0)
                        time.sleep(timer)


        def datalog(self):
                from time import sleep

                while self.datalogger:

                        sleep(300);
                        f = data.Fetcher(2,key)

if __name__ == '__main__':

        import random
        from time import sleep

        r = random.Random()


        try:
                f = open(".key.dat", "r")
                key = str(f.read())

                if len(key) == 0:
                        key = r.randint(1,1000000)
                        f = open(".key.dat", "w")
                        f.write(key)
                else:
                        key = int(key)
        except:
                key = r.randint(1,1000000)
                f = open(".key.dat", "w")
                f.write(str(key))

        client = cliente(key);
        client.run(250)
        hour = 60*60*60
        while True:
                sleep(hour)
        client.join()
