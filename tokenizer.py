import re

def tokenize(corpus):
    corpArray = corpus.split()
    #now we need to tokenize the special characters. we'll use regex
    
    #let's first split out punctuation that is included in a word's token.
    #we need to also remove these special characters if they appear at the front
    #or at the back
    end = re.compile('[,;.:\]?!:=)}\'\"]*$')
    #this is to match special chars at the end
    start = re.compile('[\[({\'\"]*')
    #we need to make provision for many of these specials occuring at the edges. 
    #hence the asterisk.
    #If the matches span the entire token, delete the whole token and then insert
    #each punctuation...that's also if the span is more than 1.
    #if the matches span only part of the token, delete the parts they span and 
    #then do the insertions
    currentLen = len(corpArray)
    k = 0
    while k < currentLen:
        tok = corpArray[k]
        s = start.match(tok)
        if ((s != None) and (len(tok) > 1)):
            prefix = s.group()
            j = 0
            for c in prefix:
                corpArray.insert(k+j, c)
                currentLen = len(corpArray)
                j += 1
            k += j 
            #now k will be at the pos of tok. remember, the insertions cause tok
            #to be moved deeper into the list
            corpArray[k] = tok[s.end():] #may have to get rid of the +1
            tok = tok[s.end():]
        e = end.search(tok)
        stillSplit = True #to signal whether we should extract end-of-word punctuation
        if (e != None): #and (len(e.group()) > 1)): # and (e.group() != '.')): #and not(corpArray[k+1][0].isupper()))): #there might not be a corpArray[k+1]
            if (e.group() == '...'):
                corpArray[k] = tok[:e.start()]
                corpArray.insert(k+1, e.group())
                k += 2
            else:
                if k < (len(corpArray)-1):
                    if ((e.group() == '.') and (corpArray[k+1][0].islower())): 
                        stillSplit = False #this is so that acronyms that end with dots do not have the dot removed
                if stillSplit:
                    suffix = e.group()
                    n = 1
                    for d in suffix:
                        corpArray.insert(k+n, d)
                        currentLen = len(corpArray)
                        n += 1
                    corpArray[k] = tok[0:e.start()]
                    k = k + n #but this will come after we truncate the original token
                    #now we'll insert the suffix chars
                else:
                    k += 1
        else:
            k += 1
        #I think we're going to have to change k within the loop. So that we don't
        #iterate over the inserted tokens.
        #First insert the preceding punctuations. Then insert the trailing puncts. 

    #then we'll need to split a token tok around ellipses. we should use a regex 
    #to detect if
    #an ellipsis is present and to find the position...No. There is a better way.
    #we could assign the result of the split to S. then we can insert an ellipsis
    #token between each element of the S. Finally we'll replace tok with S.

    #now we must split the tokens around ellipses
    q = 0
    while q < len(corpArray):
        superToken = corpArray[q].split('...')
        if (len(superToken) > 1):
            p = 0
            STCurrLen = len(superToken) #STCurrLen is the current length of superToken
            while p < (STCurrLen-1):
                superToken.insert(p+1, '...')#this inserts the ellipses as tokens between the tokens in superToken
                STCurrLen = len(superToken)
                p += 2
            del corpArray[q]
            m = 0
            while m < len(superToken):
                corpArray.insert(q+m, superToken[m])#this inserts the elements of superToken into corpArray
                m += 1
            q += m
        else:
            q += 1

    #now we have to iterate through the whole corpArray to remove null strings.
    #null strings may have been added because of the split operations
    h = 0
    finCurrLen = len(corpArray)
    while h < finCurrLen:
        if corpArray[h] == '':
            del corpArray[h]
            finCurrLen = len(corpArray)
        else:
            h += 1

    return corpArray

def normalizeCase(corpArray):
    for k in range(len(corpArray)):
        if (not(corpArray[k].isupper())):
            corpArray[k] = corpArray[k].lower()

    return corpArray

