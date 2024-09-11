#    GitHub Actions
###### **Authors**: Ziad Ahmed & Shivam Missar
###### **Emails**: ziad.ahmed@nhs.net | shivam.missar@nuh.nhs.uk
###### **Date**: 04/09/2024

## Key terms:
| **Key Terms** |**Definition** | 
| -------- | -------- |
| **Cache**     |  A cache is a type of action that stores files that can speed up workflows by reusing data from previous runs. For example when project dependencies are installed, the cache would store those dependencies so that the following jobs would skip the installation process, saving time and cost|
| **Artifact**     | This refers to any files or data generated during a workflow run, results or build outputs(e.g test reports). Artifacts are stored temporarily so they can be used across different jobs or downloaded after the workflow finishes|
| **Repository**    | A place where all your project files and code are stored and managed. |
|**Workflow** |A set of automated tasks that run in sequence to complete a process in GitHub Actions|
| **Event**    | An action that triggers a workflow, like saving changes to your code.|
| **@v3/4/5/...**    | Used for defining which version your GitHub repository is in|
| **Job**     | is a set of steps in a GitHub Actions workflow that executes on a runner(hosted-server). Each job runs in its own environment(on a virtual machine) and can run tasks like testing code and building applications. Jobs in a workflow can run in parallel or sequentially, depending on how they are configured.|
| **YAML**    | Yet Another Markup Language which is a syntax used for writing GitHub Actions |
|**Concurrent Jobs**| In GitHub Actions this refers to the number of jobs the can run simultaneously within an organization's workflow



## What is GitHub Actions?
GitHub Actions is a tool that helps automate tasks in software development. For instance, when creating a website or web app, developers usually need to manually, test to ensure everything works,publish new versions and perform other repetitive tasks.

However, with GitHub Actions, these tasks are done automatically. It's like an additional helper who checks the code, checks that everything works, and publishes an updated version online if everything looks in check. Using GitHub Actions helps save time and reduces the chances of making a mistake as everything is automated.

###### For more information about GitHub Actions follow this link: [GitHub Documentation](https://docs.github.com/en/actions)

---
## How they are applied?

To create GitHub Actions, it uses something called 'YAML' which is used for defining workflows within GitHub Actions. In GitHub Actions, 'YAML' files are used to set up automated process that run on certain triggers like for example saving a change to your project. 

GitHub Actions can be applied in a variety of ways, which are listed below:

**1. Automated Testing:** 
Every time a developer uploads new code, GitHub Actions can automatically check for errors. For example, in mobile app development, whenever a new feature or fix is added, GitHub Actions will run tests to ensure that the entire application continues to function correctly.

**2. Continuous Integration (CI):**
When multiple team members submit new code, GitHub Actions automatically combines their changes with the existing project. It then tests everything together to ensure that the app continues to work correctly as new code is added. This helps to catch and fix issues that might occur when integrating different parts of the code
        
**3. Continuous Deployment (CD):**
GitHub Actions helps with Continuous Deployment by automatically updating a website with new changes. For instance, when the developer make updates to a website, GitHub Actions will apply these updates to the live site. This means that new features, bug fixes, or other changes become available to users right after the code is tested and confirmed to be working properly.

**4. Automating Routine Tasks:**
Managing a large project with many contributors requires tracking various issues, improvements, and bugs. GitHub Actions can automate these routine tasks, such as assigning issues to the right team members or closing outdated issues. This automation helps keep things organized without manual effort. 

**5. Code Quality Checks:** 
When new code is added, GitHub Actions reviews it for quality. It checks for common mistakes, errors, inconsistent formatting, and other potential issues. This helps ensure that the code is clean and functional before it is integrated into the project.




---
## Pricing and limitation on organisation accounts.
GitHub Actions is included is included with GitHub but its usage and cost may vary based on the type of account you have (personal or organisation) and the plan you choose.

---
The breakdown of pricing and limitations for organisations accounts as of 2024:
#### Free Tier(For Organisations):
* **Included minutes**: 2,000 per month for Windows and Ubuntu but for macOS you will need to pay for usage
* **Included storage**: 500 MB is provided

---
#### GitHub Paid Plans For Organisations:
If your organisation is on a paid plan like **'GitHub Team'** or **'GitHub Enterprise'**, you'll receive more minutes and storage

**GitHub Team**: 
* **Included minutes**: 3000 minutes per month
* **Included storage**: 2 GB included

**GitHub Enterprise**:
* **Included minutes**: 50,000 minutes per month
* **Included storage**: 50 GB included

---
#### General Limitations:
*  Each task or job in a workflow can run for a maximum of 6 hours , if exceeded the job will be terminated.

