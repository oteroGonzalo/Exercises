from pathlib import Path
import re, os


userPattern = input('Introduce the regex pattern to look for:\n')


p = Path(f'{Path.cwd()}\\Regex Search')
linesMatched = []
for file in list(p.glob('*.txt')):
    f = open(file)
    contentFile = f.readlines()
    for idx, line in enumerate(contentFile):
        if bool(re.search(userPattern, line)):
            if bool(re.search("\n", line)):
                linesMatched.append(f'{line[:-2]} /// line {idx + 1} from file: {os.path.basename(file)}')
            else:
                linesMatched.append(
                    f'{line} /// line {idx + 1} from file: {os.path.basename(file)}')

if linesMatched:
    for line in linesMatched:
        print(line)
else:
    print("No lines matched")





