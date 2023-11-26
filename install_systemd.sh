#!/bin/bash

# Define the current directory and crontab file
CURRENT_DIR=$(pwd)
USERNAME=$(whoami)
CRONTAB_FILE="/etc/cron.d/n2d"

# Initialize Miniconda and create the n2d environment
# Check if the environment already exists
if conda env list | grep -q "^n2d"; then
    echo "Conda environment 'n2d' already exists."
else
    echo "Creating Conda environment 'n2d'..."
    conda create -n n2d python=3.8 -y
    conda init bash
fi
/home/$USERNAME/miniconda3/envs/n2d/bin/pip install -r ./notion2discord/requirements.txt

# Create the crontab file to run main.py every minute
# Check if the crontab file exists and create or update it
if [ -f "$CRONTAB_FILE" ]; then
    echo "Crontab file already exists. Updating..."
    echo "* * * * * root cd $CURRENT_DIR/notion2discord/ && /home/$USERNAME/miniconda3/envs/n2d/bin/python main.py >> /var/log/n2d.log 2>&1" | sudo tee -a "$CRONTAB_FILE" > /dev/null
else
    echo "Creating crontab file..."
    echo "* * * * * root cd $CURRENT_DIR/notion2discord/ && /home/$USERNAME/miniconda3/envs/n2d/bin/python main.py >> /var/log/n2d.log 2>&1" | sudo tee "$CRONTAB_FILE" > /dev/null
fi

# Set the correct permissions for the crontab file
sudo chmod 0644 "$CRONTAB_FILE"

# Reload cron to apply new crontab file
sudo systemctl restart cron

# Print conclusion
cat << EOF



<!> INSTALLATION COMPLETE <!>

The script has installed all of the necessary modules, binaries,
databases, and packages necessary to run notion2discord every minute. For any
issues with the cron job, please diagnose with the following commands:

>> sudo systemctl status cron.service     # Get status of the cron service
>> sudo systemctl restart cron.service    # Restart the cron service
>> sudo systemctl stop cron.service       # Stop the cron service
>> sudo systemctl start cron.service      # Start the cron service if stopped
>> cat /var/log/n2d.log                   # View output from the cron job
>> cat /etc/cron.d/n2d                    # View output from the cron job


EOF