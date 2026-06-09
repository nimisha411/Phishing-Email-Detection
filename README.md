# Phishing Email Detection

## Overview

This project detects phishing emails using suspicious keyword analysis and risk scoring. It helps identify potentially malicious emails that attempt to steal sensitive information.

## Features

* Suspicious keyword detection
* URL detection
* Risk score calculation
* Phishing/Legitimate email classification

## Technologies Used

* Python
* Regular Expressions (re)

## How It Works

* Each suspicious keyword adds 1 point to the risk score.
* URLs add 2 points to the risk score.
* If the total score is 3 or more, the email is classified as Phishing.

## Example

Input:
verify your bank account immediately

Output:
Risk Score: 4
Result: PHISHING EMAIL
Suspicious Keywords: ['verify', 'bank', 'account', 'immediately']

## Run the Project

python phishing_detection.py

## Phishing Attack

![Phishing Attack](image/Phishing-attack.png)

## Author

Nimisha Sharad Mali
