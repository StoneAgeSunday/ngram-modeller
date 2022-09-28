
def printProbs(probs, filename):
    f = open(filename, "w")
    for k in probs.keys():
        out = k + ": " + str(probs[k]) +"\n"
        f.write(out)
    f.close()

def printStats(statName, stat, filename):
    f = open(filename, "a")
    f.write(statName+": ")
    f.write(str(stat)+"\n\n")
    f.close()

def printOutliers(outliers, corpus, filename):
    f = open(filename, "a")
    f.write("\n")
    f.write("underliers in " + corpus + ":\n")
    for k in outliers[0]:
        f.write(k+"\n")

    f.write("overliers in " + corpus + ":\n")
    for j in outliers[1]:
        f.write(j + "\n")

    f.write("\n")
    f.close()
