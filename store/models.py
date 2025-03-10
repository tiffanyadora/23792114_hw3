from django.db import models

import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRODUCTS_FILE = os.path.join(BASE_DIR, 'data', 'product.csv')
VISUALS_FILE = os.path.join(BASE_DIR, 'data', 'visualcontent.csv')

class Product:
    # Constructor for Product class
    # It initializes the Product's attributes when a new instance is created
    def __init__(self, id, name, description, feature, rating, price, category):
        self.product_id = id # Match with the VisualContent, and to make it clearer
        self.name = name
        self.description = description
        self.feature = feature
        self.rating = float(rating) # Non-public (mutable)
        self.price = float(price) # Non-public (mutable)
        self.category = category

    # Setter for new price of a product
    def set_price(self, new_price):
        self.price = float(new_price)
    
    # Setter for new rating of a product
    def set_rating(self, new_rating):
        self.rating = float(new_rating)

    @classmethod
    # Helper (Getter) method to read products from CSV and return a list of dictionaries.
    def read_products(cls):
        with open(PRODUCTS_FILE, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [
                {
                    "id": row["ID"],
                    "name": row["Name"],
                    "description": row["Description"],
                    "feature": row["Feature"],
                    "rating": row["Average Rating"],
                    "price": row["Price"],
                    "category": row["Category"],
                }
                for row in reader
            ]

    @classmethod
    # Getter method to fetch all products from Product CSV
    def get_all(cls):
        return [cls(**product) for product in cls.read_products()]

    @classmethod
    # Getter method to fetch a single product by its ID
    def get_by_id(cls, product_id):
        for product in cls.read_products():
            if product["id"] == product_id:
                return cls(**product)
        return None

    # Getter method to fetch image file name from VisualContent CSV
    def get_image_name(self):
        visuals = VisualContent.get_for_product(self.product_id)
        return visuals[0].name if visuals else None

class VisualContent:
    # Constructor for VisualContent class
    # It initializes all attributes related to visual content
    def __init__(self, id, name, description, short_name, file_type, css_class, product_id):
        self.id = id
        self.name = name
        self.description = description
        self.short_name = short_name
        self.file_type = file_type
        self.css_class = css_class
        self.product_id = product_id

    # Getter method to fetch all visual content associated with a specific product
    @classmethod
    def get_for_product(cls, product_id):
        visuals = []
        with open (VISUALS_FILE, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Product ID"] == product_id:
                    formatted_row = {
                        "id" : row["ID"],
                        "name" : row["Name"],
                        "description" : row["Description"],
                        "short_name" : row["Short Name"],
                        "file_type" : row["File Type"],
                        "css_class" : row["CSS Class"],
                        "product_id" : row["Product ID"],
                    }
                    visuals.append(cls(**formatted_row))
        return visuals
    
    # This is to return an HTML <img> tag for the visual contents
    def get_html(self,css_override=None):
        css_class = css_override if css_override else self.css_class
        return f'<img class="{css_class}" alt="{self.description}" src="/static/images/{self.short_name}.{self.file_type}">'