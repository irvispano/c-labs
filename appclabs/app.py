from flask import Flask, request, jsonify,Response
import jwt
import datetime
import string
import json
import secrets
import os
app = Flask(__name__)
sskey=os.getenv("SSKEY","secret")
def generatejwttoken(username):
    alphabet = string.ascii_letters + string.digits
    jti = ''.join(secrets.choice(alphabet) for i in range(30,90))
   
    try:
        if username=="test":
            
            payload = {
                'iat': datetime.datetime.utcnow(),
                'jti': jti,
                'user': "username",
                'date': str(datetime.date.today())
            }
        else:
            
            payload = {
                'iat': datetime.datetime.utcnow(),
                'jti': jti,
                'user': username,
                'date': str(datetime.date.today())
            }
        token = jwt.encode(payload, sskey, algorithm='HS512')
        
        return token
    except Exception:
        print(Exception)
        return Exception


@app.route('/', methods=['POST'])
def generateroute():
    reqjson = request.get_data()
    username=json.loads(reqjson)["username"]
    try:
        if username:
            token = generatejwttoken(username)
            
        else:
            token=generatejwttoken()
            
        resp = Response("Success")
        resp.headers['`x-my-jwt`'] = token
        return resp
        
      
    except Exception as e:
        
        return jsonify({
            'status': 'Failure',
            
        })

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
