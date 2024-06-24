**Wi-Fi Based Attendance Tracking System**

This project implements a Wi-Fi based attendance tracking system using a Python script and a MySQL database. The system is designed to automatically capture attendance by detecting the MAC addresses of devices connected to a Wi-Fi network. The main components of the project include:

- **Python Script (attend.py):** This script captures attendance by identifying the MAC addresses of devices connected to the Wi-Fi network and records the attendance in the MySQL database.
- **MySQL Database:** The database is hosted locally using XAMPP and stores the details of students, including their MAC addresses, for attendance tracking.
- **Web-Based GUI:** Teachers can log in to add students, view attendance reports, and manage student records. Students can view their attendance reports as well.
- **Wi-Fi Infrastructure:** The system requires a Wi-Fi router to detect the devices connected for attendance marking. The router's IP address needs to be configured in the script.

**Networking Concepts Used:**
- **MAC Address Detection:** The script uses the MAC addresses of connected devices to identify and track attendance.
- **Localhost Server Configuration:** The MySQL database is configured to run on a local server (127.0.0.1) using XAMPP.
- **Wi-Fi Topologies:** The project leverages the basic infrastructure mode of Wi-Fi to connect devices and track their presence within the network.

**Features:**
- Automated attendance tracking using Wi-Fi.
- Web-based interface for managing student records and viewing attendance reports.
- Secure and efficient database management using MySQL.

**Steps to Execute the Code:**
1. Set up the MySQL database using the provided database file.
2. Configure the IP address in the Python script according to the router used for taking attendance.
3. Run the `attend.py` script and input the subject when prompted.
4. Access the web-based GUI to manage student records and view attendance reports.

**Technologies Used:**
- Python
- MySQL
- HTML, CSS, JavaScript (for GUI)
- XAMPP (for local server)

This project demonstrates an innovative approach to automating attendance tracking using Wi-Fi technology, reducing manual effort and enhancing accuracy.

