from paypal.standard.models import ST_PP_COMPLETED
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Donation


def process_paypal(sender, **kwargs):
    """
    Process the IPN notification from PayPal once a payment is made

    Arguments:
    sender.custom is the donation id
    """
    ipn_obj = sender
    print("received the paypal signal...")
    print('ipn_obj.payment_status = ' + str(ipn_obj.payment_status))

    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != settings.PAYPAL_ACCOUNT:
            # Not a valid payment
            print('not a valid payment.')
            return

        # ALSO: for the same reason, you need to check the amount
        # received, `custom` etc. are all what you expect or what
        # is allowed.
        print('ipn_obj.custom (donation)= ' + str(ipn_obj.custom))

        donation = get_object_or_404(Donation, pk=ipn_obj.custom)

        # TODO: write these to the db or a file so we have some traceability
        # print(ipn_obj.mc_gross + " " + ipn_obj.mc_currency)

        donation.payment_method = 'paypal'
        donation.payment_status = 'paid'
        donation.save()

        # send the thank you email
        send_mail(
            'Thank you for donating to the Triple Crown for Heart!',
            'Thank you for your donation of '
            + '${:,.2f}'.format(donation.amount) + ' to '
            + donation.fundraiser.name
            + '.\nYour PayPal receipt should arrive in a separate email.',
            'fundraising@triplecrownforheart.ca', [donation.email, ]
        )

    else:
        print('not completed')
