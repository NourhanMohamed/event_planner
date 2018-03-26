

def ErrorFailure():
    
    import os,zipfile
    
    file = zipfile.ZipFile("c:\\Users\\fayeks\\Desktop\\LL.zip", "r")
    #dir_name= 'C"\\Users||fayeks\\Desktop\\SISO'
    
    # creating a new Folder 
    newpath = r'C:\Users\fayeks\Desktop\XXX' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    # Extract the zipped file in the new folder 
        
    file.extractall(newpath) 
    
    # Change the Directory to the folder containing the extracted zipped file 
    
    os.chdir(newpath)
    
    
    # faliureError Function: Print out the error and failure in the log files taking no arguments 
    #==============================================================================
        
        
    # we loop in the folder until we get the directory of the desired log file 
    
    # Connecters-cluster log file 
    #============================================
    print ("====================================================================")
    print("Connecters-cluster log file ")
    print ("====================================================================")
    
    for root, dirs, files in os.walk(newpath):
            for name in files:
                if name.endswith("connectors-cluster.log"):
               
               # we got the directory of the log file needed
               
                   ConnectorsClustertargetPath=os.path.join(root, name)
               
               # we got the file and and uploaded it to a variable f 
             
        # read log file and output lines containing Errors and faliure 
        
    with open(ConnectorsClustertargetPath, "r") as f1:
            for line in f1:
              if "ERROR" in line and "DEBUG" not in line:
                  print line
             
                    
    print ("====================================================================")
    
    #============================================================================
    
    # Web.log
    #==============
    
    print("web log file ")
    
    print ("====================================================================")
    
    for root, dirs, files in os.walk(newpath):
        for name in files:
           if name.endswith("web.log"):
               ConnectorsClustertargetPath=os.path.join(root, name)
               
        with open(ConnectorsClustertargetPath, "r") as f2:
           for line in f2:
            if "ERROR" in line:
                print line 
            
                
    print ("====================================================================")
    
    #============================================================================   
                
     # marvin.log
    #==============
    
    print("marvin log file ")
     
    print ("====================================================================")
                
    for root, dirs, files in os.walk(newpath):
        for name in files:
           if name.endswith("marvin.log"):
               ConnectorsClustertargetPath=os.path.join(root, name)
               
        with open(ConnectorsClustertargetPath, "r") as f3:
           for line in f3:
            if "ERROR" in line:
                print line 
           
    
    print ("====================================================================")
    
    #============================================================================
    
     # loudmouth.log
    #==============
     
    print("loudmouth log file ")
    
    print ("====================================================================")
           
    for root, dirs, files in os.walk(newpath):
        for name in files:
           if name.endswith("loudmouth.log"):
               ConnectorsClustertargetPath=os.path.join(root, name)
               
        with open(ConnectorsClustertargetPath, "r") as f4:
           for line in f4:
            if "ERROR" in line:
                print line 
            
                
    print ("====================================================================")
    
    #============================================================================           
    # lcm.log
    #==============
     
    print("lcm log file ")
     
    print ("====================================================================")
                
    for root, dirs, files in os.walk(newpath):
        for name in files:
           if name.endswith("lcm.log"):
               ConnectorsClustertargetPath=os.path.join(root, name)
               
        with open(ConnectorsClustertargetPath, "r") as f5:
           for line in f5:
            if "ERROR" in line:
                print line 
             
                
    print ("====================================================================")
    
    #============================================================================
    
    # Dell PTA agent response log file:
    #==========================================
    print("DellPTAgentResponse log file ") 
    
    print ("====================================================================")
    
    for root, dirs, files in os.walk(newpath):
        for name in files:
           if name.endswith("DellPTAgentResponse.log"):
               ConnectorsClustertargetPath=os.path.join(root, name)
               
        with open(ConnectorsClustertargetPath, "r") as f6:
           for line in f6:
            if "Error" in line:
                print line 
            if "Failure" in line:
                print line   
    print ("====================================================================")
           

