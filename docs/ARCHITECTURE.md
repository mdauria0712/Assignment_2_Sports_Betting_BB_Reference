# ARCHITECTURE.md
# Technical Design Decisions

## Overview
The scraper is designed to fetch NBA player stats from Basketball-Reference, process the data, and output the top performers in key betting categories. The system balances simplicity, reliability, and respect for the target website.

## Components
1. **Data Collection**
   - Tool: Selenium (headless Chrome)
   - Purpose: Fetch raw HTML, including dynamic content
   - Retry & backoff implemented for rate-limiting protection

2. **Data Parsing**
   - Tool: BeautifulSoup
   - Purpose: Extract player stats from HTML tables and comments
   - Handles variations in table placement (direct or commented out)

3. **Data Transformation**
   - Calculate top 5 players per category (PPG, RPG, APG, 3PM)
   - Validate data (ignore incomplete or malformed rows)
   - Output formats: JSON and CSV in `/data` folder

4. **Error Handling & Reliability**
   - Exponential backoff and retry limits
   - Logging to track scraping success/failures

5. **Deployment**
   - Run locally or in a virtual environment
   - Headless mode for faster, automated execution
   - Compatible with ChromeDriver and WebDriverManager

## Key Design Decisions
- **Selenium** for dynamic content and JS-rendered tables
- **BeautifulSoup** for robust parsing of complex HTML
- **Headless mode** to avoid opening GUI while scraping
- **Retry/backoff** to minimize risk of IP blocking and maximize reliability
- **Output to `/data`** to store results locally for analysis and reporting

