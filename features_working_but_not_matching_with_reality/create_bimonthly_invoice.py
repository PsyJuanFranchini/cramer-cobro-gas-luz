from datetime import date, timedelta

def create_bimonthly_invoice(
    first_payment_amount,
    cycle_start_date,
    total_calendar_days,
    days_in_first_period,
    is_inclusive
):
    """
    Creates a full bimonthly invoice with a consistent calendar period,
    adjusting the total amount based on the inclusivity rule.
    """
    # 1. Calculate the daily rate from the first payment.
    if days_in_first_period == 0:
        return None
    daily_rate = first_payment_amount / days_in_first_period
    print(daily_rate)


    # 2. Calculate the total amount for the full cycle.
    total_amount = daily_rate * total_calendar_days

    # 3. Account for inclusive date range for prorate_charges function.
    if is_inclusive:
        days_to_add = total_calendar_days - 1
    else:
        days_to_add = total_calendar_days
    
    cycle_end_date = cycle_start_date + timedelta(days=days_to_add)


    # 5. Return the complete invoice dictionary.
    return {
        'start_date': cycle_start_date,
        'end_date': cycle_end_date,
        'amount': total_amount
    }

# --- EXAMPLE USAGE ---

# Your known information
payment1_amt = 10731.93
days_in_first = 31
total_days = 63
period_start = date(2025, 3, 20)

# Generate the invoice for Light (Exclusive)
light_invoice = create_bimonthly_invoice(
    payment1_amt,
    period_start,
    total_days,
    days_in_first,
    is_inclusive=False  # This now only affects the final 'amount'
)

print("--- Generated Light Invoice (Exclusive Billing) ---")
print(f"Generated Invoice: {light_invoice}")