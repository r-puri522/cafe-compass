import sqlite3
conn = sqlite3.connect("coffee_shop_reviews.db")
cursor = conn.cursor()

# Create Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT
)
''')

# Create Businesses table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Businesses (
    business_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    location TEXT,
    num_seats INTEGER,
    outlets_available BOOLEAN,
    internet_available BOOLEAN
)
''')

# Create Reviews table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Reviews (
    review_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    business_id INTEGER,
    rating INTEGER,
    comment TEXT,
    date TEXT,
    FOREIGN KEY(user_id) REFERENCES Users(user_id),
    FOREIGN KEY(business_id) REFERENCES Businesses(business_id)
)
''')

# Create Categories table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Categories (
    category_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
)
''')

# Create Business_Category table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Business_Category (
    business_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (business_id, category_id),
    FOREIGN KEY(business_id) REFERENCES Businesses(business_id),
    FOREIGN KEY(category_id) REFERENCES Categories(category_id)
)
''')
conn.commit()
conn.close()

print("Tables created successfully!")
