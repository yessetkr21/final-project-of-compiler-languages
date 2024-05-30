# final-project-of-compiler-languages
![image](https://github.com/yessetkr21/final-project-of-compiler-languages/assets/125666647/41fc37ed-31fd-4b04-8f10-4666462ced1c)
Usando los metodos descritos en el aula de clase para computar primeros y siguientes ´ , realizar
una implementacion que reciba como entrada un archivo llamado ´ glcs.in el cual contiene varias
GLCs y generar un archivo de salida llamado pr sig.out que contenga sus respectivos conjuntos primeros y siguientes como se describen a continuacion. ´
1.1 El formato de la entrada en el archivo glcs.in
1. Una l´ınea con un numero ´ n que indica cuantos casos entran (5 en el archivo glcs.in).
2. Una l´ınea con un numero ´ k que indica es el numero de no terminales. ´
3. Ahora, k l´ıneas con las producciones, con el formato:
<no terminal> -> <alternativas de producciones del s´ımbolo no
terminal separadas por barras verticales>
donde la primera no terminal es el s´ımbolo inicial. Observacion: El s ´ ´ımbolo inicial no
siempre sera´ S, puede ser otro dependiendo de como este definido el lenguaje ´ . En caso
que se presente una produccion´ ε aparecera la palabra ´ epsilon.
1.2 El formato de la salida en el archivo pr sig.out
1. Una l´ınea con un numero ´ n que indica cuantos casos salen.
2. Una l´ınea con un numero ´ k que indica es el numero de no terminales. ´
3. Ahora, k l´ıneas con los primeros, con el formato:
Pr(<no terminal>) = {<lista de primeros del s´ımbolo no
terminal separadas por comas>}
4. Luego, k l´ıneas con los siguientes, con el formato:
Sig(<no terminal>) = {<lista de siguientes del s´ımbolo no
terminal separadas por comas>}
