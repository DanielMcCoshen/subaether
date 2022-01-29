#!/usr/bin/env python

import sys
import os

sys.path.append('/var/www/html/recepies/recepie_book/venv/lib64/python3.6/site-packages')
sys.path.insert(0, '/var/www/html/recepies/recepie_book')

from server import app as application

if not os.path.exists(application.config["RECEPIE_PATH"]):
    print("Storage Directory does not exist, creating it")
    os.makedirs(application.config["RECEPIE_PATH"])

if not os.path.exists(f"{application.config['RECEPIE_PATH']}/all_recepies/"):
    print("Createing recepie directory")
    os.makedirs(f"{application.config['RECEPIE_PATH']}/all_recepies/")

for category in application.config["CATEGORIES"]:
    if not os.path.exists(f"{application.config['RECEPIE_PATH']}/{category}/"):
        print(f"Createing Directory for {category}")
        os.makedirs(f"{application.config['RECEPIE_PATH']}/{category}/")
