import urllib.request
import urllib.parse
import sys

def shorten(url):
    if not url.startswith("http"):
        url = "https://" + url

    api_url = f"https://is.gd/create.php?format=simple&url={urllib.parse.quote(url, safe='')}"

    try:
        with urllib.request.urlopen(api_url, timeout=5) as response:
            short = response.read().decode("utf-8").strip()

        if short.startswith("https://is.gd/"):
            print("\n" + "=" * 40)
            print("        URL SHORTENER")
            print("=" * 40)
            print(f"  Original : {url}")
            print(f"  Short    : {short}")
            print("=" * 40 + "\n")
        else:
            print(f"Error: {short}")

    except Exception as e:
        print(f"Failed to shorten URL: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shortener.py <url>")
        print("Example: python shortener.py https://github.com")
        sys.exit(1)

    url = sys.argv[1]
    shorten(url)
