import os
import shutil
source = "C:\\Users\\miche\\Downloads"
destination = "C:\\Users\\miche\\Downloads\\Project 102"
fileList = os.listdir(source)

for fileName in fileList:
    name, extension = os.path.splitext(fileName)
    if extension=="":
        continue
    if extension in [".txt",".doc",".docx",".pdf"]:
        path1 = source + "/"+ fileName
        path2 = destination + "/"+ "image_files"
        path3 = destination + "/"+ "image_files"+ "/"+ fileName

        if os.path.exists(path2):
            print("Moving" + fileName + ".....")

            shutil.move(path1, path3)

        else: 
          os.makedirs(path2)
          print("Moving" + fileName + ".....")
          shutil.move(path1, path3)
