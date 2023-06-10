# Superpy_Winc
Assignment: Superpy

#Assignment: Superpy

# How to Use:
	 --use {buy,sell,report,products}
		Choose how to use (buy, sell, report, products)
		buy to buy somthing from the store 
		sell to sell somthing from the store
		report to report history bought and sold items
		products to list all products in store and theire prices
		examples:
			python main.py --use products
			python main.py --use buy --product_name orange
			python main.py --use buy --product_name "coca cola"
			python main.py --use sell --product_name "coca cola"
			python main.py --use sell --product_name "orange"
			python main.py --use report --report sold --date yesterday
			python main.py --use report --report bought
			python main.py --use report --report bought --date 2023-06-09
	--product_name PRODUCT_NAME
		Wich Product you wish to buy or sell (--use products to list)
		examples:
			"coca cola"
			orange
			"pine apple"
			"kiwi"
	--report {sold,bought}
		Generate Report For sold or bought products (sold, bought)
		examples:
			python main.py --use report --report bought
			python main.py --use report --report sold
			python main.py --use report --report bought --date 2023-06-09
			python main.py --use report --report bought --date yesterday
	--date DATE:
		Extra Date Option Argument or Date (yesterday or date ex {2023-06-09}) or Nothing
		examples:
			python main.py --use report --report bought --date 2023-06-09
			python main.py --use report --report bought --date yesterday
	--advance_time ADVANCE_TIME:
		python main.py --advance_time 3
		Changes the Current Date For some Reason (enter a int to change by days)
	most of the options speak for it self
