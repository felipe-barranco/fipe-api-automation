import sys
import requests
from fipe_api import get_brands, get_models, get_years, get_info


def main():
    print("""
    ========================================
              FIPE VEHICLE LOOKUP
    ========================================
                    
    Welcome to FIPE Vehicle Lookup!
                    
    1. Search for a vehicle
    2. Exit""")
    
    while True:
        try:
            user_option = int(input("\nSelect an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError:
            sys.exit("Input interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            if user_option in [1, 2]:
                if user_option == 1:
                    search_vehicle()
                elif user_option == 2:
                    print("Thank you for using FIPE Vehicle Lookup. Goodbye!")
                    return
            else:
                print("Invalid option. Please select a valid option.")


def search_vehicle():
    vehicle_type = select_type()

    brand_id = select_brand(vehicle_type)
    if brand_id is None:
        return

    model_id = select_model(vehicle_type, brand_id)
    if model_id is None:
        return

    year_id = select_year(vehicle_type, brand_id, model_id)
    if year_id is None:
        return

    select_vehicle(vehicle_type, brand_id, model_id, year_id)


def get_user_input(info):
    while True:
        try:
            user_input = int(input(f"\nSelect a {info}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError:
            sys.exit("Input interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            return user_input


def select_type():
    print("""
========================================
            VEHICLE SEARCH
========================================
        
Select a vehicle type:
        
1. Cars
2. Motorcycles
3. Trucks""")

    while True:
        user_input = get_user_input("type")

        if user_input in [1, 2, 3]:
            if user_input == 1:
                print("\nYou selected: Cars")
                return "cars"
            elif user_input == 2:
                print("\nYou selected: Motorcycles")
                return "motorcycles"
            elif user_input == 3:
                print("\nYou selected: Trucks")
                return "trucks"
        else:
            print("Invalid option. Please select a valid vehicle type.")


def select_brand(vehicle_type):
    brands_data = get_brands(vehicle_type)
    
    if not brands_data:
        print("No brand found for this type.")
        return

    print("""
========================================
            VEHICLE SEARCH
========================================

Select a vehicle brand:
    """)

    for i in range(len(brands_data)):
        print(f"{i + 1}. {brands_data[i]["name"]}")

    while True:
        user_input = get_user_input("brand")

        if 1 <= user_input <= len(brands_data):
            print(f"\nYou selected: {brands_data[user_input - 1]["name"]}")
            return brands_data[user_input - 1]["code"]
        else:
            print("Invalid option. Please select a valid vehicle brand.")


def select_model(vehicle_type, brand_id):
    models_data = get_models(vehicle_type, brand_id)

    if not models_data:
        print("No model found for this brand.")
        return

    print("""
========================================
            VEHICLE SEARCH
========================================
        
Select a vehicle model:
    """)
         
    for i in range(len(models_data)):
        print(f"{i + 1}. {models_data[i]["name"]}")

    while True:
        user_input = get_user_input("model")

        if 1 <= user_input <= len(models_data):
            print(f"\nYou selected: {models_data[user_input - 1]["name"]}")
            return models_data[user_input - 1]["code"]
        else: 
            print("Invalid option. Please select a valid vehicle model.")


def select_year(vehicle_type, brand_id, model_id):
    years_data = get_years(vehicle_type, brand_id, model_id)

    if not years_data:
        print("No year found for this model.")
        return

    print("""
========================================
            VEHICLE SEARCH
========================================
        
Select a vehicle year:
""")
          
    for i in range(len(years_data)):
        print(f"{i + 1}. {years_data[i]["name"]}")

    while True:
        user_input = get_user_input("year")
        
        if 1 <= user_input <= len(years_data):
            print(f"\nYou selected: {years_data[user_input - 1]["name"]}")
            return years_data[user_input - 1]["code"]
        else:
            print("Invalid option. Please select a valid vehicle year.")


def select_vehicle(vehicle_type, brand_id, model_id, year_id):
    info_data = get_info(vehicle_type, brand_id, model_id, year_id)
    
    print(f"""
========================================
          FIPE VEHICLE LOOKUP
========================================

Vehicle information:

Brand:        {info_data["brand"]}
Model:        {info_data["model"]}
Year:         {info_data["modelYear"]}
Fuel:         {info_data["fuel"]}
Fuel Acronym: {info_data["fuelAcronym"]}

FIPE Code:    {info_data["codeFipe"]}

----------------------------------------
FIPE PRICE:   {info_data["price"]}
========================================""")


if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.RequestException:
        print("\nATTENTION!")
        print("Unable to retrieve vehicle information.")
        print("Please try again later.")