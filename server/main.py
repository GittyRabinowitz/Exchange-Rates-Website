import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configure CORS settings
origins = [
    "http://localhost",
    "http://localhost:5173",  # Your React app's development server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Load the API key from environment variable
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
if not API_KEY:
    raise Exception("Please set the EXCHANGE_RATE_API_KEY environment variable")

BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"


# Fake data for available currencies
available_currencies = ["USD", "EUR", "GBP", "CNY", "ILS"]


# This endpoint is called when a request is made to the route '/api/available-currencies'
# It returns the available currencies      
@app.get("/api/available-currencies")
def get_available_currencies():
    return {"currencies": available_currencies}


# This endpoint is called when a request is made to the route '/api/exchange-rates/{base_currency}'
# It makes a request to the exchangerate-api and returns the exchange rate of the specific currency to the available currencies  
@app.get("/api/exchange-rates/{base_currency}")
async def get_exchange_rates(base_currency: str):
    if base_currency not in available_currencies:
        raise HTTPException(status_code=404, detail="Base currency not found")
    try:
        response = requests.get(f"{BASE_URL}{base_currency}")
        data = response.json()

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=data.get("error", "Error fetching exchange rates"))

        # Extract relevant exchange rates
        rates = {currency: data["conversion_rates"].get(currency, None) for currency in available_currencies if currency != base_currency}

        return {"base_currency": base_currency, "rates": rates}

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


# #This endpoint is called when a request is made to the route '/api/available-currencies'
# It makes a request to the exchangerate-api and returns all the available currencies
# @app.get("/api/available-currencies")
# async def get_available_currencies():
#     try:
#         response = requests.get(BASE_URL + "USD")  # Fetch using a default base currency like USD
#         data = response.json()
        
#         if response.status_code != 200:
#             raise HTTPException(status_code=response.status_code, detail=data.get("error", "Error fetching currencies"))


#         available_currencies = list(data["conversion_rates"].keys())
#         return {"currencies": available_currencies}

#     except requests.RequestException as e:
#         raise HTTPException(status_code=500, detail=str(e))
