import os

from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import template
from google.appengine.api import users

class View(webapp.RequestHandler):
  def render(self, template_name, template_values={}):
    user = users.get_current_user()
    if user:
        log_in_out_url = users.create_logout_url('/')
    else:
        log_in_out_url = users.create_login_url(self.request.uri)

    values = {'user': user, 'log_in_out_url': log_in_out_url}
    values.update(template_values)

    directory = os.path.dirname(__file__)
    directory = os.path.dirname(directory)
    path = os.path.join(directory, 'templates', template_name)

    return self.response.out.write(template.render(path, values))