"""
Utility calculator module for prorating light and gas utility bills.

This module contains the core functions for calculating prorated utility charges
based on guest stay periods and utility invoices.
"""

from datetime import date

def get_ordinal_suffix(number):
    """Converts a number to its ordinal form (e.g., 1 -> 1st, 2 -> 2nd)."""
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return f"{number}{suffix}"

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
        
        # Calculate total days in the invoice period
        invoice_total_days = (inv_end - inv_start).days
        if is_inclusive:
            invoice_total_days += 1
        
        daily_cost = inv['amount'] / invoice_total_days
        
        overlap_start = max(stay_start, inv_start)
        overlap_end = min(stay_end, inv_end)
        
        # Check if there's an overlap
        if overlap_start <= overlap_end:
            # Calculate overlapping days
            overlapping_days = (overlap_end - overlap_start).days
            if is_inclusive:
                overlapping_days += 1

            charge_for_this_invoice = daily_cost * overlapping_days
            total_charge += charge_for_this_invoice
            
            # Get the ordinal number (e.g., "1st", "2nd")
            ordinal_num = get_ordinal_suffix(i + 1) 
            
            # Print the detailed, labeled line
            print(f"  {ordinal_num} {utility_name} Invoice [{inv_start} to {inv_end}]:")
            print(f"    - Overlapped for {overlapping_days} days.")
            print(f"    - Prorated charge: ${charge_for_this_invoice:,.2f}")
            
    return total_charge
