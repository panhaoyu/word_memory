from lib.models import WordModel

for word in WordModel.select():
    if ', ' in word.word:
        w1, w2 = word.word.split(', ')
        ins = WordModel.create(word=w1)
        ins.translation = word.translation
        ins.score = word.score
        ins.save()
        word.word = w2
        word.save()
