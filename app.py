from flask import Flask, render_template, jsonify
import json
import requests
import os

app = Flask(__name__)


def get_threads(board):
    search = "YGYL"
    fields = ["sub", "com"]
    found = []

    resp = requests.get("https://a.4cdn.org/"+board+"/catalog.json").json()
    for page in resp:
        for thread in page['threads']:
            for field in fields:
                if field in thread and search in thread[field]:
                    found.append(thread)
                    break

    return found

@app.route('/')
def homepage():
    ## GET THREADS

    wsg = get_threads("wsg")
    gif = get_threads("gif")


    return render_template("index.html", threads = {"wsg":wsg, "gif":gif})



@app.route("/play/<board>/<thread>")
def play_page(board, thread):
    resp = requests.get("https://a.4cdn.org/"+board+"/thread/"+thread+".json").json()
    posts = [post for post in resp['posts'] if 'ext' in post and post['ext'] == '.webm']

    return render_template("play.html", posts=json.dumps(posts), board=board, thread=thread)



if __name__ == '__main__':
    print("starting app")
    app.run(port=os.environ.get("PORT", 6969), debug=True)