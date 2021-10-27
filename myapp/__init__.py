from flask import Flask

from flask_mysqldb import MySQL


app=Flask(__name__)

app.config['SECRET_KEY']='1f1885fa5504fe599b09bf09d9cb0c44'

app.config['MySQL_HOST']='localhost'
app.config['MySQL_USER']='root'
app.config['MySQL_PASSWORD']='password123'
app.config['MySQL_DB']='myapp'
mysql=MySQL(app)

print(app.config)


from myapp import routes











