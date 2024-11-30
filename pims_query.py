"""
@Autor: Artur Trela  created : 2024-11-26
Modul for make connection and scrap data from PIMS server
"""

from sekrety import sekrety
import os
import oracledb
import pandas as pd
import time

server = ''
pc = os.environ['COMPUTERNAME']
sample_query ="SELECT * FROM LSH_PREDICTIVE.ACXISP01_PRD01_RESULT WHERE TAG_ID = 400512 "
tag_name_query = "SELECT * FROM LSH_PREDICTIVE.ACXISP01_WATCH_TAG"

"""

*************************************************************************************
Columns name for query in view LSH_PREDICTIVE.ACXISP01_WATCH_TAG

['TAG_ID', 'TAG_NAME', 'TAG_COMMENT', 'CREATION_DATE', 'CREATED_BY',
       'LAST_UPDATE_DATE', 'LAST_UPDATED_BY', 'PROCESS_ID', 'RESOURCE_ID',
       'SOURCE_SYSTEM_ID', 'CYCLE', 'UOM', 'DATA_TYPE', 'OPERATION_TYPE',
       'DATE_FROM', 'DATE_TO', 'LIMIT_XH', 'LIMIT_XL', 'LIMIT_HH', 'LIMIT_LL',
       'LIMIT_H', 'LIMIT_L', 'GRAPH_MAX', 'GRAPH_MIN', 'W_MAIL_GROUP',
       'W_MAIL_USER', 'W_MAIL_COMMENT', 'C_MAIL_GROUP', 'C_MAIL_USER',
       'C_MAIL_COMMENT', 'NODATA_CHECK_CYCLE', 'E_MAIL_GROUP', 'E_MAIL_USER',
       'E_MAIL_COMMENT', 'MONITOR_POINTS', 'CHECK_CONDITION_ID',
       'W_MAIL_CONDITION_ID', 'C_MAIL_CONDITION_ID', 'E_MAIL_CONDITION_ID',
       'FORMULA_ID', 'SOURCE_TAG_ID', 'AGGR_GROUP_TYPE', 'AGGR_GROUP_ID',
       'OPER_DATA_NUMBER', 'SOURCE_TABLE_TYPE', 'SOURCE_TABLE_NAME',
       'SOURCE_COL_NAME', 'MAX_DATA_NO', 'GRAPH_C_VISIBLE', 'PACI_DSP_TYPE',
       'PACI_DISPLAY_ORDER', 'PACI_ALIAS_KEYCODE', 'PACI_DISPLAY_NAME']

***************************************************************************************
Columns name for query in view LSH_PREDICTIVE.ACXISP01_PRD01_RESULT

['TAG_ID', 'GET_DATETIME', 'DATAVALUE_N', 'DATAVALUE_C', 'QUALITY_CODE',
       'CREATION_DATE', 'CREATED_BY', 'GET_DATE', 'CHECK_DATETIME',
       'CHECK_RESULT', 'EXCEPTION_TYPE', 'MAIL_SENT'],
"""


def zapytanie_PIMS(query):
    user = sekrety['PIMS_USER']
    pwd = sekrety['PIMS_PASSWORD']
    serv = '000.000.000.000:1521/xxxxx'
    try:
        # Nawiązanie połączenia

        conn = oracledb.connect(user=user, password=pwd, dsn=serv)
        # Połączenie udane
        # print(f'Połączono z bazą danych Oracle za pomocą oracledb z maszyny {pc} \n')
        df = pd.read_sql_query(query,conn)
        conn.close()
        return df

    except oracledb.Error as e:
        # W przypadku błędu podczas połączenia
        print(f'Wystąpił błąd podczas łączenia z bazą danych Oracle za pomocą oracledb z maszyny {pc}\n')
        print(e)

df1 = zapytanie_PIMS(sample_query)
df2 = zapytanie_PIMS(tag_name_query)

#Połączenie danych z dwóch zapytań w jedną tablice

merged_df = pd.merge(df1[['TAG_ID', 'GET_DATETIME', 'DATAVALUE_N', 'DATAVALUE_C']],
                     df2[['TAG_ID','TAG_NAME','PROCESS_ID','PACI_DISPLAY_NAME']], on='TAG_ID')
merged_df.to_csv('merged_dataframe.csv', index= False)