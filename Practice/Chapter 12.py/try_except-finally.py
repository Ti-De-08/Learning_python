"""Finally block is more reliable than try-except-elso block inside a function.
   - The finally block is executed no matter what, even if an exception occurs.
   - The try-else block is executed only if an exception occurs."""


def main():
    try:
        a = int(input("Hey, please enter a number: "))
        print(a)


    except Exception as e: #here Exception is a base class for all built-in exceptions
        print("An error occurred:", e)

    finally:
        print("Now inside finally block.")


main()

#append is used to add an element to the end of a list.