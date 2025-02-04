# NEAR Validator Ping Script Setup Guide
### if you on testnet, you have to send ping to pool every epoch.
### but if you on mainnet, you don't have to send. metapool will do it for you.

### 1. install required packages
```
apt install python3 python3-pip -y
```
### 2. create working directory
```
mkdir -p ~/near-validator
cd ~/near-validator
```
### 3. create a new file named like ping_validator.py and add the code.
```
vi ping_validator.py
```
### 4. setup screen session
screen allows the script to keep running even if SSH connection is lost.
```
# install screen
apt install screen -y

# start new screen session
screen -S ping_node
```
### 5. run script.
```
python ping_validator.py
```
### if success run script, you can see like this screenshot.
<br/>
<img width="509" alt="image" src="https://github.com/user-attachments/assets/4c692b63-4ed8-4064-bb6b-eb4d989dfc7f" />
