from django.contrib import auth
from django.contrib.auth.middleware import RemoteUserMiddleware

class SimmonsAuthMiddleware(RemoteUserMiddleware):
    header = "SSL_CLIENT_S_DN_Email"

    def clean_username(self, username, request):
        if '@' in username:
            name, domain = username.split('@')
            assert domain.upper() == 'MIT.EDU'
            return name
        else:
            return username
    #
    # def process_request(self, request):
    #     try:
    #         username = request.META[self.header]
    #     except KeyError:
    #         if request.user.is_authenticated():
    #             auth.logout(request)
    #         return
    #
    #     if request.user.is_authenticated():
    #         if request.user.get_username() == self.clean_username(username, request):
    #             return
    #
    #     user = auth.authenticate(username=self.clean_username(username, request),
    #                              password='')
    #     if user:
    #         request.user = user
    #         auth.login(request, user)
