from lib.view import View

class Index(View):
    def get(self):
        self.render('index.html', dict())