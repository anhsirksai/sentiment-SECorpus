import requests
import csv
import json
from requests.auth import HTTPBasicAuth


class fetchcomments(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    #function to loop through repos and update the dictionary.
    def repoLoop(self,a,b):
        #dictionary of key : repoid, value : list of commits in a repo.
        dictcommitids = {}
        #loop thru repos and get the commit ids from raw_node.
        for i in range(a,b+1):
            listcommitids = []
            if i < 10 :
                commiturl = 'https://bitbucket.org/api/1.0/repositories/IIITSERC/ssad0' + str(i) + '/changesets?limit=50'
            else:
                commiturl = 'https://bitbucket.org/api/1.0/repositories/IIITSERC/ssad' + str(i) + '/changesets?limit=50'
            com = requests.get(commiturl, auth=HTTPBasicAuth('*******','*******'))
            commitids=json.loads(com.text)
            #store the commit ids in list.
            for ite in commitids['changesets']:
                listcommitids.append(str(ite['raw_node'].encode('utf-8')))
            #dictkey value gets overridden every time.
            if i < 10 :
                dictkey = 'ssad0' + str(i)
            else:
                dictkey = 'ssad' + str(i)
            #save the reponame as key and list of commidids as value.
            # It is creating a problem here. It is updating 1st key's values to all the other keys.
            dictcommitids[dictkey] = listcommitids
            #dictcommitids.update({dictkey:listcommitids})
            #raw_input("press to continue..")
        with open('commiturls.json', 'a') as jsonfile:
            json.dump(dictcommitids,jsonfile)

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

    #Function to fetch comments from all the commit ids.
    def fetchcomm(self):
        dictnew = {}
        with open('commiturls.json','r') as data_file:
            dictnew = json.load(data_file)
        #for key1,value1 in dictcommitids.iteritems():
        for key1,value1 in dictnew.items():
            commenturl = 'https://bitbucket.org/api/2.0/repositories/IIITSERC/' + str(key1) + '/commit/'
            for value in value1:
                commenturl1 = None
                commenturl1 = commenturl + str(value) + '/comments'
                result = ''
                result = requests.get(commenturl1,auth=HTTPBasicAuth('**********','*****************'))
                comments = ''
                #comments=json.loads(result.text)
                comments = result.json()
                filename = 'result' + str(key1) + '.txt'
                #print str(comments['values'][2]['content']['raw'].encode('utf-8'))
                with open(filename, 'a') as data_json:
                    for item in comments['values']:
                        ac += str(item['content']['raw'].encode('utf-8'))
                        ac += '\n'
                        data_json.write(ac)

thing = fetchcomments()
#thing.repoLoop(1,2)
thing.repoLoop(1,32)
thing.repoLoop(34,39)
thing.repoLoop(41,48)
thing.fetchcomm()
