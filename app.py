from flask import Flask, request, render_template
import pymysql

db = pymysql.connect("localhost", "username", "password", "database")

app = Flask(__name__)
api = Api(app)




@app.route('/')
def someName():
    cursor = db.cursor()
    sql = "SELECT * FROM table"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)

if __name__ == '__main__':
app.run(debug=True)