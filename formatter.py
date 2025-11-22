import os
from collections import defaultdict

import regex

rootdir = '.'

for subdir, dirs, files in os.walk(rootdir):
    if regex.search(r'\p{IsCyrillic}', subdir) and 'images' not in subdir:
        for file_name in files:
            # if file_name == 'Abbot_copy.png':
            #     print(file_name)
            with open(os.path.join(subdir, file_name), encoding='UTF8', mode='r+') as file:
                changed = False
                print(file_name)
                text = file.read()
                # Замена nbsp на пробелы
                if u'\xa0' in text:
                    text = text.replace(u'\xa0', ' ')
                    changed = True

                # Замена ссылок на текущую статью на полную ссылку
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

                # Починка сломанных таблиц?
                # broken_links_in_tables = regex.findall(r'\|\s[^|]*?\[\[[^\]]+?\S\|\S.+?\]\]\s*?\|', text)
                # for broken_link in broken_links_in_tables:
                #     if '\\|' in broken_link:
                #         continue
                #     fixed_link = '|' + broken_link[1:-1].replace('|', '\|') + '|'
                #     text = text.replace(broken_link, fixed_link)
                #     changed = True

                # Приведение сабклассов к таблицам
                if 'Заклинания' in subdir and 'Архетипы:' in text:
                    archtypes_line = regex.findall(r'Архетипы:.*', text)[0]
                    archtypes = regex.findall(r'\|(.+?)\]', archtypes_line)

                    archetypes_by_class_dict = defaultdict(list)
                    for archtype in archtypes:
                        archtype_split = archtype.split('(')
                        archtype = archtype_split[0].strip()
                        dnd_class = archtype_split[1].strip(')').capitalize()
                        archetypes_by_class_dict[dnd_class].append(archtype)

                    sorted_classes = list(archetypes_by_class_dict.keys())
                    sorted_classes.sort()

                    table_head = '<div>\n<table>\n<thead>\n<tr>\n<th>Классы</th>\n'
                    classes_rows = ''
                    table_middle = '</tr>\n</thead>\n<tbody>\n<tr>\n<td>Архетипы</td>\n'
                    archtypes_rows = ''
                    table_footer = '</tr>\n</tbody>\n</table>\n</div>'

                    for dnd_class in sorted_classes:
                        archtypes = archetypes_by_class_dict[dnd_class]
                        archtypes.sort()
                        archtypes = '<br>'.join(archtypes)

                        classes_rows += f'<th>{dnd_class}</th>\n'
                        archtypes_rows += f'<td>{archtypes}</td>\n'

                    table_html = table_head + classes_rows + table_middle + archtypes_rows + table_footer

                    text = text.replace(archtypes_line, table_html)
                    print('Реформатировал сабклассы в ', file_name)
                    changed = True

                if changed:
                    file.seek(0)
                    file.write(text)
