Lista = [1,2,14,16,20,23,25]
for i in Lista:
  contador = 0
  numeros = range(2,10)
  for j in numeros:
    if i % j == 0:
      contador += 1
    elif i == 2:
      contador = 0
  if contador > 0:
    print("No es primo")
  else:
    print("Es primo")