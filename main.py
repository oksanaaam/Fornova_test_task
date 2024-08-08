import json


def load_json(file_path: str) -> dict:
    """
    Loads a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Content of the JSON file as a dictionary.
    """
    with open(file_path, "r") as file:
        return json.load(file)


def find_lowest_price(shown_prices: dict) -> tuple:
    """
    Finds the lowest price and the corresponding room type.

    Args:
        shown_prices (dict): Dictionary with room types and their prices.

    Returns:
        tuple: Lowest price and corresponding room type.
    """
    lowest_price = float("inf")
    lowest_price_room_type = None

    for room_type, price in shown_prices.items():
        price = float(price)
        if price < lowest_price:
            lowest_price = price
            lowest_price_room_type = room_type

    return lowest_price, lowest_price_room_type


def calculate_total_price(net_prices: dict, taxes: dict) -> dict:
    """
    Calculates the total price for all rooms including taxes.

    Args:
        net_prices (dict): Dictionary with room types and their net prices.
        taxes (dict): Dictionary with tax values.

    Returns:
        dict: Dictionary with room types and their total prices (net price + taxes).
    """
    total_prices = {}

    for room_type, net_price in net_prices.items():
        net_price = float(net_price)
        total_price = net_price + sum(float(tax) for tax in taxes.values())
        total_prices[room_type] = total_price

    return total_prices


def save_output_to_file(output: dict, file_path: str) -> None:
    """
    Saves the results to a JSON file.

    Args:
        output (dict): Dictionary with results.
        file_path (str): Path to the output file.
    """
    with open(file_path, "w") as file:
        json.dump(output, file, indent=4)


def main() -> None:
    # Path to the data file
    input_file_path = "Python-task.json"
    output_file_path = "output.json"

    # Load data
    data = load_json(input_file_path)
    assignment_results = data["assignment_results"][0]
    shown_prices = assignment_results["shown_price"]
    net_prices = assignment_results["net_price"]
    taxes = json.loads(assignment_results["ext_data"]["taxes"])
    number_of_guests = assignment_results["number_of_guests"]

    # Find the lowest price and the corresponding room type
    lowest_price, lowest_price_room_type = find_lowest_price(shown_prices)

    # Calculate the total price for each room type
    total_prices = calculate_total_price(net_prices, taxes)

    # Print total prices along with room types
    for room_type, total_price in total_prices.items():
        print(f"Room Type: {room_type}, Total Price: {total_price}")

    # Prepare output data
    output = {
        "lowest_price": lowest_price,
        "lowest_price_room_type": lowest_price_room_type,
        "lowest_price_room_number_of_guests": number_of_guests,
        "total_prices": total_prices,
    }

    # Save results to file
    save_output_to_file(output, output_file_path)

    print("Results saved to 'output.json'")


if __name__ == "__main__":
    main()
