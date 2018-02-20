import os
import glob

os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir("nltk_data/corpora/gutenberg")
print(os.getcwd())

listOfTxtFiles = []
for file in glob.glob("*.txt"):
	listOfTxtFiles.append(file)
print(listOfTxtFiles)

for name in listOfTxtFiles:
   tupleList = ["ight"] 
   with open(name) as file:
   
   
      """
      with open(name) as newFile:
       for line in newFile:
          print(line)
      """
      oldLine = ""
      for newLine in file:
         #line = cat jumps do
         line = oldLine + newLine
         for tuple in tupleList:
             if tuple in line.lower():
                string = line.lower()
                substring = tuple
             
                count = string.count(substring)
             
                if(count>3):
                  print(line)
                  print("\n")
         oldLine = newLine
                 
      print(name)  

