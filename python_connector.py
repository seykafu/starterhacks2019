import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   connection = mysql.connector.connect(host='localhost',
                             database='sh_questionaire',
                             user='seykafu',
                             password='398306014Yay!')
   sql_insert_query = """ INSERT INTO questionaire_data (email_user, cat1, cat2, cat3,
   email_recipient) VALUES ('kaseykungfu@gmail.com', 'books', 'pets',
   'Health & Personal Care', 'li.kh.joe@gmail.com'); """
   cursor = connection.cursor()
   result  = cursor.execute(sql_insert_query)
   connection.commit()
   print ("Record inserted successfully into questionaire_data_new table")
except mysql.connector.Error as error :
    connection.rollback() #rollback if any exception occured
    print("Failed inserting record into questionaire_data table {}".format(error))
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
