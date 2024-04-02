from flask import Flask, jsonify

app = Flask(__name__)
product = {
    "html": {"price": 15000, "name": "html", "to_who": ["front end"]},
    "css": {"price": 7000, "name": "css", "to_who": ["front end"]},
    "js": {"price": 27000, "name": "js", "to_who": ["front end"]},
    "python": {"price": 34000, "name": "python", "to_who": ["back end"]},
    "django": {"price": 35000, "name": "django", "to_who": ["back end"]},
    "dart": {"price": 27000, "name": "dart", "to_who": ["back end"]},
    "postgres": {"price": 5000, "name": "postgres", "to_who": ["front end"]},
    "figma": {"price": 8000, "name": "figma", "to_who": ["designer"]},
    "sketch": {"price": 9000, "name": "sketch", "to_who": ["designer", "ui/ux"]},
    "adobe_xd": {"price": 7000, "name": "adobe_xd", "to_who": ["designer", "ui/ux"]},
    "photoshop": {"price": 10000, "name": "photoshop", "to_who": ["designer"]},
    "illustrator": {
        "price": 9500,
        "name": "illustrator",
        "to_who": ["designer"],
    },
    "invision": {"price": 5000, "name": "invision", "to_who": ["front end", "ui/ux"]},
    "zeplin": {"price": 4800, "name": "zeplin", "to_who": ["designer", "ui/ux"]},
    "balsamiq": {"price": 5300, "name": "balsamiq", "to_who": ["designer", "back end"]},
    "axure": {"price": 5500, "name": "axure", "to_who": ["designer"]},
    "affinity_designer": {
        "price": 8700,
        "name": "affinity_designer",
        "to_who": ["designer", "ui/ux"],
    },
    "protopie": {"price": 6200, "name": "protopie", "to_who": ["ui/ux"]},
    "marvel": {"price": 4600, "name": "marvel", "to_who": ["designer", "back end"]},
    "framer": {"price": 6800, "name": "framer", "to_who": ["front end", "ui/ux"]},
    "origami_studio": {
        "price": 5000,
        "name": "origami_studio",
        "to_who": ["designer", "ui/ux"],
    },
    "uxpin": {"price": 7300, "name": "uxpin", "to_who": ["ui/ux"]},
    "mockplus": {"price": 4900, "name": "mockplus", "to_who": ["designer"]},
}


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(product)
app.run(debug=True)

