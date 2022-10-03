def unsmooth(unigramMod, bigramMod):
    rawProbs = dict()
    for w1 in unigramMod:
        for w2 in unigramMod:
            bg = w1 + " | " + w2 #bg stands for bigram
            if (bg not in rawProbs):
                headCount = unigramMod[w1] #this the count of the first word in the 
                                            #bigram
                bgCount = bigramMod[bg]
                prob = bgCount/headCount
                rawProbs[bg] = prob
    return rawProbs

def laplace(unigramMod, bigramMod):
    smoothedProbs = dict()
    for w1 in unigramMod:
        for w2 in unigramMod:
            bg = w1 + " | " + w2 #bg stands for bigram
            if (bg not in smoothedProbs):
                headCount = unigramMod[w1] #this the count of the first word in the 
                                            #bigram
                bgCount = bigramMod[bg]
                smoothProb = (bgCount+1)/(headCount+len(unigramMod))
                smoothedProbs[bg] = smoothProb
    return smoothedProbs

def GTDiscount(model):
    #we need to find the highest count. We can ignore the 0-count ngrams
    #it would also be more efficient if we used Nc+1 as the new Nc
    freqsOfFreqs = []

def unigramUnsmooth(unigramMod):
    rawProbs = dict()
    totCount = 0
    for v in unigramMod:
        totCount += unigramMod[v]
    for w in unigramMod:
        rawProbs[w] = unigramMod[w]/totCount
    return rawProbs
