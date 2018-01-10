

### Completing a numerical continuous feature
1. A simple way is to generate random numbers between mean and standard deviation.  
2. More accurate way of guessing missing values is to use other correlated features. In our case, we note correlation among Age, Gender, and Pclass. Guess Age values using median values for Age across sets of Pclass and Gender feature combinations. So, median Age for Pclass=1 and Gender=0, Pclass=1 and Gender=1.  
3. Combine methods 1 and 2. So instead of guessing age values based on median, use random numbers between mean and standard deviation, based on sets of Pclass and Gender combinations.  




