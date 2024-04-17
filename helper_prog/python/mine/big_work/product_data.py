# from flask import Flask, jsonify

# app = Flask(__name__)
product = {
    "html": {"price": 15000, "name": "html", "to_who": ["Front end"]},
    "css": {"price": 7000, "name": "css", "to_who": ["Front end", "Back end"]},
    "js": {"price": 27000, "name": "js", "to_who": ["Front end"]},
    "python": {"price": 34000, "name": "python", "to_who": ["Back end"]},
    "django": {"price": 35000, "name": "django", "to_who": ["Back end"]},
    "dart": {"price": 27000, "name": "dart", "to_who": ["Mobile dev"]},
    "postgres": {"price": 5000, "name": "postgres", "to_who": ["Back end"]},
    "figma": {"price": 8000, "name": "figma", "to_who": ["Designer"]},
    "sketch": {"price": 9000, "name": "sketch", "to_who": ["Designer", "UI/IX"]},
    "adobe_xd": {"price": 7000, "name": "adobe_xd", "to_who": ["Designer", "UI/IX"]},
    "photoshop": {"price": 10000, "name": "photoshop", "to_who": ["Designer"]},
    "illustrator": {
        "price": 9500,
        "name": "illustrator",
        "to_who": ["Designer", "Back end"],
    },
    "invision": {"price": 5000, "name": "invision", "to_who": ["Designer", "UI/IX"]},
    "zeplin": {"price": 4800, "name": "zeplin", "to_who": ["Designer", "UI/IX"]},
    "balsamiq": {"price": 5300, "name": "balsamiq", "to_who": ["Designer", "Back end"]},
    "axure": {"price": 5500, "name": "axure", "to_who": ["Designer"]},
    "affinity_designer": {
        "price": 8700,
        "name": "affinity_designer",
        "to_who": ["Designer", "UI/IX", "Back end"],
    },
    "protopie": {"price": 6200, "name": "protopie", "to_who": ["UI/IX"]},
    "marvel": {"price": 4600, "name": "marvel", "to_who": ["Designer", "Back end"]},
    "framer": {"price": 6800, "name": "framer", "to_who": ["Front end", "UI/IX"]},
    "origami_studio": {
        "price": 5000,
        "name": "origami_studio",
        "to_who": ["Designer", "UI/IX", "Back end"],
    },
    "uxpin": {"price": 7300, "name": "uxpin", "to_who": ["UI/IX"]},
    "mockplus": {"price": 4900, "name": "mockplus", "to_who": ["Designer"]},
    "swift": {"price": 30000, "name": "swift", "to_who": ["Mobile dev"]},
    "kotlin": {"price": 29000, "name": "kotlin", "to_who": ["Mobile dev"]},
    "flutter": {"price": 31000, "name": "flutter", "to_who": ["Mobile dev"]},
    "react_native": {"price": 27000, "name": "react_native", "to_who": ["Mobile dev"]},
    "azure": {"price": 25000, "name": "azure", "to_who": ["Back end", "QI"]},
    "aws": {"price": 23000, "name": "aws", "to_who": ["Back end", "QI"]},
    "docker": {"price": 20000, "name": "docker", "to_who": ["Back end"]},
    "kubernetes": {"price": 22000, "name": "kubernetes", "to_who": ["Back end", "QI"]},
    "scala": {"price": 31000, "name": "scala", "to_who": ["Back end"]},
    "ruby_on_rails": {"price": 28000, "name": "ruby_on_rails", "to_who": ["Back end"]},
    "go": {"price": 33000, "name": "go", "to_who": ["Back end"]},
    "angular": {"price": 26000, "name": "angular", "to_who": ["Front end"]},
    "vue": {"price": 24000, "name": "vue", "to_who": ["Front end"]},
    "svelte": {"price": 19000, "name": "svelte", "to_who": ["Front end"]},
    "redux": {"price": 16000, "name": "redux", "to_who": ["Front end"]},
    "node_js": {"price": 25000, "name": "node_js", "to_who": ["Back end"]},
    "express_js": {"price": 18000, "name": "express_js", "to_who": ["Back end"]},
}


# @app.route("/users", methods=["GET"])
# def get_users():
#     return jsonify(product)
# app.run(debug=True)
