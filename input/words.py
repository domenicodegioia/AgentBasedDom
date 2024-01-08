path = 'italian.txt'

words = []
with open('/home/alberto/PycharmProjects/ABAI_HandsOn/input/italian.txt', 'r') as file:
    for word in file.readlines():
        words.append(word.replace('\n', ''))

