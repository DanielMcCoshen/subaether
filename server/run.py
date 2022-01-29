from server import app
import os


if not os.path.exists(app.config["RECEPIE_PATH"]):
    print("Storage Directory does not exist, creating it")
    os.makedirs(app.config["RECEPIE_PATH"])

if not os.path.exists(f"{app.config['RECEPIE_PATH']}/all_recepies/"):
    print("Createing recepie directory")
    os.makedirs(f"{app.config['RECEPIE_PATH']}/all_recepies/")

for category in app.config["CATEGORIES"]:
    if not os.path.exists(f"{app.config['RECEPIE_PATH']}/{category}/"):
        print(f"Createing Directory for {category}")
        os.makedirs(f"{app.config['RECEPIE_PATH']}/{category}/")
