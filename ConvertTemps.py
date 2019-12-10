#!/usr/bin/python3
# Conversions for temperature
# v1 - basic functionality - Fahrenheit, Celsius, Kelvin conversions
# by -Tim Cowan

def main():
    # invalid_response set for while statement to loop until 'q' is entered to quit the program
    invalid_response = None
    while invalid_response != "q":

        # taking options for what type of value and units your starting temp is in that you want to convert from
        temp_type = input("Would you like to convert from Fahrenheit (F|f), Celsius (C|c), or Kelvin (K|k) ?: ").lower()
        temp_value = float(input("Temperature to convert? : "))
        if temp_value % 2 == 0:
            print(temp_value, "is an even number")
        if temp_value % 2 != 0:
            print(temp_value, "is an odd number")
        # conversions for temps in k,c,f -v1 specific
        f_to_c = (temp_value - 32) * (5 / 9)
        f_to_k = (temp_value + 459.67) * (5 / 9)
        c_to_k = temp_value + 273.15
        c_to_f = (temp_value * (9 / 5)) + 32
        k_to_f = (temp_value - 273.15) * (9 / 5) + 32
        k_to_c = temp_value - 273.15
        if temp_type[0] == 'f':
            print("(", temp_value, "F)  converted to celsius ---> ", f_to_c, sep='')
            print("(", temp_value, "F)  converted to kelvin ---> ", f_to_k, sep='')
            invalid_response = input("Q|q to quit or press enter to continue : ")
        if temp_type[0] == 'c':
            print("(", temp_value, "C)  converted to kelvin ---> ", c_to_k, sep='')
            print("(", temp_value, "C)  converted to fahrenheit ---> ", c_to_f, sep='')
            invalid_response = input("Q|q to quit or press enter to continue : ")
        if temp_type[0] == 'k':
            print("(", temp_value, "K)  converted to celsius ---> ", k_to_c, sep='')
            print("(", temp_value, "K)  converted to fahrenheit ---> ", k_to_f, sep='')
            invalid_response = input("Q|q to quit or press enter to continue : ")


if __name__ == "__main__":
    main()
