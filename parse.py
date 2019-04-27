#!/usr/bin/env python

from FileParser import FileParser
import logging

logging.basicConfig(level=logging.DEBUG)


def init_parser():
	import argparse
	parser = argparse.ArgumentParser(description="Converts Social Media Dumps to csv")
	parser.add_argument('-fb', '--facebook', type=str, default=None, help="Input json file for Facebook data")
	parser.add_argument('-li', '--linkedin', type=str, default=None, help="Input json file for LinkedIn data")
	parser.add_argument('-gh', '--hangouts', type=str, default=None, help="Input json file for Google Hangouts data")
	parser.add_argument('-wa', '--whatsapp', type=str, default=None, help="Input txt file for Whatsapp data")
	parser.add_argument('-o', '--outfile', type=str, default='stdout', help="Output file default stdout")
	parser.add_argument('-me', '--myname', type=str, required=True, help="User name in chat")
	return parser

## Main
if __name__ == '__main__':
	parser = init_parser()
	args = parser.parse_args()
	f = FileParser(args.myname)

	try:
		if args.facebook is not None:
			f.parse_facebook(args.facebook)

	except Exception as e:
		print ("Error: " , e.args)
		
