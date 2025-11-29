# Week 1 - Activity 2: Gross Pay (with NZ Income Tax)

# This program:
# Asks the user for their hourly pay rate and hours worked per week.
# Calculates the gross annual income.
# Calculates income tax using New Zealand individual tax brackets
# Shows gross and net income (annual and weekly).

#Creating a function
def calculate_tax(annual_income: float) -> float:
    #Calculate income tax for a given annual income using 
    #NZ progressive tax brackets (2024–2025).
    #annual_income: total yearly income before tax (float)
    #Returns: total tax to pay (float)
    
    tax = 0.0 # float to store total tax
    remaining = annual_income

    # Tax brackets (1 Apr 2024 – 31 Mar 2025)
    # 0 - 14,000           -> 10.5%
    # 14,001 - 15,600      -> 12.82%
    # 15,601 - 48,000      -> 17.5%
    # 48,001 - 53,500      -> 21.64%
    # 53,501 - 70,000      -> 30%
    # 70,001 - 78,100      -> 30.99%
    # 78,101 - 180,000     -> 33%
    # 180,001 and over     -> 39%

    # For each band we take only the portion of income in that band.

    # 0 - 14,000 @ 10.5%
    if remaining > 14_000:
        tax += 14_000 * 0.105
        remaining -= 14_000
    else:
        tax += remaining * 0.105
        return tax

    # 14,001 - 15,600 @ 12.82%
    band = 15_600 - 14_000
    if remaining > band:
        tax += band * 0.1282
        remaining -= band
    else:
        tax += remaining * 0.1282
        return tax

    # 15,601 - 48,000 @ 17.5%
    band = 48_000 - 15_600
    if remaining > band:
        tax += band * 0.175
        remaining -= band
    else:
        tax += remaining * 0.175
        return tax

    # 48,001 - 53,500 @ 21.64%
    band = 53_500 - 48_000
    if remaining > band:
        tax += band * 0.2164
        remaining -= band
    else:
        tax += remaining * 0.2164
        return tax

    # 53,501 - 70,000 @ 30%
    band = 70_000 - 53_500
    if remaining > band:
        tax += band * 0.30
        remaining -= band
    else:
        tax += remaining * 0.30
        return tax

    # 70,001 - 78,100 @ 30.99%
    band = 78_100 - 70_000
    if remaining > band:
        tax += band * 0.3099
        remaining -= band
    else:
        tax += remaining * 0.3099
        return tax

    # 78,101 - 180,000 @ 33%
    band = 180_000 - 78_100
    if remaining > band:
        tax += band * 0.33
        remaining -= band
    else:
        tax += remaining * 0.33
        return tax

    # 180,001 and over @ 39%
    tax += remaining * 0.39
    return tax


def main():
    print("=== Week 1 - Activity 2: Gross Pay Calculator (NZ Tax) ===\n")

    # Get user inputs as strings from the keyboard (input always returns a string)
    hourly_rate_input = input("Enter your hourly pay rate in NZD (for example 28.5): ")
    hours_per_week_input = input("Enter hours worked per week (for example 37.5): ")

    # Convert to float so we can do decimal calculations
    hourly_rate = float(hourly_rate_input)     # float = number with decimals
    hours_per_week = float(hours_per_week_input)

    # Calculate gross income
    weekly_gross = hourly_rate * hours_per_week     # weekly gross pay
    annual_gross = weekly_gross * 52                # assume 52 working weeks

    # Use our function to compute the yearly tax
    annual_tax = calculate_tax(annual_gross)

    # Net income is gross minus tax
    annual_net = annual_gross - annual_tax
    weekly_net = annual_net / 52

    print("\n--- Results ---")
    print(f"Weekly gross income:           ${weekly_gross:,.2f}")
    print(f"Estimated annual gross income: ${annual_gross:,.2f}")
    print(f"Estimated annual tax:          ${annual_tax:,.2f}")
    print(f"Estimated annual net income:   ${annual_net:,.2f}")
    print(f"Estimated weekly net income:   ${weekly_net:,.2f}")


# This line makes sure main() only runs when we run this file directly
if __name__ == "__main__":
    main()
