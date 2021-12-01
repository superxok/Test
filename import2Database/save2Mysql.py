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
        self.__strConn = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(self.__username, self.__password, self.__ip, self.__port, self.__db)
        self.__engine = create_engine(self.__strConn)

    def getConnStr(self):
        return self.__strConn

    # 写入mysql数据库
    def to_sql(self, sql):
        pass

    #写入mysql数据库
    def to_sql(self, tableName, df):
        df.to_sql(tableName, con=self.__engine, if_exists="replace", index=False)
        print("数据同步到mysql完毕, 表名为: {}".format(tableName))






