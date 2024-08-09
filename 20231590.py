#variables
PASS = 0
DEFFER = 0
FAIL = 0
progress = 0
Exclude = 0
Trailer = 0
Retriever = 0
credit_progress = 0
outcome_list = []
marks = {}

from graphics import *
# Histogram data
chart_height = 600;
bar_width = 80
bar_gap = 20
initial_gap = 40
footer_gap = 100

# Calculate chart height 
def chart_hight_sum():  #Fix function name here
    highest_count = max( progress, Trailer , Exclude , Retriever )
    return highest_count*20 + 300

    
def display_histogram():
    height = chart_hight_sum()
    win = GraphWin("Histogram", 600, 500)
    win.setBackground("Mint Cream")

    histogram_header(win)
    
    histogram_bar(win, 0, "Progress", progress, "palegreen")
    histogram_bar(win, 1, "Trailer", Trailer, "limegreen")
    histogram_bar(win, 2, "Retriever", Exclude, "yellowgreen")
    histogram_bar(win, 3, "Excluded", Retriever, "pink")

    histogram_footer(win)

# draw a histogram bar
def histogram_bar(win, bar_index, bar_name, count, color,):
    # calculate bar x cordinates dep
    bar_x = initial_gap + bar_index * (bar_width + bar_gap)
    bar_height = 40*count
    
    #create bar rectangle
    rectangle = Rectangle(Point(bar_x, win.getHeight() - footer_gap), Point(bar_x + bar_width, win.getHeight() - footer_gap - bar_height))
    rectangle.setFill(color)
    rectangle.draw(win)

    #bar count text
    count_text = Text(Point(bar_x + bar_width/2, win.getHeight() - footer_gap - bar_height - 20), str(count))
    count_text.draw(win)

    #bar_name_text
    bar_name = Text(Point(bar_x + bar_width/2, win.getHeight()- footer_gap + 20), bar_name)
    bar_name.draw(win)

# histogram header information
def histogram_header(win):
    heading = Text(Point(200, 30), 'Histogram Results')
    heading.draw(win)
    heading.setTextColor("grey")
    heading.setSize(24)
    heading.setStyle("bold")
    heading.setFace("helvetica")

# histogram footer information
def histogram_footer(win):
    footer = Text(Point(150, win.getHeight() - footer_gap + 50), str(total_count) + " outcomes total")
    footer.draw(win)                                    
    footer.setTextColor("grey")
    footer.setSize(20)
    footer.setFace("helvetica")

    base_line =Line(Point(20,400),Point(500,400))
    base_line.draw(win)


#function for check the range and integer in studentversion
def student_validation(credit_value_student):
    while True:
        try:
            credit_level = int(input("please enter your credit at " + credit_value_student ))
            
            if credit_level not in range(0,121,20):
                print("OUT OF RANGE")
                continue
            
        except ValueError:
            print("INTEGER REQUIRED")
            continue
        break
    return credit_level

#function for check the range and integer in staff versio
def student_validation_staff(credit_value_staff):
    while True:
        try:
            credit_level = int(input("please enter your credit at " + credit_value_staff ))
            if credit_level not in range(0,121,20):
                print("OUT OF RANGE")
                continue
            
        except ValueError:
            print("INTEGER REQUIRED")
            continue
        break
    return credit_level

#progression outcome in student version
def student_progression():
    while True:
        PASS = student_validation ("Pass  ")
        DEFER = student_validation("Defer ")
        FAIL = student_validation ("Fail  ")

        if PASS + DEFER + FAIL != 120:
            print("TOTAL INCORRECT")
            continue
        break
    
    if PASS == 120:
        credit_progress = "\nProgress"

    elif PASS == 100:
        credit_progress = "\nProgress(module trailer)"

    elif FAIL == 80 or FAIL == 100 or FAIL == 120:
        credit_progress = "\nExclude"

    else:
        credit_progress = "\nDo not progress-module retriever"

    print(credit_progress)
    print()

