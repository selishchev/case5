"""Case-study #4 Парсинг web-страниц
Developers:
Selishchev A., Paymushkin K., Krivosheenkova E.

"""

import urllib.request
url = 'http://www.nfl.com/player/brycepetty/2552369/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("player-name")
name = text[text.find('>', part_name)+1:text.find('&', part_name)]
print(name)
