from telethon import telegramClient

api_id = ''
api_hash = ''

client = telegramClient('name', api_id, api_hash)

async def main():
  me = client.get_me()

  print(me.stringify())

  username = me.username
  print(username)
  print(me.phone)
  async for dialog in client.iter_dialogs():
    print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    await client.send_message('me', 'Hello, myself!')
    # ...to some chat ID
    # ...to your contacts
    await client.send_message('+237682126221', 'Hello, friend!')
    # ...or even to any username

    # You can, of course, use markdown in your messages:
    message = await client.send_message(
        'me',
        'This message has **bold**, `code`, __italics__ and '
        'a [nice website](https://example.com)!',
        link_preview=False
    )

    # Sending a message returns the sent message object, which you can use
    print(message.raw_text)

    # You can reply to messages directly if you have a message object
    await message.reply('Cool!')

    # Or send files, songs, documents, albums...

    # You can print the message history of any chat:
    async for message in client.iter_messages('me'):
        print(message.id, message.text)

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        if message.photo:
            path = await message.download_media()
            print('File saved to', path)  # printed after download is done

  with client:
    client.loop.run_until_complete(main())