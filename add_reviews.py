import sqlite3

# Connect to the database
conn = sqlite3.connect("coffee_shop_reviews.db")
cursor = conn.cursor()

reviews = [
    # TruBru
    (1, "Great spot for a quick study session, but parking can be tricky.", 4, "2024-12-10"),
    (1, "Love the friendly staff and the coffee quality. Wish they had more outlets.", 5, "2024-12-11"),
    (1, "Perfect ambiance but too crowded during peak hours.", 4, "2024-12-12"),
    # The Dirty Penguin
    (2, "Unique vibes, great iced coffee, and plenty of outlets.", 5, "2024-12-10"),
    (2, "The seating is a bit limited, but the internet speed makes up for it.", 4, "2024-12-11"),
    (2, "Awesome place to chill, but music was a bit loud for my taste.", 4, "2024-12-12"),
    # Paderia
    (3, "Great pastries and coffee, but no Wi-Fi.", 3, "2024-12-10"),
    (3, "Love the modern decor. Ideal for quick meetings.", 4, "2024-12-11"),
    (3, "I appreciate the quiet atmosphere, but I miss having internet access.", 3, "2024-12-12"),
    # Reborn
    (4, "Cozy place with excellent coffee. Internet is reliable.", 5, "2024-12-10"),
    (4, "Seating is a bit cramped, but the staff is lovely.", 4, "2024-12-11"),
    (4, "Wish there were more tables, but the coffee is worth it.", 4, "2024-12-12"),
    # Kean Coffee
    (5, "The best coffee in Tustin! Spacious and inviting.", 5, "2024-12-10"),
    (5, "Great internet and comfortable seating. Highly recommended.", 5, "2024-12-11"),
    (5, "Perfect for remote work, but can get noisy during busy hours.", 4, "2024-12-12")

    (6, "The best coffee in Tustin! Spacious and inviting.", 3, "2024-12-10"),
    (6, "Great internet and comfortable seating. Highly recommended.", 3, "2024-12-11"),
    (6, "Perfect for remote work, but can get noisy during busy hours.", 4, "2024-12-12")

    (7, "The best coffee in Tustin! Spacious and inviting.", 5, "2024-12-10"),
    (7, "Great internet and comfortable seating. Highly recommended.", 2, "2024-12-11"),
    (7, "Perfect for remote work, but can get noisy during busy hours.", 4, "2024-12-12")

    (8, "The best coffee in Tustin! Spacious and inviting.", 4, "2024-12-10"),
    (8, "Great internet and comfortable seating. Highly recommended.", 4, "2024-12-11"),
    (8, "Perfect for remote work, but can get noisy during busy hours.", 4, "2024-12-12")

    (9, "The best coffee in Tustin! Spacious and inviting.", 5, "2024-12-10"),
    (9, "Great internet and comfortable seating. Highly recommended.", 5, "2024-12-11"),
    (9, "Perfect for remote work, but can get noisy during busy hours.", 4, "2024-12-12")
]

for review in reviews:
    cursor.execute('''
    INSERT INTO Reviews (business_id, comment, rating, date)
    VALUES (?, ?, ?, ?)
    ''', review)

conn.commit()
conn.close()

print("Reviews added successfully!")
