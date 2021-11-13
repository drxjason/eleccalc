#!/usr/bin/env python
# Electricity Calculator

import argparse
import sys
import os

class Electricity:
	def kwh_consumed(self, wattage, hours):
		kwh = (float(wattage) * float(hours)) / 1000
		return kwh

	def cost(self, kwh, hours, rate):
		if float(hours) >= 0:
			cost_daily = float(kwh) * float(rate) 
			return cost_daily

		if float(hours) >= 24:
			cost_weekly = float(kwh) * float(rate) 
			return cost_weekly

		if float(hours) >= 168:
			cost_monthly = float(kwh) * float(rate) 
			return cost_monthly

		if float(hours) >= 730.001:
			cost_yearly = float(kwh) * float(rate)
			return cost_yearly

		if float(hours) >= 8760:
			print("error in function")

def prompt_usage():
	print(
		"usage: [command] [argument]\n"
		"\n"
		"interactive prompt for power conversion\n\n"
		"commands:\n"
		"    calc [argument]   calculate kilowatt hours with a specified unit of time\n"
		"    help              display help\n"
		"    exit              exit interactive mode\n"
		"\n"
		"optional arguments:\n"
		"    --days, -d        convert to kilowatt hours a day\n"
		"    --weeks, -w       convert to kilowatt hours a week\n"
		"    --months, -m      convert to kilowatt hours a month\n"
		"    --years, -y       convert to kilowatt hours a year\n"
	)


parser = argparse.ArgumentParser(
	description="calculate cost of electricity"
)

parser.add_argument(
	'--power', '-p',
	help='current'
)

parser.add_argument(
	'--daily', '-d',
	help='usage hours per day',
	metavar='HOURS'
)

parser.add_argument(
	'--weekly', '-w',
	help='usage hours per week',
	metavar='HOURS'
)

parser.add_argument(
	'--monthly', '-m',
	help='usage hours per month',
	metavar='HOURS'
)

parser.add_argument(
	'--yearly', '-y',
	help='usage hours per year',
	metavar='HOURS'
)

parser.add_argument(
	'--rate', '-r',
	help='price per kWh',
	metavar='$$.¢¢'
)

parser.add_argument(
	'--interactive', '-i',
	help='interactive mode',
	action='store_true'
)

args = parser.parse_args()

elec = Electricity()

if args.power and args.rate:
	if args.daily:
		daily_kwh = elec.kwh_consumed(args.power, args.daily)
		cost_daily = elec.cost(daily_kwh, args.daily, args.rate)

		if int(args.daily) > 24:
			print('error -d/--daily: hours must be less than or equal to 24')

		else:
			print("Power Consumption: {} Watts".format(args.power))
			print("Cost per kWh: ${}/kWh".format(args.rate))
			print("Usage: {} hours/day".format(args.daily))
			print("Consumed: {} kWh/day".format(daily_kwh))
			print("Cost: ${}/day".format(round(cost_daily, 3)))

	elif args.weekly:
		weekly_kwh = elec.kwh_consumed(args.power, args.weekly)
		cost_weekly = elec.cost(weekly_kwh, args.weekly, args.rate)

		if int(args.weekly) > 168:
			print('error -w/--weekly: hours must be less than or equal to 168')

		else:
			print("Power Consumption: {} Watts".format(args.power))
			print("Cost per kWh: ${}/kWh".format(args.rate))
			print("Usage: {} hours/week".format(args.weekly))
			print("Consumed: {} kWh/week".format(weekly_kwh))
			print("Cost: ${}/week".format(round(cost_weekly, 3)))

	elif args.monthly:
		monthly_kwh = elec.kwh_consumed(args.power, args.monthly)
		cost_monthly = elec.cost(monthly_kwh, args.monthly, args.rate)

		if int(args.monthly) > 730:
			print('error -m/--monthly: hours must be less than or equal to 730')
		
		else:
			print("Power Consumption: {} Watts".format(args.power))
			print("Cost per kWh: ${}/kWh".format(args.rate))
			print("Usage: {} hours/month".format(args.monthly))
			print("Consumed: {} kWh/month".format(monthly_kwh))
			print("Cost: ${}/month".format(round(cost_monthly, 3)))

	elif args.yearly:
		yearly_kwh = elec.kwh_consumed(args.power, args.yearly)
		cost_yearly = elec.cost(yearly_kwh, args.yearly, args.rate)
		
		if int(args.yearly) > 8760:
			print('error -y/--yearly: hours must be less than or equal to 8760')
		
		else:
			print("Power Consumption: {} Watts".format(args.power))
			print("Cost per kWh: ${}/kWh".format(args.rate))
			print("Usage: {} hours/year".format(args.yearly))
			print("Consumed: {} kWh/year".format(yearly_kwh))
			print("Cost: ${}/year".format(round(cost_yearly, 3)))
		
	else:
		print("error")

elif args.interactive:
	prompt = True

	while prompt:
		commands = input("prompt> ")
		commands = commands.split()

		if commands:
			if commands[0] == 'calc':
				if len(commands) < 2:
					print("calc requires an argument")
					
				else:
					if commands[1] == '-d' or commands[1] == '--day':
						while True:
							wattage = input("wattage: ")
							hours = input("usage hours/day: ")

							if int(hours) < 25:
								kwh = elec.kwh_consumed(wattage, hours)
								print("{} kWh/day".format(kwh))
								break

							else:
								print("there are 24 hours in a day, error")

					elif commands[1] == '-w' or commands[1] == '--week':
						while True:
							wattage = input("wattage: ")
							hours = input("usage hours/week: ")

							if int(hours) < 169:
								kwh = elec.kwh_consumed(wattage, hours)
								print("{} kWh/week".format(kwh))
								break

							else:
								print("There are 168 hours in a week, error")

					elif commands[1] == '-m' or commands[1] == '--month':
						while True:
							wattage = input("wattage: ")
							hours = input("usage hours/month: ")

							if int(hours) < 731:
								kwh = elec.kwh_consumed(wattage, hours)
								print("{} kWh/month".format(kwh))
								break

							else:
								print("There are 160 hours in a week, error")

					elif commands[1] == '-y' or commands[1] == '--year':
						while True:
							wattage = input("wattage: ")
							hours = input("usage hours/year: ")

							if int(hours) < 8761:
								kwh = elec.kwh_consumed(wattage, hours)
								print("{} kWh/year".format(kwh))
								break

							else:
								print("There are 8760 hours in a year, error")

					else:
						print("argument {} is not valid".format(commands[1]))


			elif commands[0] == 'exit':
				prompt = False

			elif commands[0] == 'help':
				prompt_usage()
				
else:
	parser.print_help()