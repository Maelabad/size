from res.functions.menu import taille_pantalon, tour_bassin, tour_taille
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from res.models import user_pantalon


def func_tour_taille_homme():
    tour_taille_1 = fuzz.trimf(tour_taille.universe, [66, 75, 83])  # S

    tour_taille_2 = fuzz.trimf(tour_taille.universe, [82, 86, 90])  # M

    tour_taille_3 = fuzz.trimf(tour_taille.universe, [89, 94, 99])  # L

    tour_taille_4 = fuzz.trimf(tour_taille.universe, [98, 104, 110])  # XL

    tour_taille_5 = fuzz.trimf(tour_taille.universe, [109, 114, 119])  # XXL

    tour_taille_6 = fuzz.trimf(tour_taille.universe, [118, 124, 127])  # XXXL

    tour_taille_7 = fuzz.trimf(tour_taille.universe, [126, 130, 134])  # XXXXL

    tour_taille_8 = fuzz.trimf(tour_taille.universe, [133, 137, 142])  # XXXXXL

    tour_taille['S'] = tour_taille_1
    tour_taille['M'] = tour_taille_2
    tour_taille['L'] = tour_taille_3
    tour_taille['XL'] = tour_taille_4
    tour_taille['XXL'] = tour_taille_5
    tour_taille['XXXL'] = tour_taille_6
    tour_taille['XXXXL'] = tour_taille_7
    tour_taille['XXXXXL'] = tour_taille_8


def func_tour_taille_femme():
    tour_taille_1 = fuzz.trimf(tour_taille.universe, [58, 61, 63])  # XS

    tour_taille_2 = fuzz.trimf(tour_taille.universe, [62, 65, 67])  # S

    tour_taille_3 = fuzz.trimf(tour_taille.universe, [66, 71, 75])  # M

    tour_taille_4 = fuzz.trimf(tour_taille.universe, [74, 79, 83])  # L

    tour_taille_5 = fuzz.trimf(tour_taille.universe, [82, 86, 91])  # XL

    tour_taille_6 = fuzz.trimf(tour_taille.universe, [90, 99, 107])  # XXL

    tour_taille_7 = fuzz.trimf(tour_taille.universe, [106, 114, 122])  # XXXL

    tour_taille['S'] = tour_taille_1
    tour_taille['M'] = tour_taille_2
    tour_taille['L'] = tour_taille_3
    tour_taille['XL'] = tour_taille_4
    tour_taille['XXL'] = tour_taille_5
    tour_taille['XXXL'] = tour_taille_6
    tour_taille['XXXXL'] = tour_taille_7



def func_tour_bassin_homme():

    tour_bassin_1 = fuzz.trimf(tour_bassin.universe,[85,95,99]) #S

    tour_bassin_2 = fuzz.trimf(tour_bassin.universe,[98,102,105]) #M

    tour_bassin_3 = fuzz.trimf(tour_bassin.universe,[104,108,111]) #L

    tour_bassin_4 = fuzz.trimf(tour_bassin.universe,[110,115,120]) #XL

    tour_bassin_5 = fuzz.trimf(tour_bassin.universe,[119,123,126]) #XXL

    tour_bassin_6 = fuzz.trimf(tour_bassin.universe,[125,128,131]) #XXXL

    tour_bassin_7 = fuzz.trimf(tour_bassin.universe,[130,134,138]) #XXXXL

    tour_bassin_8 = fuzz.trimf(tour_bassin.universe,[137,141,144]) #XXXXXL



    tour_bassin['S'] = tour_bassin_1
    tour_bassin['M'] = tour_bassin_2
    tour_bassin['L'] = tour_bassin_3
    tour_bassin['XL'] = tour_bassin_4
    tour_bassin['XXL'] = tour_bassin_5
    tour_bassin['XXXL'] = tour_bassin_6
    tour_bassin['XXXXL'] = tour_bassin_7
    tour_bassin['XXXXXL'] = tour_bassin_8


