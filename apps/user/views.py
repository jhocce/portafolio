from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View, RedirectView
# from django.template.loader import render_to_string
# Create your views here.
# from .utils import render_to_pdf
# from weasyprint import HTML
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

import os
from sys import platform
from django.template.loader import get_template 
from django.template import Context
import pdfkit
# from django.http import HTTP404






class cv( View):

	template_name = 'user/cv.html'
	def dispatch(self, request, *args, **kwargs):
		
		return super(cv, self).dispatch(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context ={}
		return context
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)


class cvpdf(View):
	template_name = 'user/pdf.html'

	def get(self, request, *args, **kwargs):
		options = {
			'page-size': 'A4',
			'margin-top': '0.75in',
			'margin-right': '0.75in',
			'margin-bottom': '0.75in',
			'margin-left': '0.75in',
		}
		if platform=='linux':
			pdfkit.from_url("localhost:8855", "out.pdf")
		else:
			path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
			config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
			pdfkit.from_url("localhost:8855", "out.pdf", configuration=config)
		pdf = open("out.pdf",'rb')
		response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
		response['Content-Disposition'] = 'attachment; filename=output.pdf'
		pdf.close()
		os.remove("out.pdf")  # remove the locally created pdf file.
		return response  

