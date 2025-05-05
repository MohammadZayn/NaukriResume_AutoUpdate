#  Naukri Auto Resume Uploader

A Python automation script that logs into [Naukri.com](https://www.naukri.com/), navigates to the profile section, and uploads the latest resume automatically. This project uses **Selenium WebDriver** for browser automation and **Jenkins** for scheduling/resume update automation.

---

##  Features

- Secure login using environment variables  
- Automatically updates resume on Naukri profile  
- Headless browser support  
- Jenkins-compatible for daily/weekly automated runs  
- Email notification or console output for success/failure  

---

## 🛠️ Tech Stack

- **Python 3.x**  
- **Selenium WebDriver**  
- **ChromeDriver**  
- **Jenkins** (for CI/CD and scheduling)  
- Optional: **dotenv** for environment variable management  

---

## 📁 Project Structure
│
├── main.py # Main automation script
├── config.env # (Optional) Environment variables
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── jenkins_job_config.xml # Jenkins pipeline (optional)


---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/MohammadZayn/naukri_auto_upload.git
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
Create a .env file or set these variables in Jenkins:
```bash
NAUKRI_USERNAME=your_email@example.com
NAUKRI_PASSWORD=your_password
RESUME_PATH=/full/path/to/resume.pdf
```
Or use a .env file with the python-dotenv package.

### 4. Run the Script
```bash
python main.py
```


### 🤖 Jenkins Configuration
#### Step 1: Create a Jenkins Job
Set up a Freestyle Project or Pipeline Job

Add a build step: Execute Shell or Execute Python Script

#### Step 2: Schedule
Use Jenkins cron syntax to run weekly/daily:
```bash
H 9 * * 1-5
```
#### Step 3: Set Environment Variables in Jenkins
Add credentials or global env variables under Manage Jenkins → Configure System

## 🖥️ Script Logic (main.py)
Launch Chrome browser (optionally in headless mode)
Log in to Naukri using credentials
Navigate to the resume upload section
Upload the latest resume file
Confirm upload and exit

## 🔐 Security Note
Never hardcode credentials! Use .env or Jenkins credentials securely.

## 🧪 Requirements
Google Chrome
Compatible ChromeDriver (same version as your Chrome)
Python 3.7+
Jenkins (optional for automation)

###📬 Output
Console logs for status

Optional: Integrate email notifications via SMTP or Jenkins plugins
