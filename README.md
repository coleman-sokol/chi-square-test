# Chi-Squared Test
The [Chi-Squared Test](https://en.wikipedia.org/wiki/Chi-squared_test "Chi-Squared Test on Wikipedia") is a test used to find out whether or not statistical information could be considered "random" to a significant degree.

# An Explanation of This Program
### Purpose
This program's main purpose is to perform the chi-squared test, and output a result, given data.

### Start
On starting the program, the user is prompted to enter the amount of degrees of freedom that the dataset uses. If this number is less than or equal to zero, the program quits.
The user is then prompted to either enter some part of the word "limit" to enter Limit Mode, or anything else to enter Normal Mode.

### Normal Mode
In Normal Mode, the user is prompted to input an amount (degrees of freedom + 1) of expected, and outcome values.
The program then prints to the screen the number returned by the Chi-Squared, and whether or not the results can be considered "random."

### Limit Mode
In Limit Mode, the user enters an expected value.
The program then prints to the screen the upper and lower limits which data points must be between in order to be considered "random."

### Once Completed
Once answers have been returned in either Normal Mode or Limit Mode, the program goes back to the **_Start_**.
