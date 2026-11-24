import sys
from fipe_api import get_brands, get_models, get_years

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
    vehicleType = select_type()
    brandId = select_brand(vehicleType)
    modelId = select_model(vehicleType, brandId)
    yearId = select_year(vehicleType, brandId, modelId)


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


def select_brand(vehicleType):
    print("""
========================================
VEHICLE SEARCH
========================================

Select a vehicle brand:
""")
    
    brands_data = get_brands(vehicleType)

    while True:
        for i in range(len(brands_data)):
            print(f"{i + 1}. {brands_data[i]["name"]}")

        try:
            user_brand = int(input("\nSelect a brand: "))
        except ValueError:
            print("\nInvalid option. Please select a valid brand.")
        except EOFError:
            sys.exit("\nInput interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            if 1 <= user_brand <= len(brands_data):
                print(f"\nYou selected: {brands_data[user_brand - 1]['name']}")
                return brands_data[user_brand - 1]['code']
            else: 
                print("\nInvalid option. Please select a valid brand.")


def select_model(vehicleType, brandId):
    print("""
========================================
VEHICLE SEARCH
========================================

Select a vehicle model:
    """)

    models_data = get_models(vehicleType, brandId)

    while True:
        for i in range(len(models_data)):
            print(f"{i + 1}. {models_data[i]['name']}")

        try:
            user_model = int(input("\nSelect a model: "))
        except ValueError:
            print("\nInvalid option. Please select a valid brand.")
        except EOFError:
            sys.exit("\nInput interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            if 1 <= user_model <= len(models_data):
                print(f"\nYou selected: {models_data[user_model - 1]['name']}")
                return models_data[user_model - 1]['code']
            else: 
                print("\nInvalid option. Please select a valid brand.")


def select_year(vehicleType, brandId, modelId):
    print("""
========================================
VEHICLE SEARCH
========================================

Select a vehicle year:
    """)
    
    years_data = get_years(vehicleType, brandId, modelId)
    print(years_data)

    while True:
        for i in range(len(years_data)):
            print(f"{i + 1}. {years_data[i]['name']}")

        try:
            user_year = int(input("\nSelect a year: "))
        except ValueError:
            print("\nInvalid option. Please select a valid brand.")
        except EOFError:
            sys.exit("\nInput interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            if 1 <= user_year <= len(years_data):
                print(f"\nYou selected: {years_data[user_year - 1]['name']}")
                return years_data[user_year - 1]['code']
            else:
                print("\nInvalid option. Please select a valid brand.")


if __name__ == "__main__":
    main()