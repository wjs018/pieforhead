---
icon: material/lightbulb-on-outline
title: Examples
description: Some examples of Pieforhead usage.
---

# Examples

Below are some basic working examples.

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
