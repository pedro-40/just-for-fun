def temperature () :
    tem=  int (input ("enter the temperature in degrees Celsius . "))
    unit = input ("Fahrenheit -->(F) , Kelvin --> (K)")
    
    while unit !="F" and unit !="K" :
        unit = input ("Fahrenheit -->(F) , Kelvin --> (K)")

    if unit == "F" :
        far = 1.8 * tem + 32 
        print(far)

    elif unit == "K" :
        kel = tem + 273.15
        print(kel)

    





temperature()
