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
      
      if "topics/" in file[1]:
        appnametopicname=file[1].split("/topics/")
        topicName = appnametopicname[1].replace(".json","")
        appName=appnametopicname[0]
        if file[0]=='D': 
            
            print("deleting topic"+topicName)
            r=requests.delete(restTopicURL+topicName)
            print(r)
          
        elif file[0]=='A' or file[0]=='M': 
            jsonFile=open(file[1])
            jsonstring=string.Template(jsonFile.read())
            jsonstring=jsonstring.substitute(**os.environ)

            print("final topic json "+jsonstring)   
            
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            response_code = 200
            response_reason =''
            if file[0]=='A': 
               print("creating topic "+topicName)
               r = requests.post(restTopicURL, data=jsonstring, headers=headers)
               response_code = str(r.status_code)
               response_reason = r.reason
               print("this is the code "+response_code+" this is the reason: "+response_reason)   
               if(response_code.startswith("2")==False):
                  exit(1)
            else:
               print("updating topic "+topicName)
               response = requests.get(restTopicURL+topicName,  headers=headers)
               currentTopicDefinition = response.json()
               print("existing topic definition ")
               print(currentTopicDefinition)
               currentPartitionsCount=currentTopicDefinition['partitions_count']
               requestedChanges = json.loads(jsonstring)
               print("requested topic definition ")
               print(requestedChanges)
               if(requestedChanges['partitions_count']>currentPartitionsCount):
                  print("requested increasing partitions from "+str(currentPartitionsCount) +" to "+str(requestedChanges['partitions_count']))
                  r=requests.patch(restTopicURL+topicName, data="{\"partitions_count\":"+requestedChanges+"}")
                  response_code = str(r.status_code)
                  response_reason = r.reason
                  print("this is the code "+response_code+" this is the reason: "+response_reason)   
                  if(response_code.startswith("2")==False):
                     exit(1)
               elif(requestedChanges.partitions_count<currentPartitionsCount):
                  print("Attempting to reduce partitions which is not allowed")
                  exit(1)   
            
       
            
            
            
             
            
      if "connector-definitions/" in file[1]:
         appnameconnectorname=file[1].split("/connector-definitions/")
         connectorName = appnameconnectorname[1].replace(".json","")
         appName=appnameconnectorname[0]
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
            
            response_code = str(r.status_code)
            print("this is the code "+response_code+" this is the reason: "+r.reason)   
            if(response_code.startswith("2")==False):
               exit(1)
      
  except Exception as error:
     print(error)
