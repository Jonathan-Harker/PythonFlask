from flask import Flask, render_template
import requests
import json

application = Flask(__name__)

@application.route("/")
def results():
    url = "https://reqres.in/api/users?page=" + "1"
    ppl = []
    
    data = multiResults(url, ppl)
    
    ppl = data[0]
    while data[2] > data[1]:
        url = "https://reqres.in/api/users?page=" + str(data[1] + 1)
        data = multiResults(url, ppl)

    ppl = data[0]
    return render_template('people.html', ppl=ppl)

def multiResults(url, ppl):

    r = requests.get(url)
    msg = r.text

    x = json.loads(msg)

    pages = int(x["total_pages"])
    thisPage = int(x["page"])
    
    for key in x['data']:
        av = (str(key["avatar"]))
        thisId = (str(key["id"]))
        email = (str(key["email"]))
        fname = (str(key["first_name"]))
        lname = (str(key["last_name"]))
        ppl2 = [thisId, av, email, fname + " " + lname]
        ppl.append(ppl2)

    data = [ppl, thisPage, pages]
    return data

if __name__ == "__main__":
    application.run()