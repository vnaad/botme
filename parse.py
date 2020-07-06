#!/usr/bin/env python

from FileParser import FileParser
import logging

logging.basicConfig(level=logging.DEBUG)


def init_parser():
	import argparse
	parser = argparse.ArgumentParser(description="Converts Social Media Dumps to csv")
	parser.add_argument('-d', '--datadir', type=str, default='./data', help="Storage Directory default local ./data")
	parser.add_argument('-fb', '--facebook', type=str, default=None, help="Input json file for Facebook data")
	parser.add_argument('-li', '--linkedin', type=str, default=None, help="Input json file for LinkedIn data")
	parser.add_argument('-gh', '--hangouts', type=str, default=None, help="Input json file for Google Hangouts data")
	parser.add_argument('-wa', '--whatsapp', type=str, default=None, help="Input txt file for Whatsapp data")
	parser.add_argument('-o', '--outfile', type=str, default='stdout', help="Output file default stdout")
	parser.add_argument('-me', '--myname', type=str, default='', help="User name in chat")
	parser.add_argument('--create-vectors', default=False, action='store_true', help="Create vectors from data")
	parser.add_argument('-s', '--show', default=False, action='store_true', help="Display input data")
	return parser

## Main
if __name__ == '__main__':
	parser = init_parser()
	args = parser.parse_args()
	f = FileParser(args.myname, args.datadir)

	t_save=0

	try:
		if args.facebook is not None:
			f.parse_facebook(args.facebook)
			t_save+=1

		if t_save > 0:
			f.save_data()

	except Exception as e:
		print ("Error: " , e.args)
		
