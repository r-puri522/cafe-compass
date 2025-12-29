import sqlite3
conn = sqlite3.connect("coffee_shop_reviews.db")
cursor = conn.cursor()

# Coffee shop data
coffee_shops = [
    ("TruBru", "7626 E Chapman Ave d", "Orange", 15, False, True),
    ("The Dirty Penguin", "14708 Pipeline Ave STE C", "Chino Hills", 12, True, True),
    ("Paderia", "17935 MacArthur Blvd", "Irvine", 16, True, False),
    ("Reborn", "3373 E Imperial Hwy", "Brea", 10, False, True),
    ("Kean Coffee", "13681 Newport Ave Ste 14", "Tustin", 30, False, True),
    ("Chaiwale and Co", "177 N Glassel", "Orange", 25, False, True),
    ("in-sit", "6930 Beach Blvd", "Buena Park", 15, False, False),
    ("CONTRA", "115 N Orange St", "Orange", 30, False, False), 
    ("Avatar", "1951 E Dyer Rd", "Santa Ana", 20, True, True)
]

# Insert data into Businesses table
for shop in coffee_shops:
    cursor.execute('''
    INSERT INTO Businesses (name, address, location, num_seats, outlets_available, internet_available)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', shop)

print("Coffee shops added successfully!")

categories = [
    ("Study-Friendly", "Ideal for studying with quiet spaces."),
    ("Quiet", "Perfect for relaxing or focusing."),
    ("Outdoor Seating", "Great for enjoying fresh air.")
]

# Insert data into Categories table
for category in categories:
    cursor.execute('''
    INSERT INTO Categories (name, description)
    VALUES (?, ?)
    ''', category)

print("Categories added successfully!")

# Business-Category links
business_category_links = [
    (1, 1),  # Café Blue to Study-Friendly
    (2, 1),  # The Dirty Penguin to Study-Friendly
    (3, 2),  # Paderia to Quiet
    (4, 3),  # Reborn to Outdoor Seating
    (5, 1),   # Kean Coffee to Study-Friendly
    (6, 2),
    (7, 3),
    (8, 1),
    (9, 3)
]
for link in business_category_links:
    cursor.execute('''
    INSERT INTO Business_Category (business_id, category_id)
    VALUES (?, ?)
    ''', link)

print("Business-category links added successfully!")

conn.commit()
conn.close()
