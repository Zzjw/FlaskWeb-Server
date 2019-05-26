"""
Routes and views for the flask application.
"""

from flask import render_template,session, redirect, url_for,request,escape
from FlaskWebProject2 import app

from FlaskWebProject2.DBclass import DB_users
from FlaskWebProject2.backend_method import *


@app.route('/register_check',methods=['POST', 'GET']) # 处理用户登录界面的输入数据
def register_check():
    if request.method == 'POST':
        print(request.data) # 输出注册用户数据
        username = request.get_json()['username']
        password = request.get_json()['password']
        confirm = request.get_json()['confirm']
        email = request.get_json()['email']

        #注册账号
        Reg = DB_users()
        Reg.connectDB()
        Reg.create_table()
        # 判断注册信息是否正确填写
        if Reg.if_user_exist(username):
            return 'username-error'
        elif len(username)<3 or len(username)>20:
            return 'username-length-error'
        elif len(password)==0:
            return 'password-is-null'
        elif confirm!=password:
            return 'password_diff'
        elif not if_mail_legal(email):
            return 'email-error'
        else:
            print("注册成功")
            Reg.insert(username,password,email)
            return 'succeed'

@app.route('/login_check',methods=['POST', 'GET']) # 处理用户登录界面的输入数据
def login_check():
    if request.method == 'POST':
        print(request.data) # 输出登录用户的数据
        username = request.get_json()['username']
        password = request.get_json()['password']

        #检验账号密码的正确性
        test = DB_users()
        test.connectDB()
        test.create_table()
        message =  test.Verify(username,password)

        #判断登录是否成功并加入session
        if message == "succeed":
             ## 将　‘username’属性放入 session中， 在本次request返回 response的时候，服务器发送了将 
             ## session放到 cookies的指令，将session存储到客户端浏览器
             session['username'] = username
             session.permanent = False # 设置关闭浏览器结束会话
        return message

@app.route('/')
@app.route('/login')
def Login():
    #如果登录还没有过期 直接进入主页
    if 'username' in session:
        return redirect("/home")

    #跳转到登录界面
    return render_template(
        'login.html'
    )


@app.route('/logout',methods=['POST', 'GET'])
def Logout():
    # 如果会话中有用户名就删除它。
    # 同时从客户端浏览器中删除 session的 name属性
    try:
        session.pop('username', None)
        return "succeed"
    except:
        return "failed"

@app.route('/register')
# 跳转到注册主界面
def Register():
    """Renders the home page."""
    return render_template(
        'register.html'
    )

@app.route('/home')
# 跳转到网页主界面
def Home():
    # 判断本次请求的session中是否包含有 'username'属性
    if 'username' in session:
        # 如果有，从session中读取该属性
        username = session['username']
        print('Logged in as %s' % username)
        return render_template(
            'modle.html'
        )
    else:
        print("会话不存在，跳转回登录界面")
        return render_template('login.html')