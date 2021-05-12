from requests import post
import json


class AuthException(Exception):
    def __init__(self, request: str):
        self.json_error = json.loads(request)
        self.message = self.json_error['error'] + ': ' + self.json_error['errorMessage']
        super().__init__(self.message)


class ServerEndpoint(enumerate):
    BASE_URL = 'https://authserver.mojang.com/'
    AUTHENTICATE = 'authenticate'
    REFRESH = 'refresh'
    VALIDATE = 'validate'
    INVALIDATE = 'invalidate'
    SIGNOUT = 'signout'


class MojangAuth(object):

    def __init__(self):
        self.__access_token = ''
        self.__client_token = ''
        self.__profile = []
        self.__username = ''
        self.__id = ''

    @staticmethod
    def send_request(server_endpoint: str, request: dict):
        return post(ServerEndpoint.BASE_URL + server_endpoint, json=request)

    def auth(self, email: str, password: str):
        request = {
            "agent": {
                "name": "Minecraft",
                "version": 1
            },
            "username": email,
            "password": password,
        }

        request_response = self.send_request(ServerEndpoint.AUTHENTICATE, request)

        if request_response.status_code == 200:
            request_return = json.loads(request_response.text)

            self.__access_token = request_return['accessToken']
            self.__client_token = request_return['clientToken']
            self.__profile.append(request_return['selectedProfile']['name'])
            self.__profile.append(request_return['selectedProfile']['id'])
            self.__username = request_return['selectedProfile']['name']
            self.__id = request_return['selectedProfile']['id']
        else:
            raise AuthException(request_response.text)

    def refresh(self, access_token: str, client_token: str):
        request = {
            "accessToken": access_token,
            "clientToken": client_token
        }

        request_response = self.send_request(ServerEndpoint.REFRESH, request)

        if request_response.status_code == 200:
            request_return = json.loads(request_response.text)
            self.__access_token = request_return['accessToken']
            self.__client_token = request_return['clientToken']
            self.__profile.append(request_return['selectedProfile']['name'])
            self.__profile.append(request_return['selectedProfile']['id'])
            self.__username = request_return['selectedProfile']['name']
            self.__id = request_return['selectedProfile']['id']
        else:
            raise AuthException(request_response.text)

    def validate(self, access_token: str, client_token: str) -> bool:
        request = {
            "accessToken": access_token,
            "clientToken": client_token
        }

        request_response = self.send_request(ServerEndpoint.VALIDATE, request)

        return True if request_response.status_code == 204 else False

    def invalidate(self, access_token: str, client_token: str) -> bool:
        request = {
            "accessToken": access_token,
            "clientToken": client_token
        }

        request_response = self.send_request(ServerEndpoint.INVALIDATE, request)

        return True if request_response.status_code == 204 else False

    def sign_out(self, username: str, password: str) -> bool:
        request = {
            "username": username,
            "password": password
        }

        request_response = self.send_request(ServerEndpoint.SIGNOUT, request)

        return True if request_response.status_code == 204 else False

    @property
    def access_token(self) -> str:
        return self.__access_token

    @property
    def client_token(self) -> str:
        return self.__client_token

    @property
    def profile(self) -> list:
        return self.__profile

    @property
    def username(self) -> str:
        return self.__username

    @property
    def id(self) -> str:
        return self.__id