##function for student_id
def student_id():
    while True:
        try:
            Id = int(input("Please enter your ID number: w"))
            if 1000000 <= Id < 9999999:
                if Id in marks:
                    print("ID already exists. Please re-enter.")
                else:
                    break
            else:
                print("Please enter a 7 digits number.")
        except ValueError:
            print("Integer Required")
    return Id

# Progression outcome in staff version
def student_progression_staff():
    global PASS, DEFFER, FAIL, progress, Trailer, Exclude, Retriever, credit_progress, total_count

    while True:
        current_student_id = student_id()

        if current_student_id in marks:
            print("ID you entered already exists. Please re-enter.")
            continue

        PASS = student_validation_staff("PASS")
        DEFFER = student_validation_staff("DEFFER")
        FAIL = student_validation_staff("FAIL")

        if PASS + DEFFER + FAIL != 120:
            print("TOTAL INCORRECT")
            continue

        # Update marks dictionary with the entered data
        marks[current_student_id] = {"PASS": PASS, "DEFFER": DEFFER, "FAIL": FAIL}

        break

    if PASS == 120:
        credit_progress = "Progress"
        progress += 1

    elif PASS == 100:
        credit_progress = "Progress(module trailer)"
        Trailer += 1

    elif FAIL == 80 or FAIL == 100 or FAIL == 120:
        credit_progress = "Exclude"
        Exclude += 1

    else:
        credit_progress = "Do not progress-module retriver"
        Retriever += 1

    # Part 4 - Dictionary
    outcome_list.append([credit_progress, PASS, DEFFER, FAIL])
    # Part 3 - Text File
    outcome_file = open("outcome_file.txt", "a")
    outcome_file.write(f" *{credit_progress}-{PASS},{DEFFER},{FAIL}\n")
    outcome_file.close()

    print(credit_progress)
    total_count = progress + Trailer + Exclude + Retriever



#function for staff version to input y to continue and q to quit
def staff_system():
    global PASS, DEFFER, FAIL, progress, Trailer, Exclude, Retriever, credit_progress, total_count, marks

    option = input("\nIf you would like to enter another set of credits, please enter 'y' to continue or 'q' to quit\nPlease enter: ")
    print()

    if option.lower() == "y":
        staff_version()
    elif option.lower() == "q":
        display_histogram()

        # Part 2: credit_progress
        print("Part 2: credit_progress")
        for items in outcome_list:
            print(f"{items[0]}-{items[1]},{items[2]},{items[3]}")

        # Part 3: credit_progress
        print("\nPart 3:")
        try:
            outcome_file = open("outcome_file.txt", "a")
            outcome_file.write(f" *{credit_progress}-{PASS},{DEFFER},{FAIL}\n")
            outcome_file.close()

        except FileNotFoundError:
            print("Outcome file not found.")

        # Part 4 - Dictionary
        for key in marks.keys():
            mark = marks[key]
            print(f"w{key}:{mark['PASS']}-{mark['DEFFER']},{mark['FAIL']}")
    else:
        print("Invalid option. Please enter 'y' to continue or 'q' to quit.")






#loop in staff version
def staff_version():
    while True:
        student_progression_staff()
        staff_system()
        break

#user input for selecting the version
while True:
 
    user = input('''To get access to the student version please enter 1\nTo get access to the staff version please enter 2\nFor the quit program please enter 3\n Please Enter Here: ''')

#gaining access to the student version
    if user == "1":
        text = "WELCOME TO THE STUDENT VERSION"
        print()
        print(text)
        print()

        student_progression()

    #gaining access to the staff version
    elif user == "2":
        outcome_file = open("outcome_file.text","w")
        outcome_file.close()
        text = "WELCOME TO THE STAFF VERSION"
        print()
        print(text)
        print()

        staff_version()

    #to quit
    elif user == "3":
            print("THANK YOU")
            break
    else:
         print("Please, enter the correct input ")
