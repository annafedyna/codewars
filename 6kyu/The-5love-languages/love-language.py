import random

def love_language(partner, weeks):
        love_lang=["words", "acts", "gifts", "time", "touch"]
        positive_response = [0]*5
        neutral_response = [0]*5 # unnecessary
        for i in range(7*weeks):
            j = i%5
            if partner.response(love_lang[j]) == 'positive':
                positive_response[j] += 1
            else:
                neutral_response[j] += 1
        return love_lang[positive_response.index(max(positive_response))]

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
