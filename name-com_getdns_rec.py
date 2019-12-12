#!/usr/bin/env python3

# dump all the DNS records of the domain registered with Name.com
# dump all the DNS records of the domain using Name.com's Name Servers
# Jay Olinares
import sys, requests, json, os

script_name = sys.argv[0]
if len(sys.argv) > 1:
    pass #    print(sys.argv[1])
else:
    print('Error. Domain name wasn\'t add as an argument.')  
    print(f'Usage: {script_name} domain \n')
    exit(1)

domain = sys.argv[1]
name_url = 'https://api.name.com/v4/domains/'
name_user = os.environ['name_user']
name_api = os.environ['name_api']

def dom_dns_url():
	dom_join_add_recs = name_url + str(domain) + str('/records')
	return dom_join_add_recs


def get_dns_recs():
	get_dns = requests.get(dom_dns_url(), auth=(name_user, name_api))
	try:
		get_dns_data = get_dns.json()['records']
		return get_dns_data
	except KeyError as error:
		print('Error! Check if you own the domain and if DNS is hosted with Name.com.\n')
		sys.exit(1)
	except Exception as e:
		print(e)
		sys.exit(1)

#dns_dumps = get_dns_recs()
for dom_name in get_dns_recs():
	print('FQDN:', dom_name['fqdn'])
	print('DNS record_type:', dom_name['type'])
	print('Answer:', dom_name['answer'])
	print('TTL:', dom_name['ttl'])
	print('----------------------------------------------\n')

