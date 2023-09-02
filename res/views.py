from django.shortcuts import render

from res.functions.chaussures import chaussures
from res.functions.pantalon import pantalon
from res.functions.tee_shirt import tee_shirt


def response(request):
    post = request.POST
    if len(post) == 4:
        if 'taille' and 'poids' in post:
            detail = "tee-shirt"
            #print("La taille : ", post['taille'] , " - Le poids : "+post['poids'] )
            reponse = tee_shirt(post['taille'],post['poids'],post['genre'])
            #print("La reponse 1 est : " , reponse )
            print(type(reponse))


        if 'tourTaille' and 'tourHanche' in post:
            print("Il s'agit d'un pantalon")
            detail = "pantalon"
            reponse = pantalon(post['tourTaille'],post['tourHanche'],post['genre'])


    if len(post) == 3: #Il s'agit du calcul de la taille de chaussure
        if 'tchaussures' in post:

            detail = "chaussures"
            reponse = chaussures(post['tchaussures'],post['genre'])

    return render(request, "response.html", context={"detail": detail,"resultat": reponse})
