while True:
    FC = input("Celsius or Fahrenheit?")
    if FC == "C" or FC=="c" or FC== "Celsius":
        CDeg = float(input("Celsius: "))
        print((9/5)*CDeg+32 )
    if FC== "F" or FC == "f" or FC == "Fahrenheit":
         FDeg = float(input("Fahrenheit: "))
         print((5*(FDeg-32))/9)
