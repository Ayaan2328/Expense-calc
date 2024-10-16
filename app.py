from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate weekly, monthly, and yearly expenses
def calculate_expenses(km_per_day, mileage, fuel_price):
    fuel_consumed_per_day = km_per_day / mileage
    weekly_fuel_consumption = fuel_consumed_per_day * 7
    monthly_fuel_consumption = fuel_consumed_per_day * 30
    yearly_fuel_consumption = fuel_consumed_per_day * 365

    weekly_expense = weekly_fuel_consumption * fuel_price
    monthly_expense = monthly_fuel_consumption * fuel_price
    yearly_expense = yearly_fuel_consumption * fuel_price

    return weekly_expense, monthly_expense, yearly_expense

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    km_per_day = float(request.form['km_per_day'])
    mileage = float(request.form['mileage'])
    average_fuel_price = 108.00

    weekly_expense, monthly_expense, yearly_expense = calculate_expenses(km_per_day, mileage, average_fuel_price)

    return render_template('result.html', weekly_expense=weekly_expense, 
                           monthly_expense=monthly_expense, yearly_expense=yearly_expense)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
