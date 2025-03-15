import os 
num_folders=1
num_files=5
extension='txt' 
base_directory='base_directory'
for folder in range(1,num_folders+1):
    folder_name=f'decoy_folder'
    folder_path=os.path.join(base_directory,folder_name)
    os.makedirs(folder_path)
    for file in range(1,num_files+1):
        file_name=f'DecoyFile_{file}.txt'
        file_path=os.path.join(folder_path,file_name)
        with open(file_path, 'w') as f:
            f.write(f"This is decoy file {file}, do not modify it")







