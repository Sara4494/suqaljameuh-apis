# Membership APIs Ref

---

 
## Get All Endpoint
 
# Get All Endpoint
 

## Endpoint: https://suqaljameuh-apis.up.railway.app/memberships/get-memberships/

## Data: None

## Method: GET

## Description: Retrieves all membership objects.

 
## Create Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/memberships/
## create-membership/

## Data: name, price
 
## Data: name, price, features

## NOTE: features must be a list of strings
 

## Method: POST

## Description: Creates a new membership object with the given name and price.

## Update Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/memberships/update-membership/

## Data: name, price, features

## Method: PUT

## Description: Updates the name of a specific membership object by ID.

## Delete Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/memberships/delete-membership/<name>

## Data: None

## Method: DELETE

## Description: Deletes a specific membership object by name.

## FeaturedMember APIs Ref

## Create subscribeuser Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/memberships/feature-user/

## Data: name
 

## Method: POST

## Description: Creates a new featured membership object with the given name.

## Create subscribe Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/memberships/subscribe/

## Data: name, months, stripe_token

## Method: POST

## Description: Subscribes a user to a membership for a given number of months and processes payment using a Stripe token.

## Test subscribe Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/memberships/test-subscribe/

## Data: name, months

## Method: POST

## Description: Subscribes a user to a membership for a given number of months without processing payment.
 
