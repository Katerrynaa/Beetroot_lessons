
#task1
def oops():
 try:
    oops()
 except IndexError("IndexError occurred"):
  oops() 


def calls_oops():
    try:
       oops()
    except IndexError: 
       pass
    except KeyError:
       print("KeyError")
    

    calls_oops()


#task2
def numbers():
   try:
      a = int(input("Enter number a: "))
      b = int(input("Enter number b: "))

      result = (a ** 2) / b
      print(result)

   except ZeroDivisionError:
      print("Error. Division by zero is not allowed")
   except ValueError:
      print("Error.Value not available")
   finally:
      print("This is finally block")

numbers()
    

    
      

  


