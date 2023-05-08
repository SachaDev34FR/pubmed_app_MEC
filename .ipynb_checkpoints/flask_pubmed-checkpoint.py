#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# alignement requete + lists id + list meta + trials from meta par id


from Bio import Entrez
from Bio import Medline


def clean_data(x):
    chaine = str(x)
    chaine = chaine.replace("['"," ")
    chaine = chaine.replace("']"," ")
    chaine = chaine.replace("'"," ")
    return chaine

def clean(x):
    chaine = str(x)
    chaine = chaine.replace("["," ")
    chaine = chaine.replace("]"," ")
    chaine = chaine.replace("'"," ")
    return chaine

def clean_a(x):
    chaine = str(x)
    chaine = chaine.replace("/","")
    chaine = chaine.replace("*"," ")
    return chaine


def ConPub():
    Entrez.api_key = "41843b992ded592334c39fe437c425e40608"
    Entrez.email = "sacha.torres@univ_montp3.fr"
    Entrez.tool = "Inca"
    print("connexion active !!!")

def Query():
    p = input("query pubmed :")
    pq = p + " "+"and Cochrane Database Syst Rev"
    return pq

def CorQuPub(q):
    han = Entrez.espell(term=q)
    rea = Entrez.read(han)
    return rea["CorrectedQuery"]

def MetaList(q):
    hend = Entrez.esearch(db="pubmed",term=q)
    ret = Entrez.read(hend)
    return ret["IdList"]

def MetaCount(q):
    hand = Entrez.esearch(db="pubmed",term=q)
    rec = Entrez.read(hand)
    return rec["Count"]

def FetchIdList(ids):
    handle = Entrez.efetch(db="pubmed",id=ids,rettype="medline",retmode="text")
    record = Medline.parse(handle)
    return record
    #code jinja pour la liste des données dans le dictionnaire
    #for re in record:
    #    titre : re["TI"]
    #   r = clean_data(re["FAU"])
    #    auteurs : r
        
def TrFromMeta(mid):
    handlle = Entrez.elink(db="pubmed",id=mid)
    result = Entrez.read(handlle)
    print(result[0]["LinkSetDb"])
    #return result
    
def DataDbs():
    pass
    
ConPub()
a = Query()
CorQuPub(a)
b = MetaList(a)
c = MetaCount(a)
print(" nb metas : ",c)
for res in FetchIdList(b):
    print(res["TI"])
    r = clean_data(res["FAU"])
    print(r)
    print("")
print("####")    
id=31264709       
print(TrFromMeta(id))
print("")


# In[26]:


# données sur les citations de la meta analyse ou de l'article 


from Bio import Entrez ,Medline
def ConPub():
    Entrez.api_key = "41843b992ded592334c39fe437c425e40608"
    Entrez.email = "sacha.torres@univ_montp3.fr"
    Entrez.tool = "Inca"
    print("connexion engaged captain picard !!!")
    print("")
    
def clean_data(x):
    chaine = str(x)
    chaine = chaine.replace("['"," ")
    chaine = chaine.replace("']"," ")
    chaine = chaine.replace("'"," ")
    return chaine    

def PubStats(): # prendra une pmid en param
    pmid = "31564709"
    handle = Entrez.elink(db="pubmed",id=pmid)
    record = Entrez.read(handle)
    return record

def PubLink(): # prendra le resultat de PubStats en param
    pmid = "31564709"
    cpl = 0
    record = PubStats()
    for link in record[0]["LinkSetDb"]:
        print(link["DbTo"],link["LinkName"]," ",len(link["Link"]))
        cpl = cpl + 1
    print("") 
    print(" nombre de lien pubmed possibles : ",len(link["LinkName"]))
    print(" nombres de liens existant avec ",pmid," sont au total de : ",cpl)
    print("")
ConPub()
PubStats()
PubLink()
############################################
# print("DB origine : ",record[0]["DbFrom"])
# print(" pmid de la publication : ",record[0]["IdList"])

    
############################################ 

# pubmed pubmed_pubmed   310            i=0
# pubmed pubmed_pubmed_alsoviewed   6   i=1
# pubmed pubmed_pubmed_citedin   1      i=2
# pubmed pubmed_pubmed_combined   6     i=3
# pubmed pubmed_pubmed_five   6         i=4
# pubmed pubmed_pubmed_refs   61        i=5
# pubmed pubmed_pubmed_reviews   169    i=6
# pubmed pubmed_pubmed_reviews_five 6   i=7
# il faut les avoir de lister les 26 dans l'ordre.
# il manque pubmed_assembly , pubmed_bioproject , pubmed_biosystems , pubmed_biosample , pubmed_cancerchromosomes
############################################
i = 0
for i in range(5):
    print("pubmed_pubmed :  ",end="")
    print(record[0]["LinkSetDb"][0]["Link"][i])
    print("pubmed_pubmed_alsoviewed :  ",end="")
    print(record[0]["LinkSetDb"][1]["Link"][i])# on accede au type de lien par le deuxieme indice
print("")

# pour afficher les pmid selon le type de lien 
ids = record[0]["LinkSetDb"][0]["Link"]
for link in ids:
    print(link["Id"]," ",end="")
    


# In[ ]:




