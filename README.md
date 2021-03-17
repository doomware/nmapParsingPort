# nmapParsingPort
**Python 3 automatic grep to nmap grepable file ports**
This tool parsing automatically the ports and hosts of the grepable file that can be obtained in nmap

## Requirements
 - argparse
 - pyperclip
 - colorama

```bash
pip3 install -r requirements.txt
```

## Usage
```python
usage: ./portParser.py.py [-h] [-c] [-s] [-t] file
```
```bash
usage: portParser.py [-h] [-c] [-s] [-t] file

positional arguments:
  file        Name of nmap grep file

optional arguments:
  -h, --help  show this help message and exit
  -c          Copy ports to clipboard
  -s          Show services
  -t           Show ports and services in table mode
```

By default grep all open ports:

```python
./portParser.py [file]
```
```bash
./portParser.py test/nmap         

 [*] Host:       45.33.32.156 (scanme.nmap.org) 

 [*] Ports:      22,80,9929,31337 
```

If you want to show services in plain text, pass the -s flag:

```python
./portParser.py [file] -s
```
```bash
./portParser.py test/nmap -s

 [*] Host:       45.33.32.156 (scanme.nmap.org) 

 [*] Ports:      22,80,9929,31337 

 [*] Services:   ssh,http,nping-echo,Elite
```

This script has the possibility to copy the ports directly to the clipboard, you just have to indicate the -c flag (Can be copied in any mode):
```python
./portParser.py [file] -c
```
```bash
./portParser.py test/nmap -c

 [*] Host:       45.33.32.156 (scanme.nmap.org) 

 [*] Ports:      22,80,9929,31337 

 [*] Ports copied to clipboard
```

And you can also print the ports and services in table format by specifying -t. (If you pass the -t flag, the ports will not be shown in plain text, nor the services if '-s' is indicated)
```python
./portParser.py [file] -t
```
```bash
./portParser.py test/nmap -t

 [*] Host:       45.33.32.156 (scanme.nmap.org) 

 [*] Table view
        Port:       Service:
        22           ssh
        80           http
        9929       nping-echo
        31337     Elite
```


------------

Any improvement or correction will be accepted
