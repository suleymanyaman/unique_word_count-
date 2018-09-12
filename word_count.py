import docx2txt
import re

my_text = docx2txt.process("The directory to your .docx file here").lower()


match = re.findall(r'[a-zA-Z\’\d\'\-]+',my_text)



data={}

for word in match:
    if word not in data:
        data[word]=1
    else:
        data[word]+=1


print("Distinct words:",len(data.keys()))
print("Words:",  len(match))


c = input("")
