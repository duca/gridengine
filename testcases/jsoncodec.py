#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       jsoncoder.py
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

def fetch():
                import os
                from multiprocessing import cpu_count

                load = os.getloadavg()[1];
                hostname = os.uname()[1];
                kernel = os.uname()[2];
                cores = cpu_count();

                load = load*100/cores;
                try:
                        memory = os.popen("free -m").readlines()[1];
                        total = int(memory.split()[1]);
                        used = int(memory.split()[2]);
                        cached = int(memory.split()[6]);
                        free_ram = total - (used - cached);
                except:
                        total = 1000;
                        free_ = 500;

                summary = { 'name': hostname, 'load': load, 'kernel': kernel, 'cores': cores, 'total_ram' :total, 'ava_ram':free_ram }

                resumido = [hostname,load]
                return summary

def main():
        import json, hashlib, zlib,pickle, base64

        data = fetch()

        string = json.dumps(data, separators=(',','.'))
        hstring = hashlib.sha1(string).hexdigest()


        print data
        pickled= pickle.dumps(data,1)
        print pickled.__sizeof__()

        print "tam original"
        print string.__sizeof__()


        print "tam base64"
        base = base64.urlsafe_b64encode(pickled)
        #base = base64.b16encode(pickled)
        print base.__sizeof__()

        print "tam hashed"
        print hstring.__sizeof__()
        cstring = zlib.compress(string,1)

        print "tam comprimido"
        print cstring.__sizeof__()

        return 0

if __name__ == '__main__':
        main()
