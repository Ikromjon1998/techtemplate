from django.conf import settings as django_settings
from django import template

from techtemplate.validators import PhoneValidator

register = template.Library()


def settings_own(request):
    return {'settings': django_settings}


# settings value
@register.filter()
def phone_format(value):
    return PhoneValidator.format(value)
