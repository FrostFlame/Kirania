import os
import regex

rootdir = '.'

for subdir, dirs, files in os.walk(rootdir):
    if regex.search(r'\p{IsCyrillic}', subdir):
        for file_name in files:
            with open(os.path.join(subdir, file_name), encoding='UTF8', mode='r+') as file:
                print(file_name)
                text = file.read()
                text = text.replace(u'\xa0', ' ')

                file.write(text)