import math
import sys



contexto_global = {name: getattr(math, name) for name in dir(math) if not name.startswith("__")}

def evaluar_funcion(x:int, func:str) -> int:
    global contexto_global
    contexto = {"x":x}
    contexto.update(contexto_global)
    try:
        return eval(func, {}, contexto)
    except NameError:
        print(f'\n -> LA FUNCION NO ES VALIDA -> {func} ( La variable debe ser x ) \n')
        sys.exit()
    except SyntaxError:
        print(f'\n -> LA FUNCION TIENE UN ERROR DE SINTAXIS {func} \n')
        sys.exit()

def calcular_error(x1:float, x0:float) -> float:
    try:
        # print(x1)
        # print(x0)
        res = abs(((x1 - x0)/ x1)) * 100
        return res
    except ZeroDivisionError:
        print('\n -> AL CALCULAR EL ERROR SE ESTA DIVIDIENDO POR CERO ( Intente intervalos diferentes de [-a,a])\n')
        sys.exit()

def restriccion(x,res_func):
    if(x == None):
        return math.inf
    # print(evaluar_funcion(x,res_func))
    return evaluar_funcion(x,res_func)

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


def punto_fijo(func,x_inicial = 0):
    x_anterior = x_inicial
    x_actual = None

    err = math.inf
    headers = ['Iteracion','Resultado','Error']
    len_text = formato_texto(headers,headers=True)
    con = 0
     
    while err > 1 :
        x_actual = evaluar_funcion(x_anterior, func)
        # if restriccion(x_anterior,'x + 3 - (x**4)') < 0:
        #     break
        err = calcular_error(x_actual,x_anterior)
        formato_texto([f'{con}',f'{x_actual:.5f}',f'{err:.5f}'])
        x_anterior = x_actual
        
        con += 1
    print(''.ljust(len_text,'-') + '\n')


