import csv


STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310,
    "NFLX": 600,
    "META": 320,
}


def show_available_stocks():
    """Display the list of available stocks and their prices."""
    print("\nAvailable stocks and prices (per share):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")


def get_portfolio():
    """Collect stock names and quantities from the user."""
    portfolio = {}

    print("\nEnter stock symbol and quantity. Type 'done' when finished.")
    while True:
        symbol = input("\nStock symbol (or 'done'): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' not found in price list. Please choose from the available stocks.")
            continue

        qty_input = input(f"Quantity of {symbol}: ").strip()

        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("Please enter a valid positive whole number for quantity.")
            continue

        quantity = int(qty_input)

        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity

    return portfolio


def calculate_total(portfolio):
    """Calculate total investment value and per-stock breakdown."""
    breakdown = []
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        breakdown.append((symbol, quantity, price, value))

    return breakdown, total


def display_summary(breakdown, total):
    """Print a formatted summary of the portfolio."""
    print("\n" + "=" * 50)
    print("PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Symbol':<10}{'Quantity':<12}{'Price':<10}{'Value':<10}")
    print("-" * 50)

    for symbol, quantity, price, value in breakdown:
        print(f"{symbol:<10}{quantity:<12}${price:<9}${value:<9}")

    print("-" * 50)
    print(f"TOTAL INVESTMENT VALUE: ${total}")
    print("=" * 50)


def save_to_txt(breakdown, total, filename="portfolio_summary.txt"):
    """Save the portfolio summary to a .txt file."""
    with open(filename, "w") as f:
        f.write("PORTFOLIO SUMMARY\n")
        f.write("=" * 50 + "\n")
        f.write(f"{'Symbol':<10}{'Quantity':<12}{'Price':<10}{'Value':<10}\n")
        f.write("-" * 50 + "\n")
        for symbol, quantity, price, value in breakdown:
            f.write(f"{symbol:<10}{quantity:<12}${price:<9}${value:<9}\n")
        f.write("-" * 50 + "\n")
        f.write(f"TOTAL INVESTMENT VALUE: ${total}\n")
    print(f"Summary saved to {filename}")


def save_to_csv(breakdown, total, filename="portfolio_summary.csv"):
    """Save the portfolio summary to a .csv file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Value"])
        for symbol, quantity, price, value in breakdown:
            writer.writerow([symbol, quantity, price, value])
        writer.writerow([])
        writer.writerow(["Total Investment Value", "", "", total])
    print(f"Summary saved to {filename}")


def main():
    print("=" * 50)
    print("Welcome to the Stock Portfolio Tracker")
    print("=" * 50)

    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    breakdown, total = calculate_total(portfolio)
    display_summary(breakdown, total)

    save_choice = input("\nSave summary to a file? (y/n): ").lower().strip()
    if save_choice == "y":
        file_type = input("Save as .txt or .csv? ").lower().strip()
        if file_type == "csv":
            save_to_csv(breakdown, total)
        else:
            save_to_txt(breakdown, total)
    else:
        print("Summary not saved.")

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()