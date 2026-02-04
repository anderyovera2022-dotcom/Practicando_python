import pyfiglet

texto = "Anderson"
resultado = pyfiglet.figlet_format(texto, font="slant")

# Cambiar los símbolos por letras
resultado = resultado.replace("_", "A")
resultado = resultado.replace("/", "N")
resultado = resultado.replace("|", "D")

print(resultado)

#Output:
#h
#h
#a
#q  q   x  r   e e  s  e e a a r   c    h  h
#qqq  x x r   ee  ss  ee  aaa r    ccc h  hq
#qq

