# GitHub Actions Explanations
Please check the README.md file for more information


## Actions created
* **Python Installed Check:**
 Checks if the latest version of Python is installed and if not it will install it
* **Code Formatter:** 
Formats the code using the libary **'black'**. This libary formats the code under **'PEP 8'** guidelines 
* **Test Maths Function** 
 Runs the function 'add_numbers(a, b)' to get the output of two numbers added together  
* **Test String Function**:
Runs the function 'stringFunction(message)' to get the output 
* **Checking for python dependencies**:
Checks that if the file contains the relavent libaries/packages and if not it will install those packages
* **File checker(Not working at the moment)**:
Looks for files with certain file extension like '**.csv**' and will forbid it to be applied to the repository until approved by admin. 

---

## General Information


**How Data Is Consumed?** *Last Updated(05/09/2024)*
We did 34 commits, 102 workflow runs, consumed 214 minutes, 6 scripts.

**WARNING:**
Total billable is not equal to run time, it rounds up to the minute so if a build runs for 19 seconds it will end up being 1 minute.
