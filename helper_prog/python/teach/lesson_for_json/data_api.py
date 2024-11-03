from flask import Flask, jsonify, request
from flask_cors import CORS
from collections import OrderedDict

app = Flask(__name__)
CORS(app)

data = {
    "first_course": {
        "240230": {
            "name": "Anvar",
            "age": 18,
            "gender": "male",
            "city": "Andijon",
            "region": "Asaka",
            "street": "Saxiylik",
            "house": 14,
        },
        "240231": {
            "name": "Sardor",
            "age": 19,
            "gender": "male",
            "city": "Buxoro",
            "region": "Navoiy",
            "street": "Yetti chinor",
            "house": 177,
        },
    },
    "second_course": {
        "230757": {
            "name": "Azizbek",
            "age": 18,
            "gender": "male",
            "city": "Andijon",
            "region": "Asaka",
            "street": "Saxiylik",
            "house": 6,
        },
        "230786": {
            "name": "Dilshod",
            "age": 18,
            "gender": "male",
            "city": "Surxondaryo",
            "region": "Bo'taqara",
            "street": "Tanga topdi",
            "house": 61,
        },
        "240230": {
            "name": "Anvar",
            "age": 18,
            "gender": "male",
            "city": "Andijon",
            "region": "Asaka",
            "street": "Saxiylik",
            "house": 14,
        },
        "240231": {
            "name": "Sardor",
            "age": 19,
            "gender": "male",
            "city": "Buxoro",
            "region": "Navoiy",
            "street": "Yetti chinor",
            "house": 177,
        },
    },
    "third_course": {
        "230345": {
            "name": "Saydullox",
            "age": 19,
            "gender": "male",
            "city": "Andijon",
            "region": "Asaka",
            "street": "Farg'ona Ko'cha",
            "house": 45,
        },
        "220231": {
            "name": "Shaxriyor",
            "age": 19,
            "gender": "male",
            "city": "Surxondaryo",
            "region": "Kulla",
            "street": "Ozodlik",
            "house": 72,
        },
    },
    "fourth_course": {
        "230345": {
            "name": "Saydullox",
            "age": 19,
            "gender": "male",
            "city": "Andijon",
            "region": "Asaka",
            "street": "Farg'ona Ko'cha",
            "house": 45,
        },
        "220231": {
            "name": "Shaxriyor",
            "age": 19,
            "gender": "male",
            "city": "Surxondaryo",
            "region": "Kulla",
            "street": "Ozodlik",
            "house": 72,
        },
        "240230": {
            "name": "Anvar",
            "age": 18,
            "gender": "male",
            "city": "Andijon",
            "region": "Asaka",
            "street": "Saxiylik",
            "house": 14,
        },
        "240231": {
            "name": "Sardor",
            "age": 19,
            "gender": "male",
            "city": "Buxoro",
            "region": "Navoiy",
            "street": "Yetti chinor",
            "house": 177,
        },
    },
    "school_1": {
        "230345": {
            "name": "Alibek",
            "age": 19,
            "gender": "male",
            "city": "Andijon",
            "region": "Asaka",
            "street": "Farg'ona Ko'cha",
            "house": 45,
        },
        "220231": {
            "name": "Shaxriyor",
            "age": 19,
            "gender": "male",
            "city": "Surxondaryo",
            "region": "Kulla",
            "street": "Ozodlik",
            "house": 72,
        },
    },
    "school_2": {
        "230345": {
            "name": "Alibek",
            "age": 19,
            "gender": "male",
            "city": "Andijon",
            "region": "Asaka",
            "street": "Farg'ona Ko'cha",
            "house": 45,
        },
        "220231": {
            "name": "Shaxriyor",
            "age": 19,
            "gender": "male",
            "city": "Surxondaryo",
            "region": "Kulla",
            "street": "Ozodlik",
            "house": 72,
        },
    },
}


@app.route("/students", methods=["GET"])
def get_all_students():
    ordered_data = OrderedDict()
    for key in sorted(data.keys()):
        ordered_data[key] = OrderedDict(sorted(data[key].items()))
    return jsonify(ordered_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
