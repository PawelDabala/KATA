"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
"""
def get_middle(s):
    if len(s) % 2 == 0:
        mov = len(s) // 2
        return s[(mov - 1): (mov + 1)]
    else:
        return s[len(s)//2]



print(get_middle("s"))


def get_middle2(s):
   return s[(len(s)-1)/2:len(s)/2+1]