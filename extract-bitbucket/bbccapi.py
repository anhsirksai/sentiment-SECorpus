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
        listcommitids = []
        zz = 0
        #loop thru repos and get the commit ids from raw_node.
        for i in range(a,b+1):
            if i < 10 :
                commiturl = 'https://bitbucket.org/api/1.0/repositories/IIITSERC/ssad0' + str(i) + '/changesets/'
                print commiturl
            else:
                commiturl = 'https://bitbucket.org/api/1.0/repositories/IIITSERC/ssad' + str(i) + '/changesets/'
                print commiturl
            com = requests.get(commiturl, auth=HTTPBasicAuth('IIITSERC','SercSsad4567'))
            commitids=json.loads(com.text)
            #store the commit ids in list.
            print str(commitids['changesets'][0]['raw_node'].encode('utf-8'))
            if listcommitids:
                listcommitids[:] = []
            for ite in commitids['changesets']:
                listcommitids.append(str(ite['raw_node'].encode('utf-8')))
            #print listcommitids
            #dictkey value gets overridden every time.
            if i < 10 :
                dictkey = 'ssad0' + str(i)
            else:
                dictkey = 'ssad' + str(i)
            with open('commiturls.csv', 'a') as csvfile:
                w = csv.writer(csvfile)
                print listcommitids
                zz += 1
                yy = 'sai'+ str(zz)
                print yy
                w.writerow([dictkey, listcommitids])
            #save the reponame as key and list of commidids as value.
            # It is creating a problem here. It is updating 1st key's values to all the other keys.
            #dictcommitids[dictkey].append(listcommitids)
            #dictcommitids.update({dictkey:listcommitids})
            #print dictcommitids
            #update the commitids list after each iteration.
        #open a file, save the dictionary. Y do I need a json file here?
        #with open('commiturls.csv', 'a') as csvfile:
        #    w = csv.writer(csvfile)
        #    print dictcommitids
        #    for key, val in dictcommitids.items():
        #        w.writerow([key, val])
        #empty the dictionary to avoid duplicates in file.
        #dictcommitids.clear()


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
        with open('commiturls.csv','r') as data_file:
            for key, val in csv.reader(data_file):
                dictnew[key] = val
        #with open('commiturls.json') as data_file:
        #    dictnew = json.loads(data_file)
        #for key1,value1 in dictcommitids.iteritems():
        for key1,value1 in dictnew.items():
            commenturl = 'https://bitbucket.org/api/2.0/repositories/IIITSERC/' + str(key1) + '/commit/'
            for value in value1:
                commenturl1 = None
                commenturl1 = commenturl + str(value) + '/comments'
                print commenturl1
                break
                result = requests.get(commenturl1,auth=HTTPBasicAuth('IIITSERC','SercSsad4567'))
                comments=json.loads(result.text)
                #filename gets overridden everytime.
                filename = 'result' + str(key1) + '.csv'
                print str(comments['values'][0]['content']['raw'].encode('utf-8'))
                with open(filename, 'a') as csvfile:
                    ac = csv.writer(csvfile)
                    for item in comments['values']:
                        ac.writerow([str(item['content']['raw'].encode('utf-8'))])

thing = fetchcomments()
#thing.repoLoop(1,2)
#thing.repoLoop(1,32)
#thing.repoLoop(34,39)
#thing.repoLoop(41,48)
thing.fetchcomm()
