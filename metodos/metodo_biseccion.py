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

def calcular_error(xr_nuevo:float, xr_anterior:float) -> float:
    try:
        res = abs(((xr_nuevo - xr_anterior)/ xr_nuevo)) * 100
        return res
    except ZeroDivisionError:
        print('\n -> AL CALCULAR EL ERROR SE ESTA DIVIDIENDO POR CERO ( Intente intervalos diferentes de [-a,a])\n')
        sys.exit()

def calcular_xr(xa:float, xb:float) -> float:
    return (xa + xb) / 2

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

def met_biseccion():
    len_text = 0
    func = input('Ingrese la funcion (Ejemplo "x**3 + 4 * x**2 - 10"), f(x) = ')
    try:
        xa = float(input('Ingrese Xa: '))
        xb = float(input('Ingrese Xb: ')) 
        error_maximo = float(input('Ingrese el error maximo ( En un rango de 100 a 0): '))
        if error_maximo > 100 or error_maximo < 0:
            print('\n -> EL ERROR MAXIMO DEBER ESTA EN UN INTERVALO DE [100, 0] \n')
            sys.exit()
    except ValueError:
        print('\n -> SOLO ES VALIDO NUMEROS\n')
        sys.exit()
    xr = None
    error_porcentual = math.inf
    resultado = 0

    headers = ['Iteracion', 'f(Xa) * f(Xr)','Resultado Xa','Resultado Xb','Resultado Xr','Err porcentual']
    
    iteracion = 1
    while error_porcentual > error_maximo:
        if(xr == None):
            error_porcentual = calcular_error(calcular_xr(xa,xb), 100000)
            len_text = formato_texto(headers, headers= True)
            if( error_porcentual > 100):
                error_porcentual = 100
        else:
            error_porcentual = calcular_error(calcular_xr(xa,xb), xr)

        xr = calcular_xr(xa, xb)
        resultado = evaluar_funcion(xr, func) * evaluar_funcion(xa, func)
        if(resultado < 0):
            xb = xr
        elif (resultado > 0):
            xa = xr
        elif (resultado == 0):
            print( f'El Resultado mas exacto encontrado es: {xa:.5f}')
            break
        formato_texto([f'{iteracion}',f'{resultado:.4f}',f'{xa:.5f}',f'{xb:.5f}',f'{xr:.4f}',f'{error_porcentual:.10f}'])
        iteracion += 1
    print(''.ljust(len_text,'-') + '\n')
    if xa == xb:
        print('NO EXISTEN RESULTADOS CONCLUYENTES\n')



