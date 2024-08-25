import sys
import math
import sympy as sp
from metodos.utils.Utils import Utils_Metodos as U

class Metodos:
    def __init__(self) -> None:
        self.u = U()
        self.start()
        self.all_methods()

    def start(self):
        self.func = input('Ingrese la funcion (Ejemplo "x**3 + 4 * x**2 - 10"), f(x) = ')
        self.func_punto_fijo = input('Ingrese la funcion el metodo de punto fijo (despejando una x): ')
        try:
            self.err = float(input('Ingrese el error ( En un rango de 100 a 0): '))
            if self.err > 100 or self.err < 0:
                print('\n -> EL ERROR MAXIMO DEBER ESTA EN UN INTERVALO DE [100, 0] \n')
                sys.exit()
        except ValueError: self.u.value_error()
    
    def calcular_error(self, x1:float, x0:float) -> float:
        try:
            res = abs(((x1 - x0)/ x1)) * 100
            return res
        except ZeroDivisionError:
            print('\n -> AL CALCULAR EL ERROR SE ESTA DIVIDIENDO POR CERO ( Intente intervalos diferentes de [-a,a])\n')
            sys.exit()
    
    # Para el metodo de biseccion
    def calcular_xr(self, xa:float, xb:float) -> float:
        return (xa + xb) / 2


# -------------------------------------------------------------------------------------------------------------
    def met_biseccion(self):
        len_text = 0
        try:
            print('---- Intevalo para el metodo de biseccion ----')
            xa = float(input('Ingrese Xa: ')) # 1
            xb = float(input('Ingrese Xb: ')) # 2
        except ValueError: self.u.value_error()
            
        xr = None
        error_porcentual = math.inf
        resultado = 0

        headers = ['Iteracion', 'f(Xa) * f(Xr)','Resultado Xa','Resultado Xb','Resultado Xr','Err porcentual']
        
        iteracion = 1

        print('\nMETODO BISECCION\n')
        while error_porcentual > self.err:
            if(xr == None):
                error_porcentual = self.calcular_error(self.calcular_xr(xa,xb), 100000)
                len_text = self.u.formato_texto(headers, headers= True)
                if( error_porcentual > 100):
                    error_porcentual = 100
            else:
                error_porcentual = self.calcular_error(self.calcular_xr(xa,xb), xr)

            xr = self.calcular_xr(xa, xb)
            resultado = self.u.evaluar_funcion(xr, self.func) * self.u.evaluar_funcion(xa, self.func)
            if(resultado < 0):
                xb = xr
            elif (resultado > 0):
                xa = xr
            elif (resultado == 0):
                print( f'El Resultado mas exacto encontrado es: {xa:.5f}')
                break
            self.u.formato_texto([f'{iteracion}',f'{resultado:.5f}',f'{xa:.5f}',f'{xb:.5f}',f'{xr:.5f}',f'{error_porcentual:.5f}'])
            iteracion += 1
        print(''.ljust(len_text,'-') + '\n')
        if xa == xb:
            print('NO EXISTEN RESULTADOS CONCLUYENTES\n')

# -------------------------------------------------------------------------------------------------------------
    def punto_fijo(self):
        # ((-x**3 + 10)/(4))**(1/2)
        try:
            x_inicial = input('X inicial para el metodo de punto fijo (Por defecto X = 0): ')
            if x_inicial == '':
                x_inicial = 0
            else:
                x_inicial = float(x_inicial)
        except ValueError: self.u.value_error()

        x_anterior = x_inicial
        x_actual = None

        err = math.inf
        headers = ['Iteracion','X anterior','Resultado','Error']
        print('\nMETODO PUNTO FIJO\n')
        len_text = self.u.formato_texto(headers,headers=True)
        con = 0
        while err > self.err :
            x_actual = self.u.evaluar_funcion(x_anterior, self.func_punto_fijo)
            err = self.calcular_error(x_actual,x_anterior)
            self.u.formato_texto([f'{con}',f'{x_anterior:.5f}',f'{x_actual:.5f}',f'{err:.5f}'])
            x_anterior = x_actual
            
            con += 1
        print(''.ljust(len_text,'-') + '\n')
# -------------------------------------------------------------------------------------------------------------


    def all_methods(self):
        self.met_biseccion()
        self.punto_fijo()



