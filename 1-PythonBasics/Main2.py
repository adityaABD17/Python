def Addition(No1,No2):
    Result=0
    Result=No1+No2
    return Result

def main():
    Value1= int(input("Enter first number"))

    Value2= int(input("Enter second number"))

    Answer=0
    Answer = Addition(Value1, Value2)

    print("Addition is: ", Answer)

if __name__ == "__main__":  #Starter
    main()
