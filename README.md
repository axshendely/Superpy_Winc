# Readme

This project implements a script called SUPERPY that offers various functionalities for managing product inventory, generating reports, and manipulating time. The script utilizes the argparse module to parse command-line arguments and perform specific actions based on the provided inputs.

## Functionality

The SUPERPY script provides the following main functionalities:

### Buy Function

The buy function allows users to purchase a product and update the inventory accordingly. It checks if the specified product is available in the inventory (bought.csv) and, if found, adds the purchase details to the file. The function provides feedback on the success or failure of the purchase.

### Sell Function

The sell function enables users to sell a product from the inventory. Similar to the buy function, it verifies if the product exists and updates the sold.csv file with the relevant details. The function notifies the user about the success or failure of the sale operation.

### Report Function

The report function generates reports based on specified types, such as "sold" or "bought." It supports generating reports for a specific date or all available records. The function retrieves the necessary information from the respective CSV files and presents it in a structured manner.

### Change Time Function

The change_time function allows users to manipulate the system's time. It advances the current time by a specified duration, helping simulate the progression of time for testing or demonstration purposes.

### Products Function

The products function lists all the available products in the inventory. It retrieves the product information from the CSV files and presents it in a readable format.

## Usage

To use the SUPERPY script, execute the main.py file with the appropriate command-line arguments. Here are some examples:

### Buy a Product

To buy a product, use the following command:


python main.py buy --product_name <product_name>


Replace <product_name> with the name of the product you want to purchase.

### Sell a Product

To sell a product, use the following command:


python main.py sell --product_name <product_name>


Replace <product_name> with the name of the product you want to sell.

### Generate a Report

To generate a report, use the following command:


python main.py report --report_type <report_type> [--date <date>]


Replace <report_type> with "sold" or "bought" to specify the type of report. Optionally, you can provide the --date flag followed by a specific date (in a format compatible with the script) to generate a report for that date.

### Change Time

To change the system's time, use the following command:


python main.py change_time --time <change_time_to>


Replace <change_time_to> with the duration by which you want to advance the current time by date or days.

### List Products

To list all available products, use the following command:


python main.py products


## Conclusion

The SUPERPY script provides essential functionalities for managing product inventory, generating reports, and manipulating time. By leveraging the power of command-line arguments and the argparse module, users can easily interact with the script and perform various operations seamlessly.

For more detailed information on the script's functionalities, command-line arguments, and usage, refer to the script's implementation or consult the documentation.
