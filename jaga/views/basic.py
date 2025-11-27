# a simple test page to test the construct
def basic():
    return "Test ok!"


def register_views(app):
    app.add_url_rule("/basic", view_func=basic)
