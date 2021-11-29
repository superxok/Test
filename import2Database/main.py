from readFromExcel import ReadExcel
from save2Mysql import MySqlConn

if __name__ == '__main__':
    re = ReadExcel(r'E:\Work\Data\weidian\涨泰宝签约客户资产变动情况统计.xlsx', 'Sheet1')
    sqlConn = MySqlConn('root', '1234qwer', '49.235.108.166', 3306, 'test')

