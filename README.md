# UltimateInstragramFollower
Python script for automatic account follows based on Selenium
# Installation
```
cd UltimateInstagramFollower\install
pip install -r requirements.txt
python ../UltimateInstagramFollower.py
```
# Running the script

Option 1:
Simple credentials input and default values
Steps:
1. Run the script
2. Press [1]
3. Enter your Username/Email
4. Enter your Password
<br>
And you're done, let the browser do the rest.

Option 2:
Credentials and values from file
Steps:
1. Open the file `preferences.txt` with any text editor and edit the values to your liking

```
1st line: Username
2nd line: Password
3rd line: List of accounts to gather followers from
Tip: The list has to be formatted like this: ["account1", "account2", "account3"]
4th line: Minimum delay to execute an operation
5th line: Maximum delay to execute an operation
6th line: Number of accounts to follow on execution
```

2. Save the file
3. Run the script
4. Press [2]
<br>
And you're done, let the browser do the rest.

# Known Issues
1. The script stops whenever you try to follow more than 13 accounts
