import requests
import csv
import json
from requests.auth import HTTPBasicAuth


class fetchcomments(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    #function to loop through repos and update the dictionary.

    commiturl = ''
    listcommitids = []
    def repoLoop(self,a,b):
        #dictionary of key : repoid, value : list of commits in a repo.
        dictcommitids = {}
        #loop thru repos and get the commit ids from raw_node.
        for i in range(a,b+1):
            global listcommitids
            global commiturl
            listcommitids = []
            if i < 10 :
                commiturl = 'https://bitbucket.org/api/2.0/repositories/IIITSERC/ssad0' + str(i) + '/commits/master?page=1'
                #commiturl = 'https://bitbucket.org/api/1.0/repositories/IIITSERC/ssad0' + str(i) + '/changesets?limit=50'
                print commiturl
            else:
                commiturl = 'https://bitbucket.org/api/2.0/repositories/IIITSERC/ssad' + str(i) + '/commits/master?page=1'
                #commiturl = 'https://bitbucket.org/api/1.0/repositories/IIITSERC/ssad' + str(i) + '/changesets?limit=50'
                print commiturl
            def selfcall(stvar):
                print "saikrishna...."
                global listcommitids
                com = requests.get(stvar, auth=HTTPBasicAuth('IIITSERC','SercSsad4567'))
                commitids=json.loads(com.text)
                for ite in commitids['values']:
                    #print str(ite['links']['comments']['href'])
                    listcommitids.append(str(ite['links']['comments']['href']))
                if commitids.has_key('next'):
                    print "url ....."
                    print str(commitids['next'])
                    raw_input("press to continue..")
                    selfcall(str(commitids['next']))

            selfcall(commiturl)
            if i < 10 :
                dictkey = 'ssad0' + str(i)
            else:
                dictkey = 'ssad' + str(i)
            dictcommitids.update({dictkey:listcommitids})
    
        with open('commiturls.txt', 'a') as data_json:
                    for item,val in dictcommitids.iteritems():

        with open('commiturls.json', 'a') as jsonfile:
            json.dump(dictcommitids,jsonfile)
        print dictcommitids
        raw_input("press to continue..")

    def fetchcomm(self):
        dictnew = {}
        with open('comiturls3.json','r') as data_file:
            dictnew = json.load(data_file)
            #for key, val in csv.reader(data_file):
            #    dictnew[key] = val
            #print dictnew
        #with open('commiturls.json') as data_file:
        #    dictnew = json.loads(data_file)
        #for key1,value1 in dictcommitids.iteritems():
        for key1,value1 in dictnew.items():
            commenturl = 'https://bitbucket.org/api/2.0/repositories/IIITSERC/' + str(key1) + '/commit/'
            for value in value1:
                commenturl1 = None
                commenturl1 = commenturl + str(value) + '/comments'
                print commenturl1
                result = ''
                result = requests.get(commenturl1,auth=HTTPBasicAuth('*******','******'))
                comments = ''
                #comments=json.loads(result.text)
                comments = result.json()
                print comments
                print "blah ...."
                #filename gets overridden everytime.
                filename = 'result' + str(key1) + '.txt'
                #print str(comments['values'][2]['content']['raw'].encode('utf-8'))
                with open(filename, 'a') as data_json:
                    for item in comments['values']:
                        print str(item['content']['raw'].encode('utf-8'))
                        ac = str(item['content']['raw'].encode('utf-8')) + "\n"
                        data_json.write(ac)


       
thing = fetchcomments()
thing.repoLoop(1,3)

#'https://bitbucket.org/api/2.0/repositories/IIITSERC/ssad34/commits/master?page=1'

