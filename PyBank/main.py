#import Dependencies
import pandas as pd

#File to Load
PyBank = "Resources/budget_data.csv"
PyBank_df = pd.read_csv(PyBank)

#Read the modified PyBank csb and store into Pandas DataFrame
PyBank_df.head()
   
#Calculate total Number of months
month_count = len(PyBank_df["Date"].unique())

#Calculate net amount of Profit/Losses over the entire period
net_amount = PyBank_df["Profit/Losses"].sum()

#New Column display profit/loss between months
PyBank_df["Change"] = PyBank_df["Profit/Losses"].diff()

#Average change in Profit/Losses between months over the entire period
average_profitLosses = PyBank_df["Change"].mean()

#The greatest increase in profits (date and amount) over the entire period
greatest_profit = PyBank_df["Change"].max()
greatest_profit_month = PyBank_df.loc[PyBank_df["Change"] == greatest_profit, :]

#The greatest increase in losses (date and amount) over the entire period
greatest_loss = PyBank_df["Change"].min()
greatest_loss_month = PyBank_df.loc[PyBank_df["Change"] == greatest_loss,:]

#Print Financial Analysis info
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(month_count)}")
print(f"Total: ${str(net_amount)}")
print(f"Average Change: ${str(round(average_profitLosses,2))}")
print(f"Greatest Increase in Profits: {str(greatest_profit_month['Date'].values)} (${str(greatest_profit)})")
print(f"Greatest Decrease in Profits: {greatest_loss_month['Date'].values} (${str(greatest_loss)})")

#Exporting to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(month_count)}")
line4 = str(f"Total: ${str(net_amount)}")
line5 = str(f"Average Change: ${str(round(average_profitLosses,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_profit_month['Date'].values} (${str(greatest_profit)})")
line7 = str(f"Greatest Decrease in Profits: {greatest_loss_month['Date'].values} (${str(greatest_loss)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))