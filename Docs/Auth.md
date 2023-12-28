# Auth APIs Ref

---

# Login Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/user/auth/login/

## Data: email, password

# Register Endpoint

## Endpoint: https://suqaljameuh-apis.up.railway.app/user/auth/register/

## Data: email, username, full_name, phone_number, city, country, birth_date

## IMPORTANT NOTES: city and country must be one of the ones that were registered in the database, therefore here's their endpoints

## To get all the countries you can access it from here: https://suqaljameuh-apis.up.railway.app/varieties/country/countries/ (Don't need to pass anything as it's GET request)

## To get all the cities you can access it from here: http://127.0.0.1:8000/varieties/city/cities/<country name>/ (you must pass the country name to retrieve all the cities related to this country)

