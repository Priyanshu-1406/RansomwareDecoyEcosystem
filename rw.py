import os 
from cryptography.fernet import Fernet

dir=os.path.join("base_directory","decoy_folder")
decoy_files= [f for f in os.listdir(dir) if f.startswith("DecoyFile_") and f.endswith(".txt")]
key=Fernet.generate_key()
print(key)
with open("key.txt", "wb") as k:
   k.write(key)
for file_name in decoy_files:
    file_path=os.path.join(dir,file_name)
    with open(file_path, 'rb') as theFile:
      content=theFile.read()
      
    encrypted_data=Fernet(key).encrypt(content)
   
    with open(file_path,'wb') as theFile:
      theFile.write(encrypted_data)

print("Encryption done")

      


