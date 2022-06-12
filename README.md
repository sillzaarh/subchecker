# subchecker

This is a simple python tool which request given subdomains or URLs and finds out if it is working or not.

# Usage
<pre><code>
usage: checker.py [-h] [-u] [-l]

Subdomain or URL Checker Tool

options:
  -h, --help    show this help message and exit
  -u , --url    enter URL
  -l , --list   enter the path to file of list of URLs
  </code></pre>

# Installation
Clone the repository
<pre><code>git clone https://github.com/mmbverse/subchecker.git
cd subchecker
</pre></code>subchecker
Python
<pre><code>pip install -r requirements.txt
python subchecker.py
</pre></code>
Bash
<pre><code>pip3 install -r requirements.txt
chmod +x subchecker.py

# copy to /usr/local/bin to access the tool from anywhere
sudo cp subchecker.py /usr/local/bin/subchecker
</pre></code>
