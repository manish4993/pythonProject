import pandas as pd
import pyodbc
from SQLCredential import login, Pass

server = 'oibs-dev-server.database.windows.net'
database = 'OIBS'
username = login
password = Pass

# Establishing a connection to the SQL Server
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVER='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                      PWD='+password)

df = pd.read_sql('SELECT TOP (100) * FROM DM_Foresight.VW_V4_RECTYPE_PIVOT_FIN', cnxn)
print(df)
