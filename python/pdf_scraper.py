#Downloading pdfs from a url and scraping them into a csv file
#third part libraries needed: tabula-py and requests

#pip install tabula-py
#pip install requests

import requests
import tabula
import os


url= 'https://www.camara.leg.br/internet/comissao/index/mista/orca/orcamento/OR2020/precatorios/TRF%202a%20Regi%C3%A3o.pdf'
pdf = requests.get(url)

pdf_name = input("Type the name for the pdf file: ")
csv_name = input("Type the name for the csv file: ")

open(pdf_name+'.pdf', 'wb').write(pdf.content)
tabula.convert_into(pdf_name+".pdf",csv_name+".csv",output_format="csv",pages='all')