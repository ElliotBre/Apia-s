from flask import Flask
from flask import request
app = Flask(__name__)

data = {}
#untested so may not work, didnt understand where to put each request type so they may not make any sense.
#shoot me
@app.route('/')
def hello_internet():
    return "Woop Woop"

@app.route('/name', methods=['POST','GET','PUT','DELETE','PATCH'])
if request.method == 'GET':
    def getName():
        return data["name"]
elif request.method == 'POST':
    def resName():
        data = request.get_json()
        if data != None:
            return 1
        else:
            return 0
elif request.method == 'DELETE':
    def delData:
        data = None
        if data != None:
            return 0
        else:
            return 1
elif request.method == 'PATCH'
    def changeName():
        temp = data["name"]
        data["name"] = request.get_json()["name"]
        if temp == data["name"]:
            temp = None
            return 0
        else:
            temp = None
            return 1
elif request.method == 'PUT':
    def changeFull():
        data = request.get_json()
        if data == None:
            return 0
        else:
            return 1

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


