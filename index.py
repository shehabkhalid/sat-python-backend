import pyodbc


connStr = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r"DBQ=./srs2874_part1of2.mdb;"
    )
cnxn = pyodbc.connect(connStr)
crsr = cnxn.cursor()
#
for table_info in crsr.columns('grp'):
    print(table_info.column_name)
#
# row = crsr.execute('select * from grp').fetchone()
#
# print()


