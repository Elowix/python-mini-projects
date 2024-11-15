<h1>Cookie Clicker Automation</h1>

<p>This project automates the popular browser game <strong>Cookie Clicker</strong> using Selenium WebDriver in Python. The script clicks the big cookie for a specified number of times, allowing you to collect cookies automatically.</p>

<h2>Prerequisites</h2>

<p>Before running the script, ensure you have the following installed:</p>

<ul>
    <li>Python 3.x</li>
    <li>Selenium library</li>
    <li>Chrome WebDriver</li>
</ul>

<h2>Installation</h2>
    <li><strong>Install Selenium</strong>: Use pip to install the Selenium library. Run the following command in your terminal:
        <pre><code>pip install selenium</code></pre>
    </li>
    <li><strong>Download Chrome WebDriver</strong>: 
        <ul>
            <li>Check your Chrome version and download the corresponding WebDriver from <a href="https://sites.google.com/chromium.org/driver/downloads">ChromeDriver downloads</a>.</li>
            <li>Place the <code>chromedriver</code> executable in a directory that is included in your system's PATH, or specify its location in the script.</li>
        </ul>
    </li>
</ol>

<h2>Usage</h2>

<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yourusername/cookie-clicker-automation.git
cd cookie-clicker-automation</code></pre>
    </li>
    <li>Open the script in your favorite code editor and modify the number of clicks if needed in the following line:
        <pre><code>for i in range(50):  # Change 50 to your desired number of clicks</code></pre>
    </li>
    <li>Run the script:
        <pre><code>python cookie_clicker.py</code></pre>
    </li>
    <li>The script will open a Chrome browser, navigate to the Cookie Clicker game, select the English language, and click the big cookie 50 times (or the specified number of times).</li>
</ol>

<h2>Notes</h2>

<ul>
    <li>You may need to adjust the <code>WebDriverWait</code> timeouts depending on your internet speed and system performance.</li>
    <li>Make sure the game is fully loaded before running the script to ensure it functions correctly.</li>
</ul>
