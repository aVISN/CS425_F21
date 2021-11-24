# Setting up a new personal development branch
```bash
## There are a lot of unecessary steps here especially all the calls to git status
## but using lots status checks and things like fetch before pull to get a better understanding of process:
```
```bash
# make sure local is up to date with remote before create branch
git status
# see if anything updated on remote repo 
git fetch
git status
# merge updates from remote with local git
git pull
git status
```
```bash
# create a new branch
# -b option creates the branch if it does not exist and switches to it
# command is git checkout -b nameOfNewBranchHere, I am using the name "main-S" ("main-{my first initial}")
git checkout -b main-S

# check using new branch
git status
```
```bash
# create a test file and push to new branch
cd ~/hello_github
git status
vim hello_branch.txt
git status
git add .
git status
git commit -m "Testing git branch creation and use with Github"
git push --set-upstream origin main-S

# note, after setting the upstream branch, can just use git push for subsequent commits to branch
# edit hello_branch.txt
vim hello_branch.txt
git status
git add .
git status
git commit -m "Testing subsequent pushes to branch after initial upstream set "
git push 
```
```bash
# (optional) pulling from main to branch
# Example: updated repo README in main and merged updated main with my branch
# switch to main branch to update repo README
git checkout main
git status

# update repo README
cd /
vim README.md

# push to main branch
git status
git add .
git status
git commit -m "Updated to include branch creation info"
# since we have been working in different branch, be sure to set upstream with -u option
git push -u origin main
git status

# switch back to personal development branch
git checkout main-S
git status
# pull updates from main branch into local development branch
git fetch origin main
git pull origin main
git status
# push updates to development branch to remote 
git push -u origin main-S
git status
# have now merged updates from main branch into personal development branch
# does not modify/update main branch in any way
```
