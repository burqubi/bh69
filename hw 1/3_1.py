# Тут все пробелы заменяются
# text = input().replace(' ', '-')
# print(text)

# Тут, чтобы пробелов лишних не было
text = input()
text_split = text.split()
text_join = ' '.join(text_split)
print(text_join)