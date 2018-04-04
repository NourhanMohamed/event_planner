                        jenkib2@triage:/$ cat home/cavalf/extractor.py
#!/usr/bin/env python

# +-----------------------------------------------------+
# |                                                     |
# | Author: James O'Mahony                              |
# | E-mail: J.OMahony@Dell.com                          |
# |                                                     |
# | --------------------                                |
# | Prerequisite Scripts                                |
# | --------------------                                |
# |                                                     |
# | compatcheck.sh put in /usr/local/bin                |
# | HAconfig.sh put in /usr/local/bin                   |
# | Modified VCE_Start_here.sh put in /usr/local/bin    |
# | vxrmCheck.sh put in /usr/local/bin                  |
# | down.sh for EMC FTP download (requires lftp)        |
# |                                                     |
# | ----------------------                              |
# | Prerequisite Locations                              |
# | ----------------------                              |
# |                                                     |
# | /mnt/ftp-disk/ --> chown to user or group           |
# |                                                     |
# | ----------------------                              |
# | Prerequisite Tasks                                  |
# | ----------------------                              |
# |                                                     |
# | chown <user>:<group> /usr/local/bin/extractor.py    |
# |                                                     |
# +-----------------------------------------------------+

# -----------------------
# Import required modules
# -----------------------

import os
import subprocess
import zipfile
import tarfile
import shutil
import getpass
import gzip
import fnmatch
import platform

# ----------------
# Import date/time
# ----------------

from datetime import datetime

# ------
# Splash
# ------

print ""
print "+------------------------------------------------------------------------+"
print "|                                                                        |"
print "| What extractor.py does:                                                |"
print "|                                                                        |"
print "| - unpack the logs (.tgz,.tar,.zip)                                     |"
print "| - runs compatCheck.sh, VCE_start_here.sh, HAconfig.sh on vm-supports   |"
print "| - runs vxrmCheck.sh against vxrm bundle                                |"
print "| - Allows the user to pass EMC FTP link to download files to bug       |"
print "|                                                                        |"
print "+------------------------------------------------------------------------+"
print ""


# Change the directory to SR parent folder
os.chdir("/mnt/ftp-disk/")
startPwd = os.getcwd()

# Running as user
user = getpass.getuser()

print ""
print "Python Version: " + str(platform.python_version())
print "Running as user: " + user
print ""

# Take SR as string
caseNumber = raw_input ('Enter Bug number: ')
caseNumber = caseNumber.strip() # trim whitespaces

# Build folder in path /mnt/ftp-disk/ if it does not exist
if not os.path.exists(startPwd + "/" + caseNumber):
        os.makedirs(startPwd + "/" + caseNumber)
        os.chdir(startPwd + "/" + caseNumber)
else:
        os.chdir(startPwd + "/" + caseNumber)

# Print case directory
pwd = os.getcwd() # pwd defined as /mnt/ftp-disk/*/ throughout this script

print "Moving to the Bug directory :->> %s" % pwd

# Deliver some basic options
# --------------------------

print ""
print "--Options--"
print ""
print "1). Grab from EMC FTP"
print "2). Extract current logs in " + pwd
print ""

ftpSelect = raw_input('Enter Selection(1-2): ')
ftpSelect = ftpSelect.strip() # trim whitespace from ftpSelect

if ftpSelect == "1":
        emcURL = raw_input('Paste Link here: ')
        emcURL = emcURL.strip() # trim whitespace from URL
        cmd_listEMC = ['down.sh', '-emcdown', str(emcURL)] # form the command to pass to subprocess
        proc = subprocess.Popen(cmd_listEMC, shell=False) # pass command to subprocess
        print proc.communicate() # print shell output
        if os.listdir(pwd)==[]:
                print ""
                print "==============================="
                print "No files found in SR# directory"
                print "==============================="
                print ""
                raise SystemExit # stop application as nothing to do
        else:
                print ""
                print "=========================="
                print "Files found, continuing..."
                print "=========================="
                print ""
elif ftpSelect == "2":
        print ""
        print "Skipping ftp download"
        if os.listdir(pwd)==[]:
                print ""
                print "==============================="
                print "No files found in SR# directory"
                print "==============================="
                print ""
                raise SystemExit # stop application as nothing to do
        else:
                print ""
                print "=========================="
                print "Files found, continuing..."
                print "=========================="
                print ""
