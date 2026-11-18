---
icon: material/brain
title: Design Philosophy
description: Design Philosophy
---

# Design Philosophy

At a high level, this library intends to match each API endpoint in the PieFed API to a python function. The PieFed API undergoes a lot of development and changes relatively frequently. So, to help keep things consistent, there are a couple decisions I have made to keep this library relatively easy to update as the PieFed API is updated.

## Server Responses

In general, the majority of endpoints return json and a status of 200. Pieforhead simply deserializes the returned json into a dict and this is then returned from the function. This means that if fields are added or removed from the PieFed API going forward, this library is able to keep up to date. This means that there is no response models e.g. a `User` class that an endpoint like `GET user` returns. If you want object-oriented models, these would need to be built by your program from the data that Pieforhead returns.

There are some endpoints for which there is no json returned, and the server just returns a 200 status code. Pieforhead, instead of returning an empty dict, instead returns a boolean `True`. This is so that these functions don't return something falsey on a successful request. These exceptions should be type-hinted where they occur.

When there is an issue with a request and a non-200 status code is returned, pieforhead will raise an exception by default. PieFed returns a standard error structure, so pieforhead will raise an exception that includes any message from the server that was returned from the response. If you want bad server responses to fail silently and not raise an exception, initialize your client with `#!python raise_exceptions=False`.

=== "Synchronous"

    ```python hl_lines="3"
    from pieforhead import PieFed

    piefed = PieFed("https://instance.tld", raise_exceptions=False)
    ```

=== "Asynchronous"

    ```python hl_lines="5"
    import asyncio
    from pieforhead import PieFedAsync

    async def main():
        piefed = PieFedAsync("https://instance.tld", raise_exceptions=False)
    
    asyncio.run(main())
    ```

## Function Names

Where possible, I have tried to keep functions organized in a way that mirrors the API endpoints. As an example, the `GET user/mentions` endpoint can be called from the root `PieFed` class at `user.mentions()`. There are some endpoints where I have slightly rephrased them to make it clearer what the function does or there are multiple operations at the same url, but with different HTTP methods. An example of this would be that the `GET user/notifications` endpoint can be reached from the `user.get_notifications()` function. Finally, there are some cases where I have changed the name from the endpoint to avoid conflicting with reserved words in python. An example of this last type would be the `GET post/list` is accessed at `post.list_posts()` to avoid ambiguity of the `list` type in python.

I have tried to add the actual API endpoint that each function is reaching out to in the docstring for that function. They should all be documented in the [API reference](reference/pieforhead) section of these docs.

## Network Clients

This library makes use of Clients within the [httpx](https://www.python-httpx.org/) network request library. This means they can take advantage of some optimizations that make network requests faster and less computationally expensive. For more discussion of this, see the [Clients page](https://www.python-httpx.org/advanced/clients/) in the httpx docs. Clients are used for both the synchronous and asynchronous sides of the code within this library.

In practical terms, this means that when you create a `PieFed` object to make API requests, you should close down the client when you are done using it so that any persistent connections are properly closed. This can be done in two main ways using either the synchronous or async clients. In the examples below, we create a `PieFed` object, log in a hypothetical user, and then close down the client.

First, you can make an explicit call to the `close` function:

=== "Synchronous"

    ```python hl_lines="5"
    from pieforhead import PieFed

    piefed = PieFed("https://instance.tld")
    piefed.login("username", "password")
    piefed.close()
    ```

=== "Asynchronous"

    ```python hl_lines="7"
    import asyncio
    from pieforhead import PieFedAsync

    async def main():
        piefed = PieFedAsync("https://instance.tld")
        await piefed.login("username", "password")
        await piefed.close()
    
    asyncio.run(main())
    ```

Alternatively, you can open the client using a context handler (a `with` block). Then, it will be closed automatically after exiting the context manager:

=== "Synchronous"

    ```python hl_lines="3-4"
    from pieforhead import PieFed

    with PieFed("https://instance.tld") as piefed:
        pieforhead.login("username", "password")
    
    # The connection is closed once your program leaves the with block
    ```

=== "Asynchronous"

    ```python hl_lines="5-6"
    import asyncio
    from pieforhead import PieFedAsync

    async def main():
        async with PieFedAsync("https://instance.tld") as piefed:
            await piefed.login("username", "password")
        
        # The connection is closed once your program leaves the async with block
    
    asyncio.run(main())
    ```
