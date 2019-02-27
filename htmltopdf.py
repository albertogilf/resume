import pdfkit

css = 'style.css'
options={
	"margin-top":"0in",
	"margin-bottom": "0in",
	"margin-left": "0in",
	"margin-right":"0in",
	"page-height":"11in",
	"page-width":"9in",
	"encoding":"UTF-8",
	"print-media-type":"",
	"no-stop-slow-scripts":""
}
pdfkit.from_file('cv_GildelaFuenteAlberto.html','cv_GildelaFuenteAlberto.pdf',options=options)

pdfkit.from_url('cv_GildelaFuenteAlberto.html','cv_GildelaFuenteAlberto.pdf',options=options)
