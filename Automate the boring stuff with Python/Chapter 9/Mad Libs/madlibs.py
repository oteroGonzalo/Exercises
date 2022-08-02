import re

text = open('./Mad Libs/madlibstext.txt')

contentFile = re.split('(\W+)', text.read())

for idx, i in enumerate(contentFile):
    if bool(re.match("ADJECTIVE", i)) or bool(re.match("VERB", i)) or bool(re.match("ADVERB", i)) or bool(re.match("NOUN", i)):

        userInput = input(f'Enter one {i}:\n')
        contentFile[idx] = userInput

finalText = open('./Mad Libs/finalText.txt', 'w')
finalText.write("".join(contentFile))
finalText.close()
print("".join(contentFile))



