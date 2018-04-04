
import os,zipfile
    
file = zipfile.ZipFile("c:\\Users\\fayeks\\Desktop\\MekksoLogs.zip", "r")
    #dir_name= 'C"\\Users||fayeks\\Desktop\\SISO'
    
    # creating a new Folder 
newpath = r'C:\Users\fayeks\Desktop\XXX' 
if not os.path.exists(newpath):
   os.makedirs(newpath)
    
    # Extract the zipped file in the new folder 
        
file.extractall(newpath) 
    
    # Change the Directory to the folder containing the extracted zipped file 
os.chdir(newpath)



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
            
def month_name (number):
        if number == 1:
            return "Jan"
        elif number == 2:
            return "Feb"
        elif number == 3:
            return "Mar"
        elif number == 4:
            return "Apr"
        elif number == 5:
            return "May"
        elif number == 6:
            return "Jun"
        elif number == 7:
            return "Jul"
        elif number == 8:
            return "Aug"
        elif number == 9:
            return "Sep"
        elif number == 10:
            return "Oct"
        elif number == 11:
            return "Nov"
        elif number == 12:
            return "Dec"
            

def ErrorFailure():
    
  
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
    
    
    Integer=month_string_to_number(incommingInputFromUser)
    #print(type(Integer))
    monthInNumbers=str(Integer)
    #print(type(monthInNumbers))
    
    if monthInNumbers == "0":
        monthInNumbers="00"
    if monthInNumbers == "1":
        monthInNumbers="01"
    if monthInNumbers == "2":
        monthInNumbers="02"
    if monthInNumbers == "3":
        monthInNumbers="03"
    if monthInNumbers == "4":
        monthInNumbers="04"
    if monthInNumbers == "5":
        monthInNumbers="05"
    if monthInNumbers == "6":
        monthInNumbers="06"
    if monthInNumbers == "7":
        monthInNumbers="07"
    if monthInNumbers == "8":
        monthInNumbers="08"
    if monthInNumbers == "9":
        monthInNumbers="09"
    
    Syntax1TimeStamp= monthInWord+" "+ day +" "+ hrs + ":" + mins
    Syntax2TimeStamp= year +"-"+monthInNumbers+"-"+day+"T"+hrs+":"+mins
    
    print(Syntax2TimeStamp)
    print(Syntax1TimeStamp)
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
    
