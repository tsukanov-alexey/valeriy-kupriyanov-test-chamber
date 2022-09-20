from mysql.connector import Error
import pymysql


class my_database:
    def __init__(self, DB_NAME, DB_HOST, DB_USER, DB_PORT, DB_PASSWORD):
        self.db_name = DB_NAME
        self.db_host = DB_HOST
        self.db_port = DB_PORT
        self.db_user = DB_USER
        self.db_passwd = DB_PASSWORD

    def get_connection(self):
        try:
            connection = pymysql.connect(host=self.db_host,
                                         port=self.db_port,
                                         user=self.db_user,
                                         passwd=self.db_passwd)
            print("CONNECTION TO DATABASE SUCCeS,HAVE A GOOD DAY MR.MARK!")
            return connection
        except Error as db_connection_error:
            print("try again mr mark,because you have a mistakes with connection", db_connection_error)

    def lets_go(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        create_name = """CREATE DATABASE IF NOT EXISTS {}""".format("means")
        cursor.execute(create_name)
        cursor.close()
        connection.close()

    def createtabb(self):
        connection = self.get_connection()

        cursor = connection.cursor()
        try:
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS buble (
            id INT AUTO_INCREMENT,
            name TEXT NOT NULL,
            age INT ,
            gender VARCHAR(10),
            nationality TEXT ,   
            mailbox TEXT,
            CITY TEXT,                                               
            PRIMARY KEY (id)
            )ENGINE = InnoDB '''
            cursor.execute(create_table_query)
            connection.commit()

        except Error as error:
            print(error, "вы хуесос!")

        finally:
            cursor.close()
            connection.commit()
            connection.close()

    def go_value(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        try:
            go_value = '''INSERT INTO buble(name,age,gender,nationality,mailbox,city)
                       VALUES("MARK",20,"MALE","ENGLAND","snipsss228@gmail.com","London"),
                              ("gnom",20,"FEMALE","Spain","gmoom22021@gmail.com","Saint-P"),
                              ("Oleg",31,"male","USA","makar@localhost:3306","OHIO"),
                              ("MIRACKE",87,"MALE","Russia","ubernacht@locashost@3337.ru","Murmacks");'''

            cursor.execute(go_value)
            connection.commit()
        except Error as db_connection_error:
            print("Try Again Mr.mark:", db_connection_error)
        finally:
            cursor.close()
            connection.close()

    def go_query(self):
        self.connection = pymysql.connect(
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            passwd=self.db_passwd,
            database=self.db_name)


        cursor = self.connection.cursor()
        query = """SELECT *FROM buble;"""
        cursor.execute(query)
        query_res = cursor.fetchall()
        for data in query_res:
            print(data)
        else:
            cursor.close()
            self.connection.commit()


    def deleter(self):
        self.connection = pymysql.connect(
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            passwd=self.db_passwd,
            database=self.db_name)

        cursor = self.connection.cursor()
        quer = """DELETE FROM buble WHERE id > 4;"""
        cursor.execute(quer)
        cursor.close()
        self.connection.commit()


    def new_quer(self):
        self.connection = pymysql.connect(
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            passwd=self.db_passwd,
            database=self.db_name)

        cursor = self.connection.cursor()
        request = """SELECT age,name,mailbox,nationality FROM buble;"""
        cursor.execute(request)
        x = cursor.fetchall()
        for i in x:
            print(i)

        cursor.close()
        self.connection.commit()


    def updater(self):
        self.connection = pymysql.connect(
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            passwd=self.db_passwd,
            database=self.db_name)

        cursor = self.connection.cursor()
        request = """ALTER TABLE buble ADD data DATETIME NOT NULL;"""
        cursor.execute(request)
        cursor.close()
        self.connection.commit()


    def new_value(self):
        self.connection = pymysql.connect(
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            passwd=self.db_passwd,
            database=self.db_name)

        cursor = self.connection.cursor()
        request = """SELECT *FROM buble;"""
        cursor.execute(request)
        all_res = cursor.fetchall()
        x = list(all_res)
        for i in x:
            print(i)

    def insert(self):
        self.connection = pymysql.connect(
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            passwd=self.db_passwd,
            database=self.db_name)

        cursor = self.connection.cursor()
        request = """SELECT NOW();"""
        cursor.execute(request)
        cursor.close()
        self.connection.commit()




def_go = my_database(DB_NAME="means", DB_PORT=3306, DB_HOST="localhost", DB_PASSWORD="1234", DB_USER="root")
def_go.get_connection()
def_go.deleter()
#def_go.updater()
def_go.new_value()
def_go.insert()
#def_go.new_quer()
#def_go.go_value()
#def_go.go_query()
#def_go.lets_go()
#def_go.createtabb()








