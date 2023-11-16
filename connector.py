import os
import requests
import json
gitdiff = os.getenv('gitdiff')
print(gitdiff)

names=gitdiff.split("\n")
connectorurl="http://localhost:8083/connectors/"

for name in names:
  print(name)
  file= name.split("\t")
  try:
      print(file[0]+"-"+file[1])
      if file[1]=='Jenkinsfile' or file[1]=='connector.py' or file[1]=='sc':
         print('continuing for'+file[1])
         continue
     
         if file[0]=='D': 
            connectorName = file[1].replace("json","")
            print("deleting connector"+connectorName)
            r=requests.delete(connectorurl+connectorName)
            print(r)
          
         elif file[0]=='A' or file[0]=='M': 
            connectorName = file[1].replace(".json","")
            if file[0]=='A': 
               print("creating connector"+connectorName)
            else:
               print("updating connector"+connectorName)
               data = json.load(open(file[1]))   
               print(data)   
               headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
               r = requests.put(connectorurl+connectorName+"/config", data=json.dumps(data), headers=headers)
               print(r) 
       
      
  except Exception as error:
     print(error)
