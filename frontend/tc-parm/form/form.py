#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       sem título.py
#       
#       Copyright 2011  <usuario@QNInt>
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
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
	""" Class doc """
	
	def get(self):
		""" Function doc """
		self.response.out.write("""
			<html>
				<body>
					<form action="/sign" method="post">
						<div><textarea name="content" rows="3" cols="60"></textarea></div>
						<div><input type="submit" value="Sign"></div>
					</form>
				</body>
			</html>""")
class Guestbook(webapp.RequestHandler):
	""" Class doc """
	
	def post(self):
		self.response.out.write('<html><body>You wrote:<pre>')
		self.response.out.write(cgi.escape(self.request.get('content')))
		self.response.out.write('</pre></body></html>')

application = webapp.WSGIApplication(
									[('/', MainPage),'/sign', Guestbook)],
									debug=True)


def main():
	
	return 0

if __name__ == '__main__':
	main()

