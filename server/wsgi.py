#!/usr/bin/env python

import sys
import os

sys.path.append('/var/www/html/recepies/recepie_book/venv/lib64/python3.6/site-packages')
sys.path.insert(0, '/var/www/html/recepies/recepie_book')

from server import app as application

print("Starting Server...")
