# PATT: Pandora Account Takeover Tool

PATT will inject a small bit of script to take over pandora accounts who are on the proxy network.

Just run the web.py script and it runs MITMProxy with a custom script.  As accounts get taken over, it will notify you in the terminal.

Run `python web.py`

## Installation

	sudo pip install -r requirements.txt

If you want to POST the value to another server, or change the listening port, edit the options dictionary in `malware.py`.

## Running

	python web.py

This will run MITMProxy (127.0.0.1:8080 by default) and a tornado service (127.0.0.1:8000)

To test if it's working, point your browser's proxy to 127.0.0.1:8080, navigate to pandora.com.  Your account should then have it's password changed to 'stolen'.
