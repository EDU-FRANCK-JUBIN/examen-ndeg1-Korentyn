import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

error = ctrl.Antecedent(np.arange(-4, 4, 2), 'error')
error_dot = ctrl.Antecedent(np.arange(-10, 10, 5), 'error_dot')
puissance = ctrl.Consequent(np.arange(-100, 100, 50), 'puissance')

error['too_hot'] = fuzz.trimf(error.universe, [-4, -2, 0])
error['just_right'] = fuzz.trimf(error.universe, [-2, 0, 2])
error['too_cold'] = fuzz.trimf(error.universe, [0, 2, 4])

error_dot['getting_hotter'] = fuzz.trimf(error_dot.universe, [-10, -5, 0])
error_dot['no_change'] = fuzz.trimf(error_dot.universe, [-5, 0, 5])
error_dot['getting_colder'] = fuzz.trimf(error_dot.universe, [0, 5, 10])

puissance['cool'] = fuzz.trimf(puissance.universe, [-100, -50, 0])
puissance['do_nothing'] = fuzz.trimf(puissance.universe, [-50, 0, 50])
puissance['heat'] = fuzz.trimf(puissance.universe, [0, 50, 100])

rule1 = ctrl.Rule(error['too_hot'] | error_dot['getting_colder'], puissance['cool'])
rule2 = ctrl.Rule(error['too_hot'] | error_dot['no_change'], puissance['cool'])
rule3 = ctrl.Rule(error['too_hot'] | error_dot['getting_hotter'], puissance['cool'])
rule4 = ctrl.Rule(error['just_right'] | error_dot['getting_colder'], puissance['heat'])
rule5 = ctrl.Rule(error['just_right'] | error_dot['no_change'], puissance['do_nothing'])
rule6 = ctrl.Rule(error['just_right'] | error_dot['getting_hotter'], puissance['cool'])
rule7 = ctrl.Rule(error['too_cold'] | error_dot['getting_colder'], puissance['heat'])
rule8 = ctrl.Rule(error['too_cold'] | error_dot['no_change'], puissance['heat'])
rule9 = ctrl.Rule(error['too_cold'] | error_dot['getting_hotter'], puissance['heat'])

reglages_clim = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
climatiseur = ctrl.ControlSystemSimulation(reglages_clim)


#Test 1
climatiseur.input['error'] = -1.5
climatiseur.input['error_dot'] = -4
climatiseur.compute()
puissance.view(sim=climatiseur)
#print(climatiseur.output['puissance'])


#Test 2
climatiseur.input['error'] = 0.5
climatiseur.input['error_dot'] = 1
climatiseur.compute()
puissance.view(sim=climatiseur)

#Test 3
climatiseur.input['error'] = -1.5
climatiseur.input['error_dot'] = -1
climatiseur.compute()
puissance.view(sim=climatiseur)

#Test 4
climatiseur.input['error'] = 0.5
climatiseur.input['error_dot'] = 4
climatiseur.compute()
puissance.view(sim=climatiseur)
