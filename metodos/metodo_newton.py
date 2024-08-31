import math
import sys
import sympy as sp

def calcular_error(x1:float, x0:float) -> float:
        try:
            res = abs(((x1 - x0)/ x1)) * 100
            return res
        except ZeroDivisionError:
            print('\n -> AL CALCULAR EL ERROR SE ESTA DIVIDIENDO POR CERO ( Intente intervalos diferentes de [-a,a])\n')
            sys.exit()

def formato_texto(datos, headers = False):
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

def evaluar_funcion(valor:float, func:str) -> float:
    x = sp.symbols('x')
    expresion_str = sp.sympify(func)
    res = expresion_str.subs(x, valor)
    return res.evalf()

def evaluar_f_derivada(valor: float,func:str):
    x = sp.symbols('x')
    expresion_str = sp.sympify(func)
    derivada = sp.diff(expresion_str, x)
    res = derivada.subs(x, valor)
    return res.evalf()

def linea_final(len_text):
    print(''.ljust(len_text,'-') + '\n')

def newton_rapson():
        func = input('Ingrese la funcion (Ejemplo "x**3 + 4 * x**2 - 10"), f(x) = ')
        try:
            x_inicial = input('X inicial para el metodo de Newton Rapson (Por defecto X = 0): ')
            if x_inicial == '':
                x_inicial = 0
            else:
                x_inicial = float(x_inicial)
        except ValueError: 
            print('\n -> SOLO ES VALIDO NUMEROS\n')
            sys.exit()

        try:
            error = float(input('Ingrese el error ( En un rango de 100 a 0): '))
            if error > 100 or error < 0:
                print('\n -> EL ERROR MAXIMO DEBER ESTA EN UN INTERVALO DE [100, 0] \n')
                sys.exit()
        except ValueError: 
            print('\n -> SOLO ES VALIDO NUMEROS\n')
            sys.exit()


        x_anterior = x_inicial
        x_actual = None

        err = math.inf
        headers = ['Iteracion','X anterior','Resultado','Error']
        len_text = formato_texto(headers,headers=True)
        con = 0
        while err > error:
            
            x_actual = x_anterior - (evaluar_funcion(x_anterior, func) / evaluar_f_derivada(x_anterior ,func) )
            err = calcular_error(x_actual, x_anterior)
            try:
                formato_texto([f'{con}',f'{x_anterior:.5f}',f'{x_actual:.5f}',f'{err:.5f}'])
            except TypeError:
                print('\n-> PUEDE QUE LA FUNCION O SU DERIVADA NO ESTE DEFINIDA EN X INICIAL\n')
                sys.exit()
            x_anterior = x_actual

            con += 1
        linea_final(len_text)

if __name__ == '__main__':
    newton_rapson()