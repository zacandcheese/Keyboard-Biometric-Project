import os
import glob
import random

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

bigList = []
for name in listOfTxtFiles:
   tupleList = ["ight"] 
   with open(name) as file:
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
                   bigList.append(line)
         oldLine = newLine
         
      
         
         
      print(name)  
print("\n")
dataList = bigList
print (random.choice(dataList))