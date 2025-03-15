import os 
import subprocess
from tkinter import *

def monitoring_file():
    subprocess.Popen(["python","decoy_manager.py"])
    print("Monitoring....")
def view_log():
    log_file='file_activity.log'
    if os.path.exists(log_file):
        os.system(f"notepad {log_file}")
    print("Opening log files...")
def view_backup():
    backup_folder='backup_directory'
    if os.path.exists(backup_folder):
        os.system(f"explorer {backup_folder}")

window=Tk()
root=window
root.geometry('780x439')
root.title('Ransomware Decoy Ecosystem')
window.config(background='#32e1ed')
label=Label(window,text="CSE212 Cyber Security Project",bg="#eda232")
label1=Label(window,text="Ransomware Decoy Ecosystem",bg="#eda232")
label.place(x=300,y=25)
label1.place(x=300,y=50)
button= Button(window,text="Monitor Files....")
button_logs=Button(window,text="View Logs")
button_backup=Button(window,text="View Backup Folder")
button_backup.config(command=view_backup)
button_backup.place(x=500,y=100)
button_logs.config(command=view_log)
button.config(pady=10, background='#2ba141')
button_logs.config(pady=10, background='#2ba141')
button_backup.config(pady=10, background='#2ba141')
button.place(x=100,y=100)
button_logs.place(x=300,y=100)
button_backup.place()
button.config(command=monitoring_file)
window.mainloop()


