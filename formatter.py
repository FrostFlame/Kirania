import os
import regex

rootdir = '.'

for subdir, dirs, files in os.walk(rootdir):
    if regex.search(r'\p{IsCyrillic}', subdir):
        for file_name in files:
            with open(os.path.join(subdir, file_name), encoding='UTF8', mode='r+') as file:
                text = file.read()
                if u'\xa0' in text:
                    print(file_name)
                    text = text.replace(u'\xa0', ' ')
                    file.seek(0)
                    file.write(text)

                bare_links = regex.findall(r'\[\[#.*?\]\]', text)
                if bare_links:
                    for bare_link in bare_links:
                        bare_link = bare_link[2:-2]
                        link = '[[' + file_name[:-3] + bare_link
                        if '|' not in link:
                            link += '\|' + bare_link[1:]
                        link += ']]'
                        text = text.replace(f'[[{bare_link}]]', link)
                    file.seek(0)
                    file.write(text)


