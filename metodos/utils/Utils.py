import sys
import math
import sympy as sp

class Utils_Metodos:
    def __init__(self) -> None:
        pass

    def evaluar_funcion(self, valor:int, func:str) -> float:
        x = sp.symbols('x')
        expresion_str = sp.sympify(func)
        res = expresion_str.subs(x, valor)
        return res.evalf()

    def formato_texto(self, datos, headers = False):
        text = '|'
        if headers:
            for dato in datos:
                text += f'{dato:<15}|'
            print(''.ljust(len(text),'_'))
            print(text)
            return len(text)
        for dato in datos:
            text += f'{dato.center(15)}|'
        print(text)

# ERRORES
    def value_error(self):
        print('\n -> SOLO ES VALIDO NUMEROS\n')
        sys.exit()