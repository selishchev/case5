"""Case-study #4 Парсинг web-страниц
Developers:
Selishchev A., Paymushkin K., Krivosheenkova E.

"""
url = 'http://www.nfl.com/player/brycepetty/2552369/profile'
f = urllib.request.urlopen(url)
s = f.read()

text = str(s)
part_name = text.find("player-name")
name = text[text.find('>',part_name)+1:text.find('&',part_name)]
print(name)
part_total = text.find("player-totals")
total = text[text.find('TOTAL',part_total)+10:text.find('</tr>',part_total)]
value1 = total.replace('\\','')
value2 = value1.replace('</td>','')
value3 = value2.replace('<td>',',')
value4 = value3.replace('t', '')
value5 = value4.replace('n','')
value6 = value5.strip(',')
value = value6.split(',')
print('{} {}'.format('Comp:',value[0]))
print('{} {}'.format('ATT:',value[1]))
print('{} {}'.format('YDS:',value[3]))
print('{} {}'.format('TD:',value[5]))
print('{} {}'.format('INT:',value[6]))
print('{} {}'.format('PR:',value[10]))
