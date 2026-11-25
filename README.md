# FIPE Vehicle Lookup

A Python command-line application for looking up Brazilian vehicle reference prices from the FIPE Table.

The application guides the user through the selection of a vehicle type, brand, model, and model year, then displays the vehicle details and FIPE price returned by the API.

## What Is the FIPE Table?

The **FIPE Table** (*Tabela FIPE*) is published monthly by the **Fundação Instituto de Pesquisas Econômicas (FIPE)**, a Brazilian research foundation linked to the University of São Paulo (USP). It reports the average prices of new and used vehicles in the Brazilian national market, based on prices observed across the country.

In Brazil, the FIPE Table is widely used as a reference for:

- Buying and selling used vehicles.
- Setting the insured value of a vehicle in auto insurance policies.
- Calculating vehicle taxes (IPVA) in several states.
- Evaluating vehicles for financing and trade-ins.

The FIPE price is an **average reference value**, not a fixed or official sale price. The actual price of a specific vehicle can vary according to its condition, mileage, location, and accessories. Because the table is updated every month, the prices returned by this application reflect the latest reference month provided by the API. All prices are in Brazilian reais (R$).

## Features

- Search for cars, motorcycles, and trucks.
- Retrieve available brands according to the selected vehicle type.
- Retrieve models according to the selected brand.
- Retrieve model years according to the selected model.
- Display the selected vehicle's brand, model, model year, fuel, fuel acronym, FIPE code, and price.
- Validate numeric menu input and selection ranges.
- Handle empty brand, model, or year results with user-facing messages.
- Use a 10-second timeout for HTTP requests and check HTTP response status codes.
- Display an error message when an HTTP request fails.

## Technologies

- **Python 3.12+**: application language.
- **Requests**: sends HTTP requests to the FIPE API.
- **FIPE API (Parallelum)**: provides the vehicle data used by the application.

## Project Structure

```text
fipe-vehicle-lookup/
├── .gitignore          # Files and directories excluded from Git
├── fipe_api.py         # Functions responsible for communicating with the FIPE API
├── main.py             # Command-line interface and vehicle search flow
├── README.md           # Project documentation
└── requirements.txt    # Pinned Python dependencies
```

## Requirements

Before running the application, make sure you have:

- **Python 3.12 or newer** installed.
- **Git** installed to clone the repository.
- An active internet connection to access the FIPE API.

Check your Python version with:

```bash
python --version
```

> **Note:** On many macOS and Linux systems, the Python 3 command is `python3` instead of `python`. If `python --version` fails or shows Python 2, use `python3` in all commands below.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/felipe-barranco/fipe-vehicle-lookup.git
   ```

2. Navigate to the cloned repository:

   ```bash
   cd fipe-vehicle-lookup
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment.

   **Windows PowerShell:**

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   **Windows Git Bash:**

   ```bash
   source .venv/Scripts/activate
   ```

   **macOS / Linux:**

   ```bash
   source .venv/bin/activate
   ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

With the virtual environment activated, run:

```bash
python main.py
```

The application displays this main menu:

```text
========================================
          FIPE VEHICLE LOOKUP
========================================

Welcome to FIPE Vehicle Lookup!

1. Search for a vehicle
2. Exit
```

Select **1** to start a vehicle search. The application asks you to select:

1. Vehicle type: cars, motorcycles, or trucks.
2. Brand.
3. Model.
4. Model year.

After the selections, the application displays the vehicle information and FIPE price returned by the API.

Example of the result displayed after a completed search:

```text
========================================
          FIPE VEHICLE LOOKUP
========================================

Vehicle information:

Brand:         Honda
Model:         Civic Sedan EXL 2.0 Flex 16V Aut.4p
Year:          2020
Fuel:          Flex
Fuel Acronym:  F

FIPE Code:     014090-2

----------------------------------------
FIPE PRICE:    R$ 119.329,00
========================================
```

This example illustrates the output format only. The price shown is not current: FIPE prices change every month, so your results will differ.

## Exiting the Application

- Select **2** in the main menu to exit normally.
- While the application is waiting for input, you can send an end-of-file signal to close it. On **Windows**, press `Ctrl+Z` and then `Enter`; on **macOS/Linux**, press `Ctrl+D`. The application handles this input interruption and displays an exit message.
- `Ctrl+C` is not currently handled explicitly by the application; it triggers Python's standard `KeyboardInterrupt`.

## API Integration

The application uses the free FIPE API maintained by Parallelum, which provides FIPE Table data in JSON format. Documentation: <https://deividfortuna.github.io/fipe/v2/>

All requests are HTTP GET requests sent to this base URL:

```text
https://fipe.parallelum.com.br/api/v2
```

The API communication functions are defined in `fipe_api.py`:

| Function | Purpose | Endpoint pattern |
|---|---|---|
| `get_brands(vehicle_type)` | Retrieves the brands available for a vehicle type. | `/{vehicle_type}/brands` |
| `get_models(vehicle_type, brand_id)` | Retrieves the models available for a brand. | `/{vehicle_type}/brands/{brand_id}/models` |
| `get_years(vehicle_type, brand_id, model_id)` | Retrieves the years available for a model. | `/{vehicle_type}/brands/{brand_id}/models/{model_id}/years` |
| `get_info(vehicle_type, brand_id, model_id, year_id)` | Retrieves details and the price for the selected vehicle. | `/{vehicle_type}/brands/{brand_id}/models/{model_id}/years/{year_id}` |

The supported `vehicle_type` values are `cars`, `motorcycles`, and `trucks`.

The `get_data()` function centralizes HTTP GET requests, applies a 10-second timeout, checks the response status through `validate_response()`, and returns the response body as JSON.

If a request fails, `main.py` catches the Requests exception and displays an error message to the user.

### Rate Limits

The API limits the number of requests that can be made without an authentication token. If you run many searches in a short period, requests may start failing, and the application will display an error message. Check the API documentation for the current limits and for how to obtain a token.

## Future Improvements

- Add automated tests for the API functions using **pytest**.
- Mock HTTP responses to test successful requests and error scenarios without depending on live API calls.
- Allow users to return to previous selection steps.
- Handle `Ctrl+C` gracefully with a friendly exit message.
- Support an optional API token to avoid rate limits.
- Improve handling of unexpected or invalid API response data.

## License

<!-- Choose a license (for example, MIT) at https://choosealicense.com, add a LICENSE file to the repository, and update this section. -->

No license has been specified yet.

---

This project is a practical exercise in Python, command-line application development, HTTP requests, and API integration.
