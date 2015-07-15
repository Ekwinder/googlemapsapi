"""
we make a web application to get the list of directions from maps.py
and show it in html.
"""

import web
import maps

urls = (
  '/', 'Index',
)

app = web.application(urls, globals())


render = web.template.render('templates/')
class Index(object):
    def GET(self):
        return render.index(None)
    def POST(self):
    	# we take input from the form and parse the xml
    	# and according to the url return the list to the 
    	# interface
        form = web.input(start ='mohali', end ='chandigarh')
        start = str(form.start)
        end = str(form.end)
        x = maps.Directions(start,end)

        return render.index(x)


if __name__ == "__main__":
    app.run()