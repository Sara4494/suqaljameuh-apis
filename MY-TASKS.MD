# Return names of ads categories

# Return User Data as names

web: gunicorn core.wsgi --timeout 120 --workers=3 --threads=3 --worker-connections=1000 & celery -A core worker --loglevel=INFO --pool=solo -n worker2@%h & celery -A core beat -l INFO

works:
daphne core.asgi:application --port $PORT --bind 0.0.0.0

# Radwan's tasks

## Return featured users

## Rank ads

# MINE:

## - advanced search [DONE]

## - when get user's ads must return each ad's membership [DONE]

## - Rate User And Ad [DONE]

## - prevent user from subscribing at another membership meanwhile he is already subscribed at one [DONE]

## - Mark user as featured meanwhile he's subscribed an when his subscription gets expired and then remove this mark [DONE]

## - Add Permissions upon delete methods in Ad [DONE]

# - Missings:

## Warn user when he wants to follow himself [DONE]

## User Analytics [DONE]

## Return Users in the Chat [DONE]

## Elsahfi

---

## First, Adjust the space between items and navbar to be 16

## Adjust the navbar radius to be 16

## Make the navbar static

## expand the length items

## ---

## When click on shifts count:

## display shitfs as many as the number

## ability to block clients and never accept any payment from those clients

## WhatsApp Notification

## Leave the animation till the end

## In invocices recording with checkboxes
