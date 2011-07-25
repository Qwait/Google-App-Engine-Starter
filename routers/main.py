from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from views import root

def main():
    application = webapp.WSGIApplication([
        ('/', root.Index),
    ], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
