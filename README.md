¿Qué tipo de condición te resultó mas intuitiva?

La comparación encadenada (1 < numero < 100), me parecio intuitiva porque se parece mucho a la notación matemática que se aprendende en la escuela. 


¿En qué caso usarías condicionales anidadas en un programa real?

Las condicionales anidadas se usan cuando una decisión depende totalmente de que se haya cumplido una condición previa. Es como un filtro de seguridad o un árbol de decisiones.
Por eso considero el sistema de login una buena opcion para utilizar ya que primero hay que ver si el usuario existe y el if anidado seria que si existe cual seria la contraseña correcto: 

Sistemas de Login:

if: ¿El usuario existe?

if (anidado): Si existe, ¿la contraseña es correcta? (No tiene sentido validar la contraseña si el usuario ni siquiera está en la base de datos).