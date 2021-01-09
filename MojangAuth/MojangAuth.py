from requests import post
import json as j


class AuthException(Exception):
    def __init__(self, json: str):
        self.json_error = j.loads(json)
        self.message = self.json_error['error'] + ': ' + self.json_error['errorMessage']
        super().__init__(self.message)


class TokenNotFoundException(Exception):
    def __init__(self):
        super().__init__("Token not found.")


class ServerEndpoint(enumerate):
    BASE_URL = 'https://authserver.mojang.com/'
    AUTHENTICATE = 'authenticate'
    REFRESH = 'refresh'
    VALIDATE = 'validate'
    INVALIDATE = 'invalidate'
    SIGNOUT = 'signout'


class MojangAuth(object):

    def __init__(self):
        self._access_token = ''
        self._client_token = ''
        self._profile = []
        self._username = ''
        self._id = ''

    def send_request(self, server_endpoint: str, json: dict):
        return post(ServerEndpoint.BASE_URL + server_endpoint, json=json)

    def auth(self, email: str, password: str):
        json = {
            "agent": {
                "name": "Minecraft",
                "version": 1
            },
            "username": email,
            "password": password,
        }

        request_response = self.send_request(ServerEndpoint.AUTHENTICATE, json)

        if request_response.status_code == 200:
            request_return = j.loads(request_response.text)
            self._access_token = request_return['accessToken']
            self._client_token = request_return['clientToken']
            self._profile.append(request_return['selectedProfile']['name'])
            self._profile.append(request_return['selectedProfile']['id'])
            self._username = request_return['selectedProfile']['name']
            self._id = request_return['selectedProfile']['id']
        else:
            raise AuthException(request_response.text)

    def refresh(self, access_token: str, client_token: str):
        json = {
            "accessToken": access_token,
            "clientToken": client_token
        }

        request_response = self.send_request(ServerEndpoint.REFRESH, json)

        if request_response.status_code == 200:
            request_return = j.loads(request_response.text)
            self._access_token = request_return['accessToken']
            self._client_token = request_return['clientToken']
            self._profile.append(request_return['selectedProfile']['name'])
            self._profile.append(request_return['selectedProfile']['id'])
            self._username = request_return['selectedProfile']['name']
            self._id = request_return['selectedProfile']['id']
        else:
            raise AuthException(request_response.text)

    def validate(self, access_token: str, client_token: str):
        json = {
            "accessToken": access_token,
            "clientToken": client_token
        }

        request_response = self.send_request(ServerEndpoint.VALIDATE, json)

        if request_response.status_code == 204:
            return True
        else:
            raise TokenNotFoundException()

    def invalidate(self, access_token: str, client_token: str):
        json = {
            "accessToken": access_token,
            "clientToken": client_token
        }

        request_response = self.send_request(ServerEndpoint.INVALIDATE, json)

        if request_response.status_code == 204:
            return True
        else:
            raise TokenNotFoundException()

    def signout(self, username: str, password: str):
        json = {
            "username": username,
            "password": password
        }

        request_response = self.send_request(ServerEndpoint.SIGNOUT, json)

        if request_response.status_code == 204:
            return True
        else:
            return False

    @property
    def access_token(self):
        return self._access_token

    @property
    def client_token(self):
        return self._client_token

    @property
    def profile(self):
        return self._profile

    @property
    def username(self):
        return self._username

    @property
    def id(self):
        return self._id