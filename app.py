
""""This is driver code for running on server"""
import json
import os

from flask import Flask, request
from flask_cors import CORS

from get_angle import Angle
import static_html_string

app = Flask(__name__)# pylint: disable=invalid-name
CORS(app)


@app.route('/')
def home():
    """"This method display the HTML on home page on server"""
    html = static_html_string.HTML
    return html

@app.route("/angle.cal", methods=["GET"])
def get_angle():
    """"This is method a to get a input from userI.Inputs are:Hours and minutes"""
    hour = request.args.get('hour')
    minute = request.args.get('min')
    flag = validate_response(hour, minute)
    if flag["response"] == "Success":
        ihour = int(hour)
        fmin = float(minute)
        obj = Angle(hour=ihour, minute=fmin)
        result = obj.calculate_angle()
        return json.dumps(result)

    return json.dumps(flag)


def validate_response(hour, minute):
    """"This method validate the reponse of the input coming"""
    if hour is None or hour == "":
        return {"response": "No hour value"}
    if minute is None or minute == "":
        return {"response": "No Minute value"}
    return {"response": "Success"}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
