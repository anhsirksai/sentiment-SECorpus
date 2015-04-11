import requests
import csv
from requests.auth import HTTPBasicAuth

#dictionary of key : repoid, value : list of commits in a repo.
dictcommitids = {}
dictvaluecommitids = []

#loop thru repos and get the commit ids.
for i in range(10,48):
    commiturl = None
    commiturl = 'https://bitbucket.org/api/1.0/repositories/IIITSERC/ssad' + str(i) + '/changesets/'
    com = requests.get(commiturl, auth=HTTPBasicAuth('********','******'))
    commitids=json.loads(com.text)
    for ite in commitids['changesets']:
        dictvaluecommitids.append(str(ite['raw_node'].encode('utf-8')))
    dictkey = 'ssad' + str(i)
    dictcommitids.update({dictkey : dictvaluecommitids})

#print values of dictionaries:
#for key1,value1 in dictcommitids.iteritems():
#    print key1, "blah...", value1, "\n"
#r = requests.get('https://bitbucket.org/api/2.0/repositories/IIITSERC/ssad34/commit/3333e375b858650db7ce03137ace5a2f24821210/comments',auth=HTTPBasicAuth('*****', '*******'))
#rreq = r.json()

# to get all the comments in this particular commit :
#for item in rreq['values']
#list1.append(str(item['content']['raw'].encode('utf-8')))
#list1.append(str(['values'][0]['content']['raw'].encode('utf-8')))

#loop thru the dictionary of commitids
#    Get the comment from each of the commitid and store it into a csv file.
for key1,value1 in dictcommitids.iteritems():
    commenturl = None
    commenturl = 'https://bitbucket.org/api/2.0/repositories/IIITSERC/' + str(key1) + '/commit/'
    for value in value1:
        commenturl1 = commentturl
        commenturl1 += str(value) + '/comments'
        r1 = requests.get(commenturl1,auth=HTTPBasicAuth('********','**********'))
        comments=json.loads(r1.text)
        with open('resultq.csv', 'ab') as csvfile:
            ac = csv.writer(csvfile,delimiter=" ")
            for item in comments['values']:
                ac.writerow([str(item['content']['raw'].encode('utf-8'))])
