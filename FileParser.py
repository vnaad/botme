#!/usr/bin/env python

try:
	import unicodecsv as csv
except ImportError:
	import csv

import re
import json
import operator
import os
from collections import OrderedDict
from pathlib import Path

class FileParser(object):

	data = OrderedDict()
	lastline = 0

	def __init__(self, myname):
		self.myname = myname
	
	def parse_jsonfile(self,infile):
		indata = Path(infile)
		if not indata.is_file(): raise ValueError("Input file does not exist:",infile)
		with open(infile, 'r') as f: return json.load(f)

	def clean_up(self,message):
		# Remove new lines within message
		cleanedMessage = message.replace('\n',' ').lower()
		# Remove tabs within message
		cleanedMessage = message.replace('\t',' ').lower()
		# Deal with some weird tokens
		cleanedMessage = cleanedMessage.replace("\xc2\xa0", "")
		# Remove punctuation
		cleanedMessage = re.sub('([.,!?])','', cleanedMessage)
		# Remove multiple spaces in message
		cleanedMessage = re.sub(' +',' ', cleanedMessage)
		return cleanedMessage

	def load_line(self, name, ts, msg):
		print(name,ts,msg)
	
	def parse_facebook(self, infile):
		ds=self.parse_jsonfile(infile)
		for message in ds['messages']:
			self.load_line( message['sender_name'], message['timestamp_ms'], self.clean_up( message['content'] ) )
		
