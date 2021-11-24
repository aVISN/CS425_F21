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

