import skfuzzy as fuzz
from skfuzzy import control as ctrl

from res.functions.menu import taillePied, pointure
from res.models import user_chaussures


def taille_Pieds():
    taille_16 = fuzz.trimf(taillePied.universe, [8, 9, 9.6])
    taille_17 = fuzz.trimf(taillePied.universe, [9.5, 10, 10.3])
    taille_18 = fuzz.trimf(taillePied.universe, [10.4, 10.6, 10.9])
    taille_19 = fuzz.trimf(taillePied.universe, [11, 11.3, 11.6])
    taille_20 = fuzz.trimf(taillePied.universe, [11.7, 12, 12.3])
    taille_21 = fuzz.trimf(taillePied.universe, [12.4, 12.6, 12.9])
    taille_22 = fuzz.trimf(taillePied.universe, [13, 13.3, 13.6])
    taille_23 = fuzz.trimf(taillePied.universe, [13.7, 14, 14.3])
    taille_24 = fuzz.trimf(taillePied.universe, [14.4, 14.6, 14.9])
    taille_25 = fuzz.trimf(taillePied.universe, [15, 15.3, 15.6])
    taille_26 = fuzz.trimf(taillePied.universe, [15.7, 16, 16.3])
    taille_27 = fuzz.trimf(taillePied.universe, [16.4, 16.6, 16.9])
    taille_28 = fuzz.trimf(taillePied.universe, [17, 17.3, 17.6])
    taille_29 = fuzz.trimf(taillePied.universe, [17.7, 18, 18.3])
    taille_30 = fuzz.trimf(taillePied.universe, [18.4, 18.6, 18.9])
    taille_31 = fuzz.trimf(taillePied.universe, [19, 19.3, 19.6])
    taille_32 = fuzz.trimf(taillePied.universe, [19.7, 20, 20.3])
    taille_33 = fuzz.trimf(taillePied.universe, [20.4, 20.6, 20.9])
    taille_34 = fuzz.trimf(taillePied.universe, [21, 21.3, 21.6])
    taille_35 = fuzz.trimf(taillePied.universe, [21.7, 22, 22.3])
    taille_36 = fuzz.trimf(taillePied.universe, [22.4, 22.6, 22.9])
    taille_37 = fuzz.trimf(taillePied.universe, [23, 23.3, 23.6])
    taille_38 = fuzz.trimf(taillePied.universe, [23.7, 24, 24.3])
    taille_39 = fuzz.trimf(taillePied.universe, [24.4, 24.6, 24.9])
    taille_40 = fuzz.trimf(taillePied.universe, [25, 25.3, 25.6])
    taille_41 = fuzz.trimf(taillePied.universe, [25.7, 26, 26.3])
    taille_42 = fuzz.trimf(taillePied.universe, [26.4, 26.6, 26.9])
    taille_43 = fuzz.trimf(taillePied.universe, [27, 27.3, 27.6])
    taille_44 = fuzz.trimf(taillePied.universe, [27.7, 28, 28.3])
    taille_45 = fuzz.trimf(taillePied.universe, [28.4, 28.6, 28.9])
    taille_46 = fuzz.trimf(taillePied.universe, [29, 29.3, 29.6])
    taille_47 = fuzz.trimf(taillePied.universe, [29.7, 30, 30.3])
    taille_48 = fuzz.trimf(taillePied.universe, [30.4, 30.6, 30.9])
    taille_49 = fuzz.trimf(taillePied.universe, [31, 31.3, 31.6])
    taille_50 = fuzz.trimf(taillePied.universe, [31.7, 32, 33])

    taillePied['Pointure 16'] = taille_16
    taillePied['Pointure 17'] = taille_17
    taillePied['Pointure 18'] = taille_18
    taillePied['Pointure 19'] = taille_19
    taillePied['Pointure 20'] = taille_20
    taillePied['Pointure 21'] = taille_21
    taillePied['Pointure 22'] = taille_22
    taillePied['Pointure 23'] = taille_23
    taillePied['Pointure 24'] = taille_24
    taillePied['Pointure 25'] = taille_25
    taillePied['Pointure 26'] = taille_26
    taillePied['Pointure 27'] = taille_27
    taillePied['Pointure 28'] = taille_28
    taillePied['Pointure 29'] = taille_29
    taillePied['Pointure 30'] = taille_30
    taillePied['Pointure 31'] = taille_31
    taillePied['Pointure 32'] = taille_32
    taillePied['Pointure 33'] = taille_33
    taillePied['Pointure 34'] = taille_34
    taillePied['Pointure 35'] = taille_35
    taillePied['Pointure 36'] = taille_36
    taillePied['Pointure 37'] = taille_37
    taillePied['Pointure 38'] = taille_38
    taillePied['Pointure 39'] = taille_39
    taillePied['Pointure 40'] = taille_40
    taillePied['Pointure 41'] = taille_41
    taillePied['Pointure 42'] = taille_42
    taillePied['Pointure 43'] = taille_43
    taillePied['Pointure 44'] = taille_44
    taillePied['Pointure 45'] = taille_45
    taillePied['Pointure 46'] = taille_46
    taillePied['Pointure 47'] = taille_47
    taillePied['Pointure 48'] = taille_48
    taillePied['Pointure 49'] = taille_49
    taillePied['Pointure 50'] = taille_50


