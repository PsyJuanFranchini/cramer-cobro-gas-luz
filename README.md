# Utility Bill Prorator

## About This Project

This project provides a set of Python scripts to accurately calculate the prorated cost of utility bills (light and gas) for a guest's specific stay. It is designed to handle the complex and distinct billing rules for different utility companies, ensuring a fair and precise final bill.

## Key Logic

The core logic of this calculator revolves around how the `end_date` on an invoice is interpreted:

-   **Gas (Inclusive):** The end date is the last full day of service.
-   **Light (Exclusive):** The end date is the boundary of the service period, and the last day of service is the day *before* the end date.

## File Structure

-   `main.py`: The primary script to run. It contains the guest's stay information, the invoice data, and calls the calculation functions.
-   `utility_calculator.py`: A module that contains all the reusable logic, including the main `prorate_charges` function.

## How to Use

1.  Open the `main.py` file.
2.  Update the `stay_start_guest` and `stay_end_guest` variables with the correct dates.
3.  Populate the `light_invoices` and `gas_invoices` lists with the latest billing information.
4.  Run the script from your terminal:
    ```bash
    python main.py
    ```
5.  The script will print a detailed breakdown and the final grand total owed.