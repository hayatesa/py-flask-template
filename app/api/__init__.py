from app.exception.AuthException import AuthException

from app import app
from app.util.Resp import failure


@app.errorhandler(400)
def not_found(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(401)
def not_found(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(403)
def not_found(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(404)
def not_found(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(500)
def not_found(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(AuthException)
def not_found(e):
    return failure(message=e.message)


@app.errorhandler(Exception)
def not_found(e):
    return failure(message='Something Wrong. Please Try again.')
