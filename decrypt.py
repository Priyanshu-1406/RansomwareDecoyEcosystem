import os 
from cryptography.fernet import Fernet

dir=os.path.join("base_directory","decoy_folder")
decoy_files= [f for f in os.listdir(dir) if f.startswith("DecoyFile_") and f.endswith(".txt")]


with open("key.txt", "rb") as k:
   key=k.read()
   
cipher= Fernet(key)

for file_name in decoy_files:
    file_path=os.path.join(dir,file_name)
    with open(file_path, 'rb') as encrypdata:
      content=encrypdata.read()
      
    decrypted_data=cipher.decrypt(content)
   
    with open(file_path,'wb') as theFile:
      theFile.write(decrypted_data)

print("Decryption done")


