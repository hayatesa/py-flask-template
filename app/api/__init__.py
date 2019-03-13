from app.exception.LoginException import LoginException
from app.exception.AuthException import AuthException
from app import app, APPLICATION_CONFIG
from app.exception.TokenException import TokenException
from app.util.Resp import failure

context_path = APPLICATION_CONFIG['server'].get('context_path', '')
version = APPLICATION_CONFIG.get('version')


@app.errorhandler(400)
def bad_request(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(401)
def unauthorized(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(403)
def forbidden(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(404)
def not_found(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(405)
def method_not_allowed(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(500)
def internal_server_error(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(AuthException)
def auth_exception(e):
    return failure(message=e.message)


@app.errorhandler(TokenException)
def token_exception(e):
    return failure(message=e.message, status_code=401)


@app.errorhandler(LoginException)
def login_exception(e):
    return failure(message=e.message)


@app.errorhandler(Exception)
def exception(e):
    return failure(message=e.msg, status_code=500)
