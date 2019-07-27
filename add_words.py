import re
from lib.models import WordModel

with open('words.txt', mode='r', encoding='GBK') as file:
    content = file.read()
words = re.findall(
    '<tr>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?</tr>',
    content)
from pprint import pprint as print

for translation, word in words:
    try:
        WordModel.create(word=word, translation=translation)
    except:
        continue
