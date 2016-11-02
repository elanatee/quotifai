from clarifai.rest import ClarifaiApp

taglist = []

app = ClarifaiApp()
model = app.models.get('general-v1.3')

url = 'https://scontent-iad3-1.xx.fbcdn.net/t31.0-8/10459089_10204304373393316_6832105293440929868_o.jpg'

result = model.predict_by_url(url)
tags = result['outputs'][0]['data']['concepts']

for each in tags:
    # print each['name']
    tag = each['name']
    taglist.append(str(tag))

# print taglist
tag = taglist[0]