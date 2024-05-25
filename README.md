# Boba (UNDER DEVELOPMENT)

A local php development server with custom built panel. 

#
# development
windows
python -m venv venv
.\venv\Scripts\activate

mac or linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

| Requirements    | Version Number |
| --------------- | -------------- |
| Node Version    | v18.16.0 ^     |
| go Version      | 1.21.4 ^       |

#### branch rulling
short description must be separated by _  and remove the < >
```
    feature:
        feat/month/dd/yyyy/<short_description_of_feature>

    bug/
        bug/month/dd/yyyy/<short_description_of_bug>

    file_change/
        file_change/month/day/yyyy/<short_description_of_change>
```
#
# setting up github
```
    generate ssh key 
        ssh-keygen -t rsa -b 4096

    get key
        cat ~/.ssh/id_rsa.pub

    copy key and go to 
        https://github.com/settings/keys

    clone repo
        git clone <repo_name>
```
# using git

## 1: Configuring Git to Automatically Set Upstream Branches
```
    git config --global push.default current
```

## 2: Create and switch to a new branch
```
    git checkout -b <your_new_branch_name>
```
or delete
```
    git branch -d <branch_name>
```

## 3: Make changes, stage, and commit them with a message
```
    git add . or git add <file_name>
    git commit -m "Descriptive commit message about what you changed"
```

## 4: Push the new branch to the remote repository
```
    git push origin <your_new_branch_name>
```

##  1. preferably use -> pushes from the current branch
```
        git push
```

## other useful commands
```
    stash changes. hide changes
    git stash

    restore stashed (hidden) changes
    git stash apply
```

## Authors

- [Fernando](https://github.com/Fern135)
- [Paolo](https://github.com/lmaopaolo)

