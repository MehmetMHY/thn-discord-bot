# Title: Quickly Setup Raspberry Pi OS For Bot
# Date:  3-9-2022

# Update & Upgrade APT:
sudo apt -y update
sudo apt -y upgrade

# Install System Packages:
sudo apt -y install vim
sudo apt -y install htop
sudo apt -y install pydf
sudo apt -y install neofetch
sudo apt -y install curl

# Install Python's Package Manager:
sudo apt -y install python3-pip

# Install thn-discord-bot Python Packages:
pip3 install beautifulsoup4
pip3 install requests
pip3 install discord.py
pip3 install python-dotenv

