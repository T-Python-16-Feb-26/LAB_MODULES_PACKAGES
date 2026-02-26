# LAB_MODULES_PACKAGES

## Create a new module and name it "dateOP.py" ,  dateOP has the following: -- DONE
#- A function that when called prints the current date.

## Create a new module "main.py" , and do the following: -- DONE
#- import dateOP --DINE
#- call the function that print the current date --DONE

### hint : You should import the date class from the datetime module. --DONE

from datetime import date

def print_current_date ():
    today= date.today()
    print ("Today's date is: ", today)
