#!/usr/bin/python3

import subprocess
import time

value = True
while (value):
	p = subprocess.Popen('/home/USER/slideshow/slideshow.py')
	time.sleep(60)
	p.kill()
	time.slpper(60)
