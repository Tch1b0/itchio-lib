# itchio-lib
Since I didn't find one, I made it on my own.

## Purpose
Use the REST-API of itch.io in python in a simple way

## Examples
```py
import itchio

session = itchio.Session("1234")
#                        ^
#                        This is your API-key

userCollection = itchio.UserCollection(session)

me = userCollection.me()

print(me.username)
```
```
Tch1b0
```

## Installation
This library is currently **not** available on [pypi](https://pypi.org).
However, you can still install this library using [pip](https://pypi.org/project/pip/).
```
$ pip install git+https://github.com/Tch1b0/itchio-lib.git#egg=itchio
```