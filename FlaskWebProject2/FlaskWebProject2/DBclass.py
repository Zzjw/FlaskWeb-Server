import pymysql
import re
import hashlib

class DB_users(object):
    """
    为简化数据库操作编写的数据库帮助方法类
    """       

    def connectDB(self): # 要使用数据库必须先建立连接
        self.conn = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='ysy990821',
                                db='s7e8_web',
                                charset='utf8')
        self.table_name = "users_data"

    def table_exists(self):  #这个函数用来判断表是否存在
        cursor = self.conn.cursor()
        cursor.execute("show tables;")
        tables = [cursor.fetchall()]
        table_list = re.findall('(\'.*?\')',str(tables))
        table_list = [re.sub("'",'',each) for each in table_list]
        cursor.close()
        if self.table_name in table_list:
            return True    #存在返回1
        else:
            return False    #不存在返回0
        


    def create_table(self):
        if not self.table_exists():
            cursor = self.conn.cursor()
            sql_create="CREATE TABLE %s(username varchar(32),password varchar(64),email varchar(32));"%str(self.table_name)
            cursor.execute(sql_create)
            self.conn.commit()
            cursor.close()
    
            
    def if_user_exist(self,username):
        cursor = self.conn.cursor()

        # 查找用户名记录
        sql_select = "select username from %s;"%self.table_name
        cursor.execute(sql_select)
        cursor.close()

        user_list = cursor.fetchall()
        t = eval("('%s',)"%username)
        if t in user_list:
            return True
        else:
            return False


    def insert(self,username,password,email):
        cursor = self.conn.cursor()

        # 判断这个用户是否已经注册了数据
        if self.if_user_exist(username):
            print("数据库已经有此用户数据，插入失败")
        else:
            #加密用户的密码 并将用户信息保存入数据库中
            pawd_result = self.encryption(password)

            sql_insert = '''INSERT INTO %s(username,password,email)
                                 values('%s','%s','%s');'''%(self.table_name,str(username),str(pawd_result),str(email))
            try:
                cursor = self.conn.cursor()
                cursor.execute(sql_insert)
                self.conn.commit()
                print("数据库插入成功！")
            except:
                print("出现异常，插入失败！")
        cursor.close()


    def Verify(self,username,password):
        cursor = self.conn.cursor()
        if not self.if_user_exist(username): # 判断用户是否注册了数据库
            print("用户尚未注册！")
            return "no_such_user"
        else:
            #加密密码
            pawd_result = self.encryption(password)

            sql_select = "select username,password from %s;"%self.table_name # 只需要取出账号名和密码
            cursor.execute(sql_select)
            result = cursor.fetchall()
            t = eval("('%s','%s')"%(username,pawd_result))

            if t in result:
                print("登录成功！")
                return "succeed"
            else:
                print("密码错误！")
                return "password_wrong"
        cursor.close()


    def encryption(self,password):
        #加密密码
        h = hashlib.sha256()
        h.update(bytes(password, encoding='utf-8'))
        pawd_result = h.hexdigest()
        return pawd_result


    def closeDB(self):
        self.conn.close()


if __name__=="__main__":
    pass