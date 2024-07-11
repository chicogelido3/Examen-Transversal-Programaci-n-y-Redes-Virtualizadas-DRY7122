vlannum = int(input("¿Cual es el número de ID de la Vlan?"))
if vlannum >= 1 and vlannum <= 1005:
    print("Es una Vlan de rango normal.")
elif vlannum >=1006 and vlannum >= 4095:
    print("Es una Vlan de rango extendida")
else:
    print ("El numero de Vlan ingresado es desconocido")