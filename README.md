# GitHub Actions Explanations
Please check the README.txt file for more information


## Actions created
#### Python Actions:
* **Python Installed Check:**
 Checks if the latest version of Python is installed and if not it will install it
* **Code Formatter:** 
Formats the code using the libary **'black'**. This libary formats the code under **'PEP 8'** guidelines 
* **Test Maths Function** 
 Runs the function **'add_numbers(a, b)'** to get the output of two numbers added together  
* **Test String Function**:
Runs the function **'stringFunction(message)'** to get the output 
* **Checking for python dependencies**:
Checks that if the file contains the relavent libaries/packages and if not it will install those packages
* **File checker(Not working at the moment)**:
Looks for files with certain file extension like '**.csv**' and will forbid it to be applied to the repository until approved by admin. 

#### R Actions:
* **R Installed Check:**
 Checks if the latest version of R is installed and if not it will install it
* **R Code Styler:** 
Formats the code using the libary **'styler'**. This libary formats the code under **'tidyverse'** guidelines 
* **R Test Maths Function** 
 Runs the function **'addFunction <- function(a,b)'** to get the output of two numbers added together  
* **R Test String Function**:
Runs the function **'stringFunction(message)'** to get the output 
* **Checking for R dependencies**:
Checks that if the file contains the relavent libaries/packages and if not it will install those packages



---

## General Information


* **A log how much data has been consumed per day** 
* **05/09/2024:** We did 34 commits, 102 workflow runs, consumed 214 minutes, 6 scripts.
* **06/09/2024:** We did 48 commits, 338 workflow runs, consumed 166 minutes, 7 scripts.

* By commenting an action you avoid running executing it on a commit which will save minutes and storage


**Run vs Commit**
* A `run` command is used to run scripts, shell commands or any other CLI tools within a GitHub Action Workflow like installing dependencies, 

* A `commit` command refers to updating changes to the yaml.

The main difference is that `run` are usually within a workflow file and it can have multiple `run` commands in there.However a `commit` is when you either add a new file or edit previous files, which are then pushed to the repository

## Key Advice
* If you have commented out code within an action it will not show the action being ran in the image below but the action will still be ran as a workflow file has been created. To not want a workflow file to be ran. You must **DELETE** the file from under the 'Actions' tab. 

![image](https://hackmd.io/_uploads/HyBaOEDhR.png)

The action will still show up here within the image below as being ran:
![image](https://hackmd.io/_uploads/ryssKNPhR.png)


* If you want actions to run without pushes from certain files. You can use the example provided below to ignore files from triggering actions:
```
on:
  push:
    branches:
      - master
    paths-ignore:
      - '**/README.md'
```

### How to Enforce Auto-Merge based off Action Passing 

1.  Enable auto-merge for your repository, see the Github documentation here

2. Go to the branch protection rules of your repository. To get there: Go to your repository settings then go to **"branches"** in the section **"Code and automation"**

4. Add or edit the branch protection rules for the branch you want to merge your pull requests into, so e.g. main or master

4. Activate **"Require status checks to pass before merging"**

5. Type each name of your (Github Actions) workflows into the free text field with the description **"Search for status checks in the last week of this repository"**

6. Then auto-merging should be possible.

###### For more information about Merging  follow this link: [Auto Merge](https://stackoverflow.com/questions/71623045/automatic-merge-after-tests-pass-using-actions)



**WARNING:**
Total billable is not equal to run time, it rounds up to the minute so if a build runs for 19 seconds it will end up being 1 minute.

