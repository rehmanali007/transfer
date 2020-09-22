#!/usr/bin/python3
import subprocess
import re


data = subprocess.getoutput("i3-input -P 'GOOGLE: '")

outPutRegex = re.compile(r'output = (.*)')
mo = outPutRegex.search(str(data))
url = f'https://www.google.com/search?q={mo.group(1)}'

subprocess.run(["chromium-browser", url])
