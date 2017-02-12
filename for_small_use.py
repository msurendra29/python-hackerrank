file  = open("MEMORY.txt","r")
data = file.read()
dummy_memory  = data.splitlines()
file.close()
pc = 0
inst_reg = int(dummy_memory[int(pc/4)],15)

#opcode = int(inst_reg[0:5],2)
#add_mode = int(inst_reg[5:7],2)

print(inst_reg)
