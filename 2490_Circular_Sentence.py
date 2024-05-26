class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        c = 0
        sentence = (sentence.split())
        if len(sentence) == 1:
            d = len(sentence[0])
            if sentence[0][d-1] == sentence[0][0]:
                return True
            else:
                return False
        else:
            for i in range(0, len(sentence)-1):
                d = len(sentence[i])
                if sentence[i][d-1] == sentence[i+1][0]:
                    c = 1
                else:
                    c = 0
                    break
            if c == 1:
                if sentence[0][0] == sentence[-1][-1]:
                    return True
                else:
                    return False
      
        
            
