import time

from telethon import TelegramClient, events

# meng api_id dan api_hash dan mengoghey
api_id = 2896837
api_hash = 'b689ba5af7d894233f9e0379062ea69e'

session_file = '/path/to/session/file'  # bisa ditulis walau belum login asal punya akses write

# Isi pesan
message = "Hey! Sorrry, I haven't approved you to PM yet. Please wait for me to look in. Until then, please don't spam my PM. . . Thank you for being patient. *This is an automated message."

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
            if not from_.bot:  # don't auto-reply to bots
                print(time.asctime(), '-', event.message)  # optionally log time and message
                time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
