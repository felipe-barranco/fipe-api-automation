# FIPE Vehicle Lookup

A Python command-line application for looking up vehicle information and reference prices through the FIPE API.

The application guides the user through the selection of a vehicle type, brand, model, and model year. It then displays the information returned by the API for the selected vehicle.

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

- **Python 3.12+** — application language.
- **Requests** — sends HTTP requests to the FIPE API.
- **FIPE API** — provides the vehicle data used by the application.

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

Brand:       Honda
Model:       Civic Sedan EXL 2.0 Flex 16V Aut.4p
Year:        2020
Fuel:        Flex
Fuel Type:   F

FIPE Code:   014090-2

----------------------------------------
FIPE PRICE:  R$ 119.329,00
========================================
```

The example illustrates the application output format and uses vehicle data from a response shown in the [FIPE API documentation](https://fipe.api.br/docs/comece-aqui). The FIPE price may change according to the reference month returned by the API.

## Exiting the Application

- Select **2** in the main menu to exit normally.
- While the application is waiting for input, you can send an end-of-file signal to close it. On **Windows**, press `Ctrl+Z` and then `Enter`; on **macOS/Linux**, press `Ctrl+D`. The application handles this input interruption and displays an exit message.
- `Ctrl+C` is not currently handled explicitly by the application; it triggers Python's standard `KeyboardInterrupt`.

## API Integration

The application sends HTTP GET requests to the following API base URL:

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

The supported `vehicle_type` values are:

- `cars`
- `motorcycles`
- `trucks`

The `get_data()` function centralizes HTTP GET requests, applies a 10-second timeout, checks the response status through `validate_response()`, and returns the response body as JSON.

If a request fails, `main.py` catches the Requests exception and displays an error message to the user.

## Future Improvements

- Add automated tests for the API functions using **pytest**.
- Mock HTTP responses to test successful requests and error scenarios without depending on live API calls.
- Allow users to return to previous selection steps.
- Improve handling of unexpected or invalid API response data.

---

This project is a practical exercise in Python, command-line application development, HTTP requests, and API integration.
