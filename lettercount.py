#Program to find the frequency of letters in a sentence.

def lettercount(st):
    dct = dict()
    for i in st:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] = dct[i] + 1
    return dct

sent = input("Enter a sentence to find the frequency of the letters... ")
print("The letters with their corresponding frequencies are...\n",lettercount(sent))
