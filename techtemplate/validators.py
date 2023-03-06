from django.core.exceptions import ValidationError
import re
import phonenumbers
from django.utils.deconstruct import deconstructible

@deconstructible
class PhoneValidator:
    requires_context = False

    @staticmethod
    def clean(value):
        return re.sub('[^0-9]+', '', value)

    @staticmethod
    def validate(value):
        try:
            phone = phonenumbers.parse("+" + value)
            if not phonenumbers.is_valid_number(phone):
                raise ValidationError('Phone number is not valid')
        except:
            raise ValidationError('Phone number is not valid')

        if len(value) != 12 or not value.startswith('998'):
            raise ValidationError('Phone number is not valid')

        return True

    @staticmethod
    def format(value):
        try:
            phone = phonenumbers.parse("+" + value)
            if not phonenumbers.is_valid_number(phone):
                return value

            return phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        except:
            return value

    def __call__(self, value):
        if not PhoneValidator.validate(value):
            raise ValidationError('Phone number is not valid')
