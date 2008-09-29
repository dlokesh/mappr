import unittest
import logging
import models
from google.appengine.ext import db
from google.appengine.api import users


class BasicModelTests(unittest.TestCase):
    def setUp(self):
        self.sudhir_gmail = users.User('sudhir.j@gmail.com')
        self.amrita_gmail = users.User('amrita@gmail.com')
        
    def test_customer_validations(self):
        self.assertRaises(ValueError,models.Customer,None)
        self.assertRaises(ValueError,models.Customer,user = self.sudhir_gmail)
        self.assertRaises(db.BadValueError,models.Customer,url='check')
        new_customer = models.Customer(url='check',user = self.sudhir_gmail)
        self.assertTrue(new_customer)
        self.assertTrue(new_customer.put())
        logging.info(new_customer.put())
    
    def test_point_validations(self):
        self.assertRaises(db.BadValueError,models.Point,None)
        self.assertRaises(db.BadValueError,models.Point,lat=34.445)
        self.assertRaises(db.BadValueError,models.Point,lon=36.345)
        self.assertTrue(models.Point(lat=34.45,lon=32.466))
        self.assertTrue(models.Point(lat=-34.45,lon=32.466))
        self.assertRaises(ValueError,models.Point,lat=float(3462.344),lon=float(45.67))
        self.assertRaises(ValueError,models.Point,lat=float(34.344),lon=float(-2345.67))
        
        
        
        
    
    
        


# class ModelTest(unittest.TestCase):
# 
#   def setUp(self):
#     # Populate test entities.
#     entity = model.MyEntity(name='Bar')
#     self.setup_key = entity.put()
# 
#   def tearDown(self):
#     # There is no need to delete test entities.
#     pass
# 
#   def test_new_entity(self):
#     entity = model.MyEntity(name='Foo')
#     self.assertEqual('Foo', entity.name)
# 
#   def test_saved_enitity(self):
#     entity = model.MyEntity(name='Foo')
#     key = entity.put()
#     self.assertEqual('Foo', db.get(key).name)
# 
#   def test_setup_entity(self):
#     entity = db.get(self.setup_key)
#     self.assertEqual('Bar', entity.name)
# 
# 
