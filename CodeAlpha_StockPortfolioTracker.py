import csv
from datetime import datetime

def stock_portfolio_tracker():
    """Main function for the stock portfolio tracker"""
    
    # Hardcoded stock prices (in USD)
    stock_prices = {
        "AAPL": 180.50,   # Apple
        "TSLA": 250.75,   # Tesla
        "GOOGL": 145.20,  # Google
        "MSFT": 410.30,   # Microsoft
        "AMZN": 175.40,   # Amazon
        "META": 485.60,   # Meta
        "NVDA": 950.02,   # NVIDIA
        "BRK-B": 405.25   # Berkshire Hathaway
    }
    
    print("📊 STOCK PORTFOLIO TRACKER")
    print("=" * 50)
    
    # Display available stocks
    print("\nAvailable Stocks and Current Prices:")
    print("-" * 40)
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f}")
    
    portfolio = {}
    total_investment = 0
    
    print("\n" + "=" * 50)
    print("ENTER YOUR STOCK HOLDINGS")
    print("=" * 50)
    
    # Get user input for stocks
    while True:
        print("\n--- Add Stock to Portfolio ---")
        
        # Show available stocks
        print("Available stocks:", ", ".join(stock_prices.keys()))
        
        # Get stock symbol
        while True:
            stock_symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
            
            if stock_symbol == 'DONE':
                break
                
            if stock_symbol not in stock_prices:
                print(f"❌ Error: '{stock_symbol}' not found. Please enter a valid stock symbol.")
                print(f"Available: {', '.join(stock_prices.keys())}")
                continue
                
            break
        
        if stock_symbol == 'DONE':
            break
        
        # Get quantity
        while True:
            try:
                quantity = float(input(f"Enter quantity of {stock_symbol} shares: "))
                if quantity <= 0:
                    print("❌ Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
        
        # Calculate value
        current_price = stock_prices[stock_symbol]
        stock_value = current_price * quantity
        
        # Add to portfolio
        portfolio[stock_symbol] = {
            'quantity': quantity,
            'price_per_share': current_price,
            'total_value': stock_value
        }
        
        total_investment += stock_value
        
        print(f"✅ Added {quantity} shares of {stock_symbol} at ${current_price:.2f} each")
        print(f"   Value: ${stock_value:.2f}")
    
    # Display portfolio summary
    print("\n" + "=" * 50)
    print("PORTFOLIO SUMMARY")
    print("=" * 50)
    
    if not portfolio:
        print("No stocks in portfolio.")
        return
    
    print(f"\nTotal Stocks: {len(portfolio)}")
    print(f"Total Investment Value: ${total_investment:.2f}")
    
    print("\n" + "-" * 60)
    print(f"{'Stock':<10} {'Qty':<10} {'Price/Share':<15} {'Total Value':<15}")
    print("-" * 60)
    
    for stock, details in portfolio.items():
        print(f"{stock:<10} {details['quantity']:<10.2f} "
              f"${details['price_per_share']:<14.2f} "
              f"${details['total_value']:<14.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL':<35} ${total_investment:>14.2f}")
    
    # Ask user if they want to save the portfolio
    save_option = input("\nDo you want to save your portfolio? (yes/no): ").lower()
    
    if save_option in ['yes', 'y']:
        save_portfolio(portfolio, total_investment, stock_prices)
    
    print("\nThank you for using Stock Portfolio Tracker!")

def save_portfolio(portfolio, total_investment, stock_prices):
    """Save portfolio to CSV and TXT files"""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save to CSV file
    csv_filename = f"portfolio_{timestamp}.csv"
    
    try:
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            writer.writerow(['Stock Symbol', 'Quantity', 'Price per Share', 'Total Value', 'Timestamp'])
            
            # Write portfolio data
            for stock, details in portfolio.items():
                writer.writerow([
                    stock,
                    details['quantity'],
                    details['price_per_share'],
                    details['total_value'],
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ])
            
            # Write total
            writer.writerow(['TOTAL', '', '', total_investment, ''])
        
        print(f"✅ Portfolio saved to {csv_filename}")
        
        # Also save to TXT file (human readable)
        txt_filename = f"portfolio_summary_{timestamp}.txt"
        
        with open(txt_filename, 'w') as txtfile:
            txtfile.write("STOCK PORTFOLIO SUMMARY\n")
            txtfile.write("=" * 50 + "\n\n")
            txtfile.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            txtfile.write("CURRENT STOCK PRICES:\n")
            txtfile.write("-" * 40 + "\n")
            for stock, price in stock_prices.items():
                txtfile.write(f"{stock}: ${price:.2f}\n")
            
            txtfile.write("\n" + "=" * 50 + "\n\n")
            txtfile.write("YOUR PORTFOLIO:\n")
            txtfile.write("-" * 60 + "\n")
            txtfile.write(f"{'Stock':<10} {'Qty':<10} {'Price/Share':<15} {'Total Value':<15}\n")
            txtfile.write("-" * 60 + "\n")
            
            for stock, details in portfolio.items():
                txtfile.write(f"{stock:<10} {details['quantity']:<10.2f} "
                            f"${details['price_per_share']:<14.2f} "
                            f"${details['total_value']:<14.2f}\n")
            
            txtfile.write("-" * 60 + "\n")
            txtfile.write(f"{'TOTAL':<35} ${total_investment:>14.2f}\n")
            txtfile.write("=" * 50 + "\n")
        
        print(f"✅ Summary saved to {txt_filename}")
        
    except Exception as e:
        print(f"❌ Error saving files: {e}")

def load_and_view_portfolio():
    """Optional: Load and view saved portfolio"""
    
    import os
    
    print("\n📂 LOAD SAVED PORTFOLIO")
    print("=" * 50)
    
    # List CSV files
    csv_files = [f for f in os.listdir() if f.startswith('portfolio_') and f.endswith('.csv')]
    
    if not csv_files:
        print("No saved portfolio files found.")
        return
    
    print("\nAvailable portfolio files:")
    for i, filename in enumerate(csv_files, 1):
        print(f"{i}. {filename}")
    
    try:
        choice = int(input("\nEnter file number to view (or 0 to cancel): "))
        
        if choice == 0:
            return
        
        if 1 <= choice <= len(csv_files):
            filename = csv_files[choice - 1]
            
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                print(f"\nContents of {filename}:")
                print("-" * 80)
                for row in reader:
                    print(', '.join(str(cell) for cell in row))
                print("-" * 80)
        else:
            print("Invalid choice.")
            
    except (ValueError, IndexError):
        print("Invalid input.")

def portfolio_analysis():
    """Additional feature: Basic portfolio analysis"""
    
    print("\n📈 PORTFOLIO ANALYSIS TOOL")
    print("=" * 50)
    
    # Sample analysis with hardcoded data
    sample_portfolio = {
        "AAPL": {"quantity": 10, "price": 180.50},
        "TSLA": {"quantity": 5, "price": 250.75},
        "GOOGL": {"quantity": 8, "price": 145.20}
    }
    
    print("\nSample Portfolio Analysis:")
    print("-" * 40)
    
    total_value = 0
    for stock, details in sample_portfolio.items():
        value = details["quantity"] * details["price"]
        total_value += value
        print(f"{stock}: {details['quantity']} shares × ${details['price']} = ${value:.2f}")
    
    print("-" * 40)
    print(f"Total Portfolio Value: ${total_value:.2f}")
    
    # Calculate percentages
    print("\nPortfolio Allocation:")
    for stock, details in sample_portfolio.items():
        value = details["quantity"] * details["price"]
        percentage = (value / total_value) * 100
        print(f"{stock}: {percentage:.1f}%")

def main_menu():
    """Main menu for the stock tracker"""
    
    while True:
        print("\n" + "=" * 50)
        print("MAIN MENU - STOCK PORTFOLIO TRACKER")
        print("=" * 50)
        print("1. Create New Portfolio")
        print("2. View Saved Portfolios")
        print("3. Portfolio Analysis (Sample)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            stock_portfolio_tracker()
        elif choice == '2':
            load_and_view_portfolio()
        elif choice == '3':
            portfolio_analysis()
        elif choice == '4':
            print("\nThank you for using Stock Portfolio Tracker!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main_menu()
