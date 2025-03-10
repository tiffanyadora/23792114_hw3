# WildcatWear
### By: Tiffany Adora (23792114)

WildcatWear is a e-commerce website project for selling UA merchandise that uses HTML/CSS for the frontend Django for the backend. In addition to home, the site now features 8 product pages, and a search functionality.
This is a continuation of the Wildwear-website project (https://github.com/tiffanyadora/WildcatWear-website).

## Project Structure

```bash
wildcatwear/
├── data/                       # CSV data files
|   ├── product.csv             # Product information (Name, Desc, Price, etc.)
|   ├── visual.content.csv      # Visual content information (ID, Name, File type,etc)
|
├── static/                     # Static Files (CSS, images)
|   ├── css/        
|   |   ├── store.css           # Product page styles
|   |   ├── style.css           # Site-wide style
|   |   ├── utility-styles.css  # Utility classes
|   ├── images/                 # Images assets
|
├── staticfiles/    # Collected static files (from collectstatic)
|
├── store/                      # Main application
|   ├── migrations/             # Django migrations
|   ├── templates/              # HTML templates
|   |   ├── index.html          # Home page template
|   |   ├── search.html         # Search results template
|   |   ├── store.html          # Product details template
|   |
|   ├── templatetags/           # Custom template tags
|   |   ├── custom_filters.py   # Custom filters for template
|   |
|   ├── models.py               # Data Model
|   ├── views.py                # View functions
|   ├── urls.py                 # App URL Routing
|   ├── tests.py                # Test script
|
├── wildcatwear/                # Project configuration
|   ├── settings.py             # Django settings  
|   ├── urls.py                 # Project URL Routing
|   ├── wsgi.py, asgi.py        # WSGI & ASGI config
|
├── manage.py                   # Django management script
├── db.sqlite3                  # SQLite database (not used for now)
```

## Installation & Setup

### Prerequisites
- Python 3.9 or higher
- Django (latest version recommended)
- Virtual environment (venv)

### How to Set-up

To run this project, please follow the steps below:

1. **Clone the Repository**
    ```
    git clone [repository-url]
    cd wildcatwear
    ```

2. **Set up the virtual environment**
    ```
    # Windows
    python -m venv venv
    venv\Scripts\activate

    #Linux/Mac
    python -m venvvenv
    source venv/bin/activate
    ```

3. **Install required packages**
    ```
    pip install django
    ```

4. **Collect static files**
    ```
    python manage.py collectstatic
    ```
    **This is very important.** If prompted, type "Yes" to copy all the static files.

5. **Run the development server**
    ```
    python manage.py runserver
    ```

6. **Open the website!**

    Open your browser and go to: http://127.0.0.1:8000/

## Test the Application

### Manual Testing

1. **Home Page**
- Visit http://127.0.0.1:8000/ to see the home page
- All images and page contents are displayed correctly

2. **Product Page**
- Click on any product on the home page at the section 'Featured Products'
- The product information appears (description, features, price, rating,etc.)
- Check the visuals load correctly
- Suggested products at the bottom will have randomized 4 products

3. **Search Page**
- Use the search in navigation bar to search for products
- Try searching for:
    - Query: "Arizona" -> Showing Results for: all merch that includes "Arizona" in the name (eg. University of Arizona)
    - Query: "  University  of Arizona " (with scattered blank spaces) -> Showing Results for "University of Arizona"

### Run the tests.py

To run the test script, in the project folder:
```
cd store
python tests.py
```
What is tested:
- Fetching all products
- Fetching single product by ID
- Retrieving visuals for a product
- HTML generation for visuals


## Acknowledgements
- University of Arizona for brand guidelines
- Font Awesome for icons
- All images are used for demonstration purposes only


For any questions or issues, please open a Github issue or you can contact me at tiffanytjhin@arizona.edu. Thanks! :]