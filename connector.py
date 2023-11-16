import os
import requests
gitdiff = os.getenv('gitdiff')
print(gitdiff)

names=gitdiff.split("\n")


for name in names:
  print(name)
  file= name.split("\t")
  try:
      print(file[0]+"-"+file[1])
      res = requests.get('https://stackoverflow.com/questions/26000336')
      print(res) 
  except:
     print("exception occured for"+name)