def timeStampRangeHelperMethod(): 
    
    import datetime as dt
    
    def timerange (start, end, step):
        while start < end:
            yield start
            start += step
    
    print('Please enter the date and time using the following syntax: Month in wording , year,Day,hrs,min')
    print('for example: Dec,07,2017,04,30')
    print('Please enter the lower limit of the Time Range:')
    incommingInputFromUser1=raw_input()
    print('Please enter the upper limit of the Time Range:')
    incommingInputFromUser2=raw_input()
    data1=incommingInputFromUser1.split(',')
    data2=incommingInputFromUser2.split(',')
    
  #  print(data1)
   # print(data2)
    
    monthInWord1=data1[0]
    day1=data1[1]
    year1=data1[2]
    hrs1=data1[3]
    mins1=data1[4]
    
    monthInWord2=data2[0]
    day2=data2[1]
    year2=data2[2]
    hrs2=data2[3]
    mins2=data2[4] 
    
    
    dayInteger1=int(day1)
    dayInteger2=int(day2)
    
    yearInteger1=int(year1)
    yearInteger2=int(year2)
    
    hrsInteger1=int(hrs1) 
    hrsInteger2=int(hrs2)
    
    
    #print(monthInWord)
    
   # Syntax1TimeStamp= monthInWord+" "+ day +" "+ hrs + ":" + mins
   # Syntax2TimeStamp= year +"-"+monthInNumbers+"-"+day+"T"+hrs+":"+mins
   
    
    monthInteger1=month_string_to_number(incommingInputFromUser1)
    monthInteger2=month_string_to_number(incommingInputFromUser2)
    
        
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
    for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
        #print (x)
        z=str(x)
        y=z.split("-")
        #print(y)
        yearInRange=y[0]
        monthInRange=y[1]
        monthInRangeInteger=int(monthInRange)
        a=y[2]
        #print(a)
        b=a.split(" ")
        dayInRange=b[0]
        #print(dayInRange)
        c=b[1]
        #print(c)
        d=c.split(":")
        hrsInRange=d[0]
        minInRange=d[1]
        monthInWordRange= month_name(monthInRangeInteger)
        Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
        Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange
        
        with open(ConnectorsClustertargetPath, "r") as f1:
            for line in f1:
                if Syntax2TimeStamp in line:
                    if Syntax2TimeStamp and "ERROR" in line:
                        print line
                if Syntax1TimeStamp in line:
                    if Syntax1TimeStamp and "ERROR" in line:
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
        
    for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
        #print (x)
        z=str(x)
        y=z.split("-")
        #print(y)
        yearInRange=y[0]
        monthInRange=y[1]
        monthInRangeInteger=int(monthInRange)
        a=y[2]
        #print(a)
        b=a.split(" ")
        dayInRange=b[0]
        #print(dayInRange)
        c=b[1]
        #print(c)
        d=c.split(":")
        hrsInRange=d[0]
        minInRange=d[1]
        monthInWordRange= month_name(monthInRangeInteger)
        Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
        Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange
        
        with open(ConnectorsClustertargetPath, "r") as f2:
                for line in f2:
                    if Syntax2TimeStamp in line:
                        if Syntax2TimeStamp and "ERROR" in line:
                            print line 
                    if Syntax1TimeStamp in line:
                        if Syntax1TimeStamp and "ERROR" in line:
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
    

    for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
        #print (x)
        z=str(x)
        y=z.split("-")
        #print(y)
        yearInRange=y[0]
        monthInRange=y[1]
        monthInRangeInteger=int(monthInRange)
        a=y[2]
        #print(a)
        b=a.split(" ")
        dayInRange=b[0]
        #print(dayInRange)
        c=b[1]
        #print(c)
        d=c.split(":")
        hrsInRange=d[0]
        minInRange=d[1]
        monthInWordRange= month_name(monthInRangeInteger)
        Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
        Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange           
        
        with open(ConnectorsClustertargetPath, "r") as f3:
           for line in f3:
             if Syntax2TimeStamp in line: 
                 if Syntax2TimeStamp and "ERROR" in line:
                     print line 
             if Syntax1TimeStamp in line: 
                 if Syntax1TimeStamp and "ERROR" in line:
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
    
    for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
        #print (x)
        z=str(x)
        y=z.split("-")
        #print(y)
        yearInRange=y[0]
        monthInRange=y[1]
        monthInRangeInteger=int(monthInRange)
        a=y[2]
        #print(a)
        b=a.split(" ")
        dayInRange=b[0]
        #print(dayInRange)
        c=b[1]
        #print(c)
        d=c.split(":")
        hrsInRange=d[0]
        minInRange=d[1]
        monthInWordRange= month_name(monthInRangeInteger)
        Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
        Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange
           
        with open(ConnectorsClustertargetPath, "r") as f4:
           for line in f4:
            if Syntax2TimeStamp in line:
                if Syntax2TimeStamp and "ERROR" in line:
                    print line 
            if Syntax1TimeStamp in line:
                if Syntax1TimeStamp and "ERROR" in line:
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
       
    for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
        #print (x)
        z=str(x)
        y=z.split("-")
        #print(y)
        yearInRange=y[0]
        monthInRange=y[1]
        monthInRangeInteger=int(monthInRange)
        a=y[2]
        #print(a)
        b=a.split(" ")
        dayInRange=b[0]
        #print(dayInRange)
        c=b[1]
        #print(c)
        d=c.split(":")
        hrsInRange=d[0]
        minInRange=d[1]
        monthInWordRange= month_name(monthInRangeInteger)
        Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
        Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange            
       
        with open(ConnectorsClustertargetPath, "r") as f5:
           for line in f5:
            if Syntax1TimeStamp in line:
              if Syntax1TimeStamp and "ERROR" in line:
                        print line 
            if Syntax2TimeStamp in line:
                if Syntax2TimeStamp and "ERROR" in line:
                    print line
           
    print ("====================================================================")
    