else:
        print ""
        print "=========================="
        print "Invalid Selection, exiting"
        print "=========================="
        print ""
        raise SystemExit # stop application as nothing to do

dir_name = pwd # new variable for current directory

# Setup file extensions for extraction
extensionZip = ".zip"
extensionTgz = ".tgz"
extensionTar = ".tar"

os.chdir(dir_name) # change directory from working dir to dir with files

# ----------------------------------------------------------------------
# End file download section

# Set permissions
#for root, dirs, files in os.walk(pwd):
#        for d in dirs:
#                os.chmod(os.path.join(root, d), 0770)
#        for f in files:
#                os.chmod(os.path.join(root, f), 0770)

# Setup folders with processed date
today = datetime.now()

vxrailPattern = 'VxRail_Support_Bundle'
tempPattern = 'Temp'

vxrailFolder = str(pwd + "/" + vxrailPattern)
tempFolder = str(pwd + "/" + tempPattern)

# Folder to contain duplicate files and other misc failures
try: # catch directory creation failure
       if not os.path.exists(tempFolder):
                os.makedirs(tempFolder)
except: # on error
        print "Failed to create temp directory"
        pass # continue

# Find the .zip's and extract
for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(extensionZip): # check for ".zip" extension
                file_name = os.path.abspath(item) # get full path of files
                print ""
                print "Extracting *.zip"
                print file_name
                try: # prevent corrupt .zip stopping script
                        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                        zip_ref.extractall(dir_name) # extract file to dir
                        zip_ref.close() # close file
                        os.remove(file_name) # delete zipped file
                except: # on error
                        print "Error extracting " + file_name
                        pass # continue

# Find the .tar's and extract
for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(extensionTar): # check for ".tar" extension
                file_name = os.path.abspath(item) # get full path of files
                print ""
                print "Processing *.tar"
                print file_name
                try: # prevent corrupt .tar stopping script
                        tar_ref = tarfile.open(file_name) # create tarfile object
                        tar_ref.extractall(dir_name) # extract file to dir
                        tar_ref.close() # close file
                        os.remove(file_name) # delete tarred file
                except: # on error
                        print "Error extracting " + file_name
                        pass # continue
                os.chdir(pwd) # change to previous directory

# setup directory name patterns for later
vcPattern = "VMware-vCenter-support"
esxiPattern = "esx"
vmsupportPattern = "vm-support"
vxrmPattern = "mystic_manager"

# begin VMware processing
# ----------------------------------------------------------------------

for item in os.listdir(dir_name):
        if item.startswith(vcPattern): # If the ESXi files are in the VC folder
                file_name = os.path.abspath(item)
                print ""
                print "Change to VC directory: "
                print file_name
                os.chdir(file_name)
                pwdvc = os.getcwd()
                for item in os.listdir(pwdvc):
                        if item.endswith(extensionTgz): # check for ".tgz" extension
                                file_name = os.path.abspath(item) # get full path of files
                                print ""
                                print "Processing *.tgz"
                                print file_name
                                try: # prevent corrupt .tgz issues stopping script
                                        tgz_ref = tarfile.open(file_name) # create tarfile object
                                        tgz_ref.extractall(pwd) # extract file to dir
                                        tgz_ref.close() # close file
                                        os.remove(file_name) # delete tarred file
                                except: # on error
                                        print "Error extracting " + file_name
                                        pass # continue
                                print ".tgz processing completed"
                                os.chdir(pwdvc)
                os.chdir(pwd)
        else: # If the ESXi files are not in the VC folder
                for item in os.listdir(pwd):
                        if item.endswith(extensionTgz): # check for ".tgz" extension
                                file_name = os.path.abspath(item) # get full path of files
                                print ""
                                print "Processing *.tgz"
                                print file_name
                                try: # prevent corrupt .tgz issues stopping script
                                        tgz_ref = tarfile.open(file_name) # create tarfile object
                                        tgz_ref.extractall(pwd) # extract file to dir
                                        tgz_ref.close() # close file
                                        os.remove(file_name) # delete tarred file
                                except: # on error
                                        print "Error extracting " + file_name
                                        pass # continue
                                print ".tgz processing completed"
                                os.chdir(pwd)

