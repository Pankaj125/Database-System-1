import csv
import pandas as pd
import mysql.connector
con = mysql.connector.connect(host='acadmysqldb001p.uta.edu',
                              database='pvg0547',
                              user='pvg0547',
                              password='OctZero032022')

cur = con.cursor()
cur.execute("select database()")  #give db name
record = cur.fetchone()  #retrieves next tuple
print("connected",record)

def  InsertIntoTable(filepath, table_name):
    data_dump = pd.read_csv(filepath,delimiter = ',')  #reads csv file
    data_dump.head() #Retrieves n no of rows
    print(data_dump)
    data_dump["Municipal population"] = data_dump["Municipal population"].str.replace(',','')
    data_dump["Metropolitan population"] = data_dump["Metropolitan population"].str.replace(',','')
    data_dump['Most populous city'] = data_dump['Most populous city'].map(dict(Yes = 1,No = 0))
    data_dump['Metropolitan population'] = data_dump['Metropolitan population'].fillna(0)
    for i,row in data_dump.iterrows():
        sql_query = table_name 
        cur.execute(sql_query,tuple(row)) 
        print("record inserted")
    cur.close()  
    con.commit()
    con.close    


us_state = "INSERT INTO state VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
InsertIntoTable('US_county.csv' , us_state) # -> bank
