import requests
import csv
from requests.auth import HTTPBasicAuth

#list1 = []
r = requests.get('https://bitbucket.org/api/2.0/repositories/IIITSERC/ssad34/commit/3333e375b858650db7ce03137ace5a2f24821210/comments',auth=HTTPBasicAuth('*****', '*******'))
rreq = r.json()

# to get all the comments in this particular commit :
#for item in rreq['values']
#list1.append(str(item['content']['raw'].encode('utf-8')))
#list1.append(str(['values'][0]['content']['raw'].encode('utf-8')))

with open('resultq.csv', 'ab') as csvfile:
   ac = csv.writer(csvfile,delimiter=" ")
   for item in rreq['values']:
       ac.writerow([str(item['content']['raw'].encode('utf-8'))])
