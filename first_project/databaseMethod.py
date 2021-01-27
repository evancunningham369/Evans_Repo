from DummyDB import cursor, mydb
import pandas as pd


def showDataBase():
    query = 'SELECT * FROM The_Sims_3'
    dataFrame = pd.read_sql(query, mydb)
    #cursor.execute("SELECT * FROM The_Sims_3")
    #dataBaseResult = cursor.fetchall()
    return dataFrame.to_html(index=False)
