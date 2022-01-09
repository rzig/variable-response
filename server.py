from flask import Flask, request, json
from time import sleep
from platform import node

app = Flask(__name__)

db = {"delay": 0}
name = node()

@app.route("/")
def index():
    sleep(db['delay'] / 1000)
    return app.response_class(
        response=json.dumps({"host": name, "delay": db['delay']}),
        status=200,
        mimetype="application/json"
    )

@app.route("/update")
def update():
    name_for_delay = request.args.get("name")
    new_delay = int(request.args.get("delay"))
    if name == name_for_delay:
        db['delay'] = new_delay
        return app.response_class(
            response=json.dumps({"host": name, "updated": True}),
            status=200,
            mimetype="application/json"
        )
    else:
        return app.response_class(
            response=json.dumps({"host": name, "updated": False}),
            status=200,
            mimetype="application/json"
        )

app.run(port=3001)