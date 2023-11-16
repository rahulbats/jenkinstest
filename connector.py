import os
gitdiff = os.getenv('gitdiff')
print(gitdiff)

names=gitdiff.split("\n")
for name in names:
  print(name)
  file= name.split("\t")
  print(file[0]+"-"+file[1])