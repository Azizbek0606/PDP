from flask import Flask, jsonify, request
from flask_cors import CORS
from collections import OrderedDict
import json

app = Flask(__name__)
CORS(app)

with open("data.json", "r") as file:
    data = json.load(file)


@app.route("/students", methods=["GET"])
def get_all_students():
    ordered_data = OrderedDict()
    for key in sorted(data.keys()):
        ordered_data[key] = OrderedDict(sorted(data[key].items()))
    return jsonify(ordered_data)


def check_data(id, course, data):
    course_data = data.get(course.lower())
    if not course_data:
        return "course not found"

    if id in course_data:
        return "id found"

    return "id not found"


def prepare_data_save(name, age, id, city, street, gender, course, region, house):
    data_status = check_data(id, course, data)

    if data_status == "id found":
        print("id bor")
        return jsonify({"message": f"{id} Id ga ega o'quvchi allaqachon mavjud!"}), 200

    elif data_status == "course not found":
        print("kurs topilishida muammo")
        return jsonify({"message": f"{course} turdagi kurs mavjud emas!"}), 404

    new_data = {
        id: {
            "name": name,
            "age": age,
            "gender": gender,
            "city": city,
            "region": region,
            "street": street,
            "house": house,
        }
    }

    if course.lower() in data:
        data[course.lower()].update(new_data)
    else:
        data[course.lower()] = new_data

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("muvofaqqiyatli yakunlandi")
    return jsonify({"message": f"{id} Id ga ega o'quvchi muvofaqqiyatli qo'shildi!"}), 201


@app.route("/add_student", methods=["POST"])
def add_student():
    request_data = request.json
    required_keys = [
        "name",
        "age",
        "id",
        "city",
        "street",
        "gender",
        "course",
        "region",
        "house",
    ]

    if not all(key in request_data for key in required_keys):
        print("malumot to'liq emas")
        return jsonify({"message": "Ma'lumot to'liq emas!"}), 400

    return prepare_data_save(
        request_data["name"],
        request_data["age"],
        request_data["id"],
        request_data["city"],
        request_data["street"],
        request_data["gender"],
        request_data["course"],
        request_data["region"],
        request_data["house"],
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
