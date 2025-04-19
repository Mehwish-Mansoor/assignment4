def main():
    husband_age : int = 50
    wife_age : int = 10 - husband_age
    daughter2_age : int = 11
    daughter1_age : int = 2 + daughter2_age
    cousin_age : int = daughter1_age + daughter2_age 
    friend_age : int = wife_age
    
    print("Hubby_age is "  +  str (husband_age))
    print("Wife_age is "  +  str (wife_age))
    print("Daughter_2age is "  +  str(daughter2_age))
    print("Daughter1_age is "  +  str(daughter1_age))
    print("Cousin_age is "  +  str(cousin_age))
    print("Friend_age is "  +  str(friend_age))
if __name__ == '__main__':
    main() 