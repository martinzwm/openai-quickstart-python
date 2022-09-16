import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        baby = request.form["baby"]
        response = get_openai_output(baby)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def get_openai_output(baby):
    """ Returns the output of the OpenAI API. """
    return openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_prompt(baby),
        temperature=0.6,
    )


def generate_prompt(baby):
    return """Suggest three names for a baby who is an Alien in outer space.

baby: Harvard Professor
Names: Doyle Sagittarius, Chen Zoodiac, Mars Rajpurkar
baby: Brilliant
Names: Martian Einstein, Newton Saturn, Aquarius Tesla
baby: Basketball Player
Names: James Capricorn, Jordan Venus, Meteor Durant

baby: {}
Names:""".format(
        baby.capitalize()
    )