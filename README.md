# Web App Monitoring with Selenium and Ubuntu Notifications

## Requirements
- Python 3.x
- Selenium WebDriver
- ChromeDriver
- Ubuntu (for `notify-send`)

## Setup Instructions
1. **Install Python 3.x:**
   If Python is not already installed, download and install it from [python.org](https://www.python.org/).

2. **Install Selenium:**
   ```bash
   pip install selenium

4. **Install ChromeDriver:**
- Download the ChromeDriver executable suitable for your Chrome browser version from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- Place the executable in a directory accessible by your Python script. Update the `driverURL` variable in the script (`monitor_webapp.py`) with the correct path to the ChromeDriver executable.

4. **Install `notify-send` (for Ubuntu):**
    ```bash
   sudo apt-get install libnotify-bin

6. **Clone the Repository:**
Clone or download this repository to your local machine where you want to run the monitoring script.

7. **Configure the Script:**
- Open `monitor_webapp.py` in a text editor.
- Update the following variables in the script:
  - `driverURL`: Path to the ChromeDriver executable.
  - `navbar_id`: ID of the navbar element on the web page you want to monitor.
  - `url`: URL of the web application you want to monitor.
  - `appName`: Name of your web application (for notifications).

7. **Move the Script to `/etc/systemd/system`:**
Copy or move `monitor_webapp.py` to the directory `/etc/systemd/system/`:
   ```bash
   sudo cp monitor_webapp.py /etc/systemd/system/

9. **Reload Systemd Daemon:**
After moving the script, reload the systemd daemon to update its configuration:
   ```bash
   sudo systemctl daemon-reload

10. **Start and Enable the Service:**
Start the monitoring service:
   ```bash
   sudo systemctl start dival-status.service
   ```
Enable the service to start automatically on boot:
   ```bash
   sudo systemctl enable dival-status.service
   ```
## Usage
- After completing the setup, the script will monitor the specified web application (`url`) and notify you via Ubuntu notifications regarding its status.
- Adjust the `check_interval` variable in `monitor_webapp.py` to change how often the script checks the status of the web application.

## Additional Notes
- Ensure that the user running the script (`monitor_webapp.py`) has appropriate permissions and access to the ChromeDriver executable, as well as the ability to send Ubuntu notifications (`notify-send`).
- Monitor logs and notifications to ensure the script is functioning correctly, especially after system reboots or updates.



