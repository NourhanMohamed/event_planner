# -*- coding: utf-8 -*-

import os,zipfile
import webbrowser

bundle_path = raw_input("Enter bundle path: ")
file = zipfile.ZipFile(bundle_path)

# creating a new Folder 
newpath = bundle_path + '.extracted'
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Extract the zipped file in the new folder 
file.extractall(newpath) 

# Change the Directory to the folder containing the extracted zipped file 
os.chdir(newpath)

# we loop in the folder until we get the directory of the desired log file 
for root, dirs, files in os.walk(newpath):
   for name in files:
       if name.endswith("connectors-cluster.log"):
           
           # we got the directory of the log file needed
           
           targetPath=os.path.join(root, name)
           
           # we got the file and and uploaded it to a variable f 
           
           f  = open(targetPath, "r")
        #   print (f.read())
         #  print(os.path.join(root, name))
         
    # read log file and output lines containing Errors and faliure 
    
with open(targetPath, "r") as f:
       for line in f:
        if "Error" in line:
            print line


webbrowser.open('https://bugzilla.vp.lab.emc.com')
