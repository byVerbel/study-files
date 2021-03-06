# Programa que calcule nota final de estudiantes a 2 decimales, eliminando la
# peor de las notas y teniendo en cuenta que el profesor tomó las notas de 0-100
# y la universidad recibe calificaciones de 0-5

def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:
    list1 = [nota1,nota2,nota3,nota4,nota5]
    list2 = []
    list1.remove(min(list1))
    for i in list1:
        nota = i/20
        list2.append(nota)
    # Se hace round 2 veces ya que el ejercicio ya que la aproximación de python
    # no es exacta por una extraña ley de los binarios
    promedio = round(sum(list2)/len(list2),3)
    promedio = round(promedio,2)
    return f"El promedio ajustado del estudiante {codigo} es: {promedio}"

# print(nota_quices('AA0010276',40,50,39,76,96))
print(nota_quices("AA0010276", 19,90,38,55,68))
print(nota_quices("IS00201620", 37,10,50,19,79))
print(nota_quices("BIO2201810", 45,46,33,74,22))
print(nota_quices("IQ102201810", 57,100,87,93,21))
print(nota_quices("MA00201520", 5,14,76,91,5))
