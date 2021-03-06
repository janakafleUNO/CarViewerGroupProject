from django import forms
from .models import CarBrand, CarType, CarModel, CarReview


class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ('car_brand', 'car_year')


class CarTypeForm(forms.ModelForm):
    class Meta:
        model = CarType
        fields = ('car_brand', 'car_bodytype', 'car_fueltype', 'car_transmission', 'description', 'available')


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = (
            'car_brand', 'car_year', 'model_name', 'car_bodytype', 'car_fueltype', 'car_transmission', 'car_price',
            'car_mileage')


class CarReviewForm(forms.ModelForm):
    class Meta:
        model = CarReview
        fields = ('car_brand', 'car_year', 'model_name', 'car_bodytype', 'car_expert_review', 'car_user_review',
                  'car_overall_review')
