#  Phishing Website Detector

A Python machine learning project that predicts whether a website URL is phishing or safe based on key features like IP address usage, HTTPS presence, and URL length.

##  Features

- Detects phishing websites using a trained Random Forest model
- Predicts based on simple features extracted from URLs
- Prints model accuracy and results for new inputs
- Beginner-friendly ML project

##  Tech Stack

- Python
- pandas
- scikit-learn

##  Dataset

The dataset includes features:
- `Have_IP_Address` (1 if URL has IP address, 0 if domain name)
- `Have_HTTPS` (1 if it uses HTTPS, 0 otherwise)
- `URL_Length` (length of the URL)
- `Is_Phishing` (1 = phishing, 0 = safe)

##  How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/sindhureddy2204/phishing-website-detector
   cd phishing-website-detector
