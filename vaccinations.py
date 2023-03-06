
import pandas as pd
import mysql.connector

db_connect = mysql.connector.connect(host='acadmysqldb001p.uta.edu',
                              database='pvg0547',
                              user='pvg0547',
                              password='OctZero032022')
cur = db_connect.cursor()
cur.execute("select database()")  #provides database name
record = cur.fetchone()  #retrieves next tuple
print("connectd",record)

def  InsertIntoTable(filepath, table_name):
    data_dump = pd.read_csv(filepath,delimiter = ',')  #reads the csv file
    data_dump.head() #Retrieves n no of rows
    print(data_dump)
    data_dump = data_dump.where((pd.notnull(data_dump)), None)
    for i,row in data_dump.iterrows():
        sql_query = table_name  #Insert query statement
        print(row)
        cur.execute(sql_query,tuple(row)) 
        
        #print("record inserted")
    cur.close()  
    db_connect.commit()
    db_connect.close    


us_vaccin = "INSERT INTO us_vaccinations VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
InsertIntoTable('US_Vaccination.csv' , us_vaccin) 


