# <img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="100">  Daily Motivation Serverless Project
A lightweight cloud-powered system that sends a motivational quote to your email every morning using AWS Lambda, S3, SNS, and EventBridge.

---

##  Why This Project? (Mental Health) 
Small positive reminders can improve mood, reduce stress, and support healthier thinking patterns.  
This project delivers a simple daily boost to help build motivation and emotional balance.

---

##  What This Project Does
- Stores motivational quotes in an S3 JSON file  
- Uses Lambda to pick a random quote  
- Sends it to your email via SNS  
- Runs automatically every day using an EventBridge cron rule  

---

##  AWS Services Used
- **S3** — stores `quotes.json`  
- **SNS** — sends email notifications  
- **Lambda** — processes and delivers the quote  
- **IAM** — provides necessary permissions  
- **EventBridge** — schedules daily execution  
- **CloudWatch** — logging & monitoring  

---
##  Quick Setup Steps
1. Create S3 bucket → upload `quotes.json`  
2. Create SNS topic → subscribe email → confirm subscription  
3. Create Lambda function (Python 3.x)  
4. Attach `AmazonS3ReadOnlyAccess` + `AmazonSNSFullAccess` to Lambda role  
5. Add environment variables (bucket, key, SNS topic ARN)  
6. Deploy Lambda → test manually  
7. Create EventBridge rule → cron → choose Lambda target  
8. Receive your quote daily at 8:00 AM IST  

---

##  Learning Outcomes
- Build an end-to-end serverless workflow  
- Integrate AWS services effectively  
- Understand permissions, triggers, and monitoring  
- Create automation using real cloud tools  
- Deploy a practical, wellness-focused application  

---

##  Why This Is Useful
- Encourages positive daily habits  
- Demonstrates real cloud automation skills  
- Extremely low cost and simple to maintain  

---
