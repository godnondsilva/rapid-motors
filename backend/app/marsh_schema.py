from marshmallow import Schema

class CarsSchema(Schema):
    class Meta:
        fields = ('model_id', 'name', 'year', 'img_name', 'color', 'price', 'category_id', 'description', 'admin_id')   
        
class TestdrivesSchema(Schema):
    class Meta:
        fields = ('testdrive_id', 'model_id', 'cust_id', 'testdrive_date', 'state', 'city', 'comments') 

class BookingsSchema(Schema):
    class Meta:
        fields = ('booking_id', 'model_id', 'cust_id', 'booking_color', 'booking_date','booking_price', 'name')

class CustomersSchema(Schema):
    class Meta:
        fields = ('cust_id', 'name', 'email', 'phone', 'address')

class CategoriesSchema(Schema):
    class Meta:
        fields = ('category_id', 'name', 'description')
