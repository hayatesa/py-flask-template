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
