import sys
from fipe_api import get_brands

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
                sys.exit("\nInput interrupted. Exiting FIPE Vehicle Lookup.")
            else:
                if user_input in [1, 2]:
                    return user_input
    return user_input


def search_vehicle():
    vehicle_type = select_type()
    vehicle_brand = select_brand(vehicle_type)
    #vehicle_model = select_model(vehicle_brand)


def select_type():
    while True:
        print("""
        ========================================
        VEHICLE SEARCH
        ========================================
        
        Select a vehicle type:
        
        1. Cars
        2. Motorcycles
        3. Trucks
            """)
        try:
            user_type = int(input("Select a vehicle type: "))
        except ValueError:
            print("\nInvalid option. Please select a valid brand.")
        except EOFError:
            sys.exit("\nInput interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            if user_type in [1, 2, 3]:
                if user_type == 1:
                    return "cars"
                elif user_type == 2:
                    return "motorcycles"
                elif user_type == 3:
                    return "trucks"


def select_brand(type):
    print("""
========================================
VEHICLE SEARCH
========================================

Select a vehicle brand:
""")
    
    brands_data = get_brands(type)
    
    brands = []
    for i in range(len(brands_data)):
        brands.append(brands_data[i]['name'])

    while True:
        try:
            for i in range(len(brands)):
                    print(f"{i + 1}. {brands[i]}")
            user_brand = int(input("\nSelect a brand: "))
        except ValueError:
            print("Invalid option. Please select a valid brand.")
        except EOFError:
            sys.exit("\nInput interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            if 1 <= user_brand <= len(brands):
                print(f"\nYou selected: {brands[user_brand - 1]}")
                return brands[user_brand - 1]
            else: 
                print("\nInvalid option. Please select a valid brand.")


def select_model(brand):
    ...

if __name__ == "__main__":
    main()