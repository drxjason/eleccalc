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
		if float(hours) < 24:
			cost_daily = float(kwh) * float(rate) 
			return cost_daily

		if float(hours) < 168:
			cost_weekly = float(kwh) * float(rate) 
			return cost_weekly

		if float(hours) < 730.001:
			cost_monthly = float(kwh) * float(rate) 
			return cost_monthly


		if float(hours) < 8760:
			cost_yearly = float(kwh) * float(rate)
			return cost_yearly


parser = argparse.ArgumentParser(
	description="calculate cost of electricity"
)

parser.add_argument(
	'--watts', '-p',
	help='current'
)

parser.add_argument(
	'--daily', '-d',
	help='time in hours per day',
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

args = parser.parse_args()

elec = Electricity()
if args.watts and args.rate:
	if args.daily:
		daily_kwh = elec.kwh_consumed(args.watts, args.daily)
		cost_daily = elec.cost(daily_kwh, args.daily, args.rate)

		print("Power Consumption: {} Watts".format(args.watts))
		print("Cost per kWh: ${}/kWh".format(args.rate))
		print("Usage: {} hours/day".format(args.daily))
		print("Consumed: {} kWh/day".format(daily_kwh))
		print("Cost: ${}/day".format(round(cost_daily, 3)))

	elif args.weekly:
		weekly_kwh = elec.kwh_consumed(args.watts, args.weekly)
		cost_weekly = elec.cost(weekly_kwh, args.weekly, args.rate)

		print("Power Consumption: {} Watts".format(args.watts))
		print("Cost per kWh: ${}/kWh".format(args.rate))
		print("Usage: {} hours/week".format(args.weekly))
		print("Consumed: {} kWh/week".format(weekly_kwh))
		print("Cost: ${}/week".format(round(cost_weekly, 3)))

	elif args.monthly:
		monthly_kwh = elec.kwh_consumed(args.watts, args.monthly)
		cost_monthly = elec.cost(montly_kwh, args.monthly)

		print("Power Consumption: {} Watts".format(args.watts))
		print("Cost per kWh: ${}/kWh".format(args.rate))
		print("Usage: {} hours/month".format(args.monthly))
		print("Consumed: {} kWh/month".format(monthly_kwh))
		print("Cost: ${}/month".format(round(cost_monthly, 3)))

	elif args.yearly:
		yearly_kwh = elec.kwh_consumed(args.watts, args.yearly)
		cost_yearly = elec.cost(yearly_kwh, args.yearly, args.rate)

		print("Power Consumption: {} Watts".format(args.watts))
		print("Cost per kWh: ${}/kWh".format(args.rate))
		print("Usage: {} hours/year".format(args.yearly))
		print("Consumed: {} kWh/year".format(yearly_kwh))
		print("Cost: ${}/year".format(round(cost_yearly, 3)))


""" if args.watts and args.time and args.rate:
	kwh = elec.kwh_consumed(args.watts, args.time)
	cost = elec.cost(kwh, args.time, args.rate)
	print("{} kWh every {} hours, at ${}/kwh for ${} per day".format(kwh, args.time, args.rate, round(cost, 3)))"""