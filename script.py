import os
import requests
import json
import string 
gitdiff = os.getenv('gitdiff')
print(gitdiff)

names=gitdiff.split("\n")
connectorurl = os.getenv('connectorURL')
restTopicURL = os.getenv('restURL')+"v3/clusters/"+os.getenv('kafkaClusterID')+"/topics/"

print("this is the restproxy topic url "+restTopicURL)
for name in names:
  print(name)
  file= name.split("\t")
  try:
      print(file[0]+"-"+file[1])
      
      if "topics" in file[1]:
        topicName = file[1].replace(".json","").replace("topics/","") 
        if file[0]=='D': 
            
            print("deleting topic"+topicName)
            r=requests.delete(restTopicURL+topicName)
            print(r)
          
        elif file[0]=='A' or file[0]=='M': 
            
            if file[0]=='A': 
               print("creating topic "+topicName)
            else:
               print("updating topic "+topicName)
            jsonFile=open(file[1])
       
            jsonstring=string.Template(jsonFile.read())
            jsonstring=jsonstring.substitute(**os.environ)

            print("final topic json "+jsonstring)   
            
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            r = requests.post(restTopicURL, data=jsonstring, headers=headers)
            print("this is the code "+r.status_code+" this is the reason: "+r.reason)    
            response_code = str(r.status_code)
            if(response_code.startswith("2")==false):
               exit(1)
      if "connector-definitions" in file[1]:
         connectorName = file[1].replace(".json","").replace("connector-definitions/","")
         if file[0]=='D': 
            
            print("deleting connector"+connectorName)
            r=requests.delete(connectorurl+connectorName)
            print(r)
          
         elif file[0]=='A' or file[0]=='M': 
            
            if file[0]=='A': 
               print("creating connector "+connectorName)
            else:
               print("updating connector "+connectorName)
            jsonFile=open(file[1])
            jsonstring=string.Template(jsonFile.read())
            jsonstring=jsonstring.substitute(**os.environ)
            
            
            print("final connector json "+jsonstring)   
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            r = requests.put(connectorurl+connectorName+"/config", data=jsonstring, headers=headers)
            print("this is the code "+r.status_code+" this is the reason: "+r.reason)   
            response_code = str(r.status_code)
            if(response_code.startswith("2")==false):
               exit(1)
      
  except Exception as error:
     print(error)
