from __future__ import unicode_literals
import uuid
from django.db  import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='media/images', default='media/images/Aberdeen')
    # , default='images/Aberdeen.png')



    @property

    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "item_name": self.name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }
        return PayPalPaymentsForm(initial=paypal_dict)


def __unicode__(self):
    return self.name

# Create your models here.
