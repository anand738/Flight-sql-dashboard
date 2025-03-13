import mysql.connector

class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Anand@738',
                database = 'flights'
            )
            self.mycursor = self.conn.cursor()
            print("Connection established")
        except:
            print("Connection Error")
            
    
    def fetch_city_name(self):
        
        city = []
        self.mycursor.execute("""
        select distinct(destination) from flight
        union
        select distinct(source) from flight
        """)
        
        data = self.mycursor.fetchall()
        
        for item in data:
            city.append(item[0])
        
        return city


    
    def fetch_all_flights(self,source,destination):
    
        self.mycursor.execute("""
        SELECT Airline,Route,Dep_Time,Duration,Price FROM flight
        WHERE Source = '{}' AND Destination = '{}'
        """.format(source,destination))

        data = self.mycursor.fetchall()

        return data
    
    
    
    def fetch_airline_frequency(self):
        
        airline = []
        frequency = []
        self.mycursor.execute("""
        select Airline,count(*) from flight
        group by Airline;   
        """)
        
        data = self.mycursor.fetchall()
        
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
            
        return airline,frequency
    
    
    
    def busy_airport(self):
    
        city = []
        frequency = []

        self.mycursor.execute("""
        SELECT Source,COUNT(*) FROM (SELECT Source FROM flight
							UNION ALL
							SELECT Destination FROM flight) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency
    
    
    def daily_frequency(self):
    
        date = []
        frequency = []

        self.mycursor.execute("""
        SELECT Date_of_Journey,COUNT(*) FROM flight
        GROUP BY Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency