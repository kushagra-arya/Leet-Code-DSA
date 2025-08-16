class Solution(object):
    def isValid(self, word):
        con = 0
        vow = 0
        vowels = ["a", "e", "i", "o", "u"]
        if len(word) < 3:
            return False
        if word.isalnum():
            for i in word.lower():
                if i in vowels:
                    vow +=1
                elif i.isnumeric():
                    pass
                else:
                    con += 1
        if vow > 0 and con > 0:
            return True
        else:
            return False
