import mysql.connector

# Create a database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Juve-2219',
    database='podcast_booking'
)

# Create a cursor for interacting with the database
cursor = db.cursor()

# You can print a confirmation message if needed
if db.is_connected():
    print("Connected to the database!")

# The cursor and database connection will be imported and used in your Flask app
