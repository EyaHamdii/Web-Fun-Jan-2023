from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"








@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name








if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

