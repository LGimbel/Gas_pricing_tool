#region important var dec
filename = "GasPrices.txt"
months_dict = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
user_prompt = "welcome to the ultimate gas price took please select the tool to use. \n The options are: \n 1:Find average price in a given year. \n 2: Find average price in given month in given year. \n 3:Find the highest and lowest prices in a given year. \n 4:Generate a file with all prices sorted in the direction of your choosing."
prices_by_year = {
    "1993": [],
    "1994": [],
    "1995": [],
    "1996": [],
    "1997": [],
    "1998": [],
    "1999": [],
    "2000": [],
    "2001": [],
    "2002": [],
    "2003": [],
    "2004": [],
    "2005": [],
    "2006": [],
    "2007": [],
    "2008": [],
    "2009": [],
    "2010": [],
    "2011": [],
    "2012": [],
    "2013": []
}
all_prices = []
#endregion
def pull_from_file():
    global all_prices
    with open(filename, 'r') as f:
        for line in f:
            curent_line = line.rstrip('\n').rstrip('\\').strip()
            all_prices.append(curent_line)
def DataWork():
    global prices_by_year
    for string in all_prices:
       splitAray1 = string.split(':')
       splitAray2 = splitAray1[0].split('-')
       match(splitAray2[2]):
        case "1993":
            prices_by_year["1993"].append(string)
        case "1994":
            prices_by_year["1994"].append(string)
        case "1995":
            prices_by_year["1995"].append(string)
        case "1996":
            prices_by_year["1996"].append(string)
        case "1997":
            prices_by_year["1997"].append(string)
        case "1998":
            prices_by_year["1998"].append(string)
        case "1999":
            prices_by_year["1999"].append(string)
        case "2000":
            prices_by_year["2000"].append(string)
        case "2001":
            prices_by_year["2001"].append(string)
        case "2002":
            prices_by_year["2002"].append(string)
        case "2003":
            prices_by_year["2003"].append(string)
        case "2004":
            prices_by_year["2004"].append(string)
        case "2005":
            prices_by_year["2005"].append(string)
        case "2006":
            prices_by_year["2006"].append(string)
        case "2007":
            prices_by_year["2007"].append(string)
        case "2008":
            prices_by_year["2008"].append(string)
        case "2009":
            prices_by_year["2009"].append(string)
        case "2010":
            prices_by_year["2010"].append(string)
        case "2011":
            prices_by_year["2011"].append(string)
        case "2012":
            prices_by_year["2012"].append(string)
        case "2013":
            prices_by_year["2013"].append(string)
        case _:
            print("well that's not good")
            SystemExit() 
def averageYear(year):
    total_entries = 0
    total_price = 0
    for string in prices_by_year[year]:
        irellevand_and_price = string.split(':')
        price = float(irellevand_and_price[1])
        total_price += price
        total_entries += 1
    averagePrice = (total_price / total_entries)
    return averagePrice
def averageMonth(year,month):
    month_entries = []
    total_entries = 0
    total_price = 0
    for string in prices_by_year[year]:
        month_and_irrelevantX2 = string.split('-')
        if (month_and_irrelevantX2[0] == month):            
            irrelevant_and_price = (month_and_irrelevantX2[2].split(':'))   
            price = float(irrelevant_and_price[1])
            total_price += price
            total_entries += 1 
    averagePrice = (total_price / total_entries)
    return averagePrice
def FindExtremes(year):
    highest_price = 0
    lowest_price = 99
    for string in prices_by_year[year]:
        irellevand_and_price = string.split(':')
        price = float(irellevand_and_price[1])
        if price > highest_price:
            highest_price = price
        elif price < lowest_price:
            lowest_price = price
    return highest_price,lowest_price
def GenSortedFile(sort_direction):
    if sort_direction:
        filename = "Gas_Prices_highest_to_lowest.txt"
    else:
        filename = "Gas_Prices_lowest_to_highest.txt"
    with open(filename,'w') as f:
        try:
            sorted_values = sorted(all_prices, key=lambda x: float(x.split(':')[1]),reverse=sort_direction)
            for entry in sorted_values:
                f.write(entry + '\n')
                
        except Exception as e:
            print(f"something went wrong {e} please adress the issue")
def UserInterface():
    print(user_prompt)
    chosen_process = int(input("please make a selection by choosing the number that coresponds to the desired funcion."))
    if int(chosen_process) > 4 or chosen_process < 1:
        print(f"you entered {chosen_process} however {chosen_process} is not a valid operation please try again.")
        UserInterface()
    elif (chosen_process == 1):
        print("you have chosen to find the average price of gas in a given year")
        year =  input("please choose a year between 1993 and 2013 ")
        if int(year) < 1993 or int(year) > 2013:
            print(f"it apears you chose {year} which is outside the given range please try again")
            UserInterface()
        else:
             print(f" the average price of gas in the year {year} was {averageYear(year)}")
    elif (chosen_process == 2):
        print("you have chosen to find the average price of gas in a given month of a given year")
        year = (input("please enter a year between 1993 and 2013 "))
        if int(year) < 1993 or int(year) > 2013:
            print(f"it apears you chose {year} which is outside the given range please try again")
            UserInterface()
        else:
            month = (input("please enter a month using the notation 01 for January and 02 for Febuary Etc. "))
            if int(month) > 12 or int(month) < 0:
                print(f"you chose {month} which is not a valid option. Please try again.")
                UserInterface()
            else:
                print(f"The average cost of gas for the month of {months_dict.get(month)} in the year of {year} was {averageMonth(year,month)}")
    elif(chosen_process == 3):
        print("you have chosen to find the extremes in a certain year")
        year = (input("please enter a year between 1993 and 2013 "))
        if int(year) < 1993 or int(year) > 2013:
            print(f"it apears you chose {year} which is outside the given range please try again")
            UserInterface()
        else:
            highest,lowest = FindExtremes(year)
            print(f"the higest price for gas in the year {year} was {highest} and the lowest was {lowest}")
    elif(chosen_process ==4):
        print("you have chosen to generate a file of all the gas prices in a chosen direction")
        direction = input("would you like the list sorted from highest to lowest Y/N if you chose N the list will be sorted lowest to Highest ")
        sort_direction = True if direction == "Y" else False
        print("file generating")
        GenSortedFile(sort_direction)  
pull_from_file()
DataWork()
UserInterface()

        
        
        
        