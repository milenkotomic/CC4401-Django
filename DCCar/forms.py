from django.forms import ModelForm, forms

from DCCar.models import Reservation

__author__ = 'milenkotomic'


class ReserveForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['start', 'end', 'car']

