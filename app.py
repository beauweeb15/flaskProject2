from flask import Flask, render_template


app = Flask(__name__)


# TODO: add authentication when login system is working
# TODO: add the database implementations
# TODO: add admin user roles and make them be able to access the fish adding database
# TODO: for whatever reason the code isn't finding other links within the project altogether (might need to create blueprint files for each link)
# TODO: (low priority) add the user's name to the home screen when they login
# TODO: (low priority) figure out how to change the background color

@app.route('/')
def index():
    return render_template('main/index.html')


@app.errorhandler(400)
def bad_request(error):
    return render_template('400.html')


@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html')


@app.errorhandler(503)
def service_unavailable(error):
    return render_template('503.html')


if __name__ == '__main__':
    app.run()
