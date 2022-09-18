from reportlab.pdfgen import canvas
from sklearn.ensemble import GradientBoostingClassifier 
'''def GerandoPDF(lista):
	try:
		nome_pdf = input('Nome: ')
		pdf = canvas.Canvas(f'{nome_pdf}.pdf')
		x = 720 
		for n,i in lista.items():
			x-=20
			pdf.drawString(247,x,f'{n}:{i}')
		pdf.setTitle(nome_pdf)
		pdf.setFont('Helvetica-Oblique',14)
		pdf.drawString(245,750,' ')
		pdf.setFont('Helvetica-Bold',12)
		pdf.drawString(245,724,'')
		pdf.save()
		print(f'{nome_pdf}.pdf Criado com sucesso')
	except:
		print(f'Erro ao gerar {nome_pdf}.pdf')
lista = {}
GerandoPDF(lista)
'''
def GerandoPDF(lista):
	nomePdf = input('Nome: ')
	pdf = canvas.Canvas(f'{nomePdf}.pdf')
	x = 720 
	for n,i in lista.items():
		x -= 20
		pdf.drawString(247,x,f'{n}:{i}')
	pdf.setTitle(nomePdf)
	pdf.setFont('Helvetica-Oblique',14)
	pdf.drawString(245,750,' ')
	pdf.setFont('Helvetica-Bold',12)
	pdf.drawString(245,724,' ')
	pdf.save()
lista = {}
GerandoPDF(lista)
