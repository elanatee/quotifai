from clarifai.rest import ClarifaiApp

app = ClarifaiApp()
model = app.models.get('general-v1.3') # use Clarifai's general model

def getTag(url):
    '''
    parameters: 
    -----------
        url : str
            an image address
    returns:
    --------
        tags : list of str
            list of tags associated with image
    '''
    tags = []

    result = model.predict_by_url(url)
    result = result['outputs'][0]['data']['concepts'] 

    for each in result:
        tag = each['name']
        tags.append(str(tag))

    return tags