def main():
    try:
        print("Enter first number : ")
        no1=int(input())

        print("Enter second number: ")
        no2=int(input())
        Ans=0
        
        Ans= no1/no2

    except ZeroDivisionError as zobj:
        print("Divide by zero is not allowed",zobj)
        return

    except Exception as zobj:
        print("Exception occured as : ",zobj)
        return

    print("Division is : ",Ans)

if __name__ == "__main__":
    main()