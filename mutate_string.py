def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]   
    
string = input().strip()
pos_char = input().strip().split()
position = int(pos_char.pop(0))
character = pos_char.pop(0)
print(mutate_string(string,position,character))
