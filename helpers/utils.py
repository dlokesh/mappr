import os,logging, gateway
from google.appengine.api import users
def path(p='/'):
    return os.path.join(os.path.dirname(__file__), '../'+p )
    
def authdetails(page = "/"):
    user = users.get_current_user()
    if user: 
        label = "Logout"
        link = users.create_logout_url(page)
        status = 1
        customer = gateway.get_customer(user)
        url = customer.url if customer else None
    else:
        label = "Login"
        link = users.create_login_url(page)
        status = 0
        url = None
    return dict(status = status,link = link,label=label,url=url)
    
def authorize(role):
    def wrapper(handler_method):
        def check_login(self, *args, **kwargs):
            user = users.get_current_user()
            if not user:
                if self.request.method != 'GET':
                    self.error(403)
                else:
                    self.redirect(users.create_login_url(self.request.uri))
            elif role == "user" or (role == "admin" and users.is_current_user_admin()):
                handler_method(self, *args, **kwargs)
            else:
                if self.request.method == 'GET':
                    self.redirect("/403.html")
                else:
                    self.error(403)
        return check_login
    return wrapper