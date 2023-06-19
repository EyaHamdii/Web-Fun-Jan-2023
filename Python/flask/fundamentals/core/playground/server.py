from flask import Flask , render_template 
app= Flask(__name__)

@app.route('/play/<string:x>/color')
def index(x ,color):
    num_boxes=int(x)
    return render_template("index.html", num_boxes=num_boxes,color=color)
if __name__=="__main__":
    app.run(debug=True)