def method():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)


    except Exception as e:
        print("Hey Enter a number") 


    finally:
        print("Hey! I am inside a finally")

method()