def func_tour_bassin_femme():

    tour_bassin_1 = fuzz.trimf(tour_bassin.universe,[84,87,89]) #XS

    tour_bassin_2 = fuzz.trimf(tour_bassin.universe,[88,91,93]) #S

    tour_bassin_3 = fuzz.trimf(tour_bassin.universe,[92,96,101]) #M

    tour_bassin_4 = fuzz.trimf(tour_bassin.universe,[100,105,109]) #L

    tour_bassin_5 = fuzz.trimf(tour_bassin.universe,[108,113,117]) #XL

    tour_bassin_6 = fuzz.trimf(tour_bassin.universe,[116,123,129]) #XXL

    tour_bassin_7 = fuzz.trimf(tour_bassin.universe,[128,135,140]) #XXXL



    tour_bassin['S'] = tour_bassin_1
    tour_bassin['M'] = tour_bassin_2
    tour_bassin['L'] = tour_bassin_3
    tour_bassin['XL'] = tour_bassin_4
    tour_bassin['XXL'] = tour_bassin_5
    tour_bassin['XXXL'] = tour_bassin_6
    tour_bassin['XXXXL'] = tour_bassin_7


def func_taille_pantalon_homme():

    #Definition ...
    taille_pantalon_1 = fuzz.trapmf(taille_pantalon.universe,[30,30,38,41]) #S

    taille_pantalon_2 = fuzz.trapmf(taille_pantalon.universe,[42,42,43,45]) #M

    taille_pantalon_3 = fuzz.trapmf(taille_pantalon.universe,[46,46,48,49]) #L

    taille_pantalon_4 = fuzz.trapmf(taille_pantalon.universe,[50,51,54,55]) #XL

    taille_pantalon_5 = fuzz.trapmf(taille_pantalon.universe,[56,56,58,59]) #XXL

    taille_pantalon_6 = fuzz.trapmf(taille_pantalon.universe,[60,60,62,63]) #XXXL

    taille_pantalon_7 = fuzz.trapmf(taille_pantalon.universe,[64,64,66,67]) #XXXXL



    taille_pantalon['S']      = taille_pantalon_1
    taille_pantalon['M']      = taille_pantalon_2
    taille_pantalon['L']      = taille_pantalon_3
    taille_pantalon['XL']     = taille_pantalon_4
    taille_pantalon['XXL']    = taille_pantalon_5
    taille_pantalon['XXXL']   = taille_pantalon_6
    taille_pantalon['XXXXL']  = taille_pantalon_7


def func_taille_pantalon_femme():

    #Definition ...
    taille_pantalon_1 = fuzz.trapmf(taille_pantalon.universe,[30,30,32,34]) #S

    taille_pantalon_2 = fuzz.trapmf(taille_pantalon.universe,[35,35,37,38]) #M

    taille_pantalon_3 = fuzz.trapmf(taille_pantalon.universe,[39,39,41,42]) #L

    taille_pantalon_4 = fuzz.trapmf(taille_pantalon.universe,[43,43,45,46]) #XL

    taille_pantalon_5 = fuzz.trapmf(taille_pantalon.universe,[47,47,49,50]) #XXL

    taille_pantalon_6 = fuzz.trapmf(taille_pantalon.universe,[51,51,53,54]) #XXXL

    taille_pantalon_7 = fuzz.trapmf(taille_pantalon.universe,[55,55,58,60]) #XXXXL



    taille_pantalon['S']      = taille_pantalon_1
    taille_pantalon['M']      = taille_pantalon_2
    taille_pantalon['L']      = taille_pantalon_3
    taille_pantalon['XL']     = taille_pantalon_4
    taille_pantalon['XXL']    = taille_pantalon_5
    taille_pantalon['XXXL']   = taille_pantalon_6
    taille_pantalon['XXXXL']  = taille_pantalon_7


def pantalonHomme():
    func_tour_taille_homme()
    func_tour_bassin_homme()
    func_taille_pantalon_homme()


def pantalonFemme():
    func_tour_taille_femme()
    func_tour_bassin_femme()
    func_taille_pantalon_femme()


