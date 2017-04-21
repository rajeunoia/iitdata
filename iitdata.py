import requests
import json
from os import listdir
print(listdir('.\images'))
filenames=listdir('.\images')
f = open('userdetails.xls','w+')
f.write('ÍD'+'\t'+'Name' +'\t'+'Teamid' +'\t'+'Phone' +'\t'+'Email' +'\t'+'CFID' +'\t'+ 'Price'+'\n' );
for filename in filenames:
    print(filename)
    url = 'https://api.qrserver.com/v1/read-qr-code/?fileurl='
    #url = url+'http%3A%2F%2Ftechfest.org%2Fimg%2Fhospi%2Fusers%2F98485.jpg'
    url = url+'http%3A%2F%2Ftechfest.org%2Fimg%2Fhospi%2Fusers%2F'+filename
    print(url)
    data = ''
    response = requests.post(url, data=data)
    # if response code is 200
    jsontxt = response.json()
    #print(response.json())
    print(jsontxt)
    print(jsontxt[0]['symbol'][0]['data'])
    qrurl = jsontxt[0]['symbol'][0]['data']
    responseqr = requests.get(qrurl, data=data)
    jsontxt = responseqr.json()
    
    f.write(str(jsontxt[0]['id'])+'\t'+jsontxt[0]['name'] +'\t'+jsontxt[0]['teamid'] +'\t'+jsontxt[0]['phone'] +'\t'+jsontxt[0]['email'] +'\t'+jsontxt[0]['cfid'] +'\t'+ str(jsontxt[0]['price'])+'\n' );
    print(responseqr.json())
    print('id  -  '+str(jsontxt[0]['id']))
    print('Name  -  '+jsontxt[0]['name'])
    print('teamid  -  '+jsontxt[0]['teamid'])
    print('phone  -  '+jsontxt[0]['phone'])
    print('email  -  '+jsontxt[0]['email'])
    print('cfid  -  '+jsontxt[0]['cfid'])
    print('price  -  '+str(jsontxt[0]['price']))
f.close();