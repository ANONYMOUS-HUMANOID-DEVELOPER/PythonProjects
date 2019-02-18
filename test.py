import sys

print("Hello World!")

password = input("Please enter the password for file operations: ")
if password=="fileops":
  sentence = input("Please enter a string: ")

def testsentence():
  print("The sentence is : {} and the result is :\n".format(sentence))
  for i in range(len(sentence)):
       print( sentence[i] + "\t")

try:
 testfile = open("contents.txt","w")
 testfile.write(sentence)
 displaystring = dir(int)
 for i in range(len(displaystring)):
  testfile.write(displaystring[i])
 print("File operations completed...")
 testfile.close()

except:
 print("Sorry, file not created")
 raise

for i in range(len(displaystring)):
  print("{} \n".format(displaystring[i]))

print("Reading file contents..." + "\n")
testfile = open("contents.txt", "r")
reader = testfile.read()
for i in range(len(reader)):
 print( "{} \n".format(reader[i]))
''' filestring = testfile.readline() \
 print(filestring)'''

testsentence()
