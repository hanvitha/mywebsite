from flask import Flask, render_template, request

from Experiences import experiences
from Skills import skills
from Blogs import blogs
from Projects import projects

__author__ = 'hanvitha'

app = Flask(__name__)
@app.route('/',methods = ['POST', 'GET'])
def home():
    return render_template('index.html', experiences= experiences, projects= projects, skills=skills,blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)