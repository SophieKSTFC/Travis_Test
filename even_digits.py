from calculator import Calculator

calc = Calculator()
odd_numbers = [ 1, 3, 5, 7, 9]

def is_even(number):
    return False if int(number) in odd_numbers else True

def is_all_even(number):

    number_string = str(number)
    even = True
    for x in range(len(number_string)):
        even &= is_even(number_string[x])
    return even

def process_number(number, direction):

    press_count = 0
    calc.set_number(number)
    while is_all_even(calc.get_number()) != True:
        if direction == "up":
            calc.press_up()
        elif direction == "down":
            calc.press_down()
        else:
            break
        press_count+=1
    return press_count

def main():

    
    test_cases = int(input("Enter number of test cases: "))
    
    for _ in range(test_cases):
        
        display_number = int(input("Enter the display number: "))
        if is_all_even(display_number):
            print("Case #%d: 0" % _)

        else:
            d_presses = process_number(display_number, "down")
            u_presses = process_number(display_number, "up")
    
            if d_presses < u_presses:
                print("Case #%d: %d" % (_, d_presses))
            else:
                print("Case #%d: %d" % (_, u_presses))
  
if __name__ == "__main__":
    main()