# Auction Model

## Overview
In this repository I have analyzed an ecommerce dataset of a company called GalleryOne. This project is part of Stutern Inter Track project. 

## About 
In other for user to place a bid on this website, a user is required to have a minimum of 100,000 naira in his account, but in the scenario where a user is not able to fund his account at the required time and wants to join in on the bid, he should still be given access, therefore we are required to create a model that looks at the users history and data, and it should predict if the user is eligible to bid on the site without the required minimum amount in his wallet. 

### Project Structure
### data
- This folder holds the train and test data used in building the model, and they are in csv format. 

### .pkl file
- Our alogirthm is beign stored in a pickle file. This model predicts if a user is eligible to place a bid on the website on credit (Without money in his/her account)
    It returns: 
        1 - Allow to bid
        0 - Not Allowed to bid

### webapp.py
- An api that allows the backend team connect with the model to get their prediction. 
 It would require parameters such as: 
    1. `Gender` : which is a string, writter as either Male or Female 
    2. `Married` : which takes a string as it's parameter either Yes or No 
    3. `Dependents` : which takes a integer as it's parameter either runing from 1 to infinty 
    4. `Graduate` : which takes a string as it's parameter either Yes or No
    5. `Self_Employed` : which takes a string as it's parameter either Yes or No 
    6. `Income` :which takes a integer as it's parameter requesting for the users montly income
    7. `Property_Area` : which takes a string as it's parameter either restricted to states in Nigeria 
    8. `Prev_Credit_Dur` : if the user has a previously taken loan from our site, what duration was the loan
    9. `Total_Amount_Spent` : Total amount a user has spent on our site so far.
    10. `Credit_History` : Previous credit Takes an Input of Yes or No which is if the user has previously taken credit from us

    Passing all this parameters into the model, would enable the system predict what the outcome of a user is. 


 ## Installation Guide
```
git clone https://github.com/d1m3j1/project_template_stutern1.1
pip install -r requirements.txt
Deployment on heroku - https://galleryone-api.herokuapp.com/
```