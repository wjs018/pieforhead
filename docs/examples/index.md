---
icon: material/lightbulb-on-outline
title: Examples
description: Some examples of Pieforhead usage.
---

# Examples

Below are some basic working examples.

## Authentication

Logging into a PieFed instance and making authenticated requests is done by username/password. As of my writing this, the recently added TOTP option is not available via the API. Logging in using the `PieFed` object is fairly straightforward:

=== "Synchronous"

    ```python hl_lines="4"
    from pieforhead import PieFed

    piefed = PieFed("https://instance.tld")
    piefed.login("username", "password")
    # Do stuff here...
    piefed.close()
    ```

=== "Asynchronous"

    ```python hl_lines="6"
    import asyncio
    from pieforhead import PieFedAsync

    async def main():
        piefed = PieFedAsync("https://instance.tld")
        await piefed.login("username", "password")
        # Do stuff here...
        await piefed.close()
    
    asyncio.run(main())
    ```

After a successful call to the `login` function, each subsequent request is authenticated with that user's credentials. If you wish to make unauthenticated requests after logging in, then you have two options.

1. The `forget_credentials` function will simply make the client erase its saved credentials without invalidating them. This preserves logged-in sessions elsewhere that use the API, like mobile apps or alternative frontends.
2. The `log_out` function will invalidate the API credentials for the user on the server side by making an API request to the server. This will likely invalidate every API session that the user has and has a pretty low rate-limit on the server.

In general, most applications should just need the `forget_credentials` function if you need to make unauthenticated requests after logging in. If you need to make authenticated requests after calling `forget_credentials`, then you will need to call the `login` function once again.

=== "Synchronous"

    Here is how you can use the `forget_credentials` function:

    ```python hl_lines="6"
    from pieforhead import PieFed

    piefed = PieFed("https://instance.tld")
    piefed.login("username", "password")
    user_info = piefed.user.get(person_id=42)  # Authenticated request
    piefed.forget_credentials()
    user_info = piefed.user.get(person_id=42)  # Un-authenticated request
    piefed.close()
    ```

    Here is how you can use the `log_out` function:

    ```python hl_lines="6"
    from pieforhead import PieFed

    piefed = PieFed("https://instance.tld")
    piefed.login("username", "password")
    user_info = piefed.user.get(person_id=42)  # Authenticated request
    piefed.log_out()
    user_info = piefed.user.get(person_id=42)  # Un-authenticated request
    piefed.close()
    ```
    

=== "Asynchronous"

    Here is how you can use the `forget_credentials` function:

    ```python hl_lines="8"
    import asyncio
    from pieforhead import PieFedAsync

    async def main():
        piefed = PieFedAsync("https://instance.tld")
        await piefed.login("username", "password")
        user_info = await piefed.user.get(person_id=42)  # Authenticated request
        piefed.forget_credentials()  # Does not need to be awaited
        user_info = await piefed.user.get(person_id=42)  # Un-authenticated request
        await piefed.close()
    
    asyncio.run(main())
    ```

    Here is how you can use the `log_out` function:

    ```python hl_lines="8"
    import asyncio
    from pieforhead import PieFedAsync

    async def main():
        piefed = PieFedAsync("https://instance.tld")
        await piefed.login("username", "password")
        user_info = await piefed.user.get(person_id=42)  # Authenticated request
        await piefed.log_out()  # Needs to be awaited because it is making an API request
        user_info = await piefed.user.get(person_id=42)  # Un-authenticated request
        await piefed.close()
    
    asyncio.run(main())
    ```

## Post/Comment Creation

This example creates a basic post and then creates a comment as a reply to the post.

=== "Synchronous"

    ```python
    from pieforhead import PieFed

    piefed = PieFed("https://instance.tld")
    piefed.login("username", "password")
    post_info = piefed.post.create(title="test post, please ignore", community_id=42, body="This is just a test...")
    post_id = post_info["post_view"]["post"]["id"]
    comment_info = piefed.comment.create(post_id=post_id, body="Here is a test comment...")
    piefed.close()
    ```

=== "Asynchronous"

    ```python
    import asyncio
    from pieforhead import PieFedAsync

    async def main():
        piefed = PieFedAsync("https://instance.tld")
        await piefed.login("username", "password")
        post_info = await piefed.post.create(title="test post, please ignore", community_id=42, body="This is just a test...")
        post_id = post_info["post_view"]["post"]["id"]
        comment_info = await piefed.comment.create(post_id=post_id, body="Here is a test comment...")
        await piefed.close()
    
    asyncio.run(main())
    ```

## Community Information

This example gets information about a community, then logs in and edits the sidebar.

=== "Synchronous"

    ```python
    from pieforhead import PieFed

    piefed = PieFed("https://instance.tld")
    community_info = piefed.community.get_community(name="test@instance.tld")
    community_id = commuity_info["community_view"]["community"]["id"]
    piefed.login("username", "password")
    updated_community_info = piefed.community.edit(community_id=community_id, description="Edited sidebar...")
    piefed.close()
    ```

=== "Asynchronous"

    ```python
    import asyncio
    from pieforhead import PieFedAsync

    async def main():
        piefed = PieFedAsync("https://instance.tld")
        community_info = await piefed.community.get_community(name="test@instance.tld")
        community_id = commuity_info["community_view"]["community"]["id"]
        await piefed.login("username", "password")
        updated_community_info = await piefed.community.edit(community_id=community_id, description="Edited sidebar...")
        await piefed.close()
    
    asyncio.run(main())
    ```

## Uploading files

This example uploads two local images in different ways and then deletes them from the server.

=== "Synchronous"

    ```python
    from pieforhead import PieFed

    piefed = PieFed("https://instance.tld")
    piefed.login("username", "password")

    # Uploading by specifying a local filepath
    img1_response = piefed.image.upload("test1.png")
    img1_url = img1_response["url"]

    # Uploading by opening a file in a context manager
    with open("test2.png", "rb") as img_file:
        img2_response = piefed.image.upload(img_file)
        img2_url = img2_response["url"]
    
    # Delete images
    piefed.image.delete(img1_url)
    piefed.image.delete(img2_url)

    piefed.close()
    ```

=== "Asynchronous"

    ```python
    import asyncio
    from pieforhead import PieFedAsync

    async def main():
        piefed = PieFedAsync("https://instance.tld")
        await piefed.login("username", "password")

        # Uploading by specifying a local filepath
        img1_response = await piefed.image.upload("test1.png")
        img1_url = img1_response["url"]

        # Uploading by opening a file in a context manager
        with open("test2.png", "rb") as img_file:
            img2_response = await piefed.image.upload(img_file)
            img2_url = img2_response["url"]
        
        # Delete images
        await piefed.image.delete(img1_url)
        await piefed.image.delete(img2_url)

        await piefed.close()
    
    asyncio.run(main())
    ```
