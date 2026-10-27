# pieforhead

A python wrapper for the PieFed API supporting both synchronous and asynchronous usage. This is an early work in progress, and few endpoints are supported yet.

![pieforhead logo](logo.png)

## Usage Notes

In general, all successful requests to the server should return a `dict` with the server's json response. Due to the alpha nature of the PieFed API, the maintenance burden of creating and updating response models as features/fields are added to the API is a burden that I don't want to take on at this time. Please refer to the official PieFed OpenAPI specification ([stable version](https://stable.wjs018.xyz/api/alpha/swagger), [development version](https://crust.piefed.social/api/alpha/swagger)) to see what your code should expect as a response.

By default, exceptions will be raised if something goes wrong (e.g. malformed request, network timeout, 5XX errors, etc.) to provide a trace. However, to suppress these exceptions, you can pass the `raise_exceptions=False` keyword argument when instantiating your client. This will cause a returned value of `None` instead of raising an exception. Please make sure that your code handles such a case appropriately.

## Synchronous Client Usage

Users familiar with network libraries like `requests` would probably be most familiar with synchronous usage. However, to make network requests a bit more efficient, this library makes use of `Client`s within `httpx` where you can take advantage of connection pooling for multiple network requests. This means that when you instantiate a `PieFed` class, it is best practice to close it when you are done with it. Here are a couple examples that show how this can be done.

These snippets all do the same three things:

1. Create a `PieFed` object with the given instance url (this creates the client)
2. Log in using a username and password
3. Close the client after we no longer need it

Closing it manually using the `close` function:

```python
from piefedhead import PieFed

piefed = PieFed("https://instance.tld")
piefed.log_in("username", "password")

piefed.close()
```

Using a context manager (a `with` block):

```python
# Inside a context manager
with PieFed("https://instance.tld") as piefed:
    piefed.log_in("username", "password")

# The connection is closed after leaving the `with` block
```

Using a callback that ensures the `close` function is called when execution has ended:

```python
# Registering an event handler
import atexit

piefed = PieFed("https://instance.tld")
atexit.register(piefed.close)  # Automatically closes the client at program termination
```

## Asynchronous Client Usage

To use this libray in an async manner, there is a separate client, `PieFedAsync` that should be used. Everything else should work exactly the same as the synchronous client, except that results will need to be `await`ed.

Here is a snippet that does the same three actions as outlined above for the synchronous client, but using the `PieFedAsync` client.

```python
# Put things in an async function so that we can use the await keyword
async def main():
    piefed_async = PieFedAsync("https://instance.tld")
    await piefed_async.log_in("username", "password")  # Notice the await keyword

    await piefed_async.close()

# Start the event loop and execute the async function
asyncio.run(main())
```

Similar to the synchronous client, you can also use a context handler to automatically close the async client:

```python
async def main():
    async with PieFedAsync("https://instance.tld") as piefed_async:
        await piefed_async.log_in("username", "password")

    # Client is closed automatically once outside the context handler

# Start the event loop and execute the async function
asyncio.run(main())
```

## Endpoint Coverage

This project is in an early stage. Here is a high level summary of where things stand with implementing the wrapper around different PieFed API endpoint groups:

| Endpoint Group  | Sync Client | Async Client | Notes                                    |
| :-------------: | :---------: | :----------: | :--------------------------------------- |
|      Site       |     ✅      |      ✅      | Instance chooser endpoints unimplemented |
|     Upload      |     ✅      |      ✅      |                                          |
|      User       |     🟡      |      🟡      | Auth endpoints implemented               |
|      Post       |     ❌      |      ❌      |                                          |
|     Comment     |     ❌      |      ❌      |                                          |
|    Community    |     ❌      |      ❌      |                                          |
|      Feed       |     ❌      |      ❌      |                                          |
|      Topic      |     ✅      |      ✅      |                                          |
| Private Message |     ❌      |      ❌      |                                          |
|      Admin      |     ❌      |      ❌      |                                          |
|      Misc.      |     ❌      |      ❌      |                                          |
