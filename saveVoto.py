import urllib2,urllib,json
 
 
def vote(voto,votacion_id):
    data=[('vote',voto),('votation_id',votacion_id)]
    data=urllib.urlencode(data)
    path='http://php-egc.rhcloud.com/vote.php'
    req=urllib2.Request(path,data)
    response=urllib2.urlopen(req)
    response_data = json.load(response)
    result = False
    if response_data['msg']==u'1':
        result=True
    return result
