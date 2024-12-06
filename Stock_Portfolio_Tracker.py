import random  # For simulating stock prices (replace with an API call)

# Simulated function to fetch stock price (replace with a real API function)
def get_stock_price(stock_symbol):
    # Simulate a random stock price
    return round(random.uniform(100, 500), 2)

# Main Portfolio Tracker class
class StockPortfolio:
    def _init_(self):  # Fixed constructor
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to your portfolio.")

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol} from your portfolio.")
            else:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol}.")
        else:
            print(f"Stock {symbol} not found in your portfolio.")

    def view_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\nYour Portfolio:")
        print(f"{'Symbol':<10} {'Shares':<10} {'Price ($)':<10} {'Value ($)':<10}")
        total_value = 0
        for symbol, shares in self.portfolio.items():
            price = get_stock_price(symbol)
            value = price * shares
            total_value += value
            print(f"{symbol:<10} {shares:<10} {price:<10.2f} {value:<10.2f}")
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

    def track_performance(self):
        print("\nReal-Time Stock Prices:")
        print(f"{'Symbol':<10} {'Price ($)':<10}")
        for symbol in self.portfolio.keys():
            price = get_stock_price(symbol)
            print(f"{symbol:<10} {price:<10.2f}")

# Main Program
def main():
    print("Welcome to the Stock Portfolio Tracker!")
    portfolio = StockPortfolio()

    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Performance")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            symbol = input("Enter stock symbol: ").strip().upper()
            shares = int(input("Enter number of shares: ").strip())
            portfolio.add_stock(symbol, shares)

        elif choice == "2":
            symbol = input("Enter stock symbol: ").strip().upper()
            shares = int(input("Enter number of shares to remove: ").strip())
            portfolio.remove_stock(symbol, shares)

        elif choice == "3":
            portfolio.view_portfolio()

        elif choice == "4":
            portfolio.track_performance()

        elif choice == "5":
            print("Goodbye! Happy investing!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()