# NBA Player Stats Scraper

## Executive Summary
This scraper automatically collects NBA player stats from Basketball-Reference.com to help retail sports bettors quickly identify top performers in popular categories: points per game (PPG), rebounds per game (RPG), assists per game (APG), and 3-pointers made per game (3PM).  

Instead of manually searching and sorting tables, users receive the **top 5 players per category** in **JSON** and **CSV** files. This saves time, reduces manual errors, and provides actionable insights for betting decisions.

---

## Technical Architecture Diagram
[Basketball-Reference.com]
│
▼
[Selenium WebDriver] --> Headless Chrome opens page
│
▼
[HTML Page Source] ---> [BeautifulSoup Parser] ---> Extract per-game stats table
│
▼
[Data Transformation & Validation] ---> Top 5 players per category
│
▼
[Output Files]
├── data/nba_player_props_<season>.json
└── data/nba_player_props_<season>.csv

---

## Scraping Strategy

### Data Collection Priorities
1. Scrape per-game stats table first because it contains all the relevant player prop stats.
2. Focus on PPG, RPG, APG, 3PM, and other high-value prop categories for bettors.
3. Validate that numerical columns are correctly parsed as floats.

### Fallback Strategies
- If the table is inside HTML comments, extract it using BeautifulSoup and `Comment`.
- Implement retries with exponential backoff (2s → 4s → 8s, max 3 attempts).
- Log errors and continue to the next player if a row fails parsing.

### Data Quality Validation Rules
- Player name must exist and not be empty.
- Numeric stats must convert to floats; if invalid, default to 0.
- Filter out repeated header rows.

### Update Frequency Justification
- Once per day is sufficient for seasonal stats.
- Real-time or hourly updates are unnecessary unless live betting is targeted.

---

## Performance Metrics
- Pages per minute: ~2–3 (depending on machine and network)
- Retry on failure: Exponential backoff implemented
- Error rate: ~0% if site is accessible and structure is unchanged
- Headless mode: Speeds up scraping and avoids visible browser pop-ups

---

## Setup & Deployment Instructions

1. **Clone repository**
```bash
git clone <repo_url>
cd basketball-scraper