def topicTimeRange():
    
    import datetime as dt
    
    def timerange (start, end, step):
        while start < end:
            yield start
            start += step
            
    incomingNumberfromUser=raw_input()
    print('Please enter the date and time using the following syntax: Month in wording , year,Day,hrs,min')
    print('for example: Dec,07,2017,04,30')
    print('Please enter the lower limit of the Time Range:')
    incommingInputFromUser1=raw_input()
    print('Please enter the upper limit of the Time Range:')
    incommingInputFromUser2=raw_input()
    data1=incommingInputFromUser1.split(',')
    data2=incommingInputFromUser2.split(',')
    
  #  print(data1)
   # print(data2)
    
    monthInWord1=data1[0]
    day1=data1[1]
    year1=data1[2]
    hrs1=data1[3]
    mins1=data1[4]
    
    monthInWord2=data2[0]
    day2=data2[1]
    year2=data2[2]
    hrs2=data2[3]
    mins2=data2[4] 
    
    
    dayInteger1=int(day1)
    dayInteger2=int(day2)
    
    yearInteger1=int(year1)
    yearInteger2=int(year2)
    
    hrsInteger1=int(hrs1) 
    hrsInteger2=int(hrs2)
    
    
    #print(monthInWord)
    
   # Syntax1TimeStamp= monthInWord+" "+ day +" "+ hrs + ":" + mins
   # Syntax2TimeStamp= year +"-"+monthInNumbers+"-"+day+"T"+hrs+":"+mins
   
    
    monthInteger1=month_string_to_number(incommingInputFromUser1)
    monthInteger2=month_string_to_number(incommingInputFromUser2)
    
    
    
    if incomingNumberfromUser == "4-1":
        print("marvin log file ")
         
        print ("====================================================================")
                    
        for root, dirs, files in os.walk(newpath):
            for name in files:
               if name.endswith("marvin.log"):
                   ConnectorsClustertargetPath=os.path.join(root, name)
        
    
        for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
            #print (x)
            z=str(x)
            y=z.split("-")
            #print(y)
            yearInRange=y[0]
            monthInRange=y[1]
            monthInRangeInteger=int(monthInRange)
            a=y[2]
            #print(a)
            b=a.split(" ")
            dayInRange=b[0]
            #print(dayInRange)
            c=b[1]
            #print(c)
            d=c.split(":")
            hrsInRange=d[0]
            minInRange=d[1]
            monthInWordRange= month_name(monthInRangeInteger)
            Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
            Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange           
            
            with open(ConnectorsClustertargetPath, "r") as f3:
               for line in f3:
                 if Syntax2TimeStamp in line: 
                     if Syntax2TimeStamp and "ERROR" in line:
                         print line 
                 if Syntax1TimeStamp in line: 
                     if Syntax1TimeStamp and "ERROR" in line:
                         print line 
                
        print ("====================================================================")
        
    if incomingNumberfromUser == "4-2":
        
        print("marvin log file ")
         
        print ("====================================================================")
                    
        for root, dirs, files in os.walk(newpath):
            for name in files:
               if name.endswith("marvin.log"):
                   ConnectorsClustertargetPath=os.path.join(root, name)
        
    
        for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
            #print (x)
            z=str(x)
            y=z.split("-")
            #print(y)
            yearInRange=y[0]
            monthInRange=y[1]
            monthInRangeInteger=int(monthInRange)
            a=y[2]
            #print(a)
            b=a.split(" ")
            dayInRange=b[0]
            #print(dayInRange)
            c=b[1]
            #print(c)
            d=c.split(":")
            hrsInRange=d[0]
            minInRange=d[1]
            monthInWordRange= month_name(monthInRangeInteger)
            Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
            Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange           
            
            with open(ConnectorsClustertargetPath, "r") as f3:
               for line in f3:
                 if Syntax2TimeStamp in line: 
                     if Syntax2TimeStamp and "ERROR" in line:
                         print line 
                 if Syntax1TimeStamp in line: 
                     if Syntax1TimeStamp and "ERROR" in line:
                         print line 
                
        print ("====================================================================")
        
        print("web log file ")
        
        print ("====================================================================")
        
        for root, dirs, files in os.walk(newpath):
            for name in files:
               if name.endswith("web.log"):
                   ConnectorsClustertargetPath=os.path.join(root, name)
            
        for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
            #print (x)
            z=str(x)
            y=z.split("-")
            #print(y)
            yearInRange=y[0]
            monthInRange=y[1]
            monthInRangeInteger=int(monthInRange)
            a=y[2]
            #print(a)
            b=a.split(" ")
            dayInRange=b[0]
            #print(dayInRange)
            c=b[1]
            #print(c)
            d=c.split(":")
            hrsInRange=d[0]
            minInRange=d[1]
            monthInWordRange= month_name(monthInRangeInteger)
            Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
            Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange
            
            with open(ConnectorsClustertargetPath, "r") as f2:
                    for line in f2:
                        if Syntax2TimeStamp in line:
                            if Syntax2TimeStamp and "ERROR" in line:
                                print line 
                        if Syntax1TimeStamp in line:
                            if Syntax1TimeStamp and "ERROR" in line:
                                print line
                        
                    
        print ("====================================================================")
            
    if incomingNumberfromUser == "4-3":
        
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
        for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
            #print (x)
            z=str(x)
            y=z.split("-")
            #print(y)
            yearInRange=y[0]
            monthInRange=y[1]
            monthInRangeInteger=int(monthInRange)
            a=y[2]
            #print(a)
            b=a.split(" ")
            dayInRange=b[0]
            #print(dayInRange)
            c=b[1]
            #print(c)
            d=c.split(":")
            hrsInRange=d[0]
            minInRange=d[1]
            monthInWordRange= month_name(monthInRangeInteger)
            Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
            Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange
            
            with open(ConnectorsClustertargetPath, "r") as f1:
                for line in f1:
                    if Syntax2TimeStamp in line:
                        if Syntax2TimeStamp and "ERROR" in line:
                            print line
                    if Syntax1TimeStamp in line:
                        if Syntax1TimeStamp and "ERROR" in line:
                            print line  
                        
        print ("====================================================================")
        
    if incomingNumberfromUser == "4-4":
        
        print("marvin log file ")
         
        print ("====================================================================")
                    
        for root, dirs, files in os.walk(newpath):
            for name in files:
               if name.endswith("marvin.log"):
                   ConnectorsClustertargetPath=os.path.join(root, name)
        
    
        for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
            #print (x)
            z=str(x)
            y=z.split("-")
            #print(y)
            yearInRange=y[0]
            monthInRange=y[1]
            monthInRangeInteger=int(monthInRange)
            a=y[2]
            #print(a)
            b=a.split(" ")
            dayInRange=b[0]
            #print(dayInRange)
            c=b[1]
            #print(c)
            d=c.split(":")
            hrsInRange=d[0]
            minInRange=d[1]
            monthInWordRange= month_name(monthInRangeInteger)
            Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
            Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange           
            
            with open(ConnectorsClustertargetPath, "r") as f3:
               for line in f3:
                 if Syntax2TimeStamp in line: 
                     if Syntax2TimeStamp and "ERROR" in line:
                         print line 
                 if Syntax1TimeStamp in line: 
                     if Syntax1TimeStamp and "ERROR" in line:
                         print line 
                
        print ("====================================================================")
        
    if incomingNumberfromUser == "4-5":
        
        print ("====================================================================")
        
        print("web log file ")
        
        print ("====================================================================")
        
        for root, dirs, files in os.walk(newpath):
            for name in files:
               if name.endswith("web.log"):
                   ConnectorsClustertargetPath=os.path.join(root, name)
            
        for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
            #print (x)
            z=str(x)
            y=z.split("-")
            #print(y)
            yearInRange=y[0]
            monthInRange=y[1]
            monthInRangeInteger=int(monthInRange)
            a=y[2]
            #print(a)
            b=a.split(" ")
            dayInRange=b[0]
            #print(dayInRange)
            c=b[1]
            #print(c)
            d=c.split(":")
            hrsInRange=d[0]
            minInRange=d[1]
            monthInWordRange= month_name(monthInRangeInteger)
            Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
            Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange
            
            with open(ConnectorsClustertargetPath, "r") as f2:
                    for line in f2:
                        if Syntax2TimeStamp in line:
                            if Syntax2TimeStamp and "ERROR" in line:
                                print line 
                        if Syntax1TimeStamp in line:
                            if Syntax1TimeStamp and "ERROR" in line:
                                print line
                        
                    
        print ("====================================================================")
        
    if incomingNumberfromUser == "4-6":
        
        print("lcm log file ")
         
        print ("====================================================================")
                    
        for root, dirs, files in os.walk(newpath):
            for name in files:
               if name.endswith("lcm.log"):
                   ConnectorsClustertargetPath=os.path.join(root, name)
           
        for x in timerange (dt.datetime (yearInteger1, monthInteger1, dayInteger1, hrsInteger1), dt.datetime (yearInteger2, monthInteger2, dayInteger2, hrsInteger2), dt.timedelta (minutes = 1) ):
            #print (x)
            z=str(x)
            y=z.split("-")
            #print(y)
            yearInRange=y[0]
            monthInRange=y[1]
            monthInRangeInteger=int(monthInRange)
            a=y[2]
            #print(a)
            b=a.split(" ")
            dayInRange=b[0]
            #print(dayInRange)
            c=b[1]
            #print(c)
            d=c.split(":")
            hrsInRange=d[0]
            minInRange=d[1]
            monthInWordRange= month_name(monthInRangeInteger)
            Syntax2TimeStamp= yearInRange +"-"+monthInRange+"-"+dayInRange+"T"+hrsInRange+":"+minInRange
            Syntax1TimeStamp= monthInWordRange+" "+ dayInRange +" "+ hrsInRange + ":" + minInRange            
           
            with open(ConnectorsClustertargetPath, "r") as f5:
               for line in f5:
                if Syntax1TimeStamp in line:
                  if Syntax1TimeStamp and "ERROR" in line:
                            print line 
                if Syntax2TimeStamp in line:
                    if Syntax2TimeStamp and "ERROR" in line:
                        print line
               
        print ("====================================================================")
        
        
def sysInfo():
    
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
    three="3"
    four="4"
    print("Select one of the bellow") 
    print("[1] output all the errors in the log bundle (Not Recommended) ")
    print("[2] output the errors in the log bundle using a specific timestamp") 
    print("[3] output the errors in the log bundle using a timestamp Range") 
    print("[4] output the errors in the log bundle using a specific topic and a timestamp Range") 
    InputFromUser=raw_input()
    sysInfo()
    if InputFromUser == one: 
        ErrorFailure()
    if InputFromUser == two: 
        ErrorFailureTimeStamp()
    if InputFromUser == three: 
        timeStampRangeHelperMethod()
    if InputFromUser == four: 
         print("Kindly Specify one of the following topics:")
         print("[4-1] Installation") #marvin log 
         print("[4-2] Node Expansion/Replacment") #marvin log , web log
         print("[4-3] physical view") #physical > connectors log
         print("[4-4] logical view") #  mavin log > logical 
         print("[4-5] Logins/certificates")# web log 
         print("[4-6] Upgrade") # LCM log
         topicTimeRange()
Main()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        