import models,logging
from google.appengine.api import users
from google.appengine.ext import db



def get_points_for(url):
    customer = models.Customer.all().filter('url =',url).fetch(1)
    pointset = []
    if len(customer) == 0:
        return pointset
    for point in customer[0].points:
        pointset.append(dict(lat = point.point.lat,lon = point.point.lon,title = point.title))
    return pointset

def set_point(customer, lat, lon):
    newpoint = models.Point(point = db.GeoPt(lat,lon), owner = customer, parent = customer)
    newpoint.put()
    return True

def create_customer(url, user):
    if models.Customer.all().filter('url =',url.lower()).fetch(1).__len__() > 0:
        raise Exception, "URL already exists."
    if models.Customer.all().filter('user =',user).fetch(1).__len__() > 0:
        raise Exception, "This user already has an account and URL."
    new_customer = models.Customer(url = url, user = user)
    new_customer.put()
    return new_customer



    
    