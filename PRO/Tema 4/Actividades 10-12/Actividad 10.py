T = ('x','Q','d','S','A','l','o','w','M' )

mayusculas = tuple(x for x in T if x.isupper())
minusculas = tuple(x for x in T if x.islower())

resultado = mayusculas + minusculas

print(resultado)