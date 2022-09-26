from flask import request, jsonify
from app import app, db
from app.common import allowed_file
from app.models import Customer, Admin, Cars, Testdrives, Bookings, Categories
from flask_jwt_extended import create_access_token
from app.marsh_schema import CarsSchema, TestdrivesSchema, BookingsSchema, CustomersSchema, CategoriesSchema
from flask_mail import Message
from app import mail
import os

@app.route('/register', methods=['POST'])
def register():
    if request.is_json:
        data = request.get_json()
        userData = Customer(
            name=data['name'],
            phone=data['phone'],
            email=data['email'], 
            password=data['password'], 
            address=data['address'],
        )
        db.session.add(userData)
        db.session.commit()
        return {"message": f" {userData.name} has been registered successfully."}
    else:
        raise Exception("The request payload is not in JSON format")

@app.route('/updateprofile', methods=['PUT'])
def update_profile():
    if request.method == 'PUT':
        data = request.get_json()
        cust_id = data['cust_id']
        fields = (
            'name',
            'phone',
            'email', 
            'password', 
            'address',
        )
        for item in data.keys():
            if item in fields:
                db.session.query(Customer).filter_by(cust_id=cust_id).update(
                {
                    item: data[item]
                })
        db.session.commit()
        return {"message": f" Customer ID: {cust_id} has been updated successfully."}
    else:
        raise Exception("The request payload is not in JSON format")

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if not email or not password:
           return {"error": "Missing email or password"}
        
        userData = Customer.query.filter_by(email=email).first()
        if userData is None:
            return {"error": "That user does not exist"}
        if userData.password != password:
            return {"error": "Invalid credentials"}
        else:
            access_token = create_access_token(identity={"email": email})
            return {
                "cust_id": userData.cust_id, 
                "email": email, 
                "password": userData.password, 
                "name": userData.name, 
                "phone": userData.phone,
                "address": userData.address,
                "access_token": access_token
            }
    else:
        return {"error": "The request payload is not in JSON format"}

# Route for admin login
@app.route('/loginadmin', methods=['POST'])
def loginAdmin():
    if request.is_json:
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if not email or not password:
           return {"error": "Missing email or password"}
        
        adminData = Admin.query.filter_by(email=email).first()
        if adminData is None:
            return {"error": "That admin does not exist"}
        if adminData.password != password:
            return {"error": "Invalid credentials"}
        else:
            access_token = create_access_token(identity={"email": email})
            return {"admin_id": adminData.admin_id, "email": email, "access_token": access_token}
    else:
        return {"error": "The request payload is not in JSON format"}

# Route for getting all the cars from the database
@app.route('/cars', methods=['GET'])
def cars():
    cars = Cars.query.all()
    return jsonify(CarsSchema(many=True).dump(cars))

# Route to get a specific car from the database
@app.route('/car/<int:model_id>', methods=['GET'])
def car(model_id):
    carData = Cars.query.filter_by(model_id=model_id).first()
    # print(testdriveData)
    return jsonify(CarsSchema(many=False).dump(carData))

# Route to book a testdrive
@app.route('/booktestdrive', methods=['POST'])
def book_testdrive():
    if request.is_json:
        data = request.get_json()
        testdriveData = Testdrives(
            cust_id=data['cust_id'],
            model_id=data['model_id'],
            testdrive_date=data['testdrive_date'],
            state=data['state'],
            city=data['city'],
            comments=data['comments']
        )
        db.session.add(testdriveData)
        db.session.commit()
        return {"message": "Testdrive succesfully booked"}
    else:
        return {"error": "The request payload is not in JSON format"}

@app.route('/bookcar', methods=['POST'])
def book_car():
    if request.is_json:
        data = request.get_json()
        bookingData = Bookings(
            model_id=data['model_id'],
            cust_id=data['cust_id'],
            booking_color=data['booking_color'],
            booking_date=data['booking_date'],
            booking_price=data['booking_price']
        )
        db.session.add(bookingData)
        db.session.commit()
        return {"message": "Car successfully booked"}
    else:
        return {"error": "The request payload is not in JSON format"}


# Route to get testdrives for particular customer id
@app.route('/testdrives/<int:cust_id>', methods=['GET'])
def testdrive(cust_id):
    testdriveData = Testdrives.query.filter_by(cust_id=cust_id)
    # print(testdriveData)
    return jsonify(TestdrivesSchema(many=True).dump(testdriveData))

# Route to get all bookings for particular customer id
@app.route('/bookings/<int:cust_id>', methods=['GET'])
def booking(cust_id):
    bookingsData = db.session.query(Bookings.booking_id, Bookings.model_id, Bookings.cust_id, Bookings.booking_color, Bookings.booking_date, Bookings.booking_price, Cars.name).filter(Bookings.model_id == Cars.model_id).filter(Bookings.cust_id == cust_id).all()
    # print(bookingsData)
    return jsonify(BookingsSchema(many=True).dump(bookingsData))


# Admin routes
# Route to add categories
@app.route('/addcategory', methods=['POST'])
def add_category():
    if request.is_json:
        data = request.get_json()
        categoryData = Categories(
            name=data['name'],
            description=data['description']
        )
        db.session.add(categoryData)
        db.session.commit()
        return {"message": "Category succesfully added"}
    else:
        return {"error": "The request payload is not in JSON format"}

