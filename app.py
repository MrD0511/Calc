from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from calc import Eval
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def Calc():
    expression=str(request.form.get("expression"))
    eval=Eval(expression)
    res=eval.evaluate()
    if res:
        return render_template('index.html',val=eval.evaluate())
    return render_template('index.html')
@app.route("/AboutUs")
def about():
    return render_template('about.html')
if __name__=='__main__':
    app.run(debug=True)
