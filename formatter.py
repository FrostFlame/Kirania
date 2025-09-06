import os
import regex

rootdir = '.'

for subdir, dirs, files in os.walk(rootdir):
    if regex.search(r'\p{IsCyrillic}', subdir):
        for file_name in files:
            with open(os.path.join(subdir, file_name), encoding='UTF8', mode='r+') as file:
                changed = False
                print(file_name)
                text = file.read()
                if u'\xa0' in text:
                    text = text.replace(u'\xa0', ' ')
                    changed = True

                bare_links = regex.findall(r'\[\[#.*?\]\]', text)
                if bare_links:
                    for bare_link in bare_links:
                        bare_link = bare_link[2:-2]
                        link = '[[' + file_name[:-3] + bare_link
                        if '|' not in link:
                            link += '|' + bare_link[1:]
                        link += ']]'
                        text = text.replace(f'[[{bare_link}]]', link)
                    changed = True

                if 'Стрелок' in file_name or 'Следопыт' in file_name:
                    pass
                broken_links_in_tables = regex.findall(r'\|\s[^|]*?\[\[[^\]]+?\S\|\S.+?\]\]\s*?\|', text)
                for broken_link in broken_links_in_tables:
                    if '\\|' in broken_link:
                        continue
                    fixed_link = '|' + broken_link[1:-1].replace('|', '\|') + '|'
                    text = text.replace(broken_link, fixed_link)
                    changed = True

                if changed:
                    file.seek(0)
                    file.write(text)