# Route to add cars
# Note: This route uses FORM data and not JSON data
@app.route('/addcar', methods=['POST'])
def addcar():
    # if request.:
        if 'img' not in request.files:
            return {"error": "File not found!"}
        # data = request.form
        file = request.files['img']
        filename = file.filename.lower()
        if filename == '':
            return {"error": "No file selected"}

        if file and allowed_file(filename):
            file_path = app.config['UPLOAD_FOLDER'] + "/" + filename
            file.save(file_path)

            data = dict(request.form)

            carData = Cars(
                name=data['name'],
                img_name=filename,
                year=data['year'],
                color=data['color'],
                price=data['price'],
                category_id=data['category_id'],
                description=data['description'],
                admin_id=data['admin_id']
            )
            db.session.add(carData)
            db.session.commit()
            return {"message": "Car successfully added"}
        else:
            return {"error": "The file is not in the allowed format"}

# Route to delete a category (admin)
@app.route('/deletecategory/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = db.session.query(Categories).filter_by(category_id=category_id)
    if category:
        category.delete()
        db.session.commit()
        return {"message": "Category successfully deleted"}
    else:
        return {"error": "Category not found"}

# Route to delete a car (admin)
@app.route('/deletecar/<int:model_id>', methods=['DELETE'])
def deletecar(model_id):
    car = db.session.query(Cars).filter_by(model_id=model_id)
    if car:
        car.delete()
        db.session.commit()
        return {"message": "Car successfully deleted"}
    else:
        return {"error": "Car not found"}

# Route to modify a category (admin)
@app.route('/modifycategory/<int:category_id>', methods=['PUT'])
def modify_category(category_id):
    if request.is_json:
        if category_id:
            data = request.get_json()
            fields = (
                'name',
                'description', 
            )
            for item in data.keys():
                if item in fields:
                    print(data[item])
                    db.session.query(Categories).filter_by(category_id=category_id).update(
                    {
                        item: data[item]
                    })
            db.session.commit()
            return {"message": "Category successfully modified"}
        else:
            return {"error": "Category not found"}
    else:
        return {"error": "The request payload is not in JSON format"}

# Route to modify the car details
@app.route('/modifycar/<int:model_id>', methods=['PUT'])
def modifycar(model_id):
    if request.method == 'PUT':
        if 'img' in request.files:
            file = request.files['img']
            filename = file.filename.lower()
            if filename == '':
                return {"error": "No file selected"}

            if file and allowed_file(filename):
                file_path = app.config['UPLOAD_FOLDER'] + "/" + filename
                file.save(file_path)

                data = dict(request.form)

                fields = (
                    'name',
                    'year', 
                    'color',
                    'price',
                    'category_id',
                    'description',
                )
                for item in data.keys():
                    if item in fields:
                        db.session.query(Cars).filter_by(model_id=model_id).update(
                        {
                            item: data[item]
                        })
                db.session.query(Cars).filter_by(model_id=model_id).update(
                {
                    'img_name': filename
                })
                db.session.commit()
                return {"message": "Car successfully updated"}
            else:
                return {"error": "The file is not in the allowed format"}
        else:
            data = dict(request.form)
            fields = (
                'name',
                'year',
                'color', 
                'price', 
                'category_id',
                'description',
            )
            for item in data.keys():
                if item in fields:
                    db.session.query(Cars).filter_by(model_id=model_id).update(
                    {
                        item: data[item]
                    })
            db.session.commit()
            return {"message": "Car succesfully updated!"}

# Route to get all testdrives (admin)
@app.route('/admintestdrives', methods=['GET'])
def testdrives():
    testdriveData = Testdrives.query.all()
    return jsonify(TestdrivesSchema(many=True).dump(testdriveData))

# Route to get all bookings (admin)
@app.route('/adminbookings', methods=['GET'])
def bookings():
    bookingsData = Bookings.query.all()
    carData=[]
    for element in bookingsData:
        carData.append(Cars.query.filter_by(model_id=element.model_id).first())
    for index in range(len(carData)):
        if carData[index].model_id == bookingsData[index].model_id:
            bookingsData[index].name = carData[index].name
        print(bookingsData)
    return jsonify(BookingsSchema(many=True).dump(bookingsData))

# Route to get all customers (admin)
@app.route('/admincustomers', methods=['GET'])
def customers():
    customerData = Customer.query.all()
    return jsonify(CustomersSchema(many=True).dump(customerData))

# # Route to get all categories (admin)
@app.route('/admincategories', methods=['GET'])
def categories():
    categoryData = Categories.query.all()
    return jsonify(CategoriesSchema(many=True).dump(categoryData))




# Route to request forgotten password
@app.route('/forgotpassword', methods=['POST'])
def forgotpassword():
    if request.method == 'POST':
        data = request.get_json()
        email = data['email']
        user = Customer.query.filter_by(email=email).first()
        if user:
            password = Customer.query.filter_by(email=email).first().password
            msg = Message(
                'Password Recovery',
                sender = os.getenv('GMAIL_USERNAME'),
                recipients = [email],
                body = "You recently requested for your password through Rapid Motors Online Portal\nIf this wasn't you, please get in touch with us as soon as possible.\n\n\n Your Password is: " + password
            )
            mail.send(msg)
            print("Email has been sent!")
            return {"message": "Email has been sent!"}
        else:
            return {"error": "User not found"}
    else:
        return {"error": "Invalid request"}
