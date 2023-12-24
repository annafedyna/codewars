import random

def love_language(partner, weeks):
    love_lang=["words", "acts", "gifts", "time", "touch"]
    return max(love_lang, key = lambda word: sum(partner.response(word) == 'positive' for i in range(weeks)))

class TestPartner:
    def __init__(self, main_lang):
        self.main = main_lang
    def response(self, language):
        r = random.random()
        if language == self.main:
            if r < 0.85: return 'positive'
            else:        return 'neutral'
        else: # language != self.main
            if r < 0.15: return 'positive'
            else:        return 'neutral'

weeks = 6
partner = TestPartner('words')
print(love_language(partner, weeks), 'words')

partner = TestPartner('gifts')
print(love_language(partner, weeks), 'gifts')
