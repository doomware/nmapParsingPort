#!/usr/bin/env python3
# Automatic grep to nmap grepable file ports

import argparse
import re
import sys
import pyperclip
import colorama

colorama.init()
RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
BLACK = colorama.Fore.BLACK
YELLOW = colorama.Fore.YELLOW

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Name of nmap grep file")
parser.add_argument("-c", help="Copy ports to clipboard", action="store_true")
parser.add_argument("-s", help="Show services", action="store_true")
parser.add_argument("-t", help="Show ports and services in table mode", action="store_true")
args = parser.parse_args()

def tableView(ports, services):
	print(" [*] Table view")
	print(f"\tPort:\tService:")
	for port, service in zip(ports, services):
		print(f"\t{port}\t{service}")

def getHost(txt):
	global host
	firstDelimiter = "Ports: "
	secondDelimiter = "Host: "
	thirdDelimiter = "("
	host = txt[len(secondDelimiter):txt.find(firstDelimiter)]
	blankHost = host.find(thirdDelimiter)
	lenHost = len(host) - blankHost
	if lenHost <= 4:
		host = host[:-lenHost]

def quitJunk(txt):
	firstDelimiter = "Ports: "
	secondDelimiter = "Ignored"
	lenPorts = len(firstDelimiter)
	txt = txt.strip()
	portPos = txt.find(firstDelimiter)
	ignorePos = txt.find(secondDelimiter)
	lenTxt = len(txt)
	cutPos = lenTxt - ignorePos
	portPos = lenPorts + portPos
	txt = txt[portPos:-cutPos]
	return txt

def clipboard(ports):
	pyperclip.copy(ports)
	#print(BLUE,"-"*30)
	print(BLUE,"[*] Ports copied to clipboard")

def getServices(i):
	service = re.search(r'//(.*?)///', i).group(1)
	return service

def parsingPorts(i):
	port = re.search(r'(.*?)/', i).group(1)
	return port

def main(namefile):
	global arrayPorts
	global arrayServices
	lineCount = 0
	arrayPorts = []
	arrayServices = []
	try:
		file = open(nameFile, 'r')
		lines = file.readlines()
		for l in lines:
			lineCount += 1
			if "-oG" not in l and lineCount == 1:
				print("\n",RED,"[!] File not grepeable")
				file.close()
				sys.exit(0)
			if l.startswith("Host:"):
				if "Ports" in l:
					getHost(l)
					array = quitJunk(l)
					array = array.split(", ")
					#print(array)
					for i in array:
						try:
							if "filtered" not in i:
								if "closed" not in i:
									port = parsingPorts(i)
									arrayPorts.append(port)
									service = getServices(i)
									arrayServices.append(service)
						except:
							pass
		

		file.close()
	except FileNotFoundError:
		print("\n",RED,"[!] No such file or directory: {}".format(nameFile))
		sys.exit(0)

if __name__ == '__main__':
	nameFile = args.file
	#nameFile = "nmapgrep"
	boolPort = True
	boolService = args.s
	boolClipboard = args.c
	boolTable = args.t
	#boolTable = True
	#print("\n")
	main(nameFile)
	print("\n [*] Host:\t",host,"\n")
	ports = ",".join(arrayPorts)
	services = ",".join(arrayServices)
	if boolTable:
		boolPort = False
		boolService = False
		#print("Table mode")
		tableView(arrayPorts,arrayServices)
	else:
		if ports == "":
			print(YELLOW,"[!] Ports:\t No open ports")
			sys.exit(0)
		else:
			print(" [*] Ports:\t",ports,"\n")
		if boolService:
			if services != "":
				#services = ",".join(services)
				print(" [*] Services:\t",services)
			else:
				services = f"{YELLOW}[!] No services"	
	if boolClipboard:
		clipboard(ports)
