dec_input = int(input("Введите число для перевода: "))
bin_value = []

while dec_input >= 1 :
    remainder = dec_input % 2
    x = bin_value.append(remainder)
    dec_input = (dec_input - remainder) / 2
    x = str(bin_value)
    print(x [:: -1])
    

