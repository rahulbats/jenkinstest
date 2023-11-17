import string 
jsonFile=open("topicnames")
jsonstring=string.Template(jsonFile.read())

jsonstring=jsonstring.substitute(**os.environ)