# US Fossil Fuel Market Data Analysis

# Coal Prices Delivered to Power Sector Nationally 2005 through 2019

Results

US coal prices delivered to the electricity sector rose sharply to a peak price in 2011, but have steadily dropped nearly 20% since 2011. Reductions in domestic coal consumption are mainly due to stiff competition from natural gas power plants and renewables, as well lower than expected demand in electricity [1]. Transportation costs and the coal purchase price for coal deliveries to power plants have both decreased during this period, with the purchase price decreasing at a greater rate than transportations costs. This shows the purchase price has had a greater impact on the delivered coal price than transportation costs.

![1](/png/Figure_1.png)

Method

After an exhaustive search on the EIA website, data for coal prices delivered to the electricity sector only included prices from 2008 to 2019. A different data set was used which included average transportation costs, which can be found in the links below. Purchase price was assumed to equal delivered coal price minus transportation cost.

Data Sources

1.	Coal Prices
a)	Website - https://www.eia.gov/coal/data.php#coalplants
b)	Direct Link - https://www.eia.gov/coal/transportationrates/excel/table1Real.xlsx 



# Historical Average Annual Henry Hub Natural Gas Prices from 2005 through 2020

Results

Natural gas production in the US have seen a sharp increase since 2005 [2], which has coincided with a 77% reduction in the Henry Hub natural gas price during the same time period. Technological advances in hydraulic fracturing and horizontal drilling have allowed for production in previously inaccessible shale gas formations, resulting in a boom for natural gas production [1][3].

![2](/png/Figure_2b.png)

Data Sources

1.	Henry Hub Natural Gas Prices
a)	Website - https://www.eia.gov/dnav/ng/hist/rngwhhdA.htm
b)	Direct Link - https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDa.xls

# US Annual Coal and Natural Gas Electricity Generation from 2005 through 2019

Results

Coal electricity generation in the US peaked in 2007 [4], but since then, the US coal industry has crippled due to several economic forces [1]. In 2019, 92% of US coal was consumed by the electricity sector [5], so any fluctuations in the coal industry are at the whims of the power sector. A 2017 study performed by T. Houser et al. concluded that from 2008 to 2016, 50% of the reduction in coal production was due to electricity generation from natural gas [1]. Between 2005 and 2019, coal generation has dropped by 52%, whereas natural gas generation has increased by 108% during the same time period.

![3](/png/Figure_3.png)
 
Data Sources

1.	US Annual Coal and Natural Gas Electricity Generation 
a)	Website - https://www.eia.gov/electricity/data/browser/#/topic/0?agg=2,0,1&fuel=9&geo=g&sec=g&linechart=ELEC.GEN.COW-US-99.A&columnchart=ELEC.GEN.COW-US-99.A&map=ELEC.GEN.COW-US-99.A&freq=A&ctype=linechart&ltype=pin&rtype=s&maptype=0&rse=0&pin=
b)	Direct Link - Use above link to download csv file

# Projected Annual Henry Hub Natural Gas Prices from 2021 through 2040

Results

The EIA’s AEO 2020 reference case projects the Henry Hub natural gas price to not exceed $3.50 per million Btu, and the high oil and gas supply projection hovers around $2.50 and $2.60 after the year 2027. The actual 2020 price of natural gas was much lower than any of the projections, coming out at $2.02, but this should not come as a surprise when considering the historical volatility in prices. COVID-19 had a significant impact on the natural gas price drop in the US, resulting in a drop in natural gas demand [6]. 

![4](/png/Figure_4.png)

Data Sources

1.	Historical Henry Hub Natural Gas Price
a)	Website - https://www.eia.gov/dnav/ng/hist/rngwhhdA.htm
b)	Direct Link - https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDa.xls
2.	Projected Henry Hub Natural Gas Prices
a)	Website - www.eia.gov/outlooks/aeo/tables_side.php
b)	Direct Link (Reference Case) - https://www.eia.gov/outlooks/aeo/excel/sidecases/dgref/aeotab_13.xlsx
c)	Direct Link (Low Oil and Gas Supply) - https://www.eia.gov/outlooks/aeo/excel/sidecases/dglogs/aeotab_13.xlsx
d)	Direct Link (High Oil and Gas Supply) - https://www.eia.gov/outlooks/aeo/excel/sidecases/dghogs/aeotab_13.xlsx

# Natural Gas Electricity Generation as a Share of Coal Generation in 2040

Results

Using a 1% growth rate for total electricity generation, a 0.8% growth rate for natural gas electricity generation, and a 40 year service life span for coal power plants, it is projected that electricity generated from natural gas will be approximately 19 times greater than coal electricity generation by 2040. This projection is much more bearish on coal compared to other projections due to the assumption that coal power plants will retire after 40 years of operation.  
 
![5](/png/Figure_5.png)

Method

Growth rates for natural gas and total electricity generation were used from the EIA AEO 2020 report to project electricity generation in 2040. Coal power plants entering service prior to 2000 are assumed to retire by 2040. Coal electricity generation and coal capacity are assumed to be proportional, so when coal power plants are retired, a proportional amount of coal electricity generation is reduced. A detailed list of assumptions is shown below.

