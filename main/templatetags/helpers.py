from django.conf import settings as django_settings
from django import template

from main.models import Category
from techtemplate.validators import PhoneValidator

register = template.Library()


def settings_own(request):
    return {'settings': django_settings}

def load_categories(request):
    return {'categories': Category.objects.order_by('id').all()}


# settings value
@register.filter()
def phone_format(value):
    return PhoneValidator.format(value)
