# Chat APIs Ref

---

# Endpoint for get all chats for normal users

## Endpoint: https://suqaljameuh-apis.up.railway.app/chat/user-chats/

## method : GET

## permissions : user must be authenticated

## description : this end point return all chats that user in

# Endpoint for get all chat messages for normal users

## Endpoint: https://suqaljameuh-apis.up.railway.app/chat/messages/chat-uuid/

## method : GET

## permissions : user must be authenticated

## description : this end point return all messages between sender and receiver

# Endpoint for get all chats for admin users

## Endpoint: https://suqaljameuh-apis.up.railway.app/chat/admin/chats/

## method : GET

## permissions : user must be Admin

## description : this end point return all chats

# Endpoint for get all chat messages for admin users

## Endpoint: https://suqaljameuh-apis.up.railway.app/chat/admin/chat/messages/chat-uuid/

## method : GET

## permissions : user must be admin

## description : this end point return all messages between sender and receiver

# Endpoint for send image

## Endpoint: https://suqaljameuh-apis.up.railway.app/chat/send/image/chat-uuid/

## method : POST

## permissions : user must be authenticated

## description : this end point is for send image between users in the chat

## Data : image

# Endpoint for send Audio

## Endpoint: https://suqaljameuh-apis.up.railway.app/chat/send/audio/chat-uuid/

## method : POST

## permissions : user must be authenticated

## description : this end point is for send audio between users in the chat

## Data : audio

# ws endpoint for send messages

## Endpoint: ws://suqaljameuh-apis.up.railway.app/chat/chat-uuid/

## permission : user must authentciated

## description : you can send text message and recive all messages [text, image, audio] in real-time.

# ws endpoint for make user online and offline

## Endpoint: ws://suqaljameuh-apis.up.railway.app/online/

## permission : user must be authentciated

## description : this endpoint is update user state from online to offline
