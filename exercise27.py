class Dictionary():
    def __init__(self):
        self.d = {}
    def newentry(self, word, definition = ''):
        self.d = {word: definition}
    def look(self, key):
        if key in self.d:
            return self.d[key]
        else:
            return 'Cant find entry for {}'.format(key)


d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')

print(d.look('Hi'))