* The number of concurrent jobs are based on the plan.  Free Tier are limited to 20, GitHub Team is 60 and GitHub Enterprise is 180 concurrent jobs.

* The duration for your workflows can only run for a maximum of 35 days
---

#### Billing Considerations:
* The minutes and storage space (artifacts and cache) are included in your plan and are shared across all repositories in your organisation

* The billing cycle is based on the total number of minutes  and storage your organisation uses in a month. If you go beyond that you'll be charged extra at the end of each billing cycle

* To avoid unexpected costs your usage can be monitored in the ==settings== tab under ==Billing & plans== 


---
#### Additional Clarifications

#####  **How Many Minutes Do Jobs Use?:**
The number of minutes a job takes depends on the type of tasks your doing. Small tasks, like running basic tests, might only need a few minutes. Larger tasks, like building large applications might take more time.

###### Examples in R and Python:
* A simple "Hello World" script in Python would take less than 1 minute to run.
* Running a small Python project with basic unit tests might take 3-5 minutes, including installing a few dependencies using `pip`.
* A basic R script printing "Hello World" would take less than 1 minute.
* unning tests for a small R project with several libraries installed (like `ggplot2`, `dplyr`, etc.) could take around 3-6 minutes, including installation of dependencies and running tests.

#####  **How Much Storage Do I Need?:** 
In the '**Free Tier**', you get 500MB of storage which may be enough for smaller projects.  How many repositories this fits depends on how big your files are (code, artifacts, etc.). For larger projects with many files you may need to upgrade to a paid plan for more storage.
###### Examples in R and Python:
Using Python to plot a simple dataset using `matplotlib` and `pandas`. The project includes basic scripts for data loading, visualization, and some testing.
* **Code and small artifacts:** 50-100 MB.
* **Cached dependencies:** 50-100 MB (libraries like `numpy` and `matplotlib`).

Using R to plot a dataset with `ggplot2` and performing some basic data manipulation using `dplyr`. The project might involve loading a CSV file and visualizing the data.
* **Code and plot artifacts:** 50-150 MB.
* **Cached dependencies:** 50-100 MB (libraries like `ggplot2`, `dplyr`)



###### For more information about Billing for GitHub Actions follow this link: [Billing for GitHub Actions](https://docs.github.com/en/actions/administering-github-actions/usage-limits-billing-and-administration) 


---

## Case examples.
When a programmer makes changes to their project and saves them, GitHub Actions can automatically check various aspects to ensure everything is working well. GitHub Actions uses YAML files to define these automated processes. Below are examples demonstrating how GitHub Actions can be used for testing, integration, deployment, code quality checks, and automating routine tasks.

