#!/usr/bin/env python

import sqlite3
conn = sqlite3.connect('hpkp.sqlite')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE reports
             (datetime text, 
             	hostname text, 
             	port text, 
             	effectiveexpdate text, 
             	includesubdomains text,
             	notedhostname text,
             	servedcertificatechain text, 
             	validatedcertificatechain text,
             	knownpins text
             	)''')

conn.commit()

conn.close()
