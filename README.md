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
    -`Gender` : which is a string, writter as either Male or Female 
    -`Married` : which takes a string as it's parameter either Yes or No 
    -`Dependents` : which takes a integer as it's parameter either runing from 1 to infinty 
    -`Graduate` : which takes a string as it's parameter either Yes or No
    -`Self_Employed` : which takes a string as it's parameter either Yes or No 
    -`Income` :which takes a integer as it's parameter requesting for the users montly income
    -`Property_Area` : which takes a string as it's parameter either restricted to states in Nigeria 
    -`Prev_Credit_Dur` : if the user has a previously taken loan from our site, what duration was the loan
    -`Total_Amount_Spent` : Total amount a user has spent on our site so far.
    -`Credit_History` : Not for the user to imput but we are to say decide for now, we leave it at 1 or 0

    Passing all this parameters into the model, would enable the system predict what the outcome of a user is. 


 ## Installation Guide
```
git clone https://github.com/d1m3j1/project_template_stutern1.1/tree/heroku
pip install -r requirements.txt
Deployment on heroku - https://galleryone-api.herokuapp.com/
```