# Les imports
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from res.functions.menu import taille, poids, taille_v, tv
from res.models import user_tee_shirt


# TAILLE
def func_taille():
    taille_1 = fuzz.trimf(taille.universe, [30, 140, 151])  # XXS

    taille_2 = fuzz.trimf(taille.universe, [149, 155, 161])  # XS

    taille_3 = fuzz.trimf(taille.universe, [159, 165, 171])  # S

    taille_4 = fuzz.trimf(taille.universe, [169, 175, 181])  # M

    taille_5 = fuzz.trimf(taille.universe, [179, 183, 184])  # L

    taille_6 = fuzz.trimf(taille.universe, [184, 190, 196])  # XL

    taille_7 = fuzz.trimf(taille.universe, [189, 195, 201])  # XXL

    taille_8 = fuzz.trimf(taille.universe, [199, 210, 221])  # XXL

    taille['XXS'] = taille_1
    taille['XS'] = taille_2
    taille['S'] = taille_3
    taille['M'] = taille_4
    taille['L'] = taille_5
    taille['XL'] = taille_6
    taille['XXL'] = taille_7
    taille['XXXL'] = taille_8


# POIDS
def func_poids():
    poids_1 = fuzz.trimf(poids.universe, [0, 30, 41])  # XXS

    poids_2 = fuzz.trimf(poids.universe, [40, 45, 51])  # XS

    poids_3 = fuzz.trimf(poids.universe, [50, 55, 61])  # S

    poids_4 = fuzz.trimf(poids.universe, [60, 65, 71])  # M

    poids_5 = fuzz.trimf(poids.universe, [70, 75, 81])  # L

    poids_6 = fuzz.trimf(poids.universe, [80, 85, 91])  # XL

    poids_7 = fuzz.trimf(poids.universe, [90, 95, 101])  # XXL

    poids_8 = fuzz.trimf(poids.universe, [100, 115, 131])  # XXL

    poids['XXS'] = poids_1
    poids['XS'] = poids_2
    poids['S'] = poids_3
    poids['M'] = poids_4
    poids['L'] = poids_5
    poids['XL'] = poids_6
    poids['XXL'] = poids_7
    poids['XXXL'] = poids_8


def func_taille_Vetements():
    taille_v_XXS = fuzz.trapmf(taille_v.universe, [0, 0, 1, 2])

    taille_v_XS = fuzz.trapmf(taille_v.universe, [2, 2, 3, 4])

    taille_v_S = fuzz.trapmf(taille_v.universe, [4, 4, 5, 6])

    taille_v_M = fuzz.trapmf(taille_v.universe, [6, 6, 7, 8])

    taille_v_L = fuzz.trapmf(taille_v.universe, [8, 8, 9, 10])

    taille_v_XL = fuzz.trapmf(taille_v.universe, [10, 10, 11, 12])

    taille_v_XXL = fuzz.trapmf(taille_v.universe, [12, 12, 13, 14])

    taille_v_XXXL = fuzz.trapmf(taille_v.universe, [14, 14, 15, 16])

    taille_v['XXS'] = taille_v_XXS
    taille_v['XS'] = taille_v_XS
    taille_v['S'] = taille_v_S
    taille_v['M'] = taille_v_M
    taille_v['L'] = taille_v_L
    taille_v['XL'] = taille_v_XL
    taille_v['XXL'] = taille_v_XXL
    taille_v['XXXL'] = taille_v_XXXL


def vetementHommeFemme():
    func_taille()
    func_poids()
    func_taille_Vetements()


def func_Rules_Vetement(t, p):
    rule1 = ctrl.Rule(taille['XXS'] & poids['XXS'], taille_v['XXS'])
    rule11 = ctrl.Rule(taille['XS'] & poids['XXS'], taille_v['XS'])
    rule12 = ctrl.Rule(taille['XXS'] & poids['XS'], taille_v['XS'])

    rule2 = ctrl.Rule(taille['XS'] & poids['XS'], taille_v['XS'])
    rule21 = ctrl.Rule(taille['S'] & poids['XS'], taille_v['S'])
    rule22 = ctrl.Rule(taille['XS'] & poids['S'], taille_v['S'])

    rule3 = ctrl.Rule(taille['S'] & poids['S'], taille_v['S'])
    rule31 = ctrl.Rule(taille['M'] & poids['S'], taille_v['M'])
    rule32 = ctrl.Rule(taille['S'] & poids['M'], taille_v['M'])

    rule4 = ctrl.Rule(taille['M'] & poids['M'], taille_v['M'])
    rule41 = ctrl.Rule(taille['L'] & poids['M'], taille_v['L'])
    rule42 = ctrl.Rule(taille['M'] & poids['L'], taille_v['L'])

    rule5 = ctrl.Rule(taille['L'] & poids['L'], taille_v['L'])
    rule51 = ctrl.Rule(taille['XL'] & poids['L'], taille_v['XL'])
    rule52 = ctrl.Rule(taille['L'] & poids['XL'], taille_v['XL'])

    rule6 = ctrl.Rule(taille['XL'] & poids['XL'], taille_v['XL'])
    rule61 = ctrl.Rule(taille['XXL'] & poids['XL'], taille_v['XXL'])
    rule62 = ctrl.Rule(taille['XL'] & poids['XXL'], taille_v['XXL'])

    rule7 = ctrl.Rule(taille['XXL'] & poids['XXL'], taille_v['XXL'])
    rule71 = ctrl.Rule(taille['XXXL'] & poids['XXL'], taille_v['XXXL'])
    rule72 = ctrl.Rule(taille['XXL'] & poids['XXXL'], taille_v['XXXL'])

    rule8 = ctrl.Rule(taille['XXXL'] & poids['XXXL'], taille_v['XXXL'])

    rule_XXS = ctrl.Rule(taille['XXS'], taille_v['XXS'])
    rule_XS = ctrl.Rule(taille['XS'], taille_v['XS'])
    rule_S = ctrl.Rule(taille['S'], taille_v['S'])
    rule_M = ctrl.Rule(taille['M'], taille_v['M'])
    rule_L = ctrl.Rule(taille['L'], taille_v['L'])
    rule_XL = ctrl.Rule(taille['XL'], taille_v['XL'])
    rule_XXL = ctrl.Rule(taille['XXL'], taille_v['XXL'])
    rule_XXXL = ctrl.Rule(taille['XXXL'], taille_v['XXXL'])

    # Compilation des regles
    vetement_regle = ctrl.ControlSystem([rule1, rule11, rule12,
                                         rule2, rule21, rule22,
                                         rule3, rule31, rule32,
                                         rule4, rule41, rule42,
                                         rule5, rule51, rule52,
                                         rule6, rule61, rule62,
                                         rule7, rule71, rule72,
                                         rule8,
                                         rule_XXS, rule_XS, rule_S, rule_M, rule_L, rule_XL, rule_XXL, rule_XXXL
                                         ])

    vetement = ctrl.ControlSystemSimulation(vetement_regle)

    vetement.input['taille'] = t
    vetement.input['poids'] = p
    vetement.compute()

    return "Votre taille de tee-shirt est : " +  str(tv[int(vetement.output['taille_vetement']) // 2])


def tee_shirt(t: str, p: str, genre: str):
    tee = user_tee_shirt(taille=int(t), poids=int(p), genre=genre)
    tee.save()
    vetementHommeFemme()
    return func_Rules_Vetement(int(t), int(p))
