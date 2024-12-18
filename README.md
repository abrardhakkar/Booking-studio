# Booking-studio
# Raspberry Pi Booking Platform

This repository contains a project developed during my studies, where I created a booking platform integrated with Raspberry Pi for a podcast studio. The system manages bookings and provides a visual indicator (LED lights) showing the room's availability.

## Project Description
The system allows users to:
1. **Log in or register** for an account.
2. **Book a podcast room** by selecting available dates and times.
3. **Indicate room status**:
   - Green LED: The room is available.
   - Red LED: The room is occupied.

This project integrates a Raspberry Pi for physical room indication and a web-based platform for booking management.

## Technologies Used
- **Python**: Backend logic using Flask.
- **MySQL**: Database management for storing user accounts and bookings.
- **Raspberry Pi**: Controls LED lights to reflect room status.
- **HTML/CSS**: Front-end user interface for login, registration, and booking.
- **Bcrypt**: Password hashing for secure user authentication.

## Key Features
- **User Authentication**: Secure login and registration system with hashed passwords.
- **Booking System**: Users can view available time slots and book a podcast room.
- **Room Availability**: 
   - LED lights (controlled by Raspberry Pi) provide real-time room availability.
   - Booked slots trigger the red light, and free slots trigger the green light.
- **API Integration**: The system makes efficient use of database queries and integrates APIs to retrieve and display data.

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate # (Windows: venv\Scripts\activate)
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Ensure MySQL is installed and running.
   - Import the database schema:
     ```bash
     mysql -u root -p podcast_booking < podcast_booking.sql
     ```

5. **Connect Raspberry Pi**:
   - Ensure the LED lights are connected to the Raspberry Pi GPIO pins.
   - Update the GPIO pin configurations in the `create_microphone.py` file if needed.

6. **Run the application**:
   ```bash
   python app.py
   ```

7. **Access the platform**:
   Open a web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## File Structure
- **app.py**: Main Flask application.
- **mysqlConnect.py**: Contains the database connection.
- **create_microphone.py**: Raspberry Pi GPIO configuration for LED lights.
- **templates/**: HTML files for the user interface (e.g., login, registration, booking confirmation).
- **static/**: Contains CSS, images, and other static resources.

## Learning Outcomes
- Integration of a physical device (Raspberry Pi) with a web-based booking system.
- Using Python Flask for backend logic and MySQL for data management.
- Secure implementation of user authentication with password hashing.
- Real-time room availability visualization through LED indicators.
- Utilizing APIs and database queries for dynamic data handling.

## Contact
If you have questions or need further information about this project, feel free to contact me at M.AbrarParwez@gmail.com.

