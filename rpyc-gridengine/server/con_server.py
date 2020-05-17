#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       con_server.py
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
import erros, rpyc, rrdb

ws_online = {"online":None};

class mainService(rpyc.Service):

        def on_connect(self):
                import sys
                global ws_online

                sys.stderr.write("Someone Connected \t")
                text = "I have %d workstation(s) online \n" %(len(ws_online))
                print ws_online

        class exposed_Machine(object):
                def __init__(self, st_name, st_samplespday, data_callback):

                        from multiprocessing import Process, Pipe
                        import rpyc

                        self.machine = st_name;
                        self.machsummary = {};
                        self.samplespday = st_samplespday;
                        self.active = True;
                        self.callback = data_callback;
                        self.ctrlPipe = Pipe();

                        self.errorl = erros.logger("server_erros.log");
                        self.errorl.calee = "Server: mainService(__init__)";
                        self.machsummary = self.callback();
                        self.delay = 24*60*60/self.samplespday;
                        thrd = Process(target=self.worker());
                        thrd.start();

                def exposed_reg_workstation(self, summary):
                        import datetime
                        global ws_online

                        ws_time = datetime.datetime.utctimetuple(self.summary["time"]);
                        ws_online.update({self.summary["name"]:self.summary["load"]});
                        self.errorl.reg("Registering: ",1);

                def worker(self):
                        import time

                        while self.active:
                                self.machsummary = self.callback();
                                time.sleep(self.delay);

if __name__ == '__main__':
        from rpyc.utils.server import ThreadedServer

        ThreadedServer(mainService, port=8082).start()