Assumptions
1.	Use coal, natural gas, and total electricity generation from 2019 as a baseline.
2.	Assume electricity generation grows at 1% per year to 2040. Based on EIA AEO 2020.
3.	Assume natural gas electricity generation grows at 0.8% per year to 2040. Based on EIA AEO 2020.
4.	Using assumptions 1-3, natural gas and total electricity generation in 2040 can be projected.
5.	Assume coal power plants retire after 40 years of service [7]. Any power plant beginning operation before 2000 will be removed from service by 2040.
6.	Coal prices will remain high enough that new coal power plants will not be constructed.
7.	Assume direct relationship between coal capacity and coal electricity generation. As coal power plants are removed from service, coal electricity generation is proportionally reduced. Data from Form EIA-860M, released in December 2019, was used to calculate coal capacity in 2019 and 2040. Coal generation in 2019 is known, therefore coal electricity generation in 2040 can be determined.
8.	Other sources of energy, such as nuclear and renewables, will account for the remainder of electricity generation not produced by natural gas or coal.


Data Sources

1.	Coal, Natural Gas and Total Electricity Generation in 2019
a)	Website -www.eia.gov/electricity/data/browser/#/topic/0?agg=2,0,1&fuel=p&geo=g&sec=008&linechart=ELEC.GEN.ALL-US-98.A&columnchart=ELEC.GEN.ALL-US-98.A&map=ELEC.GEN.ALL-US-98.A&freq=A&ctype=linechart&ltype=pin&rtype=s&pin=&rse=0&maptype=0
2.	Future Natural Gas and Total Electricity Generation Growth Rates
a)	Website - https://www.eia.gov/outlooks/aeo/
b)	Direct Link - https://www.eia.gov/outlooks/aeo/ppt/AEO2020%20Electricity.pptx
3.	Coal Capacity in 2019
a)	Website - https://www.eia.gov/electricity/data/eia860m/
b)	Direct Link - https://www.eia.gov/electricity/data/eia860m/archive/xls/december_generator2019.xlsx

# Annual Coal Capacity Retirements from 2005 through 2020

Results

Coal retirements managed to stay relatively low during the first decade of the 21st century, but competing sources of electricity and aging plants have led to a drastic increase in coal plant retirements in the past 10 years. Due to lower costs of energy for natural gas and renewables, coal power plants have been used less frequently, reducing profits and thus increasing the likelihood of retirement [8]. Other reasons include plants reaching the end of service life [9], low growth in electricity demand [9], and stricter emissions standards [10].

![6](/png/Figure_6.png)

Method

The data from the latest Form EIA-860M was used, which was from November 2020. Pandas was utilized to remove non-coal generating stations, and to remove coal power plants that retired prior to 2005. Summer capacity of each retired power plant was used to calculate the total capacity retirements for each year. Some coal power plants did not have a listed summer capacity, so the nameplate capacity was used as a replacement value. Using a for loop in python, the total retirements for each year were totaled.

Data Sources

1.	US Coal Retirements 
a)	Website - https://www.eia.gov/electricity/data/eia860m/
b)	Direct Link - https://www.eia.gov/electricity/data/eia860m/xls/november_generator2020.xlsx

# References

[1] Houser, T., Bordoff, J., & Marsters, P. Columbia Center on Global Energy Policy (2017, April 25). Can Coal Make a Comeback? Retrieved from https://www.energypolicy.columbia.edu/research/report/can-coal-make-comeback

[2] U.S. Energy Information Administration (EIA). (2020, August 21). Natural Gas Explained - Factors Affecting Natural Gas Prices. Retrieved from https://www.eia.gov/energyexplained/natural-gas/factors-affecting-natural-gas-prices.php

[3] Lieskovsky, J., & Gorgen, S. U.S. Energy Information Administration (EIA). (2013, October 28). Rethinking Rig Count As A Predictor Of Natural Gas Production. Retrieved from https://www.eia.gov/todayinenergy/detail.php?id=13551

[4] U.S. Energy Information Administration (EIA). (2020, March 19). Electricity Explained - Electricity Generation, Capacity, and Sales in the United States. Retrieved February 02, 2021, from https://www.eia.gov/energyexplained/electricity/electricity-in-the-us-generation-capacity-and-sales.php

[5] U.S. Energy Information Administration (EIA). (2020, October 9). Coal Explained Coal Prices and Outlook. Retrieved from https://www.eia.gov/energyexplained/coal/prices-and-outlook.php

[6] Tsai, K. U.S. Energy Information Administration (EIA). (2021, January 7). In 2020, U.S. Natural Gas Prices were the Lowest in Decades. Retrieved from https://www.eia.gov/todayinenergy/detail.php?id=46376

[7] Dubin, K. U.S. Energy Information Administration (EIA). (2019, December 3). U.S. Coal Plant Retirements Linked To Plants With Higher Operating Costs. Retrieved from https://www.eia.gov/todayinenergy/detail.php?id=42155

[8] Johnson, S., Chau, K. U.S. Energy Information Administration (EIA). (2019, July 26). More U.S. Coal-Fired Power Plants are Decommissioning As Retirements Continue. Retrieved from https://www.eia.gov/todayinenergy/detail.php?id=40212

[9] Morey, M., Gorski, A. U.S. Energy Information Administration (EIA). (2020, September 1). As U.S. Coal-Fired Capacity and Utilization Decline, Operators Consider Seasonal Operation. Retrieved from https://www.eia.gov/todayinenergy/detail.php?id=44976
