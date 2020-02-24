from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = "Bruce"
    movies = [
        {'title':'杀破狼','year':'2010'},
        {'title':'杀破狼','year':'2010'},
        {'title':'杀破狼','year':'2010'},
        {'title':'杀破狼','year':'2010'},
        {'title':'杀破狼','year':'2010'},
        {'title':'杀破狼','year':'2010'},
        {'title':'杀破狼','year':'2010'},
        {'title':'杀破狼','year':'2010'},
        {'title':'杀破狼','year':'2010'},
        {'title':'杀破狼','year':'2010'}
    ]
    return render_template('index.html',name=name,movies=movies)