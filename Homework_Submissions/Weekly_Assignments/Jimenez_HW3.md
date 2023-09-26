Robert Jimenez HW3 9/26/23
1. Describe the variables `flow`, `year`, `month`, and `day`. What type of objects are they? What data types are they composed of? How long are they? 
   1. The objects are lists. The length is 12668 for each one. 
2. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
   1. 675
   2. 675/1265 * 100 = 53.4%
3. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
   1. @2000 457/598 * 100 = 76.4%
   2. @2010 376/635 * 100 = 59.2%
4. How does the daily flow generally change from the first half of September to the second?
   I set the parameter of the daily flow being greater than 120. The first half of september when day[i]<=15 has 495 counts where the flow is greater than 120. The second half of september when day is day[i] > 15 has 418 counts where flow is greater than 120. This means that the flow in the first half of september is typically greater than the flow of the second half. 

../../Homework_Working/week3_lists_starter.py