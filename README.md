# Event Registration System

## Overview

The Event Registration System is a sophisticated web application developed using Flask, designed to streamline the user registration process for an upcoming event. It consists of two main modules: the Admin Dashboard and the User Registration.

## Features

### Admin Area

#### 1. **Login Page**
   - Secure login for administrators to access the admin dashboard.

#### 2. **Admin Dashboard**
   - Comprehensive overview of system analytics.
   - Quick access to various administrative functionalities.

#### 3. **Generate Pin Page**
   - Capability for administrators to generate registration pins for three distinct categories: children, teens, and adults.

#### 4. **View Unused Pins**
   - Admins can easily review a list of unused registration pins.

#### 5. **View Used Pins**
   - Detailed list of used registration pins, aiding in tracking and management.

#### 6. **User Analytics**
   - In-depth analytical insights into registered users, including:
     - Total users registered.
     - Percentage of female and male users.
     - Percentage of users from Zone 2 and Zone 3.
     - Percentage of registered teens, children, and adults.

#### 7. **Pin Analytics**
   - Analytics related to registration pins, including:
     - Total pins generated, used, and unused.
     - Percentage distribution for each pin category.

#### 8. **View Registered Users**
   - Admins have the ability to view detailed information about all registered users.
   - Displays user information, including name, email, zone, and expectations.

### User Area

#### 1. **User Registration**
   - User-friendly registration process allowing users to register for the event using a valid registration pin.
   - Confirmation email sent upon successful registration.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/event-registration-system.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd event-registration-system
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Run the Application:**
   ```bash
   flask run
   ```

6. **Open Your Web Browser:**
   Visit [http://localhost:5000](http://localhost:5000).

## Demo Video

[Watch Demo Video](https://youtu.be/_VzK4JuSIMc) - Attach a link to the demo video.

## Screenshots

### Admin Dashboard
- ![Screenshot (149)](https://github.com/BrightDaniel/Nasfat_Project/assets/107191784/01c61eb8-6489-447a-8db8-d23597e66d41)
- ![Screenshot (150)](https://github.com/BrightDaniel/Nasfat_Project/assets/107191784/516dfc44-de39-4002-a1d1-bb510c619703)
- ![Screenshot (151)](https://github.com/BrightDaniel/Nasfat_Project/assets/107191784/c4631819-2a0e-4bc7-9681-26566e6aa2ad)
- ![Screenshot (152)](https://github.com/BrightDaniel/Nasfat_Project/assets/107191784/9f0794ed-becf-4d8e-9273-936244792a39)
- ![Screenshot (153)](https://github.com/BrightDaniel/Nasfat_Project/assets/107191784/1130b2f5-b68e-4d3b-a7cf-9c59cad24271)
- ![Screenshot (154)](https://github.com/BrightDaniel/Nasfat_Project/assets/107191784/21bd5e44-c8b9-4fcb-b844-f904f89163aa)
- ![Screenshot (155)](https://github.com/BrightDaniel/Nasfat_Project/assets/107191784/9e24bee7-76c6-4d32-a201-4eb1d436e6db)

### User Registration
- ![Screenshot (141)](https://github.com/BrightDaniel/Nasfat_Project/assets/107191784/a8ee82ae-4305-4475-ba76-34a26781e922)
- ![Screenshot (148)](https://github.com/BrightDaniel/Nasfat_Project/assets/107191784/e63f4f3b-abd0-4525-9706-8ab678528d1b)


## Contribution Guidelines

### Setup Development Environment

1. **Fork the Repository:**
   - Click on the "Fork" button on the top right of the repository page.

2. **Clone Your Fork:**
   ```bash
   git clone https://github.com/your-username/event-registration-system.git
   ```

3. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - Windows: `venv\Scripts\activate`
   - MacOS/Linux: `source venv/bin/activate`

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Set Up Local Database:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

7. **Run the Development Server:**
   ```bash
   flask run
   ```

### Contribution Process

1. **Create a Branch:**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Make Changes:**
   - Implement your desired feature or bug fix.

3. **Commit Changes:**
   ```bash
   git add .
   git commit -m "Add your descriptive commit message"
   ```

4. **Push to Your Fork:**
   ```bash
   git push origin feature/new-feature
   ```

5. **Open a Pull Request:**
   - Submit a pull request from your branch to the main repository.

## Dependencies

- Flask
- Flask-Mail
- PyMySQL

## Contributors

- [Bright Daniel](https://github.com/brightdaniel)
- [Bwave ICT](https://github.com/bwaveICT/)
- Additional Contributors

Feel free to contribute to the project by opening issues or submitting pull requests.
