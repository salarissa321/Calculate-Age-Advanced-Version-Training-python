


#----------------------------------------------------
#-------- Calculate Age Advanced Version und Training------------
#-----------------------------------------------------

# Write Note
print("#" * 80) # ################################################################################
print(" You can Write Thr First Letter or Full Name of the Time Unit ".center(80, "#")) # ######### You can Write Thr First Letter or Full Name of the Time Unit #########
print("#" * 80) # ################################################################################


# Collect Age Data

age = input("Please write your Age ? ").strip() # Please write your Age ? 27

 
# Collect Time Units Data

unit = input("Please Choose Time Unit : Months , Weeks , Days ").strip().lower() # Please Choose Time Unit : Months , Weeks , Days


# Get Time Units

months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == "months" or unit == "M":

    print("You Chossed the Unit Months") # You Chossed the Unit Months
    print(f"you Lived for {months:,} months") # you Lived for 324 months

elif unit == "Weeks" or unit == "w":
    print("You Choosed the unit Weeks ") # You Chossed the Unit Weeks
    print(f"you lived for {weeks: ,} Weeks") # you Lived for 1,296 Weeks

elif unit == "Days" or unit == "d" :
    print("You Choosed the unit Days ") # yor Chossed the Unit Days
    print(f"you lived for {days: ,} Days") # you Lived for  9,855 days 



