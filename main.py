from flask import Flask,render_template
import random
import  requests
import datetime
app = Flask(__name__)

# print(__name__)


@app.route('/guess')
def hello_world():
    num = random.randint(1,100)
    date = datetime.datetime.now().year
    response = requests.get("https://api.agify.io?name=michael")
    return render_template("index.html",num = num,nums = date,)


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("name.html",name=name,gender=gender,age=age)


@app.route("/")
def myblog():
    url = "https://project1-cag.pages.dev/"
    thought_url = "https://type.fit/api/quotes"
    thought_response = requests.get(thought_url)
    thought = thought_response.json()
    num = random.randint(1,250)
    mythought = thought[num]["text"]
    myauthor = thought[num]["author"]
    return render_template("blog.html",url=url,mythought=mythought,myauthor=myauthor)



if __name__ == '__main__':
    app.run(debug=True, port=3000)
