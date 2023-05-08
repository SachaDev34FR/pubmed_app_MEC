from Bio import Entrez, Medline


def query_pubmed(terms):

    Entrez.api_key ="12b30395a61ef72be179af00768997571608"
    Entrez.email = "sachatorres974@gmail.com"
    Entrez.tool= "MEC-INM2023"

    handle = Entrez.esearch(db="pubmed", term=terms, retmax="10")
    record = Entrez.read(handle)
    ids = record["IdList"] # type: ignore
    hendle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="text")
    return Medline.parse(hendle)

# Récupération des résultats
results = query_pubmed("neoplasms and green tea")

# Création du dataframe
df = pd.DataFrame.from_records(results)

# Affichage du dataframe
print(df.head())