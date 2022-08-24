#Paula Manese
#CFG-FULL STACK
#Task 1
#Question 3

# Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to
# quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872) and outputs the century and decade
# (e.g. "Eighteenth Century, Seventies")


while True:
    try:
        book_year = input("What year was the book written? (Enter the value from 1800 to 1950, or X to exit the program):")
        if book_year == 'X' or book_year == 'x':
            print("Exiting the program!")
            break
        else:
            book_year = int(book_year)

        if 1800 <= book_year < 1900:
            century = "Nineteenth Cantury"
        elif 1900 <= book_year < 1950:
            century = "Twentieth Century"
        else:
            print("Please only enter a value within 1800 to 1950!")
            continue
        tenths = book_year % 1800
        if tenths > 100:
            tenths -= 100
        if 90 <= tenths < 100:
            decade = "Nineties"
        elif 80 <= tenths < 90:
            decade = "Eighties"
        elif 70 <= tenths < 80:
            decade = "Seventies"
        elif 60 <= tenths < 70:
            decade = "Sixties"
        elif 50 <= tenths < 60:
            decade = "Fifties"
        elif 40 <= tenths < 50:
            decade = "Forties"
        elif 30 <= tenths < 40:
            decade = "Thirties"
        elif 20 <= tenths < 30:
            decade = "Twenties"
        elif 10 <= tenths < 20:
            decade = "Second Decade"
        elif 0 <= tenths < 10:
            decade = "First Decade"
        print(f"The book was written in the {decade} of the {century} Century. ")
        break
    except ValueError:
        print("Please only enter numerical values between 1800 to 1950!")
        continue