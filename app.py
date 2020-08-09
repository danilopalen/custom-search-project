import json
import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # file that creates flask app

@app.route('/', methods= ['GET','POST']) # route for base url

def home(): 
    subscriptionKey = "5748d72d720d42f8a2c0cfbc1cb75697"
    customConfigId = "5bc5c02b-e917-4f56-ba7c-9ce7b513cbdf"

    webpages = []

    if request.method == 'POST':
        user_input = request.form['input']

        searchTerm = user_input

        url = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?' + 'q=' + searchTerm + '&' + 'customconfig=' + customConfigId

        r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
        res = r.json()

        if 'webpages' in res:
            webpages = res['webPages']['value']
            
        print(json.dumps(res, indent=4))
            
    return render_template('index.html', webpages = webpages)


if __name__ == '__main__':
    app.run(debug=True)