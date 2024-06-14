# How to Run This Project

This project requires Python and several Python packages to be installed. Follow the steps below to set up and run the project:

## Prerequisites

- Python 3.x should be installed on your system. If not, download and install it from the [official Python website](https://www.python.org/downloads/).
- Node.js and npm should be installed. If not, download and install them from the [official Node.js website](https://nodejs.org/).

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/GittyRabinowitz/Exchange-Rates-Website.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Exchange-Rates-Website
    ```

3. Navigate to the server directory:

    ```bash
    cd server
    ```

4. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    ```

5. Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

6. Set the environment variables (replace with your actual API key):

    ```bash
    export EXCHANGE_RATE_API_KEY="a1304752dc74c2929fd62678"
    ```

    - On Windows PowerShell:

      ```powershell
      $env:EXCHANGE_RATE_API_KEY="a1304752dc74c2929fd62678"
      ```

7. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

8. Navigate to the client directory:

    ```bash
    cd ../client
    ```

9. Install the required packages:

    ```bash
    npm install
    ```

## Running the Project

1. Start the FastAPI server:

    ```bash
    cd server
    uvicorn main:app --reload
    ```

    Once the server is running, you can access the FastAPI endpoints in your web browser or using tools like cURL or Postman.

2. Start the client app:

    ```bash
    cd ../client
    npm run dev
    ```

## Additional Notes

- **Configuration**: You can modify the environment variables in the `server` directory's `.env` file to change the API key and other settings.
- **Further Information**: For more detailed information on customization, testing, deployment, and documentation, please refer to the `README.md` file.
