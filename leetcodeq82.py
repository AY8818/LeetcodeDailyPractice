# 804. Unique Morse Code Words

def uniqueMorseRepresentations(words):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    mcode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    lst = []
    for word in words:
        code = ""
        for char in word:
            code += mcode[alpha.index(char)]
        if code not in lst:
            lst.append(code)

    return len(lst)
words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))
