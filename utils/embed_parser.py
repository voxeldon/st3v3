import discord
import re

async def embed_parser(ctx, input_str):
    header = None
    footer = None
    image_url = None
    author = None
    icon = None

    # Parse options from command message
    match = re.search(r'\[header=(.*?)\]', input_str)
    if match:
        header = match.group(1).strip()

    match = re.search(r'\[footer=(.*?)\]', input_str)
    if match:
        footer = match.group(1).strip()

    match = re.search(r'\[author=(.*?)\]', input_str)
    if match:
        author = match.group(1).strip()

    match = re.search(r'\[icon=(.*?)\]', input_str)
    if match:
        icon = match.group(1).strip()
        try:
            icon_url = icon
            # Check if the URL starts with http:// or https://
            if not (icon_url.startswith("http://") or icon_url.startswith("https://")):
                raise ValueError
        except ValueError:
            await ctx.send("Error: The icon parameter must be a valid link (starting with http:// or https://).")
            return

    match = re.search(r'\[image=(.*?)\]', input_str)
    if match:
        image_url = match.group(1).strip()
        try:
            # Check if the URL starts with http:// or https://
            if not (image_url.startswith("http://") or image_url.startswith("https://")):
                raise ValueError
        except ValueError:
            await ctx.send("Error: The image parameter must be a valid link (starting with http:// or https://).")
            return

    # Remove options from input string
    input_str = re.sub(r'\[header=(.*?)\]', '', input_str)
    input_str = re.sub(r'\[footer=(.*?)\]', '', input_str)
    input_str = re.sub(r'\[author=(.*?)\]', '', input_str)
    input_str = re.sub(r'\[icon=(.*?)\]', '', input_str)
    input_str = re.sub(r'\[image=(.*?)\]', '', input_str)

    input_list = input_str.split('(', 1)
    title = input_list[0].strip()
    description = input_list[1].split(')', 1)[0].strip().replace(r'\n', '\n')  # replace "\n" with new line characters

    if len(ctx.message.attachments) > 0 and image_url is None:
        attachment = ctx.message.attachments[0]
        image_url = attachment.url

    embed = discord.Embed(title=title, description=description, color=0x00ff00)

    if header is not None:
        embed.set_author(name=header)

    if author is not None:
        if author == "":
            author = ctx.author.name
        embed.set_author(name=author, icon_url=icon)

    if footer is not None:
        embed.set_footer(text=footer)

    if image_url is not None:
        embed.set_image(url=image_url)

    # Send the embed message
    await ctx.send(embed=embed)
