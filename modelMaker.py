def make1GramMod(corpArray):
    #we're making a dictionary to represent the model
    model = dict()
    for k in range(len(corpArray)):
        w = corpArray[k]
        if (w not in model):
            model[w] = 1
        else:
            model[w] = model[w]+1
    return model

def make2GramMod(corpArray):
    model = dict()
    for k in range(len(corpArray) - 1):
        g = corpArray[k] + " | " + corpArray[k+1]
        if (g not in model):
            model[g] = 1
        else:
            model[g] = model[g]+1
    #now to include 0-count bigrams
    for j in range(len(corpArray)):
        for m in range(len(corpArray)):
            z = corpArray[j] + " | " + corpArray[m] #h is a possible zero count
                                                    #bigram
            if (z not in model):
                model[z] = 0

    return model

#def makeNGramMod(corpArray, n):
