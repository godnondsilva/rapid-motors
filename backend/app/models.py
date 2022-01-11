# from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
# from sqlalchemy.orm import relationship

# Admin Table
class Admin(db.Model):
    __tablename__ = 'admin'

    admin_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique = True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

# Customer Table
class Customer(db.Model):
    __tablename__ = 'customer'

    cust_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique = True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.Numeric(10), nullable=False)

    def __init__(self, email, password, name, address, phone):
        self.email = email
        self.password = password
        self.name = name
        self.address = address
        self.phone = phone

# Categories Table
class Categories(db.Model):
    __tablename__ = 'testdrives'

    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255), nullable=False)
        
    def __init__(self, cust_id, name, description):
        self.cust_id = cust_id
        self.name = name
        self.description = description

# Cars Table
class Cars(db.Model):
    __tablename__ = 'cars'

    model_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    img_name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Numeric(4), nullable=False)
    color = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category_id = db.column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'), nullable=False)

    def __init__(self, name, img_name, year, color, price, description, admin_id):
        self.name = name
        self.img_name = img_name
        self.year = year
        self.color = color
        self.price = price
        self.description = description
        self.admin_id = admin_id

# Bookings Table
class Bookings(db.Model):
    __tablename__ = 'bookings'

    booking_id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('cars.model_id', ondelete='cascade'), nullable=False)
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.cust_id', ondelete='cascade'), nullable=False)
    booking_color = db.Column(db.String(20), nullable=False)
    booking_date = db.Column(db.Date, nullable=False)
    booking_price = db.Column(db.Numeric(10, 2), nullable=False)

    def __init__(self, model_id, cust_id, booking_color, booking_date, booking_price):
        self.model_id = model_id
        self.cust_id = cust_id
        self.booking_color = booking_color
        self.booking_date = booking_date
        self.booking_price = booking_price

# Testdrives Table
class Testdrives(db.Model):
    __tablename__ = 'testdrives'

    testdrive_id = db.Column(db.Integer, primary_key=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.cust_id', ondelete='cascade'), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('cars.model_id', ondelete='cascade'), nullable=False)
    testdrive_date = db.Column(db.Date, nullable=False)
    state = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    comments = db.Column(db.String(255), nullable=False)
        
    def __init__(self, cust_id, model_id, testdrive_date, state, city, comments):
        self.cust_id = cust_id
        self.model_id = model_id
        self.testdrive_date = testdrive_date
        self.state = state
        self.city = city
        self.comments = comments
