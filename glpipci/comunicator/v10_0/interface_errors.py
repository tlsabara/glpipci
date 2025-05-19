class GlpiClientGenericError(Exception):
    BASE_MESSAGE = "Generic error"

    def __init__(self, msg=None):
        self.msg = msg or self.BASE_MESSAGE

    def __str__(self):
        return repr(self.msg)

class InitSessionError(GlpiClientGenericError):
    BASE_MESSAGE =  "request to Session init failed."

class ClientGlpiError400(GlpiClientGenericError):
    BASE_MESSAGE =  "The server returns a 400 Bad Request."

class ClientGlpiError401(GlpiClientGenericError):
    BASE_MESSAGE =  "The server returns a 401 Unauthorized."

class ClientGlpiError404(GlpiClientGenericError):
    BASE_MESSAGE =  "The server returns a 404 Not Found."

class ClientGlpiConfigurationError(GlpiClientGenericError):
    BASE_MESSAGE =  "Missing configuration for the client. Check the docs"