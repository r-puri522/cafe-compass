from db_operations import db_operations

def main_cli():
    db_ops = db_operations("coffee_shop_reviews.db")
    db_ops.create_tables()

    #  sample data 
    db_ops.insert_user("john_doe", "password123", "john@example.com")
    db_ops.insert_business("Cafe Blue", "123 Main St", "Downtown", 20, True, True)
    db_ops.insert_category("Study-Friendly", "Ideal for studying with quiet spaces.")
    db_ops.link_business_to_category(1, 1)
    db_ops.insert_review(1, 1, 5, "Great coffee and ambiance!", "2024-12-10")

    # Query top-rated coffee shops
    top_rated = db_ops.query_top_rated()
    for shop in top_rated:
        print(f"{shop[0]} - Average Rating: {shop[1]:.2f}")

    # Search for businesses by category and location
    results = db_ops.search_businesses("Study-Friendly", "Downtown")
    for result in results:
        print(f"Business: {result[0]}, Location: {result[1]}")
    db_ops.close_connection()

if __name__ == "__main__":
    main_cli()