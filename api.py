from flask import Flask,request
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
import requests
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
api = Api(app)

db=SQLAlchemy(app)

parser = reqparse.RequestParser()

class Users(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(100))
  password=db.Column(db.String(100))

class UsersList(Resource):
  def post(self):
    json_data=request.get_json()
    print(type(json_data))
    userName=json_data['name']
    userPassword = json_data['password']
    
    inject=['0',"'",'"','\b','\n','\r','\t','\Z','\\','%','_']
    isinject=False
    for i in inject:
      if(i in userName):
        isinject=True
        print(i)
        break
    ans={'result':'unsanitized'}
    exists=db.session.query(Users.id).filter_by(name=userName, password=userPassword).first() is not None
    if(isinject):
      return ans,200
    elif(exists):
      ans['result']='sanitized'
      return ans,201 
    return ans,200

api.add_resource(UsersList, '/user')
if __name__ == "__main__":
  app.run(debug=True)