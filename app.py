from flask import Flask, render_template,request
import sqlite3
from analysis import analyze_standard,generate_wordcloud

app=Flask(__name__)

#database

def init_db():
    con=sqlite3.connect("feedback.db")
    cur=con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS feedbacks (id INTEGER PRIMARY KEY, content TEXT)
    ''')
    con.commit()
    con.close()

@app.route('/', methods=['POST','GET'])
def index():
    sentiment=None
    if request.method=='POST':
        feedback=request.form['Feedback']
        conn=sqlite3.connect("feedback.db")
        cur=conn.cursor()
        cur.execute('''INSERT INTO feedbacks(content) VALUES (?)''',(feedback,))
        conn.commit()
        conn.close()
        sentiment=analyze_standard(feedback)
        generate_wordcloud()
    return render_template('index.html',sentiment=sentiment)

if __name__=="__main__":
    init_db()
    app.run(debug=True)

