import pymysql
from readFromExcel import ReadExcel
from save2Mysql import MySqlConn

if __name__ == '__main__':
    try:
        re = ReadExcel(r'E:\Work\Data\weidian\涨泰宝签约客户资产变动情况统计.xlsx', 0)
        sqlConn = MySqlConn('root', '1234qwer', '49.235.108.166', 3306, 'test')
        sqlConn.to_sql('t_ztb_custom_orders', re.getDataFrame())
        #raise Exception("测试的错误")

    except Exception as e:
        print("数据从excel导入mysql数据库失败")
    else:
        print("数据从excel导入mysql数据库成功")