for item in os.listdir(pwd):
        if item.startswith(esxiPattern):
                esxi_name = os.path.join(pwd,item) # append folder name to current directory
                print ""
                print "Moving to vm-support: "
                os.chdir(esxi_name) # move to the vm-support directory
                vmpwd = os.getcwd()
                print vmpwd
                cmd_compatCheck = ['compatCheck.sh']
                proc = subprocess.Popen(cmd_compatCheck, shell=False) # call compatCheck to do some analysis
                print proc.communicate() # print shell output
                cmd_startHere = ['VCE_Start_here.sh']
                proc = subprocess.Popen(cmd_startHere, shell=False) # call Start_here script to do some analysis
                print proc.communicate() # print really noisy shell output from VCE_Start_here.sh (if you suppress, script runs outside python control)
                try: # try to run HAconfig.sh here
                        print ""
                        print "Starting HAconfig.sh"
                        print ""
                        cmd_HAconfig = ['HAconfig.sh']
                        proc = subprocess.Popen(cmd_HAconfig, shell=False) # call HAconfig to check HA
                        print proc.communicate() # print shell output
                        print ""
                        print "HAconfig.sh completed successfully"
                        print ""
                except: # catch error and continue
                        print ""
                        print "HAconfig.sh error detected"
                        print ""
                        pass # continue
                os.chdir(pwd) # change to previous directory
        elif item.startswith(vmsupportPattern):
                vmsupport_name = os.path.join(pwd,item) # append folder name to current directory
                print ""
                print "Moving to vm-support: "
                os.chdir(vmsupport_name) # move to the vm-support directory
                vmpwd = os.getcwd()
                print vmpwd
                cmd_compatCheck = ['compatCheck.sh']
                proc = subprocess.Popen(cmd_compatCheck, shell=False) # call compatCheck to do some analysis
                print proc.communicate() # print shell output
                cmd_startHere = ['VCE_Start_here.sh']
                proc = subprocess.Popen(cmd_startHere, shell=False) # call Start_here script to do some analysis
                print proc.communicate() # print really noisy shell output from VCE_Start_here.sh (if you suppress, script runs outside python control)
                try: # try to run HAconfig.sh here
                        print ""
                        print "Starting HAconfig.sh"
                        print ""
                       cmd_HAconfig = ['HAconfig.sh']
                        proc = subprocess.Popen(cmd_HAconfig, shell=False) # call HAconfig to check HA
                        print proc.communicate() # print shell output
                        print ""
                        print "HAconfig.sh completed successfully"
                        print ""
                except: # catch error and continue
                        print ""
                        print "HAconfig.sh error detected"
                        print ""
                        pass # continue
                os.chdir(pwd) # change to previous directory

# ----------------------------------------------------------------------
# end VMware processing

# begin VxRAIL Manager processing
# ----------------------------------------------------------------------

for item in os.listdir(pwd):
        if item.startswith(vxrmPattern):
                vxrm_name = os.path.join(pwd,item) # append folder name to current directory
                print ""
                print "Moving to mystic-manager: "
                os.chdir(vxrm_name) # move to the vxrm directory
                vmpwd = os.getcwd()
                print vmpwd
                cmd_vxrmCheck = ['vxrmCheck.sh']
                proc = subprocess.Popen(cmd_vxrmCheck, shell=False) # call compatCheck to do some analysis
                print proc.communicate() # print shell output
                os.chdir(pwd) # change to previous directory

# ----------------------------------------------------------------------
# end VxRAIL Manager processing

print "Processing complete"
os.chdir(pwd) # change back to original directory

#print "Changing Permissions"
#os.chmod(pwd, 0770)
#for root, dirs, files in os.walk(pwd):
#       for d in dirs:
#               os.chmod(os.path.join(root, d), 0770)
#       for f in files:
#               os.chmod(os.path.join(root, f), 0770)
print ""
print "Files are here: " + pwd
print ""

Billy Jenkins
Software Engineer
Dell EMC | VXrail
Billy.Jenkins@Dell.com

