from flask import Flask, request, jsonify


app = Flask(__name__) # app is an object of Flask class

# Two ways of sending data one through url to server and one through body(can be sent with or without exception).
# Similarly, the api uses GET and POST methods where GET means send data in url or browser. 
# POST means sending data though body as data is not visible like the url. (logging in your account using username and password).

@app.route('/abc', methods=['GET', 'POST'])# Using app object we are able to access all class methods(ex:route) of class.
def test1():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b 
        return jsonify(str(result)) # convert your result to string and then return the str in json file.


# We are calling the funciton by url and not by function name as a decorator.API is language inpedendent.

@app.route('/abc/man', methods=['GET', 'POST'])# Using app object we are able to access all class methods(ex:route) of class.
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b 
        return jsonify(str(result)) # convert your result to string and then return the str in json file.
    

if __name__ == '__main__':
    app.run()

def test(a,b):
    return a+b