def pointure_Chaussures():
    pointure_16 = fuzz.trimf(pointure.universe, [15, 15.5, 16.1])
    pointure_17 = fuzz.trimf(pointure.universe, [16, 16.5, 17.1])
    pointure_18 = fuzz.trimf(pointure.universe, [17, 17.5, 18.1])
    pointure_19 = fuzz.trimf(pointure.universe, [18, 18.5, 19.1])
    pointure_20 = fuzz.trimf(pointure.universe, [19, 19.5, 20.1])
    pointure_21 = fuzz.trimf(pointure.universe, [20, 20.5, 21.1])
    pointure_22 = fuzz.trimf(pointure.universe, [21, 21.5, 22.1])
    pointure_23 = fuzz.trimf(pointure.universe, [22, 22.5, 23.1])
    pointure_24 = fuzz.trimf(pointure.universe, [23, 23.5, 24.1])
    pointure_25 = fuzz.trimf(pointure.universe, [24, 24.5, 25.1])
    pointure_26 = fuzz.trimf(pointure.universe, [25, 25.5, 26.1])
    pointure_27 = fuzz.trimf(pointure.universe, [26, 26.5, 27.1])
    pointure_28 = fuzz.trimf(pointure.universe, [27, 27.5, 28.1])
    pointure_29 = fuzz.trimf(pointure.universe, [28, 28.5, 29.1])
    pointure_30 = fuzz.trimf(pointure.universe, [29, 29.5, 30.1])
    pointure_31 = fuzz.trimf(pointure.universe, [30, 30.5, 31.1])
    pointure_32 = fuzz.trimf(pointure.universe, [31, 31.5, 32.1])
    pointure_33 = fuzz.trimf(pointure.universe, [32, 32.5, 33.1])
    pointure_34 = fuzz.trimf(pointure.universe, [33, 33.5, 34.1])
    pointure_35 = fuzz.trimf(pointure.universe, [34, 34.5, 35.1])
    pointure_36 = fuzz.trimf(pointure.universe, [35, 35.5, 36.1])
    pointure_37 = fuzz.trimf(pointure.universe, [36, 36.5, 37.1])
    pointure_38 = fuzz.trimf(pointure.universe, [37, 37.5, 38.1])
    pointure_39 = fuzz.trimf(pointure.universe, [38, 38.5, 39.1])
    pointure_40 = fuzz.trimf(pointure.universe, [39, 39.5, 40.1])
    pointure_41 = fuzz.trimf(pointure.universe, [40, 40.5, 41.1])
    pointure_42 = fuzz.trimf(pointure.universe, [41, 41.5, 42.1])
    pointure_43 = fuzz.trimf(pointure.universe, [42, 42.5, 43.1])
    pointure_44 = fuzz.trimf(pointure.universe, [43, 43.5, 44.1])
    pointure_45 = fuzz.trimf(pointure.universe, [44, 44.5, 45.1])
    pointure_46 = fuzz.trimf(pointure.universe, [45, 45.5, 46.1])
    pointure_47 = fuzz.trimf(pointure.universe, [46, 46.5, 47.1])
    pointure_48 = fuzz.trimf(pointure.universe, [47, 47.5, 48.1])
    pointure_49 = fuzz.trimf(pointure.universe, [48, 48.5, 49.1])
    pointure_50 = fuzz.trimf(pointure.universe, [49, 49.5, 51])

    pointure['Pointure 16'] = pointure_16
    pointure['Pointure 17'] = pointure_17
    pointure['Pointure 18'] = pointure_18
    pointure['Pointure 19'] = pointure_19
    pointure['Pointure 20'] = pointure_20
    pointure['Pointure 21'] = pointure_21
    pointure['Pointure 22'] = pointure_22
    pointure['Pointure 23'] = pointure_23
    pointure['Pointure 24'] = pointure_24
    pointure['Pointure 25'] = pointure_25
    pointure['Pointure 26'] = pointure_26
    pointure['Pointure 27'] = pointure_27
    pointure['Pointure 28'] = pointure_28
    pointure['Pointure 29'] = pointure_29
    pointure['Pointure 30'] = pointure_30
    pointure['Pointure 31'] = pointure_31
    pointure['Pointure 32'] = pointure_32
    pointure['Pointure 33'] = pointure_33
    pointure['Pointure 34'] = pointure_34
    pointure['Pointure 35'] = pointure_35
    pointure['Pointure 36'] = pointure_36
    pointure['Pointure 37'] = pointure_37
    pointure['Pointure 38'] = pointure_38
    pointure['Pointure 39'] = pointure_39
    pointure['Pointure 40'] = pointure_40
    pointure['Pointure 41'] = pointure_41
    pointure['Pointure 42'] = pointure_42
    pointure['Pointure 43'] = pointure_43
    pointure['Pointure 44'] = pointure_44
    pointure['Pointure 45'] = pointure_45
    pointure['Pointure 46'] = pointure_46
    pointure['Pointure 47'] = pointure_47
    pointure['Pointure 48'] = pointure_48
    pointure['Pointure 49'] = pointure_49
    pointure['Pointure 50'] = pointure_50


