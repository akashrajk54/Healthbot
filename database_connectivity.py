import mysql.connector

def DataUpdate(FirstName,LastName,location):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "4628",
        database = "rasa_feedback")

    mycursor = mydb.cursor()
    #sql = "CREATE TABLE health_data_update (firstName VARCHAR(255), lastName VARCHAR(255), location VARCHAR(255));"
    sql = '''INSERT INTO health_data_update (firstName, lastName, location) VALUES ("{}","{}","{}");'''.format(FirstName,LastName,location)
    
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def UpdateFeedback(FirstName,LastName,feedback):

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "4628",
        database = "rasa_feedback")

    mycursor = mydb.cursor()
    #sql = "CREATE TABLE UpdateFeedback (firstName VARCHAR(255), lastName VARCHAR(255), feedback VARCHAR(255));"
    sql = '''INSERT INTO UpdateFeedback (firstName, lastName, feedback) VALUES ("{}","{}","{}");'''.format(FirstName,LastName,feedback)
    
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")






if __name__ == '__main__':
    DataUpdate("Dinu", "Bhandari", "love")

#UpdateFeedback("Akash","Bhandari","Love to chat with you")
