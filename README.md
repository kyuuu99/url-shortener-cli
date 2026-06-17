# url-shortener-cli

A simple command-line URL shortener using the is.gd API.

## Features

- Shorten any URL from the terminal
- Uses is.gd free API (no API key needed)
- No external dependencies

## Usage

```bash
# Shorten a URL
python shortener.py https://github.com

# Works without https:// too
python shortener.py github.com
```

## Example Output

```
========================================
        URL SHORTENER
========================================
  Original : https://github.com
  Short    : https://is.gd/aBcDeF
========================================
```

## Requirements

- Python 3.x
- Internet connection
