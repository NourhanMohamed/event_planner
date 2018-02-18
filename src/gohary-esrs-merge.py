
'''
Created on Sep 3, 2016

@author: elgoha1


'''

from datetime import datetime


SPA = '.\spa\EMC\CEM\log\eVE\\ve_esrs.log'
SPB = '.\spb\EMC\CEM\log\eVE\\ve_esrs.log'



All_Responce_Codes = """------------------------------------All Responce Codes Meaning as in KB 485219-------------------------------------------------

  503 Service Unavailable: . The server is temporarily unable to service your request due to maintenance downtime or capacity problems. Please try again later
    - Cause: Attempt to provision with "light" level support account. When a new customer signs up for a support account, they will be assigned "light" support 
      and it takes 24 to 48 hours to authorized "full" support on that account.
    - Cause: An esrs service may be down or otherwise not functioning (more info in ve_esrs.log on network check)
  502 Proxy Error:  The proxy server received an invalid response from an upstream server.
    - Cause: Unconfirmed bug in the ESRS container (6/1 \\- not sure)
    - Cause: Service on ESRS backend required restart.
    - Cause: Firewall issue, see Port doc link below.
  500 OTP Failed: . Please check Your OTP  
    - Cause: Customer account must be changed from Partner to "Customer,Partner"
    - Cause: "read timeout "Packet drop in network"  Retry provision after correcting any network issues.
  401 Authentication Failed: User password could not be retrieved   
    - Cause: Old VEs need to be cleaned out of ESRS database (Should be test env only)
    - Cause: Keys out of sync, (Must re-provision)
  400 Bad Format for Request:  
  201 Add device failed: 
    - Cause: Business logic failed somewhere: Look in json additional items
      ESRS status "unknown"
    - Cause: Seen on status after initial provisioning (should clear in 5 minute to an hour)
    - Cause: Possible code bug (no resolution 6/4/16), restart of eVE (SP reboot) typically resolvers issue.
  200 Success :
    - Cause: ESRS succeeded, refresh the Uni-sphere web page and confirm ESRS is now connected.
    
  
"""

PortsCheck = '-------------------------------------------------Ports Check------------------------------------------------------------------ \n \n'

Flag200 = ''
Flag201 = ''
Flag204 = ''
Flag400 = ''
Flag401 = ''
Flag500 = ''
Flag502 = ''
Flag503 = ''
FlagPort443 = ' Port 443 connection status Undefined in logs \n'
FlagPort8443 = ' Port 8443 connection status Undefined in logs\n'



#SPA = 'C:\\Users\ELGOHA1\Desktop\SP A.log'
#SPB = 'C:\\Users\ELGOHA1\Desktop\SP B.log'


#SPA = r'Z:\SR Archive\Esrs logs collection\Unity_300_service_data_APM00162116201_2016-08-12_13_42_36\spa\EMC\CEM\log\eVE\ve_esrs.log'
#SPB = r'Z:\SR Archive\Esrs logs collection\Unity_300_service_data_APM00162116201_2016-08-12_13_42_36\spb\EMC\CEM\log\eVE\ve_esrs.log'

num_lines_A = sum(1 for line in open(SPA))
num_lines_B = sum(1 for line in open(SPB))

#text_file_new = open('C:\\Users\ELGOHA1\Desktop\Triage_ESRS.txt' , 'w')
text_file_new = open('Triage_ESRS.txt' , 'w')

Triage_ESRS = 'Triage_ESRS.txt'



