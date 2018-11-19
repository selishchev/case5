"""Case-study #4 Parsing web-pages
Developers:
Selishchev A., Paymushkin K., Krivosheenkova E.
"""

import urllib.request

with open('input.txt') as f_in:
    with open('output.txt', 'w') as f_out:
        for line in f_in:
            line = line.strip()
            url = line
            f = urllib.request.urlopen(url)
            s = f.read()
            text = str(s)
            part_name = text.find("player-name")
            name = text[text.find('>', part_name)+1:text.find('&', part_name)]
            f_out.write(name)
            part_total = text.find("player-totals")
            total = text[text.find('TOTAL', part_total)+10:text.find('</tr>', part_total)]
            value1 = total.replace('\\', '')
            value2 = value1.replace('</td>', '')
            value3 = value2.replace('<td>', ',')
            value4 = value3.replace('t', '')
            value5 = value4.replace('n', '')
            value6 = value5.strip(',')
            value = value6.split(',')
            f_out.write('{} {}'.format('Comp:', value[0]))
            f_out.write('{} {}'.format('ATT:', value[1]))
            f_out.write('{} {}'.format('YDS:', value[3]))
            f_out.write('{} {}'.format('TD:', value[5]))
            f_out.write('{} {}'.format('INT:', value[6]))
            f_out.write('{} {}'.format('PR:', value[10]))
