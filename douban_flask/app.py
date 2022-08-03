from flask import Flask,render_template
import sqlite3
import jieba  #分词
app = Flask(__name__)


@app.route('/') #定义一个路径
def index():  # put application's code here
    # 准备词云所需要的文字
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = 'select introduction from movie250'
    data = cur.execute(sql)
    text = ""
    for item in data:
        text = text + item[0]
    # print(text)

    # 分词
    cut = jieba.cut(text)
    string = ' '.join(cut)  # 将cut中的每一个成员用' '空格分割
    length=len(string)
    return render_template("index.html",length=length)

@app.route('/index')
def home():
    # return render_template("index.html")
    return index()

@app.route('/movie')
def movie():
    datalist=[]
    con=sqlite3.connect("movie.db")
    cur=con.cursor()
    sql="select * from movie250"
    data=cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html",movies=datalist)

@app.route('/score')
def score():
    score=[] #评分
    num=[]   #每个评分所统计出的电影数量
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html",score=score,num=num)

@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")

if __name__ == '__main__':
    print(app.config)
    app.run()
