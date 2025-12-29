import sqlite3

class db_operations:
    def __init__(self, conn_path):
        self.connection = sqlite3.connect(conn_path)
        self.cursor = self.connection.cursor()
        print("Database connection established.")

    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT
        )
        ''')

        # Create Businesses table
        self.cursor.execute('''
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
        self.cursor.execute('''
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
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Categories (
            category_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
        ''')

        # Create Business_Category table (junction table)
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Business_Category (
            business_id INTEGER,
            category_id INTEGER,
            PRIMARY KEY (business_id, category_id),
            FOREIGN KEY(business_id) REFERENCES Businesses(business_id),
            FOREIGN KEY(category_id) REFERENCES Categories(category_id)
        )
        ''')

        self.connection.commit()
        print("Tables created successfully.")

    def insert_user(self, username, password, email):
        self.cursor.execute('''
        INSERT INTO Users (username, password, email)
        VALUES (?, ?, ?)
        ''', (username, password, email))
        self.connection.commit()
        print("User added successfully.")

    def insert_business(self, name, address, location, num_seats, outlets_available, internet_available):
        self.cursor.execute('''
        INSERT INTO Businesses (name, address, location, num_seats, outlets_available, internet_available)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, address, location, num_seats, outlets_available, internet_available))
        self.connection.commit()
        print("Business added successfully.")

    def insert_review(self, user_id, business_id, rating, comment, date):
        self.cursor.execute('''
        INSERT INTO Reviews (user_id, business_id, rating, comment, date)
        VALUES (?, ?, ?, ?, ?)
        ''', (user_id, business_id, rating, comment, date))
        self.connection.commit()
        print("Review added successfully.")

    def insert_category(self, name, description):
        self.cursor.execute('''
        INSERT INTO Categories (name, description)
        VALUES (?, ?)
        ''', (name, description))
        self.connection.commit()
        print("Category added successfully.")

    def link_business_to_category(self, business_id, category_id):
        self.cursor.execute('''
        INSERT INTO Business_Category (business_id, category_id)
        VALUES (?, ?)
        ''', (business_id, category_id))
        self.connection.commit()
        print("Business linked to category successfully.")

    def search_businesses(self, category_name, location=None):
        query = '''
        SELECT Businesses.name, Businesses.location
        FROM Businesses
        JOIN Business_Category ON Businesses.business_id = Business_Category.business_id
        JOIN Categories ON Business_Category.category_id = Categories.category_id
        WHERE Categories.name = ?
        '''
        params = [category_name]
        if location:
            query += " AND LOWER(TRIM(Businesses.location)) = LOWER(TRIM(?))"
            params.append(location)
            
        self.cursor.execute(query, tuple(params))
        return self.cursor.fetchall()


    def query_top_rated(self):
        self.cursor.execute('''
        SELECT Businesses.name, AVG(Reviews.rating) as avg_rating
        FROM Businesses
        JOIN Reviews ON Businesses.business_id = Reviews.business_id
        GROUP BY Businesses.business_id
        ORDER BY avg_rating DESC
        ''')
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
        print("Database connection closed.")
