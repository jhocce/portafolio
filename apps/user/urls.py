from django.urls import path
from .views import  cv, cvpdf



urlpatterns = [
	path('', cv.as_view(), name="cv"),
	path('pdf', cvpdf.as_view(), name="cvpdf"),
	
]