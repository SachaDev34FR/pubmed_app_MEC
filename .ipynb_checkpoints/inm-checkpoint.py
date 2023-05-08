from flask import Flask, render_template
from pubmed.queries import query_pubmed, clean_data



inm = Flask(__name__)

def Correct_Query(q):
    han = Entrez.espell(term=q)
    rea = Entrez.read(han)
    return rea["CorrectedQuery"]

# @inm.route('/')
# def index():
#     


@inm.route('/')
def index():
    
    header1 = "PMID"
    header2 = "PMC"
    header3 = "Titre"
    header4 = "Abstract"
    header5 = "Auteurs"
    header6 = "Date_Publication"
    header7 = "Date_Entrez"
    header8 = "Date_Revision"
    header9 = "DOI"
    header10 = "Mesh_Terms"
    header11 = "PL"
    terms = "neoplasms and green tea"
    results = query_pubmed(terms)
    #terms_mesh = Correct_Query(terms)
    return render_template('resultats.html', 
                           header1=header1, header2=header2, header3=header3, 
                           header4=header4, header5=header5,
                           header6=header6, header7=header7, header8=header8, 
                           header9=header9,
                           header10=header10, header11=header11,
                           terms=terms, #terms_mesh=terms_mesh,
                           results=results,
                           clean_data=clean_data)


if __name__ == '__main__':
    inm.run(debug=True)
