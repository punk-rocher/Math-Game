def ppd():
    

        import mysql.connector

    #Open database connection with a dictionary

        conDict = {"host":"localhost","database":"math_game","user":"root","password":""}

        db = mysql.connector.connect(**conDict)

    #Preapare a cursor object using cursor() method
        cursor = db.cursor()

    #Execute SQL query using execute() method
        cursor.execute("SELECT * FROM sample")

    #Fetch results using fetchall() method
        data = cursor.fetchall()

        for item in data:
            print(item)

    #Disconnect from server
        db.close()
