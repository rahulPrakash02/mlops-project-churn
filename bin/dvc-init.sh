# Create a 'data' directory to store the dataset files
mkdir data

# Navigate into the 'data' directory
cd data

# Initialize a new Git repository in the 'data' directory
git init

# Initialize DVC in the current directory, with the force flag to reinitialize if needed
dvc init -f

# Download the 'churn_data_collection.csv' file from a GitHub repository using curl
curl -O https://raw.githubusercontent.com/rahulPrakash02/personal-filestore/refs/heads/main/churn_data_collection.csv

# Check the DVC status to verify if there are files to track or push (initial setup status check)
dvc status

# Add the 'churn_data_collection.csv' file to DVC for tracking
dvc add churn_data_collection.csv

# Add .gitignore and the DVC tracking file to Git staging for commit
git add .gitignore churn_data_collection.csv.dvc

# Commit the changes to Git with a message indicating the initial data setup
git commit -m "Initial Data"

# Add a DVC remote named 'storage' and set its path to '/tmp/dvc-storage', making it the default
dvc remote add -d storage /tmp/dvc-storage

# Push the tracked data to the remote storage location set in the previous step
dvc push

# Navigate back to the root directory
cd ..
