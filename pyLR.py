import time

# colors 
cyan = "\033[1;96m"
yellow = "\033[1;33m"
red = "\033[1;31m"
green = "\033[1;32m"
none = "\033[0m"

# importing libraries 
print(f"{red} [•]{yellow} importing scipy.stats{none}", end="\r")
from scipy import stats	
print(f"{red} [•]{yellow} importing pandas     {none}", end="\r")
import pandas as pd	
print(f"{red} [•]{yellow} importing numpy      {none}", end="\r")
import numpy as np	
print(f"{red} [•]{yellow} successfully initialized!{none}", end="\r")
time.sleep(0.5)

print(f"{cyan}~~~~~~~ LINEAR REGRESSION CALCULATOR ~~~~~~~{cyan}")	
try:
	
	# assigning values
	inputX = input(f"\n {red}[•] {yellow}Enter Xs (comma separated) => {cyan}")
	inputY = input(f"{red} [•] {yellow}Enter Ys (comma separated) => {cyan}")
	
	x = []
	y = []
	
	for entryX in inputX.split(" "):
		if entryX.isdigit():
			x.append(int(entryX))
		
	for entryY in inputY.split(" "):
		if entryY.isdigit():
			y.append(int(entryY))
	
	# storage
	x_squared = []
	y_squared = []
	XY = []
	
	# loops to calculate each iterations
	for i in x:
		squared = i ** 2
		x_squared.append(squared)
	
	for w in y:
		squared = w ** 2
		y_squared.append(squared)
	
	for values in range(len(x)):	
		Xs = x[values]
		Ys = y[values]
		xyVal = Xs * Ys
		XY.append(xyVal)
	
	# necessary values
	xSumm = sum(x)
	ySumm = sum(y)
	xySumm = sum(XY)
	xSquareSumm = sum(x_squared)
	ySquareSumm = sum(y_squared)		
	
	# needed values
	slope, intercept, r, p, std_err = stats.linregress(x,y)
	
	# variable for dataframe
	data = {
		"x": x,
		"y": y,
		"XY": XY,
		"x\u00b2": x_squared,
		"y\u00b2": y_squared
		}
	
	# header
	print(f"{yellow}_"*50)
	time.sleep(0.01)
	print(f"\n\t\t• {cyan}DATAFRAME{none} •")	
	time.sleep(0.01)
	
	# creating dataframe
	dataFrame = pd.DataFrame(data)
	
	print(f"{yellow}_"*50)
	time.sleep(0.01)
	print(f"\n\n{yellow}",dataFrame,f"{none}")
	time.sleep(0.01)
	print(f"{yellow}_"*50)
	time.sleep(0.1)
	print(" ")
	
	# means or averages
	xMean = round(np.mean(x),4)
	yMean = round(np.mean(y),4)
	
	# printing values
	print(f" {red}[•] {yellow}\u03BC(x) : {green}{xMean}")
	time.sleep(0.01)
	print(f" {red}[•] {yellow}\u03BC(y) : {green}{yMean}{yellow}")
	time.sleep(0.01)
			
	print("_"*50)
	time.sleep(0.01)
	print(f"\n {red}[•] {yellow}\u2211x : {green}{xSumm}\t\t{red}[•] {yellow}\u2211y : {green}{ySumm}")
	time.sleep(0.01)
	print(f" {red}[•] {yellow}\u2211XY : {green}{xySumm}\t\t{red}[•] {yellow}\u2211x\u00b2 : {green}{xSquareSumm}")
	time.sleep(0.01)
	print(f" {red}[•] {yellow}\u2211y\u00b2 : {green}{ySquareSumm}\t\t{red}[•] {yellow}\u2211XY : {green}{xySumm}{yellow}")
	time.sleep(0.01)
	
	print("_"*50)
	time.sleep(0.01)
	print(f"\n {red}[•] {yellow}r_Value : {green}{r}")
	time.sleep(0.01)
	print(f" {red}[•] {yellow}p_Value : {green}{p}")
	time.sleep(0.01)
	print(f" {red}[•] {yellow}std_err : {green}{std_err}")
	time.sleep(0.01)
	print(f" {red}[•] {yellow}slope : {green}{slope}")
	time.sleep(0.01)
	print(f" {red}[•] {yellow}intercept : {green}{intercept}{yellow}")
	time.sleep(0.01)
	print(f"_"*50)
	time.sleep(0.01)
	print("\n")
	print(f"{none}")
	
except Exception as e:
	print(f"\n\n {cyan}[•] {red}ERROR : {green}{e}{none}")
	
