# Boba (UNDER DEVELOPMENT)

A local php development server with custom built panel. 

<!-- dev -->
windows
python -m venv venv
.\venv\Scripts\activate

mac or linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

branch rulling
    <!-- short description must be separated by _ -->
    feature:
        f/month/dd/yyy/<short_description_of_feature>

    bug/
        b/month/dd/yyy/<short_description_of_bug>

    file_change/
        fs/month/day/yyy/<short_description_of_change>


<!-- using git -->
# step 1: Configuring Git to Automatically Set Upstream Branches
git config --global push.default current

# Step 2: Create and switch to a new branch
git checkout -b <your_new_branch_name>

# Step 3: Make changes, stage, and commit them with a message
git add . or git add <file_name>
git commit -m "Descriptive commit message about what you changed"

# Step 4: Push the new branch to the remote repository
git push origin <your_new_branch_name>

# preferably use
# pushes from the current branch
git push

# stash changes
git stash

# restore stashed changes
git stash apply
