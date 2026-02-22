import sqlite3
from typing import List, Dict

class ProductCatalog:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.row_factory = sqlite3.Row
        self._setup()

    def _setup(self):
        self.conn.executescript('''
            CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price DECIMAL, category_id INTEGER);
            CREATE TABLE categories (id INTEGER PRIMARY KEY, name TEXT);
            CREATE TABLE reviews (id INTEGER PRIMARY KEY, product_id INTEGER, rating INTEGER, text TEXT);

            INSERT INTO categories VALUES (1, 'Electronics'), (2, 'Books');
            INSERT INTO products VALUES (1, 'Laptop', 999, 1), (2, 'Phone', 499, 1), (3, 'Novel', 15, 2);
            INSERT INTO reviews VALUES (1, 1, 5, 'Great!'), (2, 1, 4, 'Good'), (3, 2, 3, 'OK');
        ''')

    def get_catalog(self) -> List[Dict]:
        # For each product, it makes 2 additional queries (category + reviews)
        # Refactor to use JOINs or batch queries
        products = self.conn.execute('SELECT * FROM products').fetchall()
        result = []
        for p in products:
            # N+1 Query #1: Get category for each product
            cat = self.conn.execute(
                'SELECT name FROM categories WHERE id = ?', (p['category_id'],)
            ).fetchone()

            # N+1 Query #2: Get reviews for each product
            reviews = self.conn.execute(
                'SELECT rating FROM reviews WHERE product_id = ?', (p['id'],)
            ).fetchall()

            avg_rating = sum(r['rating'] for r in reviews) / len(reviews) if reviews else 0
            result.append({
                'name': p['name'], 'price': p['price'],
                'category': cat['name'] if cat else 'Unknown',
                'avg_rating': round(avg_rating, 1), 'review_count': len(reviews),
            })
        return result

    def get_catalog_optimized(self) -> List[Dict]:
        pass

    @property
    def query_count(self):
        # This tracks how many queries were made (for testing)
        return getattr(self, '_query_count', 0)
