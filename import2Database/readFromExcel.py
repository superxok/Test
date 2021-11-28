import pandas as pd

sExcelFile = "E:\Work\Data\weidian\涨泰宝签约客户资产变动情况统计.xlsx"
df = pd.read_excel(sExcelFile, sheet_name="Sheet1")
nrows = df.shape[0]
ncols = df.columns.size

print('Max Rows:'+str(nrows))
print('Max Columns'+str(ncols))

#显示列名，以列表形式显示
print(df.columns)

#显示列名，并显示列名的序号
for iCol in range(ncols):
    print(str(iCol)+':'+df.columns[iCol])

# 列出特定行列，单元格的值
print(df.iloc[0, 0])
print(df.iloc[0, 1])

#查看某列内容
sColumnName='所属营业部'
print(df[sColumnName])


#查看某行的内容
iRow=0
for iCol in range(ncols):
    print(df.iloc[iRow, iCol])

#遍历逐行逐列
for iRow in range(nrows):
    for iCol in range(ncols):
        print(df.iloc[iRow,iCol])