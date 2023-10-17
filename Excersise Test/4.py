while True:
    x = input("Enter a number:")
    try:
        x = int(x)
        print(x*x)
        break
    except:
        continue