# FAAN Airport Protocol Management System

A web-based **Airport Protocol Management System** developed to streamline the registration, management, tracking, and reporting of protocol passengers and related information within the **Federal Airports Authority of Nigeria (FAAN)**.

The system provides a centralized platform for managing passenger information, organizations, service levels, special needs, protocol officers, and administrative activities.

---

## 📌 Project Overview

The FAAN Airport Protocol Management System is designed to replace manual and fragmented passenger-record management processes with a secure, organized, and user-friendly digital solution.

The application enables authorized personnel to:

* Register and manage protocol passengers
* Capture passenger travel information
* Record passenger signatures
* Associate passengers with organizations
* Manage service levels
* Manage passenger special needs
* Manage system users
* Activate or deactivate user accounts
* Generate passenger reports
* Export reports to Excel
* Generate downloadable PDF reports
* Track the officer/user who registered a passenger
* Provide role-based access to system functions

---

## 🚀 Key Features

### 1. User Authentication

The system supports role-based authentication for:

* **Administrator**
* **Protocol Officer**
* **Normal User**

Each role has access to the functions appropriate to its responsibilities.

The authentication system also supports maintaining separate Admin and User sessions within the same browser environment.

---

### 2. Passenger Registration

Authorized users can register passengers with information including:

* Passenger name
* Travel date
* Position
* Flight
* Itinerary
* Organization
* Service level
* Additional requests
* Special needs
* Passenger signature

Passenger records are linked to the user who registered them.

---

### 3. Organization Management

Administrators can:

* Register organizations
* View organizations
* Edit organization information
* Delete organizations
* Store contact information

Organization records can then be associated with registered passengers.

---

### 4. Service Level Management

Administrators can create and manage service levels used during passenger registration.

Each service level contains:

* Service name
* Description

---

### 5. Special Needs Management

The system provides a centralized list of passenger special needs.

Administrators can:

* Add special needs
* Edit special needs
* View special needs
* Delete special needs

Multiple special needs can be assigned to a passenger during registration.

---

### 6. User Management

Administrators can manage system users.

Available functions include:

* Create users
* View users
* Edit users
* Activate/deactivate users
* Upload officer signatures
* Manage user roles

User roles currently include:

```text
admin
protocol
user
```

---

### 7. Passenger Reports

The system provides passenger reporting functionality with filtering options.

Reports can be generated based on available passenger information and can include:

* Passenger details
* Travel information
* Organization
* Service level
* Special needs
* Registering officer
* Officer signature

---

### 8. Excel Export

Passenger reports can be exported to Microsoft Excel.

The Excel reports are formatted for improved readability and include appropriate headings and passenger information.

---

### 9. PDF Export

Passenger reports can also be generated as PDF documents.

The PDF reporting system supports:

* FAAN branding
* Landscape A4 layout
* Passenger information
* Officer information
* Officer signature
* Structured report tables

---

## 👥 User Roles

### Administrator

The Administrator has the highest level of access.

Administrators can:

* Access the Admin Dashboard
* Manage users
* Manage organizations
* Manage service levels
* Manage special needs
* Register passengers
* View passenger records
* Edit passenger records
* Delete passenger records
* Generate reports
* Export Excel reports
* Export PDF reports

---

### Protocol Officer

Protocol Officers have access to protocol-related passenger activities and their assigned functions.

They can register and manage passenger information according to the permissions assigned to their role.

---

### Normal User

Normal users can access user-level functions provided by the system.

Users can:

* Access the User Dashboard
* Register passengers
* View passengers associated with their account
* View their reports
* Edit permitted passenger information

---

## 🛠️ Technology Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* SQLAlchemy
* Flask-Mail
* Flask-Login

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap
* Font Awesome

### Database

* PostgreSQL
* Neon PostgreSQL

The application is designed to support migration between database environments where required.

### Reporting

* ReportLab
* Pandas
* OpenPyXL

### Deployment

* Render
* Gunicorn
* GitHub
* Neon PostgreSQL

---

## 📂 Project Structure

```text
protocol_app/
│
├── app/
│   ├── models/
│   │   ├── admin.py
│   │   ├── forms.py
│   │   └── user.py
│   │
│   ├── routes/
│   │   ├── admin/
│   │   │   ├── dashboard
│   │   │   ├── forms.py
│   │   │   ├── passenger.py
│   │   │   ├── report.py
│   │   │   ├── user.py
│   │   │   └── views.py
│   │   │
│   │   ├── root/
│   │   │   ├── login.py
│   │   │   ├── index.py
│   │   │   └── user_dashboard.py
│   │
│   ├── templates/
│   │   ├── admin/
│   │   └── ...
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── uploads/
│   │
│   ├── utils/
│   │   ├── auth.py
│   │   └── decorators.py
│   │
│   └── __init__.py
│
├── migrations/
│
├── config.py
├── requirements.txt
├── run.py
├── Procfile
├── .python-version
├── .env
└── README.md
```

