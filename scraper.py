#!/usr/bin/env python3
# src/scraper.py

import logging
import time
import json
import csv
from datetime import datetime
from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasketballScraper:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def fetch_nba_stats(self, season=2024, retries=3):
        url = f"https://www.basketball-reference.com/leagues/NBA_{season}_per_game.html"
        self.logger.info(f"Fetching NBA {season} per-game stats from {url}")

        # Headless Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        backoff = 2  # seconds
        for attempt in range(1, retries + 1):
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                      options=chrome_options)
            try:
                self.logger.info(f"Attempt {attempt}: Loading page...")
                driver.get(url)
                time.sleep(3)  # wait for page load

                soup = BeautifulSoup(driver.page_source, "html.parser")

                # Try to find table directly first
                table = soup.find("table", {"id": "per_game_stats"})
                if not table:
                    self.logger.info("Table not found directly, checking HTML comments...")
                    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
                    self.logger.info(f"Found {len(comments)} comments")
                    for c in comments:
                        if "per_game_stats" in c:
                            table = BeautifulSoup(c, "html.parser").find("table", {"id": "per_game_stats"})
                            if table:
                                break

                if not table:
                    raise ValueError("Could not find per-game stats table!")

                # Extract player data
                players = []
                rows = table.find("tbody").find_all("tr")
                for row in rows:
                    cells = row.find_all("td")
                    if not cells:
                        continue
                    try:
                        player = {
                            "name": cells[0].text.strip(),
                            "ppg": float(cells[28].text.strip() or 0),
                            "rpg": float(cells[22].text.strip() or 0),
                            "apg": float(cells[23].text.strip() or 0),
                            "threepm": float(cells[10].text.strip() or 0)
                        }
                        players.append(player)
                    except Exception:
                        continue

                self.logger.info(f"Scraped {len(players)} players successfully.")
                return players

            except Exception as e:
                self.logger.warning(f"Attempt {attempt} failed: {e}")
                if attempt < retries:
                    self.logger.info(f"Sleeping for {backoff:.1f}s before retry...")
                    time.sleep(backoff)
                    backoff *= 2
                else:
                    self.logger.error("Failed to fetch data after max retries")
                    return []
            finally:
                driver.quit()
                self.logger.info("Closed Chrome.")

    @staticmethod
    def get_top_players(players, stat, top_n=5):
        return sorted(players, key=lambda x: x[stat], reverse=True)[:top_n]

    def export_data(self, players, season=2024):
        top_categories = ['ppg', 'rpg', 'apg', 'threepm']
        data = {}
        for cat in top_categories:
            data[cat] = self.get_top_players(players, cat)

        # Save JSON
        json_file = f"data/nba_player_props_{season}.json"
        with open(json_file, 'w') as f:
            json.dump({
                'scraped_at': datetime.now().isoformat(),
                'data': data
            }, f, indent=2)

        # Save CSV
        csv_file = f"data/nba_player_props_{season}.csv"
        all_rows = []
        for cat, top_players in data.items():
            for p in top_players:
                p_copy = p.copy()
                p_copy['category'] = cat
                all_rows.append(p_copy)

        if all_rows:
            with open(csv_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=all_rows[0].keys())
                writer.writeheader()
                writer.writerows(all_rows)

        self.logger.info(f"Exported top players to {json_file} and {csv_file}")

    def run(self, season=2024):
        players = self.fetch_nba_stats(season)
        if not players:
            self.logger.error("No player data scraped")
            return

        self.export_data(players, season)
        self.logger.info("Scraping pipeline complete")
        return players

if __name__ == "__main__":
    scraper = BasketballScraper()
    scraper.run()
