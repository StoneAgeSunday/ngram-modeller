import math

def vocSize(ngramMod):
    ngramSet = {k for k in ngramMod.keys() if ngramMod[k] > 0}
    return len(ngramSet)

def stanDev(model):
    #we're only going to consider non-zero ngrams 
    #first calculate variance
    variance = 0
    nonZeros = 0
    for count in model.values():
        if (count>0):
            nonZeros += 1
            variance += (count**2)

    variance /= nonZeros
    stDev = math.sqrt(variance)

    return stDev

def proportionUnused(model):
    #calculates the sparseness of the ngram model
    totNGrams = len(model)
    totUnused = 0
    for count in model.values():
        if (count == 0):
            totUnused += 1
    
    result = totUnused/totNGrams
    return result

def outliers(model, stDev, mean):
    underliers = []
    overliers = []
    #we need to calculate the mean of the ngram counts. we'll do it in a new 
    #function

    for key in model:
        if ((model[key] != 0) and (model[key] < (mean-stDev))):
            underliers.append(key)
        elif (model[key] > (mean + stDev)):
            overliers.append(key)

    result = [underliers, overliers]
    return result

def avg(model):
    totCount = 0
    totNonZero = 0
    for count in model.values():
        if (count > 0):
            totNonZero += 1
            totCount += count

    result = totCount/totNonZero
    return result

def amountShared(model1, model2):
    set1 = {k for k in model1.keys() if model1[k] > 0}
    set2 = {j for j in model2.keys() if model2[j] > 0}

    setUnion = set1 & set2

    shared = len(setUnion)/len(set1)
    return shared
