import pandas as pd
from sqlalchemy import create_engine
from readFromExcel import ReadExcel

class MySqlConn:
    """从excel读取数据并写入mysql的类"""

    def __init__(self, userName, password, ip, port, db):
        self.__username = userName
        self.__password = password
        self.__ip = ip
        self.__port =port
        self.__db = db

    def getConnStr(self):
        strConn = 'mysql+pymysql://{}:{}@{}:{}/{}', format(self.__username, self.__password, self.__ip, self.__port)
        return strConn


    self.engine = create_engine(strConn)


    # 写入mysql数据库
    def to_sql(selfself, sql):
        df =

