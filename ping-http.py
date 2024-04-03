import requests
import argparse
import time

def ensure_scheme(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url

def ping_url(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        elapsed_time = time.time() - start_time
        if response.status_code == 200:
            print(f"200 OK    time={elapsed_time * 1000:.2f} ms")
        else:
            print(f"{response.status_code} {response.reason}    time={elapsed_time * 1000:.2f} ms")
    except requests.exceptions.Timeout:
        print("Request Time Out    time=10000.00 ms")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}    time=N/A")

    time.sleep(2)

def main():
    parser = argparse.ArgumentParser(description="Ping a URL and check for a 200 OK response.")
    parser.add_argument("--url", required=True, help="URL to ping.")
    
    args = parser.parse_args()
    args.url = ensure_scheme(args.url)

    try:
        while True:
            ping_url(args.url)
    except KeyboardInterrupt:
        print("\nPing stopped by user.")
        exit(0)

if __name__ == "__main__":
    main()