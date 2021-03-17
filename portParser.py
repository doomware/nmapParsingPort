#!/usr/bin/env python3
# Automatic grep to nmap grepable file ports

import argparse
import re
import sys

import colorama
import pyperclip

colorama.init()
RED, BLUE, BLACK, YELLOW = colorama.Fore.RED,colorama.Fore.BLUE,colorama.Fore.BLACK,colorama.Fore.YELLOW

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

def get_open(line):
	""" 
	This function receives the iterated line of the grep file and adds the ports and services that are open to a list 
	"""
	line = "".join(line) # Convert from list to str to be able to split the ports later 
	line = line.split(", ") # Cut the line by the commas, separating the ports
	for i in line:
		if "open" in i:
			port = "".join(re.findall(r"(.*\d)/", i)).strip() # Regex to get the port if it is open 
			service = "".join(re.findall(r"//(.*)///",i)).strip() # Regex to get the service on the line 
			arrayPorts.append(port) # It is added to the 'arrayPorts' list 
			arrayServices.append(service) # It is added to the 'arrayServices' list 
		else:
			pass

def main(namefile):
	"""
	The Main function first establishes a counter at 0, then tries to open the past grep file as an argument, and with a for cycle you start touring that file, if the file is not grepable ends the program. Then go through until it finds the line that contains the ports and calls the function 'get_open' passing as argument 'l' 
	"""
	global arrayPorts
	global arrayServices
	global host
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
					host = "".join(re.findall(r"Host: (.*)\tPorts:", l)) # Remove all unnecessary words, leaving only the host 
					line = re.findall(r"Ports: (.*)\tIgnored", l) # Remove all unnecessary words, leaving only ports
					if "".join(line) == "":
						line = re.findall(r"Ports:(.*)", l) # In case it doesn't work in regex this may work 
					get_open(line)
		file.close()
	except FileNotFoundError:
		print("\n",RED,"[!] No such file or directory: {}".format(nameFile))
		sys.exit(0)

if __name__ == '__main__':
	nameFile = args.file
	boolPort = True
	boolService = args.s
	boolClipboard = args.c
	boolTable = args.t
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
				print(" [*] Services:\t",services)
			else:
				services = f"{YELLOW}[!] No services"	
	if boolClipboard:
		pyperclip.copy(ports)
		print(BLUE,"[*] Ports copied to clipboard")
