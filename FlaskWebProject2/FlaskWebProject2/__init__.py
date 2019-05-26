"""
The flask application package.
"""

from flask import Flask,session

 # 在这里定义的变量在整个包内都被视为全局的
app = Flask(__name__,static_folder='static')

# 设置密钥，复杂一点：
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

import FlaskWebProject2.backend
