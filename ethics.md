1. Legal Analysis
Terms of Use & Robots.txt
Our project scrapes Basketball-Reference.com, which explicitly allows automated access within published limits (≤20 requests/minute) but prohibits creating a competing product, reselling data, or training AI models without permission. We stayed under this rate limit and cached results locally to minimize load.
Relevant Laws & Cases
Computer Fraud and Abuse Act (CFAA), 18 U.S.C. § 1030 – prohibits “unauthorized access” to protected computers. Since Basketball-Reference is publicly accessible and we did not bypass authentication, scraping within published limits is unlikely to violate CFAA.
Contract Law – Terms of Use act as a contract; we followed their restrictions by using limited requests and not redistributing data.
Copyright Law (17 U.S.C. § 101 et seq.) – Facts (like box scores) are not copyrightable per Feist Publ’ns v. Rural Tel. Serv., 499 U.S. 340 (1991), but the site’s compilation/formatting may be protected. We used the data solely for educational purposes and not for republication.
Case Precedent: hiQ Labs v. LinkedIn, 938 F.3d 985 (9th Cir. 2019) ruled that scraping publicly available web pages does not constitute CFAA “hacking,” provided no circumvention of authentication occurs — supporting our use case.
2. Impact on Website Operations
We scraped 1 page for this project, well under the 20 req/min limit they set.
We inserted randomized delays (time.sleep()) between requests and cached data to avoid re-scraping.
Result: negligible server impact, no risk of degrading human users’ experience, and full compliance with site guidance.
3. Privacy Considerations
The scraped data contains only publicly available sports statistics — no personal user data or PII.
No accounts, cookies, or login-required information were accessed.
If in the future we collected user data (e.g. picks, betting behavior), we would comply with GDPR (Reg. EU 2016/679) and CCPA (Cal. Civ. Code § 1798.100 et seq.), including anonymization and user consent.
4. Our Ethical Framework
We applied these principles throughout the project:
Respect for Terms of Use – Stayed below rate limits, did not create a competing product, and cited the data source.
Minimize Harm – Used caching, throttling, and off-peak scraping to reduce load.
Transparency – Documented scraping methodology, legal considerations, and limitations in our final report.
Educational Intent – The project is for a university course, not for profit or public distribution.
Future Awareness – Acknowledge that a real public-facing product would require a commercial license or API agreement.
5. Alternative Approaches Considered
Official Data Providers (Sportradar, Stats Perform): Provide commercial-grade feeds, but are expensive and out of scope for a school project.
Public APIs (balldontlie, MLB-StatsAPI): Freely available and designed for developers, but lacked some historical/statistical depth needed for our analysis.
Manual CSV Downloads: Basketball-Reference offers downloadable CSVs for some tables — we considered this but included scraping to meet the course requirement to demonstrate automated collection.
