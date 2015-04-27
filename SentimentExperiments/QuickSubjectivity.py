from pattern.en import sentiment
import os
import matplotlib.pyplot as plt

def sentimentSummary(folder):
    sentiments = []
    subjectivity = []
    files = [x for x in os.listdir(folder) if "txt" in x]
    for f in files:
        lines = [x.strip() for x in open(folder+'/'+f).readlines()]
        for l in lines:
            sent = sentiment(l)
#             print l, sent
            sentiments.append(sent[0])
            subjectivity.append(sent[1])
    print len(sentiments)
    print len(subjectivity)
    
#     plt.hist(sentiments, 20)
    plt.hist(subjectivity, 20)
#     plt.bar(left, height, width, bottom, hold)
    plt.show()
            

if __name__ == '__main__':
    sentimentSummary("../extract-bitbucket/final/")