def func_Rules_Chaussures(tchaussures: float, genre: str):
    rule_16 = ctrl.Rule(taillePied['Pointure 16'], pointure['Pointure 16'])
    rule_17 = ctrl.Rule(taillePied['Pointure 17'], pointure['Pointure 17'])
    rule_18 = ctrl.Rule(taillePied['Pointure 18'], pointure['Pointure 18'])
    rule_19 = ctrl.Rule(taillePied['Pointure 19'], pointure['Pointure 19'])
    rule_20 = ctrl.Rule(taillePied['Pointure 20'], pointure['Pointure 20'])
    rule_21 = ctrl.Rule(taillePied['Pointure 21'], pointure['Pointure 21'])
    rule_22 = ctrl.Rule(taillePied['Pointure 22'], pointure['Pointure 22'])
    rule_23 = ctrl.Rule(taillePied['Pointure 23'], pointure['Pointure 23'])
    rule_24 = ctrl.Rule(taillePied['Pointure 24'], pointure['Pointure 24'])
    rule_25 = ctrl.Rule(taillePied['Pointure 25'], pointure['Pointure 25'])
    rule_26 = ctrl.Rule(taillePied['Pointure 26'], pointure['Pointure 26'])
    rule_27 = ctrl.Rule(taillePied['Pointure 27'], pointure['Pointure 27'])
    rule_28 = ctrl.Rule(taillePied['Pointure 28'], pointure['Pointure 28'])
    rule_29 = ctrl.Rule(taillePied['Pointure 29'], pointure['Pointure 29'])
    rule_30 = ctrl.Rule(taillePied['Pointure 30'], pointure['Pointure 30'])
    rule_31 = ctrl.Rule(taillePied['Pointure 31'], pointure['Pointure 31'])
    rule_32 = ctrl.Rule(taillePied['Pointure 32'], pointure['Pointure 32'])
    rule_33 = ctrl.Rule(taillePied['Pointure 33'], pointure['Pointure 33'])
    rule_34 = ctrl.Rule(taillePied['Pointure 34'], pointure['Pointure 34'])
    rule_35 = ctrl.Rule(taillePied['Pointure 35'], pointure['Pointure 35'])
    rule_36 = ctrl.Rule(taillePied['Pointure 36'], pointure['Pointure 36'])
    rule_37 = ctrl.Rule(taillePied['Pointure 37'], pointure['Pointure 37'])
    rule_38 = ctrl.Rule(taillePied['Pointure 38'], pointure['Pointure 38'])
    rule_39 = ctrl.Rule(taillePied['Pointure 39'], pointure['Pointure 39'])
    rule_40 = ctrl.Rule(taillePied['Pointure 40'], pointure['Pointure 40'])
    rule_41 = ctrl.Rule(taillePied['Pointure 41'], pointure['Pointure 41'])
    rule_42 = ctrl.Rule(taillePied['Pointure 42'], pointure['Pointure 42'])
    rule_43 = ctrl.Rule(taillePied['Pointure 43'], pointure['Pointure 43'])
    rule_44 = ctrl.Rule(taillePied['Pointure 44'], pointure['Pointure 44'])
    rule_45 = ctrl.Rule(taillePied['Pointure 45'], pointure['Pointure 45'])
    rule_46 = ctrl.Rule(taillePied['Pointure 46'], pointure['Pointure 46'])
    rule_47 = ctrl.Rule(taillePied['Pointure 47'], pointure['Pointure 47'])
    rule_48 = ctrl.Rule(taillePied['Pointure 48'], pointure['Pointure 48'])
    rule_49 = ctrl.Rule(taillePied['Pointure 49'], pointure['Pointure 49'])
    rule_50 = ctrl.Rule(taillePied['Pointure 50'], pointure['Pointure 50'])

    # Compilation des regles
    chaussure_regle = ctrl.ControlSystem([rule_16, rule_17, rule_18, rule_19,
                                          rule_20, rule_21, rule_22, rule_23, rule_24, rule_25, rule_26, rule_27,
                                          rule_28, rule_29,
                                          rule_30, rule_31, rule_32, rule_33, rule_34, rule_35, rule_36, rule_37,
                                          rule_38, rule_39,
                                          rule_40, rule_41, rule_42, rule_43, rule_44, rule_45, rule_46, rule_47,
                                          rule_48, rule_49,
                                          rule_50])

    chaussure = ctrl.ControlSystemSimulation(chaussure_regle)
    chaussure.input['taillePied'] = tchaussures
    chaussure.compute()

    return "Votre pointure est : " + str(int(chaussure.output['pointure']))


def chaussures(tchaussures: str, genre: str):
    c = user_chaussures(taille_pied=float(tchaussures), genre=genre)
    c.save()
    taille_Pieds()
    pointure_Chaussures()
    return func_Rules_Chaussures(float(tchaussures), genre)
