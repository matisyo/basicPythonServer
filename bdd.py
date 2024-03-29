from sqlalchemy import create_engine

db_string = "postgres://wvbwcrtihrztjd:685061152768524d7b451de246e64ac07165d27e1143e8f696265ead51cb949b@ec2-174-129-209-212.compute-1.amazonaws.com:5432/dcm2kgq8jv6g1h"
#db_string = "postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"
db = create_engine(db_string)

# Create 
db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")  
db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

# Read
result_set = db.execute("SELECT * FROM films")  
for r in result_set:  
    print(r)

# Update
db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")

# Delete
db.execute("DELETE FROM films WHERE year='2016'")  