def timeStampHelperMethod():

    print('Please enter the date and time using the following syntax: Month in wording , year,Day,hrs,min')
    print('for example: Dec,07,2017,04,30')
    incommingInputFromUser=raw_input()
    data=incommingInputFromUser.split(',')
    #print(data)
    
    monthInWord=data[0]
    day=data[1]
    year=data[2]
    hrs=data[3]
    mins=data[4]
    
    #print(monthInWord)
    
    def month_string_to_number(string):
        m = {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr':4,
             'may':5,
             'jun':6,
             'jul':7,
             'aug':8,
             'sep':9,
             'oct':10,
             'nov':11,
             'dec':12
            }
        s = string.strip()[:3].lower()
    
        try:
            out = m[s]
            return out
        except:
            raise ValueError('Not a month')
            
    
    Integer=month_string_to_number(incommingInputFromUser)
    #print(type(Integer))
    monthInNumbers=str(Integer)
    #print(type(monthInNumbers))
    
    Syntax1TimeStamp= monthInWord+" "+ day +" "+ hrs + ":" + mins
    Syntax2TimeStamp= year +"-"+monthInNumbers+"-"+day+"T"+hrs+":"+mins
    
        #Connecters-cluster , web and LCM Will use Syntax1 TimeStamp
        #loudmouth and marvin logs will use Syntax 2 TimeStamp 
        # for example: 
        # Loudmouth log Timestamp: 2017-11-14T00:34:39.836Z
        #Marvin Log TimeStamp model: [MARVIN] 2017-07-25T20:51:00:421Z
        #Connecters-Cluster TimeStamp Model : Nov 14 03:40:00,168 GMT 2017
        #web log TimeStamp Model: Nov 14 10:04:28,876 GMT 2017
        #LCM Log TimeStamp Model:Apr 02 07:33:41,022 GMT 2017    


#timeStampHelperMethod()
    yield Syntax1TimeStamp
    yield Syntax2TimeStamp


def ErrorFailureTimeStamp():

    import os,zipfile
    #Connecters-cluster , web and LCM Will use Syntax1 TimeStamp
    #loudmouth and marvin logs will use Syntax 2 TimeStamp 
    #a=Syntax1TimeStamp
    #b=Syntax2TimeStamp

    a,b= timeStampHelperMethod()
    
  #  data1=a.split(" ")  
   # print(data1)
    #print(data1[0]) 
    #print(data1[1])
    #print(data1[2])
    #data2=b.split(",")
    
  #  print(data1)
  
   # Syntax1TimeStamp= monthInWord+" "+ day +" "+ hrs + ":" + mins
   # Syntax2TimeStamp= year +"-"+monthInNumbers+"-"+day+"T"+hrs+":"+mins

   # print(a)
   # print(b)
    
    file = zipfile.ZipFile("c:\\Users\\fayeks\\Desktop\\LL.zip", "r")
    #dir_name= 'C"\\Users||fayeks\\Desktop\\SISO'
    
    # creating a new Folder 
    newpath = r'C:\Users\fayeks\Desktop\XXX' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    # Extract the zipped file in the new folder 
        
    file.extractall(newpath) 
    
    # Change the Directory to the folder containing the extracted zipped file 
    
    os.chdir(newpath)
    
    
    # faliureError Function: Print out the error and failure in the log files taking no arguments 
    #==============================================================================
        
        
    # we loop in the folder until we get the directory of the desired log file 
    
    # Connecters-cluster log file 
    #============================================
    
    print ("====================================================================")
    print("Connecters-cluster log file ")
    print ("====================================================================")
    
    for root, dirs, files in os.walk(newpath):
            for name in files:
                if name.endswith("connectors-cluster.log"):
               
               # we got the directory of the log file needed
               
                   ConnectorsClustertargetPath=os.path.join(root, name)
               
               # we got the file and and uploaded it to a variable f 
             
        # read log file and output lines containing Errors and faliure 
        
    with open(ConnectorsClustertargetPath, "r") as f1:
            for line in f1:
                if a in line:
                    if a and "ERROR" in line:
                        print line
               
                    
    print ("====================================================================")
    
    #============================================================================
    
    # Web.log
    #==============
    
    print("web log file ")
    
    print ("====================================================================")
    
    for root, dirs, files in os.walk(newpath):
        for name in files:
           if name.endswith("web.log"):
               ConnectorsClustertargetPath=os.path.join(root, name)
               
        with open(ConnectorsClustertargetPath, "r") as f2:
           for line in f2:
            if b in line:
                if b and "ERROR" in line:
                    print line 
            
           
                
    print ("====================================================================")
    
    #============================================================================   
                
     # marvin.log
    #==============
    
    print("marvin log file ")
     
    print ("====================================================================")
                
    for root, dirs, files in os.walk(newpath):
        for name in files:
           if name.endswith("marvin.log"):
               ConnectorsClustertargetPath=os.path.join(root, name)
               
        with open(ConnectorsClustertargetPath, "r") as f3:
           for line in f3:
             if b in line: 
                 if b and "ERROR" in line:
                     print line 
            
    
    print ("====================================================================")
    
    #============================================================================
    
     # loudmouth.log
    #==============
     
    print("loudmouth log file ")
    
    print ("====================================================================")
           
    for root, dirs, files in os.walk(newpath):
        for name in files:
           if name.endswith("loudmouth.log"):
               ConnectorsClustertargetPath=os.path.join(root, name)
               
        with open(ConnectorsClustertargetPath, "r") as f4:
           for line in f4:
            if b in line:
                if b and "ERROR" in line:
                    print line 
            
                
    print ("====================================================================")
    
    #============================================================================           
    # lcm.log
    #==============
     
    print("lcm log file ")
     
    print ("====================================================================")
                
    for root, dirs, files in os.walk(newpath):
        for name in files:
           if name.endswith("lcm.log"):
               ConnectorsClustertargetPath=os.path.join(root, name)
               
        with open(ConnectorsClustertargetPath, "r") as f5:
           for line in f5:
            if a in line:
              if a and "ERROR" in line:
                        print line 
           
    print ("====================================================================")
    
    #============================================================================
    


def sysInfo():
    
    import os,zipfile
    
    file = zipfile.ZipFile("c:\\Users\\fayeks\\Desktop\\LL.zip", "r")
    #dir_name= 'C"\\Users||fayeks\\Desktop\\SISO'
    
    # creating a new Folder 
    newpath = r'C:\Users\fayeks\Desktop\XXX' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    # Extract the zipped file in the new folder 
        
    file.extractall(newpath) 
    
    # Change the Directory to the folder containing the extracted zipped file 
    
    os.chdir(newpath)
    
    
    # faliureError Function: Print out the error and failure in the log files taking no arguments 
    #==============================================================================
    #SYSINFO TEST
    print ("====================================================================")
    print("SYSINFO SYSINFO SYSINFO SYSINFO")
    print ("====================================================================")
    
   
    for root, dirs, files in os.walk(newpath):
            for name in files:
                if name.endswith("application.properties"):
               
               # we got the directory of the log file needed
               
                   ConnectorsClustertargetPath=os.path.join(root, name)
               
               # we got the file and and uploaded it to a variable f 
             
        
    with open(ConnectorsClustertargetPath, "r") as f1:
            for line in f1:
                if "# The build version of VxRail" in line:
                    print line
                if "applicationProperties.about.marvin.version=VxRail" in line:
                    print line 
                    
    #==============================================================================


              
        
def Main():
    
    one="1"
    two="2"
    print("Select one of the bellow") 
    print("[1] output all the errors in the log bundle ")
    print("[2] output the errors in the log bundle using a timestamp") 
    InputFromUser=raw_input()
    if InputFromUser == one: 
        sysInfo()
        ErrorFailure()
    
    if InputFromUser == two: 
        sysInfo()
        ErrorFailureTimeStamp()

Main()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        