def func_Rules_Pantalon(tourTaille: int, tourHanche: int):
    # definitions des regles
    rule1 = ctrl.Rule(tour_taille['S'] & tour_bassin['S'], taille_pantalon['S'])
    rule11 = ctrl.Rule(tour_taille['M'] & tour_bassin['S'], taille_pantalon['M'])
    rule12 = ctrl.Rule(tour_taille['S'] & tour_bassin['M'], taille_pantalon['M'])

    rule2 = ctrl.Rule(tour_taille['M'] & tour_bassin['M'], taille_pantalon['M'])
    rule21 = ctrl.Rule(tour_taille['L'] & tour_bassin['M'], taille_pantalon['L'])
    rule22 = ctrl.Rule(tour_taille['M'] & tour_bassin['L'], taille_pantalon['L'])

    rule3 = ctrl.Rule(tour_taille['L'] & tour_bassin['L'], taille_pantalon['L'])
    rule31 = ctrl.Rule(tour_taille['XL'] & tour_bassin['L'], taille_pantalon['XL'])
    rule32 = ctrl.Rule(tour_taille['L'] & tour_bassin['XL'], taille_pantalon['XL'])

    rule4 = ctrl.Rule(tour_taille['XL'] & tour_bassin['XL'], taille_pantalon['XL'])
    rule41 = ctrl.Rule(tour_taille['XXL'] & tour_bassin['XL'], taille_pantalon['XXL'])
    rule42 = ctrl.Rule(tour_taille['XL'] & tour_bassin['XXL'], taille_pantalon['XXL'])

    rule5 = ctrl.Rule(tour_taille['XXL'] & tour_bassin['XXL'], taille_pantalon['XXL'])
    rule51 = ctrl.Rule(tour_taille['XXXL'] & tour_bassin['XXL'], taille_pantalon['XXXL'])
    rule52 = ctrl.Rule(tour_taille['XXL'] & tour_bassin['XXXL'], taille_pantalon['XXXL'])

    rule6 = ctrl.Rule(tour_taille['XXXL'] & tour_bassin['XXXL'], taille_pantalon['XXXL'])
    rule61 = ctrl.Rule(tour_taille['XXXXL'] & tour_bassin['XXXL'], taille_pantalon['XXXXL'])
    rule62 = ctrl.Rule(tour_taille['XXXL'] & tour_bassin['XXXXL'], taille_pantalon['XXXXL'])

    rule7 = ctrl.Rule(tour_taille['XXXXL'] & tour_bassin['XXXXL'], taille_pantalon['XXXXL'])

    rule_S = ctrl.Rule(tour_bassin['S'], taille_pantalon['S'])
    rule_M = ctrl.Rule(tour_bassin['M'], taille_pantalon['M'])
    rule_L = ctrl.Rule(tour_bassin['L'], taille_pantalon['L'])
    rule_XL = ctrl.Rule(tour_bassin['XL'], taille_pantalon['XL'])
    rule_XXL = ctrl.Rule(tour_bassin['XXL'], taille_pantalon['XXL'])
    rule_XXXL = ctrl.Rule(tour_bassin['XXXL'], taille_pantalon['XXXL'])
    rule_XXXXL = ctrl.Rule(tour_bassin['XXXXL'], taille_pantalon['XXXXL'])

    # Compilation des regles
    pantalon_regles = ctrl.ControlSystem([rule1, rule11, rule12,
                                          rule2, rule21, rule22,
                                          rule3, rule31, rule32,
                                          rule4, rule41, rule42,
                                          rule5, rule51, rule52,
                                          rule6, rule61, rule62,
                                          rule7,
                                          rule_S, rule_M, rule_L, rule_XL, rule_XXL, rule_XXXL, rule_XXXXL
                                          ])

    pantalon = ctrl.ControlSystemSimulation(pantalon_regles)

    pantalon.input['tour_taille'] = tourTaille
    pantalon.input['tour_bassin'] = tourHanche

    pantalon.compute()

    return "Votre taille de pantalon est : " + str(int(pantalon.output['taille_pantalon']))


def pantalon(tourTaille: str, tourHanche: str,genre: str):
    p = user_pantalon(tourTaille=int(tourTaille), tourHanche=int(tourHanche), genre=genre)
    p.save()
    if genre == "M":
        pantalonHomme()
    else:
        pantalonFemme()

    return  func_Rules_Pantalon(int(tourTaille), int(tourHanche))

