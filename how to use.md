# How to Use

This guide provides detailed information on how to use the SUPERPY script and its various functionalities. The script utilizes the argparse module to parse command-line arguments and perform specific actions based on the provided inputs. Below, you will find the command-line argument trees for each functionality along with their respective usage examples.

## Buy Function

The buy function allows users to purchase a product and update the inventory accordingly.

Command-line argument tree for the buy function:


buy
└── --product_name PRODUCT_NAME


Usage example:


python main.py buy --product_name <product_name>


Replace <product_name> with the name of the product you want to purchase.

## Sell Function

The sell function enables users to sell a product from the inventory.

Command-line argument tree for the sell function:


sell
└── --product_name PRODUCT_NAME


Usage example:


python main.py sell --product_name <product_name>


Replace <product_name> with the name of the product you want to sell.

## Report Function

The report function generates reports based on specified types, such as "sold" or "bought."

Command-line argument tree for the report function:


report
├── --report_type {sold,bought}
└── [--date DATE]


Usage examples:

To generate a report for all sold items:


python main.py report --report_type sold


To generate a report for all bought items:


python main.py report --report_type bought


To generate a report for a specific date (replace <date> with a valid date):


python main.py report --report_type sold --date <date>


## Change Time Function

The change_time function allows users to manipulate the system's time.

Command-line argument tree for the change_time function:


change_time
└── --time TO_CHANGE_TO


Usage example:


python main.py change_time --time <time_to_change_to>


Replace <time_duration> with the duration by which you want to advance the current time.

## Products Function

The products function lists all available products in the inventory.

Command-line argument tree for the products function:


products


Usage example:


python main.py products


## Conclusion

By following the command-line argument trees and usage examples provided above, you can effectively utilize the SUPERPY script and its various functionalities. Experiment with different commands and explore the capabilities of the script for managing product inventory, generating reports, and manipulating time.

For more detailed information on the script's functionalities, command-line arguments, and usage, refer to the script's implementation or consult the documentation.