from datetime import date
from utility_calculator import prorate_charges

def main():
    """
    Main function to set up data, run prorating calculations, and print the summary.
    """
    # --- DATA SETUP ---

    # The period the guest stayed
    guest_stay_start = date(2025, 5, 11)
    guest_stay_end = date(2025, 6, 27)
    stay_duration = (guest_stay_end - guest_stay_start).days + 1

    # List of all light bill invoices
    light_invoices = [
        {'start_date': date(2025, 3, 20), 'end_date': date(2025, 5, 22), 'amount': 22355.9},
        {'start_date': date(2025, 5, 22), 'end_date': date(2025, 7, 22), 'amount': 193879.18},
    ]

    # List of all gas bill invoices
    gas_invoices = [
        {'start_date': date(2025, 4, 11 ), 'end_date': date(2025, 5, 12), 'amount': 3621.23},
        {'start_date': date(2025, 5, 13), 'end_date': date(2025, 6, 11), 'amount': 4284.86},
        {'start_date': date(2025, 6, 12), 'end_date': date(2025, 7, 11), 'amount': 4219.41},
    ]

    # --- CALCULATION & SUMMARY ---

    print(f"Guest Stay: {guest_stay_start} to {guest_stay_end} ({stay_duration} days)")

    # Calculate the total for each utility
    # For light, add utility_name="Light"
    total_light_charge = prorate_charges(
        guest_stay_start, 
        guest_stay_end, 
        light_invoices, 
        is_inclusive=False, 
        utility_name="Light"
    )

    # For gas, add utility_name="Gas"
    total_gas_charge = prorate_charges(
        guest_stay_start, 
        guest_stay_end, 
        gas_invoices, 
        is_inclusive=True, 
        utility_name="Gas"
    )
    grand_total = total_light_charge + total_gas_charge

    # Print the final summary
    print("\n--- Final Summary ---")
    print(f"Total Prorated Light Charge: ${total_light_charge:,.2f}")
    print(f"Total Prorated Gas Charge  : ${total_gas_charge:,.2f}")
    print("-----------------------")
    print(f"GRAND TOTAL OWED           : ${grand_total:,.2f}")

# This block ensures the main function is called only when the script is run directly
if __name__ == "__main__":
    main()
