from flask import Flask,render_template,url_for,request
from database import UserPost
app= Flask(__name__)

db=UserPost()
db.creatDatabase()
db.userPostTable()



@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":    
        post=request.form['user_post']
        if post=='':
            pass
        else:
            db.userPost(post)
            post=db.seeUserPost()
            return render_template('index.html',post=post)
    post=db.seeUserPost()
    return render_template('index.html',post=post)


if __name__=="__main__":
    app.run(debug=True)