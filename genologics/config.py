import os
import sys
import warnings

import ConfigParser

config = ConfigParser.SafeConfigParser()
try:
	conf_file = config.read(['genologics.cfg', os.path.expanduser('~/.genologicsrc'), '.genologicsrc',
				'genologics.conf', '/etc/genologics.conf'])

	# First config file found wins
	config.readfp(open(conf_file[0]))
	
	BASEURI = config.get('genologics', 'BASEURI').rstrip()
	USERNAME = config.get('genologics', 'USERNAME').rstrip()
	PASSWORD = config.get('genologics', 'PASSWORD').rstrip()

except:
	warnings.warn("Please make sure you've created your own Genologics configuration file (i.e: ~/.genologicsrc) as stated in README.md")
	sys.exit(-1)

if config.has_section('logging') and config.has_option('logging','MAIN_LOG'):
	MAIN_LOG = config.get('logging', 'MAIN_LOG').rstrip()
else:
	MAIN_LOG = None
