from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class NotFound(webapp.RequestHandler):
  # Constructor
  def get(self):
    # Set the file name
    self.path = 'templates/error404.html'
    self.render()
  
  # Method for rendering the page
  def render(self):
    # Prepare the page
    template_values = { }
    
    # Render this template
    self.response.out.write(template.render(self.path, template_values))
  
application = webapp.WSGIApplication([('/.*', NotFound)], debug=False)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()

  