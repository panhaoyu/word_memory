from lib.word import WordModel

result = WordModel.select(WordModel.word, WordModel.translation).where(~WordModel.abandoned)
lines = [f'{i.word},{i.translation}\n' for i in result]

with open("a.csv", mode='w', encoding='gbk') as file:
    file.writelines(lines)
