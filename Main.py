#from nltk.tokenize import word_tokenize
from modelMaker import *
from ngramStats import *
from smoother import *
from tokenizer import *
from reporter import *
import subprocess
import sys

#we need to spawn the corpusSelector.
#then we need to capture its output and extract the corpus names from its output
corpSelOut = subprocess.run(["python", "corpusSelector.py"], capture_output = True, text = True)
fileList = corpSelOut.stdout.split("\n")
fileName1 = fileList[0]
fileName2 = fileList[1]

f1 = open(fileName1, 'r')
corpus = f1.read()
f1.close()

f2 = open(fileName2, 'r')
corpus2 = f2.read()
f2.close()

corpArray = tokenize(corpus)
corpArray2 = tokenize(corpus2)

#this is to make all words lowercase; so that each word only occurs once in the 
#model, regardless of whether it appears with the first letter capitalized
corpArray = normalizeCase(corpArray)

#do the same to corpArray2
corpArray2 = normalizeCase(corpArray2)

unigramMod = make1GramMod(corpArray)
unigramMod2 = make1GramMod(corpArray2)
bigramMod = make2GramMod(corpArray)
bigramMod2 = make2GramMod(corpArray2)

usedUnigrams_1 = vocSize(unigramMod)
usedUnigrams_2 = vocSize(unigramMod2)
printStats("used unigrams in corpus 1", usedUnigrams_1, "ngram stats.txt")
printStats("used unigrams in corpus 2", usedUnigrams_2, "ngram stats.txt")

usedBigrams_1 = vocSize(bigramMod)
usedBigrams_2 = vocSize(bigramMod2)
printStats("used bigrams in corpus 1", usedBigrams_1, "ngram stats.txt")
printStats("used bigrams in corpus 2", usedBigrams_2, "ngram stats.txt")

bigram_1_StDev = stanDev(bigramMod)
bigram_2_StDev = stanDev(bigramMod2)
printStats("standard dev. of bigrams in corpus 1", bigram_1_StDev, "ngram stats.txt")
printStats("standard dev. of bigrams in corpus 2", bigram_2_StDev, "ngram stats.txt")

unigram_1_StDev = stanDev(unigramMod)
unigram_2_StDev = stanDev(unigramMod2)
printStats("standard dev. of unigrams in corpus 1", unigram_1_StDev, "ngram stats.txt")
printStats("standard dev. of unigrams in corpus 2", unigram_2_StDev, "ngram stats.txt")

propBi1 = proportionUnused(bigramMod)
propBi2 = proportionUnused(bigramMod2)
printStats("proportion of unsused bigrams in corpus 1", propBi1, "ngram stats.txt")
printStats("proportion of unsused bigrams in corpus 2", propBi2, "ngram stats.txt")

unigram_1_Mean = avg(bigramMod)
unigram_2_Mean = avg(bigramMod2)
printStats("average unigram count in corpus 1", unigram_1_Mean, "ngram stats.txt")
printStats("average unigram count in corpus 2", unigram_2_Mean, "ngram stats.txt")

bigram_1_Mean = avg(bigramMod)
bigram_2_Mean = avg(bigramMod2)
printStats("average bigram count in corpus 1", bigram_1_Mean, "ngram stats.txt")
printStats("average bigram count in corpus 2", bigram_2_Mean, "ngram stats.txt")

sharedByUGM1 = amountShared(unigramMod, unigramMod2)
sharedByUGM2 = amountShared(unigramMod2, unigramMod)
printStats("proportion of shared unigrams in corpus 1", sharedByUGM1, "ngram stats.txt")
printStats("proportion of shared unigrams in corpus 2", sharedByUGM2, "ngram stats.txt")

sharedByBGM1 = amountShared(bigramMod, bigramMod2)
sharedByBGM2 = amountShared(bigramMod2, bigramMod)
printStats("proportion of shared bigrams in corpus 1", sharedByBGM1, "ngram stats.txt")
printStats("proportion of shared bigrams in corpus 2", sharedByBGM2, "ngram stats.txt")

outliersUni1 = outliers(unigramMod, unigram_1_StDev, unigram_1_Mean)
outliersUni2 = outliers(unigramMod2, unigram_2_StDev, unigram_2_Mean)
printOutliers(outliersUni1, "corpus 1 (unigrams)", "ngram stats.txt")
printOutliers(outliersUni2, "corpus 2 (unigrams)", "ngram stats.txt")

outliers1 = outliers(bigramMod, bigram_1_StDev, bigram_1_Mean)
outliers2 = outliers(bigramMod2, bigram_2_StDev, bigram_2_Mean)
printOutliers(outliers1, "corpus 1 (bigrams)", "ngram stats.txt")
printOutliers(outliers2, "corpus 2 (bigrams)", "ngram stats.txt")

rawUniProbs1 = unigramUnsmooth(unigramMod)
rawUniProbs2 = unigramUnsmooth(unigramMod2)
printProbs(rawUniProbs1, "raw probabilities for unigram model 1.txt")
printProbs(rawUniProbs2, "raw probabilities for unigram model 2.txt")

rawProbs1 = unsmooth(unigramMod, bigramMod)
rawProbs2 = unsmooth(unigramMod2, bigramMod2)
printProbs(rawProbs1, "raw probabilities for bigram model 1.txt")
printProbs(rawProbs2, "raw probabilities for bigram model 2.txt")

smoothedProbs1 = laplace(unigramMod, bigramMod)
smoothedProbs2 = laplace(unigramMod2, bigramMod2)
printProbs(smoothedProbs1, "laplace-smoothed probabilities for bigram model 1.txt")
printProbs(smoothedProbs2, "laplace-smoothed probabilities for bigram model 2.txt")
end = input("Press any key to exit ")