from weasyprint import HTML
stylesheets = ['./OSEHelvetica/css/style.css']
HTML('./OSEHelvetica/index.html').write_pdf('./test_print.pdf', stylesheets)