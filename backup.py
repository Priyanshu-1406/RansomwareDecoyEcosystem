import shutil
from datetime import date
from time import time 
import os 
from shutil import copyfile
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
    

