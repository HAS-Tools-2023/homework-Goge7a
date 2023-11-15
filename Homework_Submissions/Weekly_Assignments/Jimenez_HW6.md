Robert Jimenez
HW6
11/6/23

1. Provide a summary of the data frames properties.
  - What are the column names? 
  - 'agency_cd', 'site_no', 'datetime', 'flow', 'code'  'year', 'month', 'day'
  - What is its index?
  - The index would be 0-12703
  - What data types do each of the columns have?
objects
2. Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.
   np.min(data['flow'])= 19
   np.max(data['flow'])= 63400
   np.mean(data['flow']) = 352.35
   np.std(data['flow']) = 1462.61
   np.percentile(data['flow'],25) = 93
   np.percentile(data['flow'],75) = 215
   or use
   data.describe()

3. Provide the same information but on a monthly basis (i.e. for all January, February, March etc). (Note: you should be able to do this with one or two lines of code)
   
data_monthly=data.groupby(["month"])[["flow"]].describe()
print(data_monthly)

         flow                                                            \
        count         mean          std    min      25%    50%      75%   
month                                                                     
1      1084.0   694.385609  2642.701653  158.0  202.000  220.0   314.00   
2       988.0   877.008097  3208.739869  136.0  199.000  238.0   612.50   
3      1085.0  1064.491244  2416.095415   97.0  180.000  378.0  1070.00   
4      1050.0   323.222857   584.313196   64.9  111.000  141.0   218.75   
5      1085.0   103.845991    49.928918   39.9   76.600   92.0   118.00   
6      1050.0    65.066762    28.191344   22.1   48.325   60.0    76.00   
7      1085.0   105.943871   214.174556   19.0   52.000   70.0   110.00   
8      1085.0   170.843687   288.914361   29.6   78.000  116.0   178.00   
9      1050.0   166.601810   274.594973   37.5   86.150  117.0   166.00   
10     1068.0   144.427903   110.761734   55.7  105.000  126.0   152.25   
11     1020.0   199.985294   225.677357  117.0  153.000  171.5   197.00   
12     1054.0   330.376660  1052.000260  153.0  189.000  203.0   225.00   

                
           max  
month           
1      63400.0  
2      61000.0  
3      42200.0  
4       4690.0  
5        546.0  
6        481.0  
...
9       5590.0  
10      1910.0  
11      4600.0  
12     28700.0 

4. Provide a table with the 5 highest and 5 lowest flow values for  the period of record. Include the date, month and flow values in your summary. (Hint: you will want to use the sort_values function for this)

data.sort_values(by="flow")
print(data[['datetime', 'month', 'flow']].head(5))
print(data[['datetime', 'month', 'flow']].tail(5))

     datetime  month   flow
0  1989-01-02      1  205.0
1  1989-01-03      1  205.0
2  1989-01-04      1  232.0
3  1989-01-05      1  259.0
4  1989-01-06      1  278.0
         datetime  month  flow
12699  2023-10-10     10  82.1
12700  2023-10-11     10  79.6
12701  2023-10-12     10  75.8
12702  2023-10-13     10  74.8
12703  2023-10-14     10  78.

5. Provide a list of historical dates with flows that are within 10% of your week 1 forecast value for the month of September. If there are none than increase the %10 window until you have at least one other  value and report the date and the new window you used

620      1990-09-14
621      1990-09-15
983      1991-09-12
995      1991-09-24
1345     1992-09-08
            ...    
12321    2022-09-27
12322    2022-09-28
12323    2022-09-29
12664    2023-09-05
12675    2023-09-16
Name: datetime, Length: 145, dtype: object