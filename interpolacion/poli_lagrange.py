from sympy import symbols, sympify,simplify, expand, lambdify
import matplotlib.pyplot as plt
import numpy as np
import sys

class P_Lagrange:
    def __init__(self, puntos: dict, errores = False) -> None:
        self.p = puntos
        self.x = []
        self.y = []
        self.terminos = ''
        self.expresion = ''
        self.func = ''
        if errores:
            self.completar_puntos()
        self.format_coords()
        self.poli_lagrange()
        if errores:
            self.poner_error()
        self.draw(errores)

    def lagrange(self, i):
        l = ''
        try:
            for j, (p_numero, valor) in enumerate(self.p.items(), start=1):
                if j != i:
                    xj = valor['x']
                    xi = self.p[f'p{i}']['x']
                    l += f'((x - {xj})/({ xi } - { xj }))*'
        except KeyError: self.key_error(i)

        l = l[:-1]
        poli = expand(l)
        print(f'   L{i - 1}(x) = {poli}')
        return l
                

    def poli_lagrange(self):
        print('\n Terminos del polinomio:')
        for i,(p_numero, valor) in enumerate(self.p.items(),start=1):
            f_x = valor['f(x)']
            self.terminos += f'({f_x} * {self.lagrange(i)}) +'

        self.terminos = self.terminos[:-1]
        self.expresion = simplify(self.terminos)
        print( f'\nPOLINOMINO DE LAGRANGE:  P{len(self.p)}(x) = {self.expresion}' )

    def draw(self, errores):
        x = symbols('x')
        func_evaluar_f = lambdify(x, self.expresion, 'numpy')
        if errores:
            expresion_str = sympify(self.func)
            x_f_real = np.linspace(min(self.x), max(self.x), 100)
            y_f_real = []
            for valor in x_f_real:
                y_f_real.append(self.evaluar_func(x, expresion_str, valor))
            plt.plot(x_f_real, y_f_real, color='green', label='Curva de la función real')
            

        x_curva = np.linspace(min(self.x), max(self.x), 100)
        y_curva = func_evaluar_f(x_curva)
        plt.plot(x_curva, y_curva, color='red', label='Curva del polonomio de Lagrange')
        plt.scatter(self.x,self.y, color='blue', marker='x')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.show()

    def completar_puntos(self):
        try:
            self.func = input('Ingrese el la funcion para encotrar el polinomio interpolante (EJ: 1/x): ')
            x = symbols('x')
            expresion_str = sympify(self.func)
            for punto in self.p:
                self.p[f'{punto}']['f(x)'] = self.evaluar_func(x, expresion_str, self.p[f'{punto}']['x'])

        except: self.func_invalida_error()

    def evaluar_func(self, x, expresion_str, valor):
        res = expresion_str.subs(x, valor)
        return res.evalf()

    def format_coords(self):
        for valor in self.p.values():
            self.x.append(valor['x'])
            self.y.append(valor['f(x)'])
        
        if len(self.x) != len(set(self.x)): self.elementos_repetidos_error()
    
    def calcular_error(self, x1:float, x0:float) -> float:
        try:
            res = abs(((x1 - x0)/ x1)) * 100
            return res
        except ZeroDivisionError:
            print('\n -> AL CALCULAR EL ERROR SE ESTA DIVIDIENDO POR CERO\n')
            sys.exit()
    
    def poner_error(self):
        try:
            v = float(input('En que valor desea evaluar el error: '))
            x = symbols('x')
            expresion_str = sympify(self.func)
            real = self.evaluar_func(x, expresion_str, v)
            expresion_str = sympify(self.expresion)
            estimado = self.evaluar_func(x, expresion_str, v)
            print(f'Valor Real: {real:.6f}')
            print(f'Valor estimado: {estimado:.6f}')
            print(f'Error: {self.calcular_error(real,estimado):.6f}')
        except TypeError:
            print(f'LA FUNCION NO ESTA DEFINIDA EN EL PUNTO "{v}" O LA FUNCION NO ES VALIDA')
            sys.exit()
        except ValueError:
            print(f'EL VALOR NO SE VALIDO')
            sys.exit()

    #ERRORES
    def key_error(self,i):
        print(f'\n ---> NO EXISTE p{i} DENTRO DEL LOS PUNTOS:')
        for (clave, valor) in self.p.items():
            print(f"{clave} : {valor}")
        sys.exit()
    
    def elementos_repetidos_error(self):
        print('\n ---> EXISTEN ELEMENTOS QUE ESTAN REPETIDOS EN LAS COORDENADAS X DE LOS PUNTOS <--- \n ---> PUEDE QUE CAUSE VALORES INDETERMINADOS  <--- \n ')
        sys.exit()
    
    def func_invalida_error(self,func):
        print(f'\n ---> LA FUNCION {func} NO ES VALIDA')
        sys.exit()

if __name__ == '__main__':

    # Ejercicio de la clase
    puntos = {
        'p1' : { 'x' :2 , 'f(x)' :5 },
        'p2' : { 'x' :4 , 'f(x)' :6 },
        'p3' : { 'x' :5 , 'f(x)' :3 },
    }

    # Diferentes puntos de prueba
    puntos_prueba_1 = {
        'p1': {'x': 1, 'f(x)': 2},
        'p2': {'x': 3, 'f(x)': 4},
        'p3': {'x': 6, 'f(x)': 5},
        'p4': {'x': 7, 'f(x)': 7},
        'p5': {'x': 9, 'f(x)': 10}
    }
    puntos_prueba_2 = {
        'p1': {'x': -1, 'f(x)': -1},
        'p2': {'x': 0 , 'f(x)': 1},
        'p3': {'x': 1 , 'f(x)': 3},
        'p4': {'x': 3 , 'f(x)': 7}
    }

    puntos_prueba_3 = {
        'p1': {'x': -2, 'f(x)': -5},
        'p2': {'x': 0 , 'f(x)': 1},
        'p3': {'x': 1 , 'f(x)': 0},
        'p4': {'x': 3 , 'f(x)': 22},
    }

# IMPORTANTE 
    # Solo remplazar ( puntos ) por otro conjunto de puntos, EJ: (puntos_prueba_3)
    # Esto solo calculara el polinomio y lo graficara, pero no dara el calculo del error
    
    # P_Lagrange(puntos) # <---

    # Para comparar con un funcion los puntos tiene que tener 'f(x)' en 0
    puntos_1 = {
        'p1' : { 'x' :2   , 'f(x)' :0 },
        'p2' : { 'x' :2.5 , 'f(x)' :0 }, # Para estos puntos la funcion es '1/x'
        'p3' : { 'x' :4   , 'f(x)' :0 },
    }
    puntos_prueba_4 = {
        'p1': {'x': 0        , 'f(x)': 0},
        'p2': {'x': np.pi/2  , 'f(x)': 0}, # Para estos puntos la funcion es 'sin(x)'
        'p3': {'x': np.pi    , 'f(x)': 0},
        'p4': {'x': 3*np.pi/2, 'f(x)': 0},
    }
    # y se tiene que agregar 'errores=True' dentro de los parametros del objeto
    P_Lagrange(puntos_1, errores=True) # <---