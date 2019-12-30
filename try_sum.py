import pyttsx3


try:
    n1=input("Please Enter first num: ")
    n2=input("Please Enter first num: ")
    DIV=int(n1)/int(n2)
    sum=int(n1)+int(n2)
    print("SUM: ",sum)
    print("DIV: ",DIV)


except (ValueError,NameError):
       print("Please Enter the Number")
       s=pyttsx3.init()
       s.say("Please Enter the Number")
       s.runAndWait()
except ZeroDivisionError:
       print("Zero Not Allowed")
except:
    print("May be U need to Learn")
finally:
    print("great job we are improving...")
