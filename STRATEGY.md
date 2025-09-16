# Basketball-Reference Scraper: Strategy Document

## 1. Data Collection Priorities

**Primary goal:** Provide retail bettors with actionable insights on player performance for popular prop bets.  

**Priority order for scraping:**

1. **Per-game stats table (`per_game_stats`)**
   - **Why first:** Contains all basic per-game metrics (PPG, RPG, APG, 3PM, etc.) needed to calculate top players for prop bets.
   - **Key columns:** `Player`, `PTS`, `TRB`, `AST`, `3P`.

2. **Player identification**
   - Ensure all players are valid (exclude rows without stats or repeated headers).  

3. **Top player categories**
   - Extract top performers per category: points, rebounds, assists, and 3-pointers made.
   - Additional optional stats: steals, blocks, turnovers (if expanded to more prop bets).

4. **Metadata for traceability**
   - Scrape season, scrape timestamp, source URL for reproducibility.

---

## 2. Fallback Strategies for Common Failures

| Failure | Fallback Strategy |
|---------|-----------------|
| Table not found directly in HTML | Search HTML comments for `per_game_stats` table |
| Network error / temporary ban (HTTP 403, 429) | Retry with **exponential backoff**: start with 2s → 4s → 8s (max retries = 3) |
| Chrome fails to load page | Headless Chrome fallback, ensure driver is up-to-date via `webdriver_manager` |
| Parsing error / malformed row | Skip row and log the error for review |
| Site structure changes | Log number of HTML comments and table detection failure to notify developer |

---

## 3. Data Quality Validation Rules

1. **Player rows**
   - Must have non-empty `Player` name.
   - All numeric stats (`PPG`, `RPG`, `APG`, `3PM`) must be floats ≥ 0.

2. **Top 5 selection**
   - After filtering valid rows, sort stats descending to select top 5 per category.

3. **Duplicate prevention**
   - Remove repeated headers and extra table rows from comments.

4. **Output verification**
   - Ensure CSV and JSON files contain expected keys (`name`, `ppg`, `rpg`, `apg`, `threepm`, `category`) and at least 5 entries per category.

---

## 4. Update Frequency Justification

- **Daily updates recommended**
  - Player stats do not change more frequently than after each NBA game.
  - Daily scrape ensures accurate prop bet insights while reducing load on Basketball-Reference servers.
  
- **Optional**
  - **Hourly updates** if providing live prop betting odds or integrating with real-time betting systems.
  - **Weekly/monthly** updates only if historical data collection is needed for analytics or trend visualization.
  
- **Avoid**: Minute-level updates
  - Basketball-Reference is static during games; excessive requests may trigger IP bans and violate respectful scraping principles.
