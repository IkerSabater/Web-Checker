<h1>Web App Monitoring with Selenium and Ubuntu Notifications</h1>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Selenium WebDriver</li>
        <li>ChromeDriver</li>
        <li>Ubuntu (for <code>notify-send</code>)</li>
    </ul>

    <h2>Setup Instructions</h2>
    <ol>
        <li><strong>Install Python 3.x:</strong><br>
            If Python is not already installed, download and install it from <a href="https://www.python.org/">python.org</a>.
        </li>
        <li><strong>Install Selenium:</strong><br>
            <code>pip install selenium</code>
        </li>
        <li><strong>Install ChromeDriver:</strong><br>
            <ul>
                <li>Download the ChromeDriver executable suitable for your Chrome browser version from <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads">ChromeDriver Downloads</a>.</li>
                <li>Place the executable in a directory accessible by your Python script. Update the <code>driverURL</code> variable in the script (<code>monitor_webapp.py</code>) with the correct path to the ChromeDriver executable.</li>
            </ul>
        </li>
        <li><strong>Install <code>notify-send</code> (for Ubuntu):</strong><br>
            <code>sudo apt-get install libnotify-bin</code>
        </li>
        <li><strong>Clone the Repository:</strong><br>
            Clone or download this repository to your local machine where you want to run the monitoring script.
        </li>
        <li><strong>Configure the Script:</strong><br>
            <ul>
                <li>Open <code>monitor_webapp.py</code> in a text editor.</li>
                <li>Update the following variables in the script:
                    <ul>
                        <li><code>driverURL</code>: Path to the ChromeDriver executable.</li>
                        <li><code>navbar_id</code>: ID of the navbar element on the web page you want to monitor.</li>
                        <li><code>url</code>: URL of the web application you want to monitor.</li>
                        <li><code>appName</code>: Name of your web application (for notifications).</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>Move the Script to <code>/etc/systemd/system</code>:</strong><br>
            Copy or move <code>monitor_webapp.py</code> to the directory <code>/etc/systemd/system/</code>:
            <pre><code>sudo cp monitor_webapp.py /etc/systemd/system/</code></pre>
        </li>
        <li><strong>Reload Systemd Daemon:</strong><br>
            After moving the script, reload the systemd daemon to update its configuration:
            <pre><code>sudo systemctl daemon-reload</code></pre>
        </li>
        <li><strong>Start and Enable the Service:</strong><br>
            Start the monitoring service:
            <pre><code>sudo systemctl start dival-status.service</code></pre>
            Enable the service to start automatically on boot:
            <pre><code>sudo systemctl enable dival-status.service</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <ul>
        <li>After completing the setup, the script will monitor the specified web application (<code>url</code>) and notify you via Ubuntu notifications regarding its status.</li>
        <li>Adjust the <code>check_interval</code> variable in <code>monitor_webapp.py</code> to change how often the script checks the status of the web application.</li>
    </ul>

    <h2>Additional Notes</h2>
    <ul>
        <li>Ensure that the user running the script (<code>monitor_webapp.py</code>) has appropriate permissions and access to the ChromeDriver executable, as well as the ability to send Ubuntu notifications (<code>notify-send</code>).</li>
        <li>Monitor logs and notifications to ensure the script is functioning correctly, especially after system reboots or updates.</li>
    </ul>
