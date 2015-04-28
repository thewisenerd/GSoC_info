#!/usr/bin/env python

import urllib
import types
import codecs
import sys
import os

_abstract_f="abstract.txt"

os.remove(_abstract_f)

f = urllib.urlopen(sys.argv[1])

_doc=f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(_doc)

div = soup.find_all('p', {"class": "description"})
if len(div):
	for elem in div:
		_content = elem.find('strong')
		if ( _content.text == "Abstract:" ):
			_desc = elem.text[len("Abstract: "):]
			with open (_abstract_f, "w") as myfile:
				myfile.write(_desc)
				myfile.close()

exit(0);
