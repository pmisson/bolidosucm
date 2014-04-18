# IPython log file
import numpy as np
import flickrapi
import json
import datetime
t=datetime.datetime.now()
y=datetime.datetime.fromordinal((t.toordinal()-1)).strftime('%Y-%m-%d %H:%M:%S')
def get_flickr_photos(date=y):
    api_key = '31c572120176f492413eeec8a67cf5c6'
    flickr = flickrapi.FlickrAPI(api_key)
    api_secret = 'cc7dbc2d478587a8'
    flickr = flickrapi.FlickrAPI(api_key, api_secret)
    (token, frob) = flickr.get_token_part_one(perms='write')
    if not token: 
        raw_input("Press ENTER after you authorized this program")
        flickr.get_token_part_two((token, frob))
        print flickr.get_token_part_two((token, frob))

    import json
    url=flickr.urls_getUserPhotos(user='65933735@N00',format='json')
    urlG=json.loads(url[14:-1])
    urlG=urlG['user']['url']
    datos=flickr.photos_search(user_id='65933735@N00',format='json',min_upload_date=date)
    datosP=json.loads(datos[14:-1])

    m=[]
    b=[]
    l=[]
    q=[]
    t=[]
    photos=[]
    n=len(datosP['photos']['photo'])
    for x in range(n):
        m.append('https://farm'+str(datosP['photos']['photo'][x]['farm'])+'.staticflickr.com/'+datosP['photos']['photo'][x]['server']+'/'+datosP['photos']['photo'][x]['id']+'_'+datosP['photos']['photo'][x]['secret']+'_m.jpg')
        q.append('Can you see a meteor?')
        b.append('https://farm'+str(datosP['photos']['photo'][x]['farm'])+'.staticflickr.com/'+datosP['photos']['photo'][x]['server']+'/'+datosP['photos']['photo'][x]['id']+'_'+datosP['photos']['photo'][x]['secret']+'_b.jpg')
        l.append(urlG+datosP['photos']['photo'][x]['id'])
        t.append(datosP['photos']['photo'][x]['title'])
        
    data = np.zeros((n,),dtype=[('Link','a100'),('question','a100'), ('Url_m','a100'), ('Url_b', 'a100'),('Title', 'a100')])
    data['Link']=np.array(l)
    data['question']=np.array(q)
    data['Url_m']=np.array(m)
    data['Url_b']=np.array(b)
    data['Title']=np.array(t)
    
    for x in range(n):
        link = data[x]['Link']
        imgTitle = data[x]['Title']
        imgUrl_m = data[x]['Url_m']
        imgUrl_b = data[x]['Url_b']
        photos.append({'link': link, 'url_m':  imgUrl_m,
                       'url_b': imgUrl_b,'title': imgTitle})
    return photos
