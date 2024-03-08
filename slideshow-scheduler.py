#!/usr/bin/python3

import subprocess
import time

p = subprocess.Popen('/home/USER/slideshow/slideshow.py')

time.sleep(60)

p.kill()
