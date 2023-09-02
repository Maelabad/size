
#Les imports
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


#*************************************Taille du tee-shirt********************************************************
#La taille est situe dans un intervale de 0 a 230 coupe par pas de 5
taille = ctrl.Antecedent(np.arange(0,220,2), 'taille')

#Le poids est situe dans un intervale de 0 a 200 coupe par pas de 5
poids = ctrl.Antecedent(np.arange(0,130,2),'poids')

taille_v = ctrl.Consequent(np.arange(0,16,1),'taille_vetement')


#*************************************Taille du pantalon********************************************************

#Le tour de taille est situe dans un intervale de 66 a 142 coupe par pas de 2
tour_taille = ctrl.Antecedent(np.arange(58,142,2), 'tour_taille')

#Le tour de bassin est situe dans un intervale de 85 a 144 coupe par pas de 2
tour_bassin = ctrl.Antecedent(np.arange(84,144,2),'tour_bassin')

#La taille de pantalon situe dans un interval de 30 a 70 (S a XXXXXL)
taille_pantalon = ctrl.Consequent(np.arange(30,70,2),'taille_pantalon')



#*************************************Taille des chaussures********************************************************
### Antecedent
# la taille du pied est située dans un intervalle de 8,5 à 32,4 coupé par pas de 0.1
taillePied = ctrl.Antecedent(np.arange(8.5,32.4,0.1), 'taillePied')
### Consequent
# la pointure est situé dans un intervalle de 16 à 50 coupé par pas de 0.1
pointure = ctrl.Consequent(np.arange(16,50,0.1), 'pointure')



#Le Genre M pour homme et F pour femmes
x='M'

#Liste des differents intervales de chaques taille
tph = [[30,41], [42,45], [46,49] , [50,55] , [56,59], [60,63], [64,67], [68,70]] #Taille pantalon homme
tpf = [[30,34], [35,38], [39,42] , [43,46] , [47,50], [51,54], [55,60]] #Taille pantalon femme


#Liste des differentes tailles de tee-shirt hommes
tv = ["XXS","XS","S","M","L","XL","XXL","XXXL"]
