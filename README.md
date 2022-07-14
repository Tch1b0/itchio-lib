# itchio-lib

Use the REST-API of itch.io with python in a simple way.

## Installation

You can install this library via [pip](https://pypi.org):

```
$ pip install itchio
```

You **may** need to install the `typing` module, depending on your python version.

## Documentation

You can read the docs [right here](https://tch1b0.github.io/itchio-lib/)

## How does it work?

When you want to use the lib, you first need to create a `Session` object, in which you have to pass your
API-key. It could look something like this:

```py
import itchio

session = itchio.Session(key)
```

If you want to access your games, you can just now create an `GameCollection` object with your session.

```py
gameCollection = itchio.GameCollection(session)
```

After that you can get a game by its `id` or you can just get all of your games.

```py
all_my_games = gameCollection.all()
```

The `all_my_games` variable is now a list containing Game objects. You can now easily access the information of a game.

```py
my_game = all_my_games[0]

print(my_game.views_count)
```

```
35
```

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
