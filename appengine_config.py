from lib.session import SessionMiddleware

COOKIE_KEY = '029b90d7056d130df2830a3be0030a95'

def webapp_add_wsgi_middleware(app):
    app = SessionMiddleware(app, cookie_key=COOKIE_KEY)
    return app