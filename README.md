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
![Alt text](/docs/help_menu.png?raw=true "Help Menu")

By default grep all open ports:

```python
./portParser.py [file]
```
![Alt text](/docs/port_auto.png?raw=true "")

If you want to show services in plain text, pass the -s flag:

```python
./portParser.py [file] -s
```

![Alt text](/docs/services.png?raw=true "Services")

This script has the possibility to copy the ports directly to the clipboard, you just have to indicate the -c flag (Can be copied in any mode):
```python
./portParser.py [file] -c
```

![Alt text](/docs/clipboard.png?raw=true "Clipboard")

And you can also print the ports and services in table format by specifying -t. (If you pass the -t flag, the ports will not be shown in plain text, nor the services if '-s' is indicated)
```python
./portParser.py [file] -t
```

![Alt text](/docs/tableview.png?raw=true "Table")


------------

Any improvement or correction will be accepted
