# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

import platform
import subprocess
import sys
import argparse
import csv
import random
from texttable import Texttable
from datetime import timedelta, datetime, date
from colorama import Fore, Style
from art import text2art


def clear():
    """ clean function """
    if platform.system() == "Windows":
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)


class SUPERPY:
    """ Class """

    def __init__(self):
        print(self.banner())
        self.bought_path = 'bought.csv'
        self.sold_path = 'sold.csv'
        self.parser = argparse.ArgumentParser(description='Use This Program!')
        self.sub_parser = self.parser.add_subparsers(dest="use")

        self.sub_parser.add_parser('products', help='list all products in the store and there prices')

        self.buyer = self.sub_parser.add_parser('buy',
                                                help="buy a product from the store (python main.py sell -h) for help")
        self.buyer.add_argument('--product_name', type=str,
                                help='Wich Product you wish to buy ("python main.py products" to list)',
                                dest="product_name",
                                required=True)

        self.seller = self.sub_parser.add_parser('sell',
                                                 help="sell a product from the store (python main.py buy -h) for help")
        self.seller.add_argument('--product_name', type=str,
                                 help='Wich Product you wish to sell ("type python main.py products" to list)',
                                 dest="product_name", required=True)

        self.report = self.sub_parser.add_parser("report",
                                                 help='report the store history (python main.py report -h) for more help')
        self.report.add_argument('--report_type', choices=['sold', 'bought'],
                                 help='Generate Report For sold or bought products Choose (sold, bought)',
                                 required=True,
                                 dest="report_type", type=str)
        self.report.add_argument('--custom_date',
                                 help='Extra Date Option Argument or Date (yesterday or date ex {2023-06-09}) or Nothing',
                                 dest="date")
        self.change_time = self.sub_parser.add_parser('change_time',
                                                      help='Change your Server Date (python main.py change_time -h)')
        self.change_time.add_argument('--time',
                                      help='Changes the Current Date For some Reason (enter a date 2023-06-09 or a INT to jump by days)',
                                      required=True, dest="time_to_change")
        self.args = self.parser.parse_args()

    @staticmethod
    def banner():
        bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
        codes = vars(Fore)
        colors = [codes[color] for color in codes if color not in bad_colors]
        colored_chars = [random.choice(colors) + text2art("Superpy_Winc", "random")]
        return ''.join(colored_chars) + Style.RESET_ALL

    @staticmethod
    def get_date():
        """ get writen date function """
        file_contents = open("date.txt", "r").read()
        return file_contents

    @staticmethod
    def get_real_date():
        """ get real date function """
        return date.today().strftime('%Y-%m-%d')

    @staticmethod
    def list_products():
        """ get products function """
        values = []
        t = Texttable()
        with open('bought.csv', mode='r', encoding='utf-8', errors='ignore') as reader_csv:
            values_in = csv.reader(reader_csv)
            for all_values in values_in:
                t.add_row([all_values[0], all_values[1], all_values[3], all_values[4]])
        sys.stdout.write(t.draw())
        return values

    @staticmethod
    def csv_reader(path, date_to=None):
        """ csv reader function """
        values = []
        with open(path, mode='r', encoding='utf-8', errors='ignore') as reader_csv:
            values_in = csv.reader(reader_csv)
            for all_values in values_in:
                if date_to is not None and date_to == all_values[2]:
                    values.append(all_values)
                elif date_to is None:
                    values.append(all_values)
        if len(values) == 0:
            return False
        return values

    def product_id(self, type_id='bought'):
        """ get_product_id function """
        try:
            product_id = int(str(self.csv_reader(path=f'{type_id}.csv')[-1][0]))
        except (ValueError, Exception):
            product_id = 0
        product_id += 1
        return product_id

    @staticmethod
    def is_int(value):
        try:
            int(value)
            return True
        except Exception as e:
            return False

    def advance_time(self, fix_by_days):
        """ advance_time function """
        current_date = self.get_date()
        dt = datetime.strptime(current_date, '%Y-%m-%d')
        if self.is_int(value=fix_by_days):
            fixed_date = dt + timedelta(days=int(fix_by_days))
            current_date = fixed_date.strftime('%Y-%m-%d')
        else:
            current_date = fix_by_days
        with open("date.txt", "w") as tijd:
            tijd.write(current_date)
        sys.stdout.write("DONE!")

    @staticmethod
    def csv_writer(path, value_to_write: list, mode="a"):
        """ csv writer function """
        try:
            with open(path, mode=mode, encoding='utf-8', errors='ignore', newline='') as reader_csv:
                writer = csv.writer(reader_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(value_to_write)
                return True
        except (FileExistsError, FileNotFoundError, Exception):
            return False

    def read_and_return(self, type_to_report, date_to):
        """ as the name says function """
        get = self.csv_reader(path=f"{type_to_report}", date_to=date_to)
        if get is not False or get is not None or len(get) != 0:
            return get
        else:
            sys.stdout.write("ERROR: Nothing sold that day or No data Found About That Day!")
            return False

    def to_report(self, type_to_report='sold', date_to=None):
        """ report function """
        t = Texttable()
        if type_to_report != "sold" and type_to_report != "bought":
            return False
        if date_to == "yesterday":
            current_date = self.get_date()
            dt = datetime.strptime(current_date, '%Y-%m-%d')
            yesterday = dt - timedelta(days=1)
            date_to = yesterday.strftime('%Y-%m-%d')
            get = self.read_and_return(type_to_report=f"{type_to_report}.csv", date_to=date_to)
        elif date_to is not None:
            get = self.read_and_return(type_to_report=f"{type_to_report}.csv", date_to=date_to)
        elif date_to is None:
            get = self.read_and_return(type_to_report=f"{type_to_report}.csv", date_to=date_to)
        else:
            sys.stdout.write("ERROR: You Play to Much!!")
            return False
        if get is False or len(get) == 0:
            sys.stdout.write("ERROR: Nothing sold that day!")
            return False
        t.add_rows(get)
        sys.stdout.write(t.draw())
        total_amount = f"€{float(sum([float(alles[3]) for alles in get if '.' in alles[3] and len(alles[3].split('.')) == 2])):0.2f} EURO"
        sys.stdout.write(f"\nYour Total Amount Earned in Euro is € {total_amount} !")
        return True

    def buy(self, product_name):
        """ buy function """
        product = None
        for item in self.csv_reader(path='bought.csv'):
            if item[1] == product_name:
                product = item
        if product is None:
            sys.stdout.write("ERROR: Product not in stock")
            return False
        product_price = product[3]
        product_expiry = product[4]
        x = self.csv_writer(path='bought.csv',
                            value_to_write=[self.product_id(type_id='bought'), product_name, self.get_real_date(),
                                            product_price, product_expiry])
        if x is False:
            sys.stdout.write("ERROR: WE COULD NOT WRITE TO CSV!")
            return False
        sys.stdout.write(f"SUCCESS: You Bought A {product_name} for {float(product_price)}!")
        return True

    def sell(self, product_name):
        """ sell function """
        product = None
        for item in self.csv_reader(path='bought.csv'):
            if item[1] == product_name:
                product = item
        if product is None:
            sys.stdout.write("ERROR: Product not in stock")
            return False
        product_price = product[3]
        tims = self.get_real_date()
        product_id = self.product_id(type_id='sold')
        x = self.csv_writer(path='sold.csv', value_to_write=[product_id, product_id, tims, product_price])
        if x is False:
            sys.stdout.write("ERROR: WE COULD NOT WRITE TO CSV!")
            return False
        sys.stdout.write(f"SUCCESS: You Sold A {product_name} Date: {tims}!")
        return True

    def main(self):
        """ main function """
        if self.args.use == "buy" or self.args.use == "sell":
            if self.args.product_name:
                if self.args.use == 'buy':
                    return self.buy(product_name=self.args.product_name)
                elif self.args.use == 'sell':
                    return self.sell(product_name=self.args.product_name)
                else:
                    exit("python main.py -h")
        elif self.args.use == "report":
            if self.args.report_type == "sold":
                if self.args.date:
                    return self.to_report(type_to_report=self.args.report_type, date_to=self.args.date)
                else:
                    return self.to_report(type_to_report=self.args.report_type)
            elif self.args.report_type == "bought":
                if self.args.date:
                    return self.to_report(type_to_report=self.args.report_type, date_to=self.args.date)
                else:
                    return self.to_report(type_to_report=self.args.report_type)
            else:
                exit("python main.py report -h")
        elif self.args.use == "change_time":
            return self.advance_time(self.args.time_to_change)
        elif self.args.use == 'products':
            return self.list_products()
        else:
            exit("python main.py -h for help!")
            return False


if __name__ == '__main__':
    clear()
    main_class = SUPERPY()
    main_class.main()
