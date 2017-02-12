
fo = open("foo.txt","wb")
print("Name of the file",fo.name)
print("closed or not?: ",fo.closed)
print("opening mode",fo.mode)
fo.close()
