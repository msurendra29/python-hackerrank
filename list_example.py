l = []
n = int(input("no of commands"))
for i in range(1,n+1):
    command = input("enter the command please:  ").strip().split(' ')
    operation = command.pop(0)
    if(operation == "insert"):
        pos = command.pop(0)
        ele = command.pop(0)
        eval("l.insert({},{})".format(pos,ele))
    elif operation == "print":
        print(l)
    elif (operation == "remove" or operation == "append"):
        ele = command.pop(0)
        eval("l.{}({})".format(operation,ele))
    elif (operation == "sort" or operation == "pop" or operation == "reverse"):
             eval("l.{}()".format(operation))
    else:
                  print("Invalid command")
