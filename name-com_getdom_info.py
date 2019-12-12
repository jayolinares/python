#!/usr/bin/env python

import os, sys, requests, json, urlparse

script_name = sys.argv[0]
name_url = 'https://api.name.com/v4/domains/'
name_user = os.environ['name_user']
name_api = os.environ['name_api']

try:
    domain = sys.argv[1]
except:
    print 'Error. Domain name wasn\'t add as an argument.'
    print 'Usage: {} domain \n'.format(script_name)
    exit(1)

def dom_url():
	dom_join = urlparse.urljoin(name_url, domain)
	return dom_join


def getDomain():
	get_dom = requests.get(dom_url(), auth=(name_user, name_api))
	try:
		get_dom_cre = get_dom.json()['createDate']
		get_dom_exp = get_dom.json()['expireDate']
		get_dom_sta = get_dom.json()['locked']
		get_dom_ns = get_dom.json()['nameservers']
		get_dom_data = (get_dom_cre, get_dom_exp, get_dom_sta, get_dom_ns);
		return get_dom_data
	except:
		print 'Error! Check if you own the domain and if it is registered with Name.com. \n'
		sys.exit(1)

dom_details = getDomain()
n_servers = dom_details[3]


print '\n', domain, '\n'
print "Create date: ", dom_details[0]
print "Expire date: ", dom_details[1]
print "Status (if locked): ", dom_details[2]
print '\n'
for ns in n_servers:
	try:
		print "Name Servers: ", ns
	except:
		print "Name Servers: None"

print '----------------------------------------------'
