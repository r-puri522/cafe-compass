# Café Compass - December 2024

![Python](https://img.shields.io/badge/Python-3-blue?style=flat)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat)
![Shiny](https://img.shields.io/badge/UI-Shiny-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)

## Overview

Café Compass is a database-backed application for discovering and reviewing local coffee shops based on work- and study-friendly criteria such as seating capacity, outlet availability, and internet access. The project demonstrates relational database design, SQL querying, and backend-to-UI integration using Python and SQLite.

---

## Executive Summary

Café Compass is a Yelp-style review system tailored specifically for coffee shops. Users can search for cafes by location or category, view top-rated businesses, and submit reviews. This tool particularly benefits students and professionals looking for the perfect study or work environment. The app integrates a database backend with a user-friendly interface to streamline the discovery and review process.

## Key Technical Concepts Demonstrated

- Relational database schema design
- One-to-many and many-to-many relationships
- SQLite database implementation
- Python-based database operations
- SQL querying for filtering and aggregation
- Backend logic connected to a UI layer


---

## Technical Specifications

### Database

The application uses an SQLite database with the following schema:

#### Tables
- **Users**: Stores user accounts (username, password, email).
- **Businesses**: Contains coffee shop details (name, address, location, seating capacity, availability of outlets and internet).
- **Reviews**: Links users to businesses, storing ratings, comments, and review dates.
- **Categories**: Groups coffee shops into searchable categories (e.g., Study-Friendly, Outdoor Seating).
- **Business_Category**: A junction table linking businesses to multiple categories.

#### Relationships
- **One-to-many**: Users write multiple reviews.
- **Many-to-many**: Businesses can belong to multiple categories via the Business_Category table.

---

## Backend Files

1. **db_operations.py** encapsulates all database operations, such as inserting records, linking categories, querying businesses by location and category, and fetching top-rated coffee shops.
2. **create_tables.py** initializes the database by creating all required tables.
3. **add_coffee_shops.py** populates the Businesses, Categories, and Business_Category tables with sample data.
4. **add_reviews.py** adds sample reviews for coffee shops into the Reviews table.
5. **app.py** provides a command-line interface for testing backend functionality like inserting users, adding businesses, and querying the database.

---

## Frontend

**ui.py** implements a Shiny-based UI with a coffee-themed color scheme. It features three main functionalities:

1. **Search Coffee Shops**: Allows users to search by category and location.
2. **Top Rated**: Displays the highest-rated coffee shops.
3. **Submit a Review**: This lets users add ratings and comments for coffee shops.

---

## How the Files Interconnect

- The database layer, handled by **db_operations.py**, interacts directly with the SQLite database and provides reusable functions for querying and modifying data.
- The backend logic in **app.py** acts as a bridge between the database and the user by calling functions in **db_operations.py**.
- The frontend in **ui.py** connects to the backend via **db_operations.py** to query data and render results in the Shiny interface.

---

## How the Database Is Utilized

The database stores all information about users, coffee shops, reviews, and categories.

- Queries like `search_businesses(category, location)` fetch cafes based on user-defined criteria.
- The `query_top_rated()` function retrieves the highest-rated coffee shops.
- Reviews are submitted via the `insert_review()` function.

---

## How to Run the Application

1. **Set up the database in the terminal**
   - Run the `create_tables.py` file to create all required tables in the SQLite database.
   - Populate the database with sample data by running the `add_coffee_shops.py` and `add_reviews.py` files in sequence.

2. **Test the backend**
   - Run the `app.py` file to test various backend functionalities like inserting users, adding businesses, and querying data.

3. **Start the Shiny app**
   - Run the `ui.py` file to launch the Shiny UI.
   - Open the provided link in your browser (usually `http://127.0.0.1:8000`) to interact with the application.

---

## Challenges and Resolutions

1. **Location Search Not Returning Results**
   - The issue was resolved by ensuring case-insensitive and trimmed input handling in queries. SQL logic was adjusted to use functions like `LOWER(TRIM())` for consistent matching.

2. **Static Image Not Displaying**
   - This was fixed by ensuring the image file was placed in the correct directory and referencing it via the correct path.

---
