#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       frontgrid.py
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
import mcache, wsDB
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
class MainPage(webapp.RequestHandler):
        def get(self):
                self.response.out.write('<html><body>')

                machines = wsDB.manager()
                mws = mcache.cacher("machines")
                total_machines = machines.retrieveActive()

                if len(total_machines) == 0:
                        self.response.out.write("<p>No machines are online at the moment</p>")
                else:
                        for machine in total_machines:
                                load = mws.retrievedict(machine)
                                if load != -1:
                                        tmp = str(load)+ r'%'
                                        self.response.out.write("<p>%s load is %s</p>" % (machine,tmp))
                                else:
                                        self.response.out.write("<p>%s is offline at the moment</p>" % (machine))


                self.response.out.write("</body></html>")

def main():

        application = webapp.WSGIApplication([('/', MainPage),], debug=True)
        run_wsgi_app(application)

if __name__ == '__main__':
        main()
