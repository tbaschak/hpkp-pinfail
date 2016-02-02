#!/usr/bin/env python

import sqlite3
conn = sqlite3.connect('hpkp.sqlite')

c = conn.cursor()

# Create table
for row in c.execute('''SELECT * FROM reports'''):
      print row

conn.close()
