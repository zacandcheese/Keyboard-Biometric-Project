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
   file = open(name, "r")
   for line in file.readlines():
      print(line)

