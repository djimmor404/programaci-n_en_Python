
horas = segundos // 3600  
minutos = (segundos % 3600) // 60  
segundos_restantes = segundos % 60

 horas, mibutos, segundos_restantes

segundos = int(imput("Dime un numero total de segundos"))

horas, minutos, segundos_restantes = convertir_tiempo(segundos)

print("(segundos) segundos equivalen a (horas), (horas) minutos y (segundos_restantes) segundos.")

<