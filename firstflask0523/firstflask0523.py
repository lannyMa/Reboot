from flask import Flask,request,render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)


# @app.route('/',methods=['GET'])
# def hello_world():
#     name=request.args.get('name')
#     return render_template("index.html")
#     # return '<input type="text" value="%s"><br><input type="button">' % name
# @app.route('/login',methods=['POST','GET'])
# def login():
#     if request.method=='POST':
#     # name=request.args.get('username')
#     # pwd=request.args.get('password')
#         name=request.form.get('username')
#         pwd=request.form.get('password')
#         return 'username is %s and password is %s' % (name,pwd)
#     else:
#         pass
@app.route('/',methods=['GET','POST'])
def hello_world():
    # name=request.args.get('name')
    # return request.method
    # if request.method=='POST':
    #     name=request.form.get('username')
    #     pwd=request.form.get('password')
    #     return 'username is %s and password is %s' % (name,pwd)
    # else:
        return render_template("index.html")
@app.route('/test')
def test():
    status=request.args.get('status')
    if not status:
        return 'no status'
    return 'status is %s' % (status)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090,debug=True)
