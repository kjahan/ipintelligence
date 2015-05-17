import requests, json, sys

ipinfo_baseurl = 'http://ipinfo.io/'

def get_ipinfo(ip_addr):
    r = requests.get(ipinfo_baseurl + ip_addr + '/json')
    ipinfo = json.loads(r.text)
    return ipinfo

def get_loc(ipinfo):
    return ipinfo['loc']

def get_city(ipinfo):
    return ipinfo['city']

def get_region(ipinfo):
    return ipinfo['region']

def get_country(ipinfo):
    return ipinfo['country']

def get_hostname(ipinfo):
    return ipinfo['hostname']

def get_org(ipinfo):
    return ipinfo['org']

def get_loc(ipinfo):
    return ipinfo['loc']

def get_postal(ipinfo):
    return ipinfo['postal']

def main(ipaddr):
    ipinfo = get_ipinfo(ipaddr)
    print get_org(ipinfo)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Usage: %s ip-address' % sys.argv[0])
    main(sys.argv[1])
