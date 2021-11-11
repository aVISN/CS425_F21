File to test git set up. 


Git/Github setup: 

apt install git

git config --global user.name "Sarah Skidmore"
git config --global user.email "obeytheviszla@gmail.com"
# check
git config --global user.name
git congig --global user.email

# check for ssh key
ls -al ~/.ssh
# generate ssh key pair
ssh-keygen -t ed25519 -C "obeytheviszla@gmail.com"
# start ssh-agent
eval "$(ssh-agent -s)"
# add key to ssh-agent
ssh-add ~/.ssh/id_ed25519
# copy public key to github settings
cat ~/.ssh/id_ed25519.pub
# test SSH connection to GitHub
ssh -T git@github.com

cd ~
mkdir hello_github
vim hello_github/hello_git.txt
# add text and save: 
File to test git set up. 

cd /
# initialize git 
git init
# check
git status
# create .gitignore
vim .gitignore
	# add text and save: 
	# ignore root files and root directories
	/*
	/*/
	# allow root's home dir
	!/root/
	# but not the Desktop in root's home dir
	/root/Desktop
	# or any dot files in root's home dir
	/root/.*
git add .
git status
git commit -m "Initial commit, testing git and github"
git status
git branch -M main
git status
git remote add origin git@github.com:aVISN/CS425_F21.git
git push -u origin main
# check github online repo

# add another file
vim hello_github/README.txt
# (created this text file)

# add file to staging
git add .
# check
git status
# commit file
git commit -m "Added README on git setup"
# check
git status
# push (don't need to add origin this time and it is already set as upstream after initial commit above)
git push
# check github online repo

