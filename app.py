import os
import sys
import click

from flask import Flask,render_template

from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
db = SQLAlchemy(app)

# 注册命令
@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库。。。')

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)  # 主键
    name = db.Column(db.String(20))  # name

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key = True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4)) # 电影年份

@app.cli.command()
def forge():
    db.create_all()
    name = "Bruce"
    movies = [
        {'title':'杀破狼','year':'2010'},
        {'title':'扫毒','year':'2010'},
        {'title':'机器之血','year':'2010'},
        {'title':'分手大师','year':'2010'},
        {'title':'这个杀手不太冷','year':'2010'},
        {'title':'邻里的人们','year':'2010'},
        {'title':'釜山行','year':'2010'},
        {'title':'拯救大兵瑞恩','year':'2010'},
        {'title':'我的特工爷爷','year':'2010'},
        {'title':'战狼','year':'2010'}
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('导入数据完成')

@app.route('/')
def index():
    user = User.query.first()  # 读取用户记录
    movies = Movie.query.all()  # 读取所有的电影记录
    return render_template('index.html',user=user,movies=movies)