> **Note:** `.env` contains environment-specific configuration and sensitive credentials and should never be committed to GitHub.

---

## 🔐 Authentication Architecture

The system uses role-specific session keys to allow different user roles to maintain independent authentication states.

Examples include:

```python
session["admin_user_id"]
session["protocol_user_id"]
session["user_user_id"]
```

The application provides helper functions for retrieving the authenticated role:

```python
get_admin_user()
get_protocol_user()
get_user()
```

Role-specific decorators are available through:

```python
admin_required
protocol_required
user_required
```

This architecture allows an Administrator and a normal User to remain logged in simultaneously in different browser tabs/windows.

---

## 🗄️ Database Configuration

The production application uses **Neon PostgreSQL**.

The database connection is supplied through an environment variable:

```env
DB_URI=your_database_connection_string
```

Other sensitive configuration values are also stored in environment variables.

Example:

```env
SECRET_KEY=your_secret_key
DB_URI=your_postgresql_connection_string
```

Never commit real credentials to the repository.

---

## ⚙️ Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mufatech/faan-protocol-management-system.git
```

Move into the project directory:

```bash
cd faan-protocol-management-system
```

---

### 2. Create a Virtual Environment

On Windows:

```bash
python -m venv venv
```

Activate it:

### Git Bash

```bash
source venv/Scripts/activate
```

### Command Prompt

```cmd
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
DB_URI=your-neon-postgresql-connection-string
```

Do not commit `.env` to GitHub.

---

### 5. Initialize the Database

Run the Flask migration command:

```bash
flask db upgrade
```

---

### 6. Run the Application

```bash
python run.py
```

The application will normally be available at:

```text
http://127.0.0.1:5000
```

---

## 🌐 Deployment

The application is deployed using **Render**.

The production architecture consists of:

```text
GitHub
   │
   ▼
Render Web Service
   │
   ▼
Flask Application
   │
   ▼
Neon PostgreSQL
```

### Render Build Command

```bash
pip install -r requirements.txt
```

### Render Start Command

```bash
gunicorn run:app
```

Python version is controlled through:

```text
.python-version
```

---

## 🔄 Database Migrations

Database changes are managed using **Flask-Migrate/Alembic**.

To generate a migration:

```bash
flask db migrate -m "Describe your changes"
```

To apply migrations:

```bash
flask db upgrade
```

To check the current migration:

```bash
flask db current
```

Always review generated migration files before applying them to production.

---

## 📊 Reporting

The system provides two major reporting formats:

### Excel

Excel reports are generated using:

```text
Pandas
OpenPyXL
```

### PDF

PDF reports are generated using:

```text
ReportLab
```

Reports are designed to support FAAN administrative and operational documentation requirements.

---

## 🔒 Security Considerations

The application follows several security practices:

* Passwords are hashed before storage.
* Sensitive credentials are stored in environment variables.
* User accounts can be activated/deactivated.
* Role-based access control is implemented.
* Uploaded files use secure filenames.
* Uploaded signature filenames can be generated uniquely.
* Database access is handled through SQLAlchemy.
* `.env` files are excluded from source control.

### Never commit:

```text
.env
database passwords
API keys
SMTP passwords
private credentials
secret keys
```

---

## 🧪 Testing

Before deploying changes to production, test:

* Admin login
* Protocol Officer login
* User login
* User activation/deactivation
* Passenger registration
* Passenger editing
* Passenger deletion
* Organization management
* Service level management
* Special needs management
* Passenger reports
* Excel export
* PDF export
* Signature uploads
* Logout functionality
* Role-based dashboard access
* Simultaneous Admin/User sessions

### Simultaneous Session Test

The application should support:

```text
Browser Tab 1
Admin → Admin Dashboard

Browser Tab 2
User → User Dashboard
```

Logging in the User should not replace the Admin session in Tab 1.

Likewise, logging out the User should not log out the Administrator.

---

## 📝 Future Enhancements

Potential future improvements include:

* Advanced audit trail
* Activity logs
* Dashboard analytics
* Search and advanced filtering
* Pagination for large passenger records
* Automated email notifications
* Password reset functionality
* Two-factor authentication
* More detailed permission management
* Improved report customization
* Automated database backups
* Mobile-responsive improvements
* API integration
* Comprehensive automated testing

---

## 👩🏽‍💻 Developer

**Engr. Sidiqoh Abosede Fasasi**

Software Engineer
Federal Airports Authority of Nigeria (FAAN)

---

## 📄 License

This project is developed for organizational/operational use.

Unauthorized copying, distribution, modification, or deployment should be subject to the applicable organizational policies and permissions.

---

## 🙏 Acknowledgement

Developed to support the digital transformation and improved efficiency of airport protocol passenger management processes within FAAN.

**Federal Airports Authority of Nigeria (FAAN)**

---

```

This is ready to save as **`README.md`** in the root of your GitHub repository. I deliberately kept the README professional and avoided putting any real database credentials, passwords, or `.env` contents into it.
```
