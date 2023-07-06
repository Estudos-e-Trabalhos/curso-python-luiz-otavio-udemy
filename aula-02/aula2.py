# o sep serve para escolher um separador 
print(12, 34, sep="-")

# quebras
# \r \n -> CRLF - windows
# \n -> LF
print(12, 34, sep="/", end='\r\n')  
print(12, 10, sep="/", end='##\n')  