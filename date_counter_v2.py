from datetime import date

def prorate_charges(stay_start, stay_end, invoices, is_inclusive, utility_name):
    """
    Calculates the prorated utility charges for a specific stay period.

    Args:
        stay_start (date): The start date of the stay.
        stay_end (date): The end date of the stay.
        invoices (list): A list of invoice dictionaries. 
                         Each dict needs 'start_date', 'end_date', and 'amount'.

    Returns:
        float: The total prorated charge for the given invoices.
    """
    total_charge = 0.0
    
    # Use the new utility_name parameter in the header
    print(f"\n--- Calculating Charges for {utility_name} ---")
    
    # Use enumerate to get the index 'i' (starting from 0) and the invoice
    for i, inv in enumerate(invoices):
        inv_start = inv['start_date']
        inv_end = inv['end_date']
        
        # ... (all the calculation logic remains exactly the same) ...
        invoice_total_days = (inv_end - inv_start).days
        if is_inclusive:
            invoice_total_days += 1
        
        daily_cost = inv['amount'] / invoice_total_days
        
        overlap_start = max(stay_start, inv_start)
        overlap_end = min(stay_end, inv_end)
        
        if overlap_start <= overlap_end:
            overlapping_days = (inv_end - inv_start).days
            if is_inclusive:
                overlapping_days += 1

            charge_for_this_invoice = daily_cost * overlapping_days
            total_charge += charge_for_this_invoice
            
            # --- THIS IS THE UPDATED PRINT STATEMENT ---
            # Get the ordinal number (e.g., "1st", "2nd")
            ordinal_num = get_ordinal_suffix(i + 1) 
            
            # Print the detailed, labeled line
            print(f"  {ordinal_num} {utility_name} Invoice [{inv_start} to {inv_end}]:")
            print(f"    - Overlapped for {overlapping_days} days.")
            print(f"    - Prorated charge: ${charge_for_this_invoice:,.2f}")
            
    return total_charge

def get_ordinal_suffix(number):
    """Converts a number to its ordinal form (e.g., 1 -> 1st, 2 -> 2nd)."""
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return f"{number}{suffix}"

# --- DATA SETUP ---

# The period the person stayed
person_stay_start = date(2025, 5, 11)
person_stay_end = date(2025, 6, 27)
stay_duration = (person_stay_end - person_stay_start).days + 1

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

print(f"Guest Stay: {person_stay_start} to {person_stay_end} ({stay_duration} days)")

# Calculate the total for each utility
# For light, add utility_name="Light"
total_light_charge = prorate_charges(
    person_stay_start, 
    person_stay_end, 
    light_invoices, 
    is_inclusive=False, 
    utility_name="Light"
)

# For gas, add utility_name="Gas"
total_gas_charge = prorate_charges(
    person_stay_start, 
    person_stay_end, 
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