#!/usr/bin/env python

from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/hpkp', methods=['POST'])
def testhpkp():
	content = request.get_json(force=True)
	conn = sqlite3.connect('hpkp.sqlite')
	c = conn.cursor()
	servedchain = ""
	validatedchain = ""
	pinchain = ""

	for cert in content["served-certificate-chain"]:
		servedchain += cert
	for cert in content["validated-certificate-chain"]:
		validatedchain += cert
	for pin in content["known-pins"]:
		pinchain += pin + ";"

	q = "INSERT INTO reports values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')"
	query = q.format(content["date-time"], content["hostname"], content["port"], content["effective-expiration-date"], content["include-subdomains"], content["noted-hostname"], servedchain, validatedchain, pinchain)
	c.execute(query)
	conn.commit()
	conn.close()
	return 'Success'

if __name__ == '__main__':
	app.run(debug=True)
