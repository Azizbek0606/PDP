# from flask import Flask, jsonify

# app = Flask(__name__)
product = {
    "html": {"price": 15000, "name": "html", "to_who": ["Front end"], "quantity": 7},
    "css": {
        "price": 7000,
        "name": "css",
        "to_who": ["Front end", "Back end"],
        "quantity": 3,
    },
    "js": {"price": 27000, "name": "js", "to_who": ["Front end"], "quantity": 8},
    "python": {"price": 34000, "name": "python", "to_who": ["Back end"], "quantity": 5},
    "django": {"price": 35000, "name": "django", "to_who": ["Back end"], "quantity": 9},
    "dart": {"price": 27000, "name": "dart", "to_who": ["Mobile dev"], "quantity": 6},
    "postgres": {
        "price": 5000,
        "name": "postgres",
        "to_who": ["Back end"],
        "quantity": 4,
    },
    "figma": {"price": 8000, "name": "figma", "to_who": ["Designer"], "quantity": 10},
    "sketch": {
        "price": 9000,
        "name": "sketch",
        "to_who": ["Designer", "UI/IX"],
        "quantity": 2,
    },
    "adobe_xd": {
        "price": 7000,
        "name": "adobe_xd",
        "to_who": ["Designer", "UI/IX"],
        "quantity": 8,
    },
    "photoshop": {
        "price": 10000,
        "name": "photoshop",
        "to_who": ["Designer"],
        "quantity": 1,
    },
    "illustrator": {
        "price": 9500,
        "name": "illustrator",
        "to_who": ["Designer", "Back end"],
        "quantity": 7,
    },
    "invision": {
        "price": 5000,
        "name": "invision",
        "to_who": ["Designer", "UI/IX"],
        "quantity": 3,
    },
    "zeplin": {
        "price": 4800,
        "name": "zeplin",
        "to_who": ["Designer", "UI/IX"],
        "quantity": 5,
    },
    "balsamiq": {
        "price": 5300,
        "name": "balsamiq",
        "to_who": ["Designer", "Back end"],
        "quantity": 6,
    },
    "axure": {"price": 5500, "name": "axure", "to_who": ["Designer"], "quantity": 4},
    "affinity_designer": {
        "price": 8700,
        "name": "affinity_designer",
        "to_who": ["Designer", "UI/IX", "Back end"],
        "quantity": 9,
    },
    "protopie": {"price": 6200, "name": "protopie", "to_who": ["UI/IX"], "quantity": 2},
    "marvel": {
        "price": 4600,
        "name": "marvel",
        "to_who": ["Designer", "Back end"],
        "quantity": 7,
    },
    "framer": {
        "price": 6800,
        "name": "framer",
        "to_who": ["Front end", "UI/IX"],
        "quantity": 8,
    },
    "origami_studio": {
        "price": 5000,
        "name": "origami_studio",
        "to_who": ["Designer", "UI/IX", "Back end"],
        "quantity": 6,
    },
    "uxpin": {"price": 7300, "name": "uxpin", "to_who": ["UI/IX"], "quantity": 4},
    "mockplus": {
        "price": 4900,
        "name": "mockplus",
        "to_who": ["Designer"],
        "quantity": 3,
    },
    "swift": {"price": 30000, "name": "swift", "to_who": ["Mobile dev"], "quantity": 5},
    "kotlin": {
        "price": 29000,
        "name": "kotlin",
        "to_who": ["Mobile dev"],
        "quantity": 7,
    },
    "flutter": {
        "price": 31000,
        "name": "flutter",
        "to_who": ["Mobile dev"],
        "quantity": 9,
    },
    "react_native": {
        "price": 27000,
        "name": "react_native",
        "to_who": ["Mobile dev"],
        "quantity": 2,
    },
    "azure": {
        "price": 25000,
        "name": "azure",
        "to_who": ["Back end", "QI"],
        "quantity": 8,
    },
    "aws": {"price": 23000, "name": "aws", "to_who": ["Back end", "QI"], "quantity": 6},
    "docker": {"price": 20000, "name": "docker", "to_who": ["Back end"], "quantity": 3},
    "kubernetes": {
        "price": 22000,
        "name": "kubernetes",
        "to_who": ["Back end", "QI"],
        "quantity": 7,
    },
    "scala": {"price": 31000, "name": "scala", "to_who": ["Back end"], "quantity": 4},
    "ruby_on_rails": {
        "price": 28000,
        "name": "ruby_on_rails",
        "to_who": ["Back end"],
        "quantity": 5,
    },
    "go": {"price": 33000, "name": "go", "to_who": ["Back end"], "quantity": 10},
    "angular": {
        "price": 26000,
        "name": "angular",
        "to_who": ["Front end"],
        "quantity": 1,
    },
    "vue": {"price": 24000, "name": "vue", "to_who": ["Front end"], "quantity": 2},
    "svelte": {
        "price": 19000,
        "name": "svelte",
        "to_who": ["Front end"],
        "quantity": 6,
    },
    "redux": {"price": 16000, "name": "redux", "to_who": ["Front end"], "quantity": 7},
    "node_js": {
        "price": 25000,
        "name": "node_js",
        "to_who": ["Back end"],
        "quantity": 9,
    },
    "express_js": {
        "price": 18000,
        "name": "express_js",
        "to_who": ["Back end"],
        "quantity": 4,
    },
}


# @app.route("/users", methods=["GET"])
# def get_users():
#     return jsonify(product)
# app.run(debug=True)
