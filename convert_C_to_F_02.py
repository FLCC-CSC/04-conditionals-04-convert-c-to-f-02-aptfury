# FILE NAME - convert_C_to_F_02.py

# NAME: Blake Lemarr
# DATE: 03/02/2026
# BRIEF DESCRIPTION: A program that converts values from C to F or F to C depending on user input.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius")

menu_selection: int = int(input("Please choose from the above menu: "))
temperature: float = float(input("Enter a temperature to convert: "))

if menu_selection == 1:
    result: float = temperature * 9/5 + 32
    print(f"{temperature} degrees Celsius is {result} degrees Fahrenheit.")
elif menu_selection == 2:
    result: float = (temperature - 32) * 5/9
    print(f"{temperature} degrees Fahrenheit is {result} degrees Celsius.")

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

I did learn more about how to offer menus for users in the terminal.
I also learned that -40F equals -40C, which is fascinating!





'''