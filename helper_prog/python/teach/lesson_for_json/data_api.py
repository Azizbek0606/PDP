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


@app.route("/add_student", methods=["POST"])
def add_student():
    try:
        new_student_data = request.get_json()

        if new_student_data != None:
            s_name = new_student_data.get("name")
            s_age = new_student_data.get("age")
            s_id = new_student_data.get("id")
            s_city = new_student_data.get("city")
            s_street = new_student_data.get("street")
            s_gender = new_student_data.get("gender")
            s_course = new_student_data.get("course")
            s_region = new_student_data.get("region")
            s_house = new_student_data.get("houes")
        else:
            return jsonify({"message": "Ha mazgi bizi lo'x deb o'ylaydi bular \nqani malumot !!!"}), 201

        # if not student_id or not student_info:
        #     return jsonify({"error": "student_id va student_info kerak"}), 400

        # data[student_id] = student_info

        # with open("data.json", "w") as file:
        #     json.dump(data, file, indent=4)

        return jsonify({"message": "Talaba muvaffaqiyatli qo'shildi"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
