import urllib2,urllib,json,string,random
 
 
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

def cuentaVotos(votacion_id):
    response = urllib2.urlopen("http://php-egc.rhcloud.com/get_votes.php?votation_id="+votacion_id);
    dic = json.load(response)
    msg = dic['msg']
    if msg!=1:
        raise Exception("The response message is 0, the query was done incorrectly")
    votes = dic['votes']
    longitud = len(votes)
    return longitud
def id_generator(size=50, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__=='__main__':
    votacionId = "8080"
    longitudInicial = cuentaVotos(votacionId)
    voto = id_generator()
    vote(voto,votacionId)
    longitudFinal = cuentaVotos(votacionId)
    if longitudFinal!=longitudInicial+1:
        raise Exception("The vote was not kept properly")
    else:
        print "The vote was save properly"
