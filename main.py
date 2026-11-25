import sys
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
                    break
                elif user_option == 2:
                    sys.exit("Thank you for using FIPE Vehicle Lookup. Goodbye!")
            else:
                print("Invalid option. Please select a valid option.")


def search_vehicle():
    vehicle_type = select_type()
    brand_id = select_brand(vehicle_type)
    model_id = select_model(vehicle_type, brand_id)
    year_id = select_year(vehicle_type, brand_id, model_id)
    select_vehicle(vehicle_type, brand_id, model_id, year_id)


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
        try:
            user_type = int(input("\nSelect a type: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError:
            sys.exit("Input interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            if user_type in [1, 2, 3]:
                if user_type == 1:
                    return "cars"
                elif user_type == 2:
                    return "motorcycles"
                elif user_type == 3:
                    return "trucks"
            else:
                print("Invalid option. Please select a valid vehicle type.")


def select_brand(vehicle_type):    
    brands_data = get_brands(vehicle_type)

    print("""
========================================
            VEHICLE SEARCH
========================================

Select a vehicle brand:
    """)

    for i in range(len(brands_data)):
        print(f"{i + 1}. {brands_data[i]["name"]}")

    while True:
        try:
            user_brand = int(input("\nSelect a brand: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError:
            sys.exit("Input interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            if 1 <= user_brand <= len(brands_data):
                print(f"\nYou selected: {brands_data[user_brand - 1]['name']}")
                return brands_data[user_brand - 1]['code']
            else:
                print("Invalid option. Please select a valid vehicle brand.")


def select_model(vehicle_type, brand_id):
    models_data = get_models(vehicle_type, brand_id)

    print("""
========================================
            VEHICLE SEARCH
========================================
        
Select a vehicle model:
    """)
         
    for i in range(len(models_data)):
        print(f"{i + 1}. {models_data[i]['name']}")

    while True:
        try:
            user_model = int(input("\nSelect a model: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError:
            sys.exit("Input interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            if 1 <= user_model <= len(models_data):
                print(f"\nYou selected: {models_data[user_model - 1]['name']}")
                return models_data[user_model - 1]['code']
            else: 
                print("Invalid option. Please select a valid vehicle model.")


def select_year(vehicle_type, brand_id, model_id):
    years_data = get_years(vehicle_type, brand_id, model_id)

    print("""
========================================
            VEHICLE SEARCH
========================================
        
Select a vehicle year:
""")
          
    for i in range(len(years_data)):
        print(f"{i + 1}. {years_data[i]['name']}")

    while True:
        try:
            user_year = int(input("\nSelect a year: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError:
            sys.exit("Input interrupted. Exiting FIPE Vehicle Lookup.")
        else:
            if 1 <= user_year <= len(years_data):
                print(f"\nYou selected: {years_data[user_year - 1]['name']}")
                return years_data[user_year - 1]['code']
            else:
                print("Invalid option. Please select a valid vehicle year.")


def select_vehicle(vehicle_type, brand_id, model_id, year_id):
    info_data = get_info(vehicle_type, brand_id, model_id, year_id)
    
    print(f"""
========================================
          FIPE VEHICLE LOOKUP
========================================

Vehicle information:

Brand:       {info_data['brand']}
Model:       {info_data['model']}
Year:        {info_data['modelYear']}
Fuel:        {info_data['fuel']}
Fuel Type:   {info_data['fuelAcronym']}

FIPE Code:   {info_data['codeFipe']}

----------------------------------------
FIPE PRICE:  {info_data['price']}
========================================""")


if __name__ == "__main__":
    main()