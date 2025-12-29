from shiny import App, ui, render
import pandas as pd
import os

# Database operations placeholder
from db_operations import db_operations
db_ops = db_operations("coffee_shop_reviews.db")

app_ui = ui.page_fluid(
    ui.tags.style("""
    body {
        background-color: #f5f0e1; /* Cream background */
        font-family: 'Georgia, serif';
        color: #4d3e3e; /* Coffee-brown text */
    }
    h1, h2 {
        color: #2d2424; /* Darker brown for headers */
        text-align: center;
    }
    .btn-primary {
        background-color: #8b5a2b; /* Button color */
        border-color: #8b5a2b;
        color: white;
    }
    """),

    # App title and header image
    ui.tags.div(
        ui.tags.h1("Café Compass"),
        ui.tags.img(src='https://www.shutterstock.com/image-photo/horizontal-banner-cup-coffee-beans-600nw-1803607621.jpg', style="width: 40%; height: auto; margin: 0 auto; display: block;"),
        style="margin-bottom: 20px;"
    ),

    ui.navset_tab(
        ui.nav_panel(
            "Search Coffee Shops",
            ui.input_text("search_category", "Search by Category:", placeholder="e.g., Study-Friendly"),
            ui.input_text("search_location", "Search by Location:", placeholder="e.g., Orange"),
            ui.input_action_button("search_btn", "Search", class_="btn-primary"),
            ui.output_table("results")
        ),
        ui.nav_panel(
            "Top Rated",
            ui.output_table("top_rated")
        ),
        ui.nav_panel(
            "Submit a Review",
            ui.input_text("business_name", "Coffee Shop Name:"),
            ui.input_text("review", "Your Review:"),
            ui.input_slider("rating", "Rating (1-5):", value=3, min=1, max=5),
            ui.input_action_button("submit_review", "Submit", class_="btn-primary")
        )
    )
)

# Define server logic
def server(input, output, session):
    @output
    @render.table
    def results():
        data = []

        if input.search_btn():
            category = input.search_category().strip()
            location = input.search_location().strip()
            data = db_ops.search_businesses(category, location)

        if not data:
            return pd.DataFrame({"Message": ["No results found for the given search."]})
        
        df = pd.DataFrame(data, columns=["Business Name", "Address", "Location"])
        return df

    @output
    @render.table
    def top_rated():
        data = db_ops.query_top_rated()
        df = pd.DataFrame(data, columns=["Business Name", "Average Rating"])
        return df

    
    

app = App(app_ui, server)

from shiny import App

if __name__ == "__main__":
    app = App(app_ui, server)
    app.run()
