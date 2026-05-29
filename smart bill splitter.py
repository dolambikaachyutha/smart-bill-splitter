from colorama import Fore,Style,init
import os
import time
import datetime
init()
def clear_screen():
   os.system("cls")
def welcome():
  print(Fore.CYAN+"="*50+Style.RESET_ALL)
  print( Fore.CYAN+"         Welcome to smart bill splitter!"+Style.RESET_ALL)
  print(Fore.CYAN+"="*50+Style.RESET_ALL)
  time.sleep(1)
  print(Fore.CYAN+"This program helps you to split the bill among your friends in a smart way:")
  time.sleep(1)
  print(Fore.CYAN+"You can split the bill equally or based on the food ordered by each person."+Style.RESET_ALL)
def get_positive_int(prompt):
  while True:
     try:
       value = int(input(prompt))
       if value <= 0:
                print(Fore.RED + "Please enter a number greater than zero.")
       else:
                return value
     except ValueError:
        print(Fore.RED + "Invalid input. Please enter a whole number.")
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print(Fore.RED + "Value cannot be negative.")
            else:
                return value
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")       
def get_menu_choice():
    while True:
        try:
            choice=int(input("Enter your choice(1/2/3/4):"))
            if choice in [1,2,3,4]:
                return choice
            else:
                print(Fore.RED+"Please enter 1,2,3,or 4."+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input.Please enter a number."+Style.RESET_ALL)                     
def equal_split(): 
      no_of_people=get_positive_int("Enter number of people:")   
      total_cost=get_positive_float("Enter total bill cost:")
      tip_percentage=get_positive_float("Enter tip percentage:")
      gst_percentage=get_positive_float("Enter GST percentage:")
      gst_amount=(total_cost*gst_percentage)/100
      tip_amount=(total_cost*tip_percentage)/100
      total_amount=total_cost+tip_amount+gst_amount
      with open("history.txt","a") as f1:
          f1.write("="*50+"\n")
          f1.write("        EQUAL SPLIT\n")
          f1.write("="*50+"\n")
          f1.write("Date: {}.\n".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
          f1.write("Total Bill: {}.\n".format(total_cost))
          f1.write("Tip Percentage: {}%.\n".format(tip_percentage))
          f1.write("GST Percentage: {}%.\n".format(gst_percentage))
          f1.write("Number of people: {}.\n".format(no_of_people))
          f1.write("Total amount after adding gst and tip: {}.\n".format(total_amount))
      amount_per_person=total_amount/no_of_people
      print(Fore.WHITE+"="*50+Style.RESET_ALL)
      print(Fore.YELLOW+"             BILL SUMMARY"+Style.RESET_ALL)
      print(Fore.WHITE+"="*50+Style.RESET_ALL)
      print(Fore.YELLOW+"GENERATING BILL SUMMARY..."+Style.RESET_ALL)
      time.sleep(0.5)
      print(Fore.LIGHTBLUE_EX+"Total bill: {}".format(total_cost)+Style.RESET_ALL)
      time.sleep(0.5)
      print(Fore.LIGHTBLUE_EX+"Tip percentage: {}%".format(tip_percentage)+Style.RESET_ALL)
      time.sleep(0.5)
      print(Fore.LIGHTBLUE_EX+"GST percentage: {}%".format(gst_percentage)+Style.RESET_ALL)
      print(Fore.YELLOW+"CALCULATING TOTAL...."+Style.RESET_ALL)
      time.sleep(1)
      print(Fore.LIGHTBLUE_EX+"Each person should pay: {}".format(round(amount_per_person,2))+Style.RESET_ALL)
      print(Fore.WHITE+"="*50+Style.RESET_ALL)
      print(Fore.GREEN+"         Thank you for using smart bill splitter!"+Style.RESET_ALL)
      print(Fore.WHITE+"="*50+Style.RESET_ALL)
def unequal_split():
   lib={}
   no_of_people=get_positive_int("Enter number of people:")
   for  i in range(no_of_people):
      name=input("Enter name of the person:")
      food_cost=get_positive_float("Enter cost of food ordered by {}:".format(name))
      lib[name]=food_cost
   total_cost=sum(lib.values())
   tip_percentage=get_positive_float("Enter tip percentage:")
   gst_percentage=get_positive_float("Enter GST percentage:")
   gst_amount=(total_cost*gst_percentage)/100
   gst_per_person=gst_amount/no_of_people
   tip_amount=(total_cost*tip_percentage)/100
   tip_amount_per_person=tip_amount/no_of_people
   total=total_cost+tip_amount+gst_amount
   with open("history.txt","a") as f1:
     f1.write("="*50+"\n")
     f1.write("        UNEQUAL SPLIT\n")
     f1.write("="*50+"\n")
     f1.write("Date: {}.\n".format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
     f1.write("Total Bill: {}.\n".format(total_cost))
     f1.write("Tip Percentage: {}%.\n".format(tip_percentage))
     f1.write("GST Percentage: {}%.\n".format(gst_percentage))
     f1.write("Number of people: {}.\n".format(no_of_people))
     f1.write("Total amount after adding tip and GST: {}.\n".format(total))
     for name,food_cost in lib.items():
          total_amount=food_cost+tip_amount_per_person+gst_per_person
          f1.write("{} should pay: {}\n".format(name,round(total_amount,2)))
   tip_amount_per_person=tip_amount/no_of_people
   print(Fore.WHITE+"="*50+Style.RESET_ALL)
   print(Fore.YELLOW+"            BILL SUMMARY"+Style.RESET_ALL)
   print(Fore.WHITE+"="*50+Style.RESET_ALL)
   print(Fore.YELLOW+"GENERATING BILL SUMMARY..."+Style.RESET_ALL)
   time.sleep(0.5)
   print(Fore.LIGHTBLUE_EX+"Total bill: {}".format(total_cost)+Style.RESET_ALL)
   time.sleep(0.5)
   print(Fore.LIGHTBLUE_EX+"Tip percentage: {}%".format(tip_percentage)+Style.RESET_ALL)
   time.sleep(0.5)
   print(Fore.LIGHTBLUE_EX+"GST percentage: {}%".format(gst_percentage)+Style.RESET_ALL)
   print(Fore.YELLOW+"CALCULATING TOTAL AMOUNT..."+Style.RESET_ALL)
   time.sleep(1)
   print(Fore.LIGHTBLUE_EX+"Total amount to be paid: {}".format(total)+Style.RESET_ALL)
   for name,food_cost in lib.items():
        total_amount=food_cost+tip_amount_per_person+gst_per_person
        print("{} should pay: {}".format(name,round(total_amount,2)))   
   print(Fore.WHITE+"="*50+Style.RESET_ALL)
   print(Fore.GREEN+"        Thank you for using smart bill splitter!"+Style.RESET_ALL)
   print(Fore.WHITE+"="*50+Style.RESET_ALL)    
def view_history():
    if os.path.exists("history.txt"):
     with open("history.txt","r") as f1:
      print(Fore.YELLOW+"GENERATING HISTORY..."+Style.RESET_ALL)
      time.sleep(2)
      print("         HISTORY OF BILL SPLITS")
      print(f1.read())
    else:
        print("No history found.") 
def clear_history():
   with open("history.txt","w") as f1:
       f1.write("")
   print(Fore.YELLOW+"CLEARING HISTORY..."+Style.RESET_ALL)
   time.sleep(2)
   print( Fore.GREEN+"History cleared successfully."+Style.RESET_ALL)  
def main():
     print(Fore.MAGENTA+"How do you want to split the bill:"+Style.RESET_ALL)
     time.sleep(1)
     print(Fore.MAGENTA+"1. Equal split"+Style.RESET_ALL)
     time.sleep(1)
     print(Fore.MAGENTA+"2. split by each person's food order or unequal split"+Style.RESET_ALL)
     time.sleep(1)
     print(Fore.MAGENTA+"3. View history of bill splits"+Style.RESET_ALL)
     time.sleep(1)
     print(Fore.MAGENTA+"4. Clear history"+Style.RESET_ALL)
     time.sleep(1)
     choice=get_menu_choice()
     if choice==1:
          equal_split()
     elif choice==2:
         unequal_split()
     elif choice==3:
        view_history()
     elif choice==4:
        clear_history()   
     else:
        print( Fore.RED+"Invalid choice. please enter 1 or 2 or 3 or 4."+Style.RESET_ALL)  
while True:
    clear_screen()
    welcome()
    main()
    again = input("\nDo you want to continue?(yes/no): ")
    if again.lower() != "yes":
        print(Fore.GREEN+"Thank you for using Smart Bill Splitter!"+Style.RESET_ALL)
        break
    clear_screen()