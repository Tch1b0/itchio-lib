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