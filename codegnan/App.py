from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.secret_key="Secret Key"

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Data(db.Model):
     id=db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(100))
     college=db.Column(db.String(100))
     
     def __init__(self,name,college):
          self.name=name
          self.college=college
     
     
@app.route("/",methods=['GET','POST'])
def index():
     if request.method=='POST':
          userDetails=request.formname
          name=userDetails['name']
          email=userDetails['college']
     return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)