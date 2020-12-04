# Project Overview

The project takes you through the creation of the environment, the delivery of the software, the automated testing of the software, using an Azure DevOps pipeline.

![App diagram](/screenshots/Projectoverviewdaigpng.png)  

[![Build Status](https://dev.azure.com/mathew0179/Ensuring-Quality-Releases-DevOps/_apis/build/status/mhaywardhill.Ensuring-Quality-Releases-DevOps?branchName=main)](https://dev.azure.com/mathew0179/Ensuring-Quality-Releases-DevOps/_build/latest?definitionId=13&branchName=main)  


## Repo Structure

<b>Automatedtesting</b>:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>jmeter</b>: JMeter (stress and endurance) Tests  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>postman</b>: Postman Integration Tests  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>selenium</b>: Selenium Functional UI Tests  
<b>devops/pipeline</b>: Azure DevOps Pipeline (YAML file)  
<b>fakerestapi</b> : App deployed to Azure WebApp  
<b>terraform</b>: Terraform (IaC) modules used to create Azure infrastructure  