For more information about GitHub Actions and case examples, visit: [GitHub Actions Use Cases](https://docs.github.com/en/actions/use-cases-and-examles/creating-an-example-workflow).

#### Common Elements
For each case, the following YAML syntax elements are common:

* **name**: Labels the workflow or job.
* **on**: Specifies the event that triggers the workflow.
* **jobs**: Contains the tasks to be performed.
* **runs**-on: Defines the operating system for the job.
* **steps**: Lists individual tasks within a job.
* **uses**: Refers to pre-made actions.
* **run**: Executes commands directly.


#### **1. Automatic Testing**
When you save changes to your project, GitHub Actions can automatically test your application to ensure it works correctly. 

##### Code Explaination:
* **'name'**: This labels the task as "Test Recipe App" so you know what this process is for.
* **'on: [push]'**: This means the task starts automatically whenever you save new changes to your project.
* **'jobs'**: Lists what needs to be done in this task.
* **'test'**: This is a name for the specific job, which in this case is "test."
* **'runs-on'**: ubuntu-latest: This means the job will run on the latest version of Ubuntu, which is a type of computer system.
* **'steps'**: Details each action that will be performed:
* **'uses'**: actions/checkout@v4: This gets the latest version of your project code.
* **'uses'**: 'actions/setup-node@v4': This sets up a specific tool (Node.js) needed to run the tests.
* with: 'node-version': '16': Specifies which version of Node.js to use (version 16).
* **'run'**: 'npm install': This installs any additional tools or libraries needed for the project.
* '**run**': npm test: Runs the tests to check if everything in your project is working correctly.


```
name: Test Recipe App

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '16'
      - run: npm install
      - run: npm test
```
#### **2. Continuous Integration (CI)**
GitHub Actions can automatically integrate new code with existing code and check for issues every time code is pushed.

##### Code Explaination:

* **'build-and-test'**: Names this job "build-and-test."
* **'runs-on'**: ubuntu-latest: Runs the job on the latest version of Ubuntu.
* **'uses'**: 'actions/checkout@v4': Retrieves the latest version of your project code.
* **'uses'**: actions/setup-node@v4: Sets up Node.js, a tool needed for this project.
* **'with'**: node-version: '18': Specifies using Node.js version 18.
* **'run'**: 'npm install': Installs project dependencies.
* **'run'**: 'npm run build': Builds the project to prepare it for use.
* **'run'**: 'npm test': Runs tests to ensure everything works together.


```
name: CI for Messaging App

on: [push]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
      - run: npm install
      - run: npm run build
      - run: npm test

```


3. Continuous Deployment (CD)
Every time you push updates, GitHub Actions can automatically deploy the latest version of your project to a live server.


##### Code Explaination:
* **'deploy'**: Names the job "deploy."
* **'runs-on'**: ubuntu-latest: Runs the job on the latest version of Ubuntu.
* **'run'**: npm install: Installs the necessary tools and libraries.
* **'run'**: npm run build: Builds the project to prepare it for deployment.
* **'run'**: scp -r ./build user@server:/path/to/blog: Copies the built project to a live server so it’s available on the web.



```
name: Deploy Blog

on: [push]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
      - run: npm install
      - run: npm run build
      - name: Deploy to Server
        run: |
          scp -r ./build user@server:/path/to/blog

```


4. Code Quality Checks
GitHub Actions can automatically check your code for style issues and errors whenever you save changes.

##### Code Explaination:

* **'lint:'**: Names the job "lint," which means checking code quality.
* **'runs-on'**: 'ubuntu-latest': Runs the job on the latest Ubuntu.
* **'run'**: 'npm install': Installs the necessary tools and libraries.
* **'run'**: 'npm run lint': Checks the code for style issues and errors.

```
name: Code Quality Checks

on: [push]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '14'
      - run: npm install
      - run: npm run lint

```

5. Automating Routine Tasks
GitHub Actions can automate routine tasks, such as managing issues, based on specific events.

##### Code Explaination:

* **'issues:'**: Tells GitHub Actions to start this process for new issues.
* **'label-issues:'**: Names the job "label-issues," which means adding labels to issues.
* **'with:'** script:: Contains the script that labels new issues based on their title (e.g., "bug" or "feature")


```
name: Automate Issue Management

on:
  issues:
    types: [opened]

jobs:
  label-issues:
    runs-on: ubuntu-latest
    steps:
      - name: Label New Issues
        uses: actions/github-script@v6
        with:
          script: |
            const issue = context.issue;
            const label = issue.title.includes('bug') ? 'bug' : 'feature';
            await github.issues.addLabels({
              ...context.repo,
              issue_number: issue.number,
              labels: [label]
            });

```

---


## Does it change regarding R and Python/other languages.


GitHub Actions works the same way regardless of the programming language your using , whether its Python,R, JavaScript or any other language. However configuring the workflow and the types of files managed during the process differ based on the language.

**Configuring Workflows For Different Languages(Python and R):**
##### Setting The Enviroments:
For each language, the workflow file (usually a `.yml` file) needs to define how to set up the environment where your code will run. This may include specifying the operating system (Windows, Ubuntu, or macOS) and installing the necessary dependencies.

###### Example for Python:
* **'actions/checkout@v2:'**: Takes out the code from GitHub repository so it can be used in the workflow.
* **'actions/setup-python@v2:'**: Installs Python in the workflow in this case Python version 3.
* **'run: pip install -r requirements.txt'** installs all the necessary Python libraries listed in the `requirements.txt` file using the `pip install` command.
```
steps:
  - uses: actions/checkout@v2
  - name: Set up Python
    uses: actions/setup-python@v2
    with:
      python-version: '3.x'
  - name: Install dependencies
    run: pip install -r requirements.txt
```

###### Example for R:

* This is similar to the above example except when the dependencies for R is installed it installs the remotes package, and then it uses `remotes::install_deps()` to install the rest of the required packages listed in your project files (like `DESCRIPTION`).

```
steps:
  - uses: actions/checkout@v2
  - name: Set up R
    uses: r-lib/actions/setup-r@v2
  - name: Install R dependencies
    run: |
      install.packages('remotes')
      remotes::install_deps()

```
#### Caching Dependencies
Once the dependencies are installed the cache action is called to save them for speeding up subsequent workflows, especially in large projects.

###### Example for Python:
* **'actions/cache@v2:'**: Starts the Caching process
* **'path:'**: Describes the path were the dependencies would be stored in this case `~/.cache/pip`.
* **Key:** Generates a unique key based on the operating system and the `requirements.txt` file. If the `requirements.txt` file hasn't changed, it will reuse the cache, speeding up the workflow.
* **'restore-keys'** give the workflow a second chance to find and use an existing cache, even if it’s not an exact match, to save time.

```
- name: Cache pip dependencies
  uses: actions/cache@v2
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```
###### Example for R:
* This is similar to the above example except we are caching the dependencies for R.
```
- name: Cache R libraries
  uses: actions/cache@v2
  with:
    path: ${{ env.R_LIBS_USER }}
    key: ${{ runner.os }}-r-${{ hashFiles('DESCRIPTION') }}
```
#### Type Of Artifacts Generated:
These files may vary based on the language:

* **Python**: These files includes test reports,build logs and plots.
* **R**: These files includes report outputs like PDF files and data analysis reports




---
## Pre-Coded Solutions?
 
 #### What Are They?

Pre-coded solutions are like ready-made tools or instructions that someone else has already created. Instead of building something from scratch, you can use these pre-made solutions to save time and effort.
 
#### Where can you find these Pre-coded Solutions?
You can find pre-coded solutions in the GitHub Marketplace. This is an online store where developers share their tools and solutions. In the GitHub Marketplace, you can browse through a wide variety of tools that can help with different tasks, such as:

* **Automated Testing Tools:** To automatically check if your code works correctly.
* **Deployment Helpers:** To automatically update your website or app whenever changes are made.
* **Code Quality Checkers:** To review your code for mistakes or improvements.

Seen in the figure below, it shows how GitHub Marketplace looks like with access to thousands of different actions to best benefit you. To access GitHub Marketplace visit this link: [GitHub Marketplaces](https://github.com/marketplace?type=actions)  

### How to Add Pre-Coded Solutions from GitHub Marketplace
In order to add Actions from the GitHub MarketPlace below provides a step by step guide on how to do so. This is then followed by an actual example following these listed steps. 

#### Step 1: Find a Pre-Coded Solution:

**Visit the GitHub Marketplace and search for the right action:**
Use the search bar to find an Action that suits your needs. For example, if you want to automatically test your code, you can search for “testing” or “CI.”

**Select an Action:**
Click on an Action that looks helpful. On the Action’s page, you’ll see a description of what it does, instructions on how to use it, and the exact code snippet you’ll need to add to your project. For example, to add this 'GoSec Security Checker' the user would need to click 'Use latest version' 
![image](https://hackmd.io/_uploads/S1SGDJUhR.png)
![image](https://hackmd.io/_uploads/B12OPkL3A.png)

#### Step 2: Add the Action to Your Project

**Copy the Code Snippet:**
On the Action’s page, you’ll find a code snippet in YAML format. This snippet tells GitHub Actions to use that particular Action in your project. Copy this snippet.

**Create or Edit Your YAML File:**
Go to your GitHub repository and look for a folder named '.github/workflows'. If it doesn’t exist, you can create it.Inside this folder, create a new file with a .yml extension (e.g., main.yml). This file will contain the instructions for GitHub Actions.

**Paste the Snippet into Your YAML File:**
Open the '.yml' file in your repository and paste the code snippet you copied earlier.

**Customize the YAML File:**
You may need to adjust the snippet to fit your specific needs. For example, you might need to specify the version of the software you’re using or set specific options. The Action’s page on GitHub Marketplace usually provides instructions on how to customize it.


##### How to add 'Gosec Security Checker'

Below provides a walk-through how to add the 'Gosec Security Checker' from GitHub Marketplace to your project. 'Gosec Security Checker'  is a tool that automatically scans your Go code for security issues.

### Step 1: Find the 'Gosec Security Checker' Action on GitHub Marketplace

**1. Visit the GitHub Marketplace**

**2. Search for 'Gosec'**
Use the search bar at the top and type “Gosec.” This will bring up the 'Gosec Security Checker' action.

**3. Select the 'Gosec Security Checker' Action:**
Click on the 'Gosec Security Checker' Action in the search results. You’ll be taken to a page that provides a description of the tool, what it does, and how to use it.

### Step 2: Add the 'Gosec Security Checker' Action to Your Project

**1. Copy the YAML Snippet:**
On the 'Gosec Security Checker' Action page, there will be a section with a code snippet in YAML format. This is the code you need to add to your project to start using 'Gosec Security Checker'.
Here's an example snippet:

```
name: Gosec Security Checker
uses: securego/gose@v2.20.0
```
**2. Create or Edit Your YAML File:**
In your GitHub repository, navigate to the .github/workflows directory. If this directory doesn’t exist, create it.Create a new file in this directory, such as gosec.yml, and open it for editing.

**3. Paste the YAML Snippet:**
Paste the 'Gosec Security Checker' snippet you copied into this file.
Customize if Necessary:
The provided snippet should work as is, but you can customize it based on your project’s needs. For instance, you can adjust the Go version or add more steps if required.
Step 3: Save and Push Your Changes

**4. Commit Your Changes:**
After pasting the YAML code into the file, save the file and commit it to your repository. This records your changes.


