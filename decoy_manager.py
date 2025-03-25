import os 
import hashlib
import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil 
import time
from datetime import date
from shutil import copyfile
import logging
from plyer import notification 
import smtplib 
from email.message import EmailMessage
import subprocess

backup_dir='backup_directory'
folder_name=f"Backup_Folder"
folder_path=os.path.join(backup_dir,folder_name)
os.makedirs(folder_path,exist_ok=True)

date_backup=date.today()
print(date_backup)
str_date_backup=str(date_backup).replace('-','.')
print(str_date_backup)
path_input=r'base_directory\decoy_folder'
path_output=os.path.join(backup_dir,str_date_backup)
print(path_output)
if os.path.exists(path_input):
    if os.path.exists(path_output):
        shutil.rmtree(path_output)
    shutil.copytree(path_input,path_output)

dir=os.path.join("base_directory","decoy_folder")
decoy_files= [f for f in os.listdir(dir) if f.startswith("DecoyFile_") and f.endswith(".txt")]
file_hashes={}
for file_name in decoy_files:
    file_path=os.path.join(dir,file_name)
    hasher=hashlib.sha256()
    with open(file_path,'rb') as f:
        hasher.update(f.read())
    file_hashes[file_path]= hasher.hexdigest()
    print(f"File path is {file_path}")
    print(f"SHA256 Hash: {hasher.hexdigest()}")

print("Running....")     
class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.email_sent={}
    def on_modified(self, event):
        if not event.is_directory:
            logging.basicConfig(
             filename="file_activity.log",
             level=logging.INFO,
             format="%(asctime)s - %(message)s",
             datefmt="%Y-%m-%d %H:%M:%S"
             )
            logging.info(f"Modified:{event.src_path}")
            
            notification.notify(title='Suspicious Modification Detected!!',
                                message="Alert: A file has been modified!! Please verify if this change was intentional",app_icon='5173006_alarm_alert_internet_light_security_icon.ico')
            time.sleep(0.2) 
            print(f"Modified : {event.src_path}")
            hasher=hashlib.sha256()
            with open(event.src_path, 'rb') as f:
                hasher.update(f.read())
            new_hash=hasher.hexdigest()
            if event.src_path in file_hashes:
                if file_hashes[event.src_path]!=new_hash:
                    print(f"New SHA hash:{new_hash}")
                    file_hashes[event.src_path]=new_hash

                    if not self.email_sent.get(event.src_path,False):
                        msg=EmailMessage()
                        msg['Subject']="Alert!!"
                        msg['From']="Ransomware Detection System"
                        msg['To']="*********@gmail.com"
                        msg.set_content("A file modification has been detected in your system! Please verify if this change was intentional.")
                        MyServer=smtplib.SMTP('smtp.gmail.com',587)
                        MyServer.starttls()
                        MyServer.login("******@gmail.com","*********")
                        MyServer.send_message(msg)
                        MyServer.quit()
                        self.email_sent[event.src_path]=True
                    en=subprocess.run(['netsh','interface','set','interface','wi-fi','DISABLED'])
observer=Observer()
event_handler=MyHandler()
observer.schedule(event_handler, path=dir, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

log_file_path = "file_activity.log"
txt_file_path = "log.txt"

last_position = 0
stop_time = time.time() + 6  

while time.time() < stop_time:
    with open(log_file_path, "r") as log_file:
        log_file.seek(last_position)
        new_lines = log_file.readlines()
        last_position = log_file.tell()
    
    if new_lines:
        with open(txt_file_path, "a") as txt_file:
            txt_file.writelines(new_lines)

    time.sleep(1)

print("Script stopped automatically after 6 seconds.")




