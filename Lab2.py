def display_main_menu():
    user_input = input("Enter some numbers separated by commas (e.g. 5, 67,32)")
    formatted_input = user_input.split(",")
    int_list=list(map(int,formatted_input))
    print(f"Your list = {int_list}")
    return(int_list)

def calc_min(lists):
    return min(lists)

def calc_max(lists):
    return max(lists)

def calc_avg(lists):
    return sum(lists)/len(lists)

def calc_median(lists):
    sorted_list=sorted(lists)
    if len(sorted_list)%2 ==1:
        median_index=sorted_list//2
        return sorted_list[median_index]
    else:
        mid1 = len(sorted_list)//2
        mid2 = len(sorted_list)//2-1
        midvalue = (sorted_list[mid1]+sorted_list[mid2])/2
        return midvalue

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    user_input=display_main_menu()
    maxval=calc_max(user_input)
    print(f"The max value in the list = {maxval}")
    minval=calc_min(user_input)
    print(f"The min value in the list = {minval}")
    avgval=calc_avg(user_input)
    print(f"The average value in the list = {avgval}")
    median = calc_median(user_input)
    print(f"The median value = {median:.2f}")


if __name__ == "__main__":
    main()