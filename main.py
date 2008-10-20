import wsgiref.handlers,logging, presenter, os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from helpers import utils
from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users

class MainHandler(webapp.RequestHandler):
    def get(self,url=None):
        pointset = presenter.get_points_for(url)
        template_values = {'points':pointset}
        self.response.out.write(users.create_login_url("/"))
        self.response.out.write(template.render(utils.path('templates/index.html'),template_values ))
        
    def post(self, url=None):
        pass
    

        

ROUTES =    [
            (r'/(.*)', MainHandler),
            (r'/(.*)/setpoint', MainHandler)
            ]


def createMainApplication():
    return webapp.WSGIApplication(ROUTES,debug=True)
                                        
def main():
    wsgiref.handlers.CGIHandler().run(createMainApplication())

if __name__ == '__main__':
    main()