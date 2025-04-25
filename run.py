from user_profile import user_profile
from search import search


from flask import Flask
from user_profile import user_profile
from search import search

app = Flask(__name__)
app.secret_key = 'your-secret-key'

app.register_blueprint(user_profile)
app.register_blueprint(search)

if __name__ == "__main__":
    app.run(debug=True)

