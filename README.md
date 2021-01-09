# MojangAuth-Python

A lib for mojang authentification.

## Made with

* [**requests**](https://pypi.org/project/requests/)

## Examples

**Simple Authentification :**
```python
from MojangAuth import MojangAuth

mojang_auth = MojangAuth()

mojang_auth.auth("email", "password")

access_token = mojang_auth.access_token #str : return access token
client_token = mojang_auth.client_token #str : return client token
profile = mojang_auth.profile #list : return selected profile
username = mojang_auth.username #str : return username
id = mojang_auth.id #str : return id
```

**Refresh Token :**
```python
from MojangAuth import MojangAuth

mojang_auth = MojangAuth()

mojang_auth.refresh("access token", "client token")
```

**Validate Token :**
```python
from MojangAuth import MojangAuth

mojang_auth = MojangAuth()

mojang_auth.validate("access token", "client token") #return True if token is good and False if not

```

**Invalidate Token :**
```python
from MojangAuth import MojangAuth

mojang_auth = MojangAuth()

mojang_auth.invalidate("access token", "client token") #invalide token and return True if token is good and False if not

```

**Signout :**
```python
from MojangAuth import MojangAuth

mojang_auth = MojangAuth()

mojang_auth.signout("email", "password") #signout user and return True if user successfully signout and False if not

```

## Author

[<img width="64" src="https://avatars3.githubusercontent.com/u/59535754?s=400&u=48aecdd175dd2dd8867ae063f1973b64d298220b&v=4" alt="Asthowen">](https://github.com/Asthowen)

## License

**DiscordBotPihole | Mozilla Public License 2.0**