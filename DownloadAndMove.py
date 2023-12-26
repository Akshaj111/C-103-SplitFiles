import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/akshajaryash/Desktop/Akshaj-eQE Work of Y7"
to_dir = "C:/Users/akshajaryash/Desktop/Akshaj-eQE Work of Y7/Split Files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov', '.mp3'],
    "Document_Files": ['.ppt', '.xls','.xlsx', '.csv', '.pdf', '.txt', '.doc', '.docx', '.rtf', '.pptx', '.odp', '.odt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'],
    "CAD Files": ['.sldprt', '.stl']
}

# Event Handler Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,extension = os.path.splitext(event.src_path)
        for key,value in dir_tree.items():
            time.sleep(1)
            print("downloaded")
            if extension in value:
                file_name = os.path.basename(event.src_path)
                
                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + file_name

                if os.path.exists(path2):
                    print("Directory exists")
                    print("Moving"+ file_name + "...")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("Making directory")
                    os.makedirs(path2)
                    print("Moving"+ file_name + "...")
                    shutil.move(path1,path3)
                    time.sleep(1)

        print(event)
        print(event.src_path)


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
    observer.stop()