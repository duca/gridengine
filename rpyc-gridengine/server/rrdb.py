#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       rrdb.py
#
#       Copyright 2020 Eduardo Martins <edumlopes@gmail.com>
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
class rrdb1D:

        def __init__(self, nsamples):

                self.size = nsamples;
                self.database = range(self.size);
                self.zeroer();
                self.ndx = 0;

        def insert(self,item):

                self.database[self.ndx] = item;
                self.ndx = self.ndx + 1;

                if self.ndx == self.size:
                        self.restart();

        def restart(self):
                self.ndx = 0; #restart the counter

        def dump(self):
                return self.database;

        def zeroer(self):

                for i in range(0,len(self.database)):
                        self.database[i] = 0;

if __name__ == '__main__':

        test = rrdb1D(10000);

        test.zeroer()
        for i in range(0,10000):
                test.insert(i)
        print test.dump()

        j = 10000;
        for i in range(0, 10000):
                j = 10000 - i;
                test.insert(j)

        print test.dump()
