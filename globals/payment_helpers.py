import stripe
from django.conf import settings


def create_customer(user, stripe_token):
    print("STRIPE TOKEN", settings.STRIPE_PRIVATE_KEY)
    """
    this method creates a customer to associate him with a payment transaction.

    PLEASE NOTE: use it at the begging of any payment transaction, also wrap it inside an error handler to catch 
    any potential errors
    """
    customer = stripe.Customer.create(
        email=user.email,
        name=user.full_name,
        # username=user.profile.username,
        source=stripe_token,
        api_key="sk_test_51LMruHIG8Ho6949S6TzTcQXjxAz70lcEwYYw1tacrT4UzdrUucrXfgotZN3WP80V64tNhdMmHkctd1V03Qlu785700gNVQTuSF"
    )
    return customer


def create_charge(customer, amount, description=None):
    print("STRIPE TOKEN", "sk_test_51LMruHIG8Ho6949S6TzTcQXjxAz70lcEwYYw1tacrT4UzdrUucrXfgotZN3WP80V64tNhdMmHkctd1V03Qlu785700gNVQTuSF")
    """
    this method charges the user for a certain amount of money.

    NOTES:
    1. this is should be used after creating a customer (generally comes at the end)
    2. you must provide the customer which will be charged
    3. provide the amount not in cents (the method will do this task for you)
    4. (optionally) you can provide description for this charge describes why did you charge
    5. ensure that it's wrapped inside of an error handler to handle any potential errors
    """
    stripe.Charge.create(
        customer=customer,
        amount=int(amount * 100),
        currency='usd',
        description=description,
        api_key="sk_test_51LMruHIG8Ho6949S6TzTcQXjxAz70lcEwYYw1tacrT4UzdrUucrXfgotZN3WP80V64tNhdMmHkctd1V03Qlu785700gNVQTuSF"
    )
