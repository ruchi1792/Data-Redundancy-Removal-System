# 🚀 Data Redundancy Removal System

A serverless AWS project that detects duplicate employee records, stores only unique data, creates backups, sends notifications, and maintains logs.

---

# 📖 Project Overview

This project validates incoming employee records before storing them in the database.

If a duplicate record exists:

- ❌ The record is rejected.
- 📧 An email notification is sent using Amazon SNS.

If the record is unique:

- ✅ Stored in Amazon DynamoDB
- 📁 JSON backup stored in Amazon S3
- 📧 Success email sent using Amazon SNS
- 📊 Logs stored in Amazon CloudWatch

---

# 🛠 AWS Services Used

| Service | Purpose |
|---------|----------|
| AWS Lambda | Business Logic |
| Amazon DynamoDB | Store Employee Records |
| Amazon S3 | JSON Backup |
| Amazon SNS | Email Notifications |
| Amazon API Gateway | REST API |
| AWS IAM | Permissions |
| Amazon CloudWatch | Logs |
| Postman | API Testing |

---

# 🔄 Project Workflow

```text
User
   │
   ▼
Postman
   │
   ▼
API Gateway
   │
   ▼
AWS Lambda
   │
Validate Employee Data
   │
Check Duplicate
   │
┌───────────────┴───────────────┐
│                               │
Duplicate                    Unique
│                               │
▼                               ▼
SNS Email                 Save to DynamoDB
                                │
                                ▼
                         Backup to Amazon S3
                                │
                                ▼
                         SNS Success Email
                                │
                                ▼
                         CloudWatch Logs
```

---

# 📷 Project Screenshots

## 1. DynamoDB Table

![DynamoDB](Screenshots/1-dynamodb-table.PNG)

![DynamoDB](Screenshots/2-dynamodb-table.PNG)

---

## 2. Amazon S3 Bucket

![S3](Screenshots/3-s3-bucket.PNG)

![S3](Screenshots/4-s3-bucket.PNG)

---

## 3. Amazon SNS

![SNS](Screenshots/5-sns-topic.PNG)

![SNS](Screenshots/6-sns-topic.PNG)

![SNS](Screenshots/7-sns-topic.PNG)

---

## 4. AWS Lambda

![Lambda](Screenshots/8-lambda-function.PNG)

![Lambda](Screenshots/9-lambda-function.PNG)

![Lambda](Screenshots/10-lambda-function.PNG)

![Lambda](Screenshots/11-lambda-function.PNG)

---

## 5. API Gateway

![API Gateway](Screenshots/12-api-gateway.PNG)

![API Gateway](Screenshots/13-api-gateway.PNG)

---

## 6. Postman Testing

### Successful Record

![Postman](Screenshots/14-postman-record.PNG)

![Postman](Screenshots/15-postman-record.PNG)

### Duplicate Record

![Duplicate](Screenshots/16-postman-duplicate.PNG)

---

## 7. CloudWatch Logs

![CloudWatch](Screenshots/17-cloudwatch-logs.PNG)

![CloudWatch](Screenshots/18-cloudwatch-logs.PNG)

---

## 8. Email Notification

![Email](Screenshots/19-email-notification.PNG)

![Email](Screenshots/20-email-notification.PNG)

---

## 9. JSON Backup in Amazon S3

![JSON Backup](Screenshots/21-s3-json-file.PNG)

---

# 📤 Sample Request

```json
{
    "employeeId":"101",
    "name":"Ruchita",
    "email":"ruchita@example.com"
}
```

---

# ✅ Success Response

```json
{
    "statusCode":200,
    "body":"Record Added Successfully"
}
```

---

# ❌ Duplicate Response

```json
{
    "statusCode":400,
    "body":"Duplicate Record Found"
}
```

---

# 💻 Technologies Used

- Python
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- Amazon SNS
- Amazon API Gateway
- AWS IAM
- Amazon CloudWatch
- Postman
- Git
- GitHub

---

# 📂 Project Structure

```
Data-Redundancy-Removal-System
│
├── lambda_function.py
├── requirements.txt
├── README.md
└── Screenshots
```

---

# 👩‍💻 Author

**Ruchita Amey Deshmukh**

AWS Cloud Internship Project

CodeAlpha

---

⭐ If you found this project useful, please give it a Star!
