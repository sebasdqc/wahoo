# IMPORTAMOS LOS MODULOS QUE VAYAMOS A UTILIZAR
import random
from collections import Counter

# GUARDAMOS EL NUMERO QUE NOS OTORGA EL USUARIO O USAMOS EL VALOR DE EJEMPLO
def main():    
    lista_numero = [ ]
    def almacenamiento():
        while True:
#                input_usuario = input(
#"""GENERADOR DE NUMEROS TELEFONICOS
#********************************
#Ingresa un numero de 11 digitos sin delimitadores=> """) 
                input_usuario = ["0","0","2","2","3","4","4","8","8","9","9"] # SI SE DESEA REALIZAR UN INPUT POR CONSOLA, COMENTAR ESTA LINEA Y QUITAR COMENTARIOS DEL IMPUT SUPERIOR
                if len(input_usuario) == 11:
                    for numero in input_usuario:
                        lista_numero.append(numero)
                    return lista_numero
                else:
                    print("Ha habido un problema con tu numero, vuelve a intentarlo.") 
                
    lista_numero_usuario = almacenamiento() # Los elementos de la lista son Strings

    # EXTRAEMOS EL PREFIJO DEL NUMERO QUE INGRESO EL USUARIO ACORDE A LA DISPONIBILIDAD DE LOS DIGITOS
    prefijo_usuario = []
    def prefijo_numero():
        try:
            for digito in lista_numero_usuario:
                if digito == "0":
                    prefijo_usuario.insert(0,digito)
                    lista_numero_usuario.remove("0")
                    break   

            for digito in lista_numero_usuario:
                if digito == "4":
                    prefijo_usuario.insert(1,digito)
                    lista_numero_usuario.remove("4")
                    break
    
            for digito in lista_numero_usuario:
                if digito == "1" or digito == "2":
                    prefijo_usuario.insert(2,digito)
                    lista_numero_usuario.remove(digito)
                    break
                
            if prefijo_usuario[2] == "1":
                for digito in lista_numero_usuario:
                    if digito == "4":
                        prefijo_usuario.insert(3,digito)
                        lista_numero_usuario.remove(digito)
                        break
                    if digito == "6":
                        prefijo_usuario.insert(3,digito)
                        lista_numero_usuario.remove(digito)
                        break
                    if digito == "2":
                        prefijo_usuario.insert(3,digito)
                        lista_numero_usuario.remove(digito)
                        break            

            if prefijo_usuario[2] == "2":
                for digito in lista_numero_usuario:
                    if digito == "4":
                        prefijo_usuario.insert(3,digito)
                        lista_numero_usuario.remove(digito)
                        break

            return prefijo_usuario
        
        except:
            print("Ha ocurrido un error con la creaciòn del prefijo")
            return False
        
    prefijo = prefijo_numero()
    lista = lista_numero_usuario


    # UNIMOS TODOS LOS OCHOS DISPONIBLES PARA CUMPLIR UNA DE LAS CONDICIONES DEL PROYECTO
    lista_ochos_nueva = []
    def ochos():
        for i in lista:
            if i == "8":
                lista_ochos_nueva.append(str(i))
        while "8" in lista:
            lista.remove("8")
        string_ochos = "".join(lista_ochos_nueva)
        string_ochos = (string_ochos)   
        if len(string_ochos) > 0:    
            lista.append(string_ochos)

        return string_ochos

    ochos() # Hacermos el llamado a la funcion
    lista = [int(x) for x in lista] # Guardamos los elementos de la lista como enteros para su mejor manipulacion


    # FUNCION PARA OBTENER LOS VALORES UNICOS DENTRO DE LA LISTA
    def obtener_valores_unicos(lista):
        # Contar las ocurrencias de cada elemento
        conteo = Counter(lista)
        
        # Filtrar los elementos que aparecen solo una vez
        valores_unicos = [valor for valor, count in conteo.items() if count == 1]
        return valores_unicos

    valores_unicos =(obtener_valores_unicos(lista))

    # FUNCION PARA ENCONTRAR LOS VALORES REPETIDOS DENTRO DE LA LISTA
    def encontrar_numeros_repetidos(lista):
        # Usar Counter para contar las ocurrencias de cada número
        conteo = Counter(lista)
        
        # Filtrar los números que aparecen más de una vez
        numeros_repetidos = [numero for numero, frecuencia in conteo.items() if frecuencia > 1]
        return numeros_repetidos

    numeros_repetidos = encontrar_numeros_repetidos(lista)

    # FUNCION PARA RODEAR LOS 3 POR VALORES UNICOS
    def rodear_tres(lista):
        # Encontrar números repetidos en la lista
        conteo = Counter(lista)
        repetidos = numeros_repetidos
        
        if not repetidos or 3 not in lista:
            return False  # No se puede realizar la operación y pasamos la funcion por alto
        
        posiciones_tres = [i for i, num in enumerate(lista) if num == 3]
        
        for pos_tres in posiciones_tres:
            if not repetidos:
                return False  # No quedan números repetidos para usar
            
            num_repetido = random.choice(repetidos)
            posiciones_repetido = [i for i, num in enumerate(lista) if num == num_repetido]
            
            if len(posiciones_repetido) < 2:
                continue  # Necesitamos al menos dos instancias del número repetido para poder rodear el 3
            
            # Intentar colocar el mismo número repetido a ambos lados del 3
            izquierda = pos_tres - 1 if pos_tres > 0 else None
            derecha = pos_tres + 1 if pos_tres < len(lista) - 1 else None
            
            if izquierda is not None and derecha is not None:
                lista[izquierda], lista[posiciones_repetido[0]] = lista[posiciones_repetido[0]], lista[izquierda]
                lista[derecha], lista[posiciones_repetido[1]] = lista[posiciones_repetido[1]], lista[derecha]
            elif izquierda is not None:
                lista[izquierda], lista[posiciones_repetido[0]] = lista[posiciones_repetido[0]], lista[izquierda]
            elif derecha is not None:
                lista[derecha], lista[posiciones_repetido[0]] = lista[posiciones_repetido[0]], lista[derecha]
            
            repetidos.remove(num_repetido)
        
        # Verificar si todos los 3 están rodeados por el mismo número repetido
        for pos in posiciones_tres:
            izquierda = lista[pos-1] if pos > 0 else None
            derecha = lista[pos+1] if pos < len(lista)-1 else None
            if izquierda != derecha or izquierda is None or derecha is None:
                return False
        
        return True  # Todos los 3 están rodeados correctamente

    tres=rodear_tres(lista)

    #FUNCION FINAL PARA LA GENERACION DEL NUMERO, DONDE INTEGRAMOS FUNCIONES Y CONDICIONALES
    def funcion_generadora():
        try:
            while True:
                random.shuffle(lista)
                if (lista[0]==9 and lista[1] == 9) or (lista[1]==9 and lista[2] == 9) or (lista[2]==9 and lista[3] == 9) or (lista[3]==9 and lista[4] == 9) or (lista[4]==9 and lista[5] == 9):
                    continue
                else:
                    
                    if (lista[0]==9 and lista[2] == 9 and lista[1]== any(valores_unicos)) or (lista[1]==9 and lista[3] == 9 and lista[2] == any(valores_unicos) or (lista[2]==9 and lista[4] == 9 and lista[3] == any(valores_unicos))) or (lista[3]==9 and lista[5] == 9 and lista[4] == any(valores_unicos)):
                        pass
                    if tres == True or tres== False:
                        if lista[-1] == 2: # USAMOS EXCLUSIVAMENTE LOS 2 PORQUE USAR EL 3 REQUIERE QUE ESTE RODEADO POR AMBOS LADOS
                            # PENULTIMO DIVISIBLE POR ULTIMO
                            if lista[-2] % lista[-1]== int(0) and lista[-2] != 0:
                                    # INDICE 5,6,7 MAYORES DE 0
                                if lista[0] > 0 and lista[1] > 0 and lista[2] > 0:
                                        break   
                                else:
                                    continue


        except:
            return "No fue posible generar el numero"
            
    funcion_generadora()
    prefijo.extend(lista)
    return prefijo



numero_final = main()
print(f"\nNumero de telefono generado\n{numero_final}\n")