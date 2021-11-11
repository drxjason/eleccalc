#!/usr/bin/env python
# Electricity Calculator

import argparse
import sys
import os

class Electricity:
	def kwh(self, wattage, time):
		kwh = (float(wattage) * float(time)) / 1000
		return kwh

	def cost(self, kwh, time, rate):
		cost = float(kwh) * float(rate)
		return cost

parser = argparse.ArgumentParser(
	description="calculate cost of electricity"
)

parser.add_argument(
	'--watts', '-w',
	help='current'
)

parser.add_argument(
	'--time', '-t',
	help='time in hours',
	metavar='HOURS'
)

parser.add_argument(
	'--rate', '-r',
	help='price per kWh',
	metavar='$X.XX'
)

args = parser.parse_args()

elec = Electricity()

if args.watts and args.time and args.rate:
	kwh = elec.kwh(args.watts, args.time)
	cost = elec.cost(kwh, args.time, args.rate)
	print("{} kWh every {} hours, at ${}/kwh for ${} per day".format(kwh, args.time, args.rate, round(cost, 3)))

elif args.watts and args.time and args.rate is None:
	print("--watts/-w and --time/-t require --rate/-r")

elif args.watts and args.time is None and args.rate:
	print("--watts/-w and --rate/-r require --time/-t")

elif args.watts is None and args.time and args.rate:
	print("--time/-t and --rate/-r require --watts/-w")

elif args.watts and args.time is None and args.rate is None:
	print("--watts/-w require --time/-t and --rate/-r")

elif args.watts is None and args.time and args.rate is None:
	print("--time/-t requires --watts/-w and --rate/-r")

elif args.watts is None and args.time is None and args.rate:
	print("--rate/-r requires --watts/-w and --time/-t")