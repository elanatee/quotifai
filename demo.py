from clarifai.rest import ClarifaiApp

taglist = []

app = ClarifaiApp()
model = app.models.get('general-v1.3')

def getTag(url):

    url = url

    result = model.predict_by_url(url)
    tags = result['outputs'][0]['data']['concepts']

    for each in tags:
        tag = each['name']
        taglist.append(str(tag))

    tag = taglist[0]
    return tag