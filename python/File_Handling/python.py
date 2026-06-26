'''file = open("text_file.txt",'r')
data = file.read()
print(data)
file.close()'''
with open("text_file.txt",'r') as file:
  data = file.read()
print(data)
with open("text_file.txt",'r') as file:
  for line in file:
   print(line)
with open("text_file.txt",'r') as file:
  for word in file:
   print(word)
with open("text_file.txt", "r") as file:
    content = file.read()       # Reads the entire file as a string
    words = content.split()     # Splits the string into a list of individual words
    
    for word in words:
        print(word)
with open("text_file.txt", "r") as file:
    content = file.read()       # Reads the entire file as a string
    words = content.split()     # Splits the string into a list of individual words
    
    for word in words:
        print(word)
    
    '''with open("text_file.txt",'w') as file:
       file.write("python")'''
with open('text_file.txt','a') as file:
   file.write('append')

