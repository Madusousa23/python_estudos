"""Peça uma hora (de 0 a 23). Se for antes das 12, diga "Bom dia". Se for entre 12 e 18, diga "Boa tarde". Se for após 18, diga "Boa noite"."""

hora=int(input("Entre com um horário (0 a 23): "))

if hora < 12 :
    print ("BOM DIA!")
elif hora >= 12 and hora < 18 :
    print("BOA TARDE!")
else : 
    print("BOA NOITE!")