with open (SPA) as a, open (SPB) as b:
  lines_a = a.readlines()
  lines_b = b.readlines()
  
  
  j=0
  i=0
  print("Building ESRS Triage")
  while j < num_lines_A:
      
      flag = False
      lineA = lines_a[j]   
      words = lineA.split()    
      
      try:                               
          s = (words[1] +' '+ words[2] +' '+ words[3]+' 2016')         
          date_a = datetime.strptime(s, '%b %d %X %Y')                            
                 
      except (IndexError , ValueError) :          
          text_file_new.write ('A     '+ lineA)
          flag = True
            
      while i < num_lines_B :
        lineB = lines_b[i]       
       
        words = lineB.split()
        try:
          s = (words[1] +' '+ words[2] +' '+ words[3]+' 2016')
          date_b = datetime.strptime(s, '%b %d %X %Y')
         
          if date_a <= date_b :
            
            if flag == False:
              text_file_new.write('A    '+lineA )
            
            if j == num_lines_A -1:
              while i < num_lines_B:             
                #print('B  test ' + lines_b[i])
                text_file_new.write('B    ' + lines_b[i])
                i = i + 1                      
            break
          elif date_b <= date_a:
            #print('B  '+lineB ) 
            text_file_new.write('B    '+lineB )
            
            
            if i == num_lines_B -1 :
              while j < num_lines_A:             
                
                text_file_new.write('A    ' + lines_a[j])
                j = j+1
                      
              
        except (IndexError , ValueError) :
          
          text_file_new.write('B     '+lineB) 
            
        i = i+1    
      j = j + 1 
  text_file_new.close()
 
  
  
  
  
  
  #num_lines_All = sum(1 for line in open(Triage_ESRS))
  searchfile = open(Triage_ESRS, 'r+')
  #searchfile.seek(0)
  
  #text_file_new.write('\n testtttttttsladhflkjdsahfkjdssha \n \n \n \n')
  
  #text_file_new.write('---------------------------Response Codes Found on The Unity-------------------------------------\n \n')
  for lineAll in searchfile:
    if ("'responseCode' => '200'" or "'responseCode' => 200") in lineAll:
      Flag200 = "'responseCode' => '200' 'Success' \n"
      
      break
  searchfile.seek(0)
  for lineAll in searchfile:
    if ("'responseCode' => '201'" or "'responseCode' => 201") in lineAll:
      Flag201 = "'responseCode' => '201' 'Device failed' >> Check KB : 488483 \n"
      break
  searchfile.seek(0) 
  for lineAll in searchfile:
    if ("'responseCode' => '204'" or "'responseCode' => 204") in lineAll:
      Flag204 = "'responseCode' => '204' \n"
      break
    
  searchfile.seek(0)
  for lineAll in searchfile:  
    if ("'responseCode' => '400'" or "'responseCode' => 400")  in lineAll:
      Flag400 = "'responseCode' => '400' 'Bad Format for Request' \n"
      break 
  searchfile.seek(0)
  for lineAll in searchfile:  
    if ("'responseCode' => '401'" or "'responseCode' => 401")  in lineAll:
      Flag401 = "'responseCode' => '401' 'Authentication Failed' >> Check KB : 488946 \n"
      break  
  searchfile.seek(0)
  for lineAll in searchfile:  
    if ("'responseCode' => '500'" or "'responseCode' => 500")  in lineAll:
      Flag500 = "'responseCode' => '500' 'OTP Failed' >> Check KB : 488611 \n"
      break

  searchfile.seek(0)
  for lineAll in searchfile:  
    if ("'responseCode' => '502'" or "'responseCode' => 502")  in lineAll:
      Flag502 = "'responseCode' => '502' 'Proxy Error' \n"
      break
  searchfile.seek(0)      
  for lineAll in searchfile:  
    if ("'responseCode' => '503'" or "'responseCode' => 503")  in lineAll:
      Flag503 = "'responseCode' => '503' 'Service Unavailable' \n"
      break
  searchfile.seek(0)
  
  
  for lineAll in searchfile:  
    if ('"port443":"Connected"')  in lineAll:
      FlagPort443 = '"port443":"Connected"  \n'
      break
  searchfile.seek(0)
  for lineAll in searchfile:  
    if ('"port8443":"Connected"')  in lineAll:
      FlagPort8443 = '"port8443":"Connected" \n'
      break
  searchfile.seek(0)
  
  
  
  for lineAll in searchfile:  
    if ('"port443":"Not Connected"')  in lineAll:
      FlagPort443 = '"port443":"Not Connected" \n'
      break
  searchfile.seek(0)
  for lineAll in searchfile:  
    if ('"port8443":"Not Connected"')  in lineAll:
      FlagPort8443 = '"port8443":"Not Connected" \n'
      break
  searchfile.seek(0)
  
  
    
  
  content = searchfile.read()
  searchfile.seek(0)
  searchfile.write('--------------------------------------Response Codes Found on The Unity------------------------------------------------------' +'\n'+'\n' +Flag200 + Flag201 + Flag204 + Flag400 +Flag401 + Flag500 + Flag502 + Flag503  + '\n' + '\n' + PortsCheck + FlagPort443 + FlagPort8443 + '\n' + All_Responce_Codes + '\n' + '------------------------------------------------------Triage Logs-----------------------------------------------------------------' + '\n' + '\n' + '\n'  + content )
  
  print('Successfully Built')

