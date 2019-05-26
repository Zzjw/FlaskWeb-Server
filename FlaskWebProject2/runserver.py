"""
This script runs the FlaskWebProject2 application using a development server.
"""

from os import environ
from FlaskWebProject2 import app

import webbrowser


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    # 自动打开网页
    p = 8039
    webbrowser.open("http://127.0.0.1:%s/"%str(p), new=0, autoraise=True)
    # 当调用app.run()的时候，用到了Werkzeug库，它会生成一个子进程，当代码有变动的时候它会自动重启
    app.run(host='0.0.0.0',port=p,debug=True,use_reloader=False)
    