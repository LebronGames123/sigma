def calculate_bmi(Height,Weight):
    print(f"Height = {Height}")
    print(f"Weight = {Weight}")


    BMI = Weight/(Height**2)
    formatted_bmi="{:.2f}".format(BMI)

    print(f"Your BMI = {formatted_bmi}")


    if BMI<18.5:
        Classification="Under Weight"
        return -1
    elif BMI>= 18.5 and BMI<=25.0:
        Classification="Normal Weight"
        return 0
    else:
        Classification="Over Weight"
        return 1

    print("Your BMI classification is: " + Classification)



calculate_bmi(Height=1.73,Weight=53)