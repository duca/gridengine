#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       services.py
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
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import postservice
from protorpc.webapp import service_handlers

application = webapp.WSGIApplication(service_handlers.service_mapping([('/tick', postservice.ReceiveTick)]),debug=True)


def main():
        util.run_wsgi_app(application)
        #webapp.WSGIApplication(application)
if __name__ == '__main__':
        main()
