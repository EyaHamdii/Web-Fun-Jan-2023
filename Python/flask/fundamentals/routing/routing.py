from flask import Flask ,render_template
app = Flask(__name__)


@app.route('/<phrase>')
def index(phrase):
    return render_template("index.html",phrase=phrase)


@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:name>')
def repeat_word(num, name):
    output = ''

    for i in range(0,num):
        output += f"<p>{name}</p>"

    return output
if __name__=="__main__":
    app.run(debug=True)
