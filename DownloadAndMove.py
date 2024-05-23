#Even if a piece of code is techniqley correct, it might still display an error. Exceptions basiclly act as a fall back plan if somthing doesnt work.There are built in exception events
#A try is what you want to happen and if it doesnt work, it falls onto a except clause.
#Watchdog reports any changes to us by raising a specific event that we can deal with
#Watchdog.observers.Observer is the class that will acually look for any changes


import sys #system
import time
import random

import os # operating syste,
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "image_files"
to_dir = "moved"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)
        print(event.src_path)
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name=os.path.basename(event.src_path)
                print("downloaded"+ file_name)
                path1=from_dir+"/"+file_name
                path2=to_dir+"/"+key
                path3=to_dir+"/"+key+"/"+file_name

                if os.path.exists(path2):
                    shutil.move(path1,path3)
                    time.sleep(1)

                else:
                    os.makedirs(path2)
                    shutil.move(path1,path3)
                    time.sleep(1)



# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:

    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop(1) 
    