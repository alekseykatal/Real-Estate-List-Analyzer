# reads the file and returns the data as a list
def getDataInput(filename):
    records = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    # skips the first line and removes extra spaces
    for line in lines[1:]:
        records.append(line.strip())

    return records


# calculates and returns the median
def getMedian(values):
    sorted_values = sorted(values)
    count = len(sorted_values)

    if count % 2 != 0:
        median = sorted_values[count // 2]
    else:
        mid_index = count // 2
        median = (sorted_values[mid_index - 1] + sorted_values[mid_index]) / 2

    return median


# the main function that calculates the rest of the values and displays everything
def main():
    filename = 'RealEstateData.csv'
    records = getDataInput(filename)

    # create lists and dictionaries to store the data
    property_prices = []
    city_summary = {}
    zip_summary = {}
    property_type_summary = {}

    # calculates and updates all the values
    for record in records:

        # divides the data when it sees the ','
        field = record.split(',')

        city = field[1]
        property_type = field[7]
        price = float(field[8])
        zipcode = field[2]

        # price gets added to list
        property_prices.append(price)

        # totals up the price for city
        if city in city_summary:
            city_summary[city] += price
        else:
            city_summary[city] = price

        # totals up price for zip
        if zipcode in zip_summary:
            zip_summary[zipcode] += price
        else:
            zip_summary[zipcode] = price

        # totals up the price for the property type
        if property_type in property_type_summary:
            property_type_summary[property_type] += price
        else:
            property_type_summary[property_type] = price

        # sorts the property prices list
        property_prices.sort()

    # calculate all the summaries
    min_price = min(property_prices)
    max_price = max(property_prices)
    total_price = sum(property_prices)
    average_price = total_price / len(property_prices)
    median_price = getMedian(property_prices)

    # prints out all the summaries
    print(f"Minimum{'':<8} {min_price:>20,.2f}")
    print(f"Maximum{'':<8} {max_price:>20,.2f}")
    print(f"Sum{'':<12} {total_price:>20,.2f}")
    print(f"Avg{'':<12} {average_price:>20,.2f}")
    print(f"Median{'':<9} {median_price:>20,.2f}")

    # prints the property type summaries
    print("\nSummary by Property Type:")
    for property_type, total in property_type_summary.items():
        print(f"{property_type:<15} {total:>20,.2f}")

    # prints the city summaries
    print("\nSummary by City:")
    for city in city_summary:
        print(f"{city:<15} {city_summary[city]:>20,.2f}")

    print("\nSummary by ZIP Code: ")
    for zipcode, total in zip_summary.items():
        print(f"{zipcode:<10} {total:>20,.2f}")


# calls the main function to run
main()
