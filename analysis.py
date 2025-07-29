from textblob import TextBlob
from wordcloud import WordCloud
import sqlite3

def analyze_standard(text):
    blob=TextBlob(text)
    polarity=blob.sentiment.polarity

    if polarity>0:
        return "Positive"
    elif polarity<0:
        return "Negative"
    else:
        return "Neutral"

def generate_wordcloud():
    conn=sqlite3.connect("feedback.db")
    cur=conn.cursor()
    cur.execute("SELECT content FROM feedbacks")
    texts=[row[0] for row in cur.fetchall()]
    conn.close()
    all_text="".join(texts)
    wordcloud=WordCloud(width=800, height=400).generate(all_text)
    wordcloud.to_file("static/wordcloud.png")