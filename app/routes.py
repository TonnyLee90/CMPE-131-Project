from app import myapp

@myapp.route('/')
def home():
    return "home page"

@myapp.route('/test')
def test():
    return "test123"
