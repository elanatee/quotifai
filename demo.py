from clarifai.rest import ClarifaiApp

# tags = []

app = ClarifaiApp()
model = app.models.get('general-v1.3')

def getTag(url):
    tags = []
    url = url

    result = model.predict_by_url(url)
    result = result['outputs'][0]['data']['concepts']

    for each in result:
        tag = each['name']
        tags.append(str(tag))
    
    tag = tags[0]
    return tag