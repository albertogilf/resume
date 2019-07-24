import pdfkit


options={
	"margin-top":"0",
	"margin-bottom": "0",
	"margin-left": "0",
	"margin-right":"0",
	"page-height":"11in",
	"page-width":"9in",
	"encoding":"UTF-8",
	"print-media-type":"",
	"no-stop-slow-scripts":""
}

path_wkthmltopdf = r'C://Program Files//wkhtmltopdf//bin//wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)


pdfkit.from_file('cv_GildelaFuenteAlberto.html','cv_GildelaFuenteAlberto.pdf',options=options)
