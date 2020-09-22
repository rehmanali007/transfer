import subprocess
import pyperclip


run = subprocess.run

url = f'https://www.google.com/search?q={pyperclip.paste()}'

run(["chromium-browser", url])

