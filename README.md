# MojangAuth-Python
A lib for mojang authentification.

## Made with
* [**requests**](https://pypi.org/project/requests/)

## Install prerequisites
* Execute command: ```pip3 install MojangAuthPython```

## Examples

### Simple Authentification
```python
from MojangAuth import MojangAuth

mojang_auth = MojangAuth()

mojang_auth.auth("email", "password")

access_token = mojang_auth.access_token # return access token (str)
client_token = mojang_auth.client_token # return client token (str)
profile = mojang_auth.profile # return selected profile (list)
username = mojang_auth.username # return username (str)
id = mojang_auth.id #str : return id (str)
```

### Refresh Token
```python
from MojangAuth import MojangAuth

mojang_auth = MojangAuth()

mojang_auth.refresh("accessToken", "clientToken")
```

### Validate Token
```python
from MojangAuth import MojangAuth

mojang_auth = MojangAuth()

mojang_auth.validate("accessToken", "clientToken") # return True if token is good and False if not
```

### Invalidate Token
```python
from MojangAuth import MojangAuth

mojang_auth = MojangAuth()

mojang_auth.invalidate("accessToken", "clientToken") # invalidated token and return True if token is good and False if not
```

### Sign-out

```python
from MojangAuth import MojangAuth

mojang_auth = MojangAuth()

mojang_auth.sign_out("email", "password")  # sign-out user and return True if user successfully sign-out and False if not
```

## Author
[<img width="64" src="https://avatars3.githubusercontent.com/u/59535754?s=400&u=48aecdd175dd2dd8867ae063f1973b64d298220b&v=4" alt="Asthowen">](https://github.com/Asthowen)

## License
**[MojangAuth-Python](https://github.com/Asthowen/MojangAuthPython) | [Mozilla Public License 2.0](https://github.com/Asthowen/MojangAuthPython/blob/main/LICENSE)**