def display_main_menu():
    user_input = input("Enter some numbers separated by commas (e.g. 5, 67,32)")
    formatted_input = user_input.split(",")
    int_list=list(map(int,formatted_input))
    print(f"Your list = {int_list}")
    return(int_list)

def calc_min(list):
    return min(list)

def calc_max(list):
    return max(list)

def calc_avg(list):
    return sum(list)/len(list)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    user_input=display_main_menu()
    maxval=calc_max(user_input)
    print(f"The max value in the list = {maxval}")
    minval=calc_min(user_input)
    print(f"The min value in the list = {minval}")
    avgval=calc_avg(user_input)
    print(f"The average value in the list = {avgval}")


if __name__ == "__main__":
    main()