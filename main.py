import sys
import requests
from fipe_api import get_brand

def main():
    user_option = int(input("""
========================================
FIPE VEHICLE LOOKUP
========================================
        
Welcome to FIPE Vehicle Lookup!
        
1. Search for a vehicle
2. Exit
        
Select an option: """
    ))

    if get_valid_option(user_option) == 1:
        search_vehicle()
    else:
        sys.exit("\nThank you for using FIPE Vehicle Lookup. Goodbye!")


def get_valid_option(user_input):
    if user_input not in [1, 2]:
        print("\nInvalid option. Please select a valid option to continue.")
    
        while True:
            try:
                user_input = int(input("""
========================================
FIPE VEHICLE LOOKUP
========================================
        
Welcome to FIPE Vehicle Lookup!
        
1. Search for a vehicle
2. Exit
        
Select an option: """
            ))
            except ValueError:
                print("\nInvalid option. Please select a valid option to continue.")
            except EOFError:
                print("\nInput interrupted. Exiting FIPE Vehicle Lookup.")
            else:
                if user_input in [1, 2]:
                    return user_input
    return user_input


def search_vehicle():



if __name__ == "__main__":
    main()