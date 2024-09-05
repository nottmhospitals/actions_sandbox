
## General Information


* **How Data Is Consumed?** *Last Updated(05/09/2024)*
We did 34 commits, 102 workflow runs, consumed 214 minutes, 6 scripts.

* By commenting an action you avoid running executing it on a commit which will save minutes and storage


**Run vs Commit**
* A `run` command is used to run scripts, shell commands or any other CLI tools within a GitHub Action Workflow like installing dependencies, 

* A `commit` command refers to updating changes to the yaml.

The main difference is that `run` are usually within a workflow file and it can have multiple `run` commands in there.However a `commit` is when you either add a new file or edit previous files, which are then pushed to the repository

## Key Advice
* If you have commented out code within an action it will not show the action being ran in the image below but the action will still be ran as a workflow file has been created. To not want a workflow file to be ran. You must **DELETE** the file from under the 'Actions' tab. 

![image](https://hackmd.io/_uploads/HyBaOEDhR.png)


**WARNING:**
Total billable is not equal to run time, it rounds up to the minute so if a build runs for 19 seconds it will end up being 1 minute.
