# HTTP Ping Script

This script mimics the traditional ping command but for HTTP URLs. It sends a request to the specified URL and prints the response status and round trip time in milliseconds.

## Usage

To run the script, use the following command:

```
python ping-http.py --url www.google.com
200 OK    time=166.37 ms
200 OK    time=139.74 ms
200 OK    time=141.33 ms
^C
Ping stopped by user.
```

## Installation

Clone this repository and navigate into the project directory: 

`git clone https://github.com/darekm101/ping-http.git`

Then, install the required Python packages into virtual environment using:

`python3 -m venv venv`

`source venv/bin/activate`

`pip instal -r requirements ` 



