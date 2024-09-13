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
* **K-number Checker**:
 Checks if a python file contains a K number (**Case sensitive**), throws an error if found
 * **Ward Name Checker:**
 Reads from a `.txt` file that contains a All the ward names. If any of these ward names are in any python script the workflow will throw an error
 * **Python asserts checker:**
 This workflow was created to see if testing works in Github Actions. The workflow will run a python script that has an `assert` which will run an addition fuction that will fail. This throws an error in the workflow

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
* **R_Test**:
Contains a assert function to see how GitHub Actions handles tests found within a R file. 

---

## General Information

#### Log of data consumed per day

* **05/09/2024:** We did 34 commits, 102 workflow runs, consumed 214 minutes, 6 scripts.
* **06/09/2024:** We did 48 commits, 338 workflow runs, consumed 166 minutes, 7 scripts.

*  **11/09/2024:** We did 23 commits, 557 workflow runs, consumed 448 minutes, 8 scripts.
* **12/09/2024:** We did 7 commits, 639 workflow runs, consumed 484 minutes, 10 scripts.
---

#### Notes

* By commenting an action you avoid running executing it on a commit which will save minutes and storage

* As of right now **11/09/2024** there is no possible way to hide actions. The methods that can be used but not effective to mimic hiding actions: the use of API keys or rewriting the workflows to allow authorized users to run it manually


**Run vs Commit**
* A `run` command is used to run scripts, shell commands or any other CLI tools within a GitHub Action Workflow like installing dependencies, 

* A `commit` command refers to updating changes to the yaml.

The main difference is that `run` are usually within a workflow file and it can have multiple `run` commands in there.However a `commit` is when you either add a new file or edit previous files, which are then pushed to the repository

## Key Advice

* If you have a **.txt** file and want to read from it, GitHub Actions allows you to do so without needing to place it inside the **actions/workflow** folder. Instead, you can leave it out in the main directory if you wish to do so.

 * To ignore files the only way at the current moment of time is through the use of `.gitignore` file. There is no automated way of checking for these specified files. *For more guidance on the usage of `.gitignore` please see Tutorials and Guides  in `tutorials.md`(Link below).*

* For identification of personal information such as name, phone number and vice versa. There is not a current package from GitHub itself to help automate this process to avoid manual work. This is something which at the current moment of time must be done by an actual human. However, there is something in the works from Azure which uses Entity Congetive Recognition Service that helps identify and label these issues if a name or personal bit of information has been pushed. 

    This is current package avaliable on the GitHub MarketPlace and does require a Azure account and a subscription. For more information about this Action please use this [link](https://github.com/marketplace/actions/pii-detection)

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

#### For more information about Merging  follow this link: [Auto Merge](https://stackoverflow.com/questions/71623045/automatic-merge-after-tests-pass-using-actions)






**WARNING:**
Total billable is not equal to run time, it rounds up to the minute so if a build runs for 19 seconds it will end up being 1 minute.



#### For more information about the use of GitHub Actions  follow this link: [Tutorials](https://github.com/nottmhospitals/actions_sandbox/blob/main/tutorials.md)
