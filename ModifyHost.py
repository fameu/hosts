# -*- coding: gbk -*-

import sys
import urllib

def ModifyHost(host_path, host_url):
	f1 = urllib.urlopen(host_url)
	host_contect = f1.read()
	host_file = open(host_path, "w")
	host_file.write(host_contect)
	host_file.close()


if __name__ == "__main__":
	if len(sys.argv) == 3:
		print sys.argv
		host_path = sys.argv[1]
		host_url = sys.argv[2]
	else:
		host_path = "C:\Windows\System32\drivers\etc\hosts"
		host_url = "https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts-files/hosts"
	
	ModifyHost(host_path, host_url)
	
