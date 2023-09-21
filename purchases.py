#Jake Fernandez
def add_tax(costs, tax_rate):
    return [cost + cost * tax_rate for cost in costs]


def main():
    num_purchases = int(input("Number of purchases: "))
    sales_tax = float(input("Sales tax: "))
    customers = []
    costs = []


    for _ in range(num_purchases):
        customer_name = input("Customer: ")
        cost = float(input("Cost: "))
        customers.append(customer_name)
        costs.append(cost)


    costs_with_tax = add_tax(costs, sales_tax)

    
    total_costs = {}
    for i in range(num_purchases):
        if customers[i] in total_costs:
            total_costs[customers[i]] += costs_with_tax[i]
        else:
            total_costs[customers[i]] = costs_with_tax[i]


    print(total_costs)

main()
