# cloud_fetcher.py
import asyncio
import os
import sys
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def fetch_linkedin_profile(profile_url, output_filename="profile_data.md"):
    print(f"[Stealth] Initializing secure cloud crawler for: {profile_url}")
    
    # 1. Retrieve the authentication cookie from GitHub Secrets
    li_at_cookie = os.getenv("LI_AT_COOKIE")
    if not li_at_cookie:
        print("[Error] LI_AT_COOKIE environment variable is missing. Cannot bypass Authwall.")
        sys.exit(1)
        
    # Format the cookie for Playwright/Crawl4AI
    cookies = [
        {
            "name": "li_at",
            "value": li_at_cookie,
            "domain": ".linkedin.com",
            "path": "/"
        }
    ]

    # 2. Configure Stealth Browser
    browser_config = BrowserConfig(
        headless=True,
        enable_stealth=True,
        cookies=cookies,
        verbose=False
    )
    
    # 3. Configure Human-like Run Settings
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        magic=True,
        simulate_user=True,
        scan_full_page=True,
        remove_overlay_elements=True,
        markdown_generator=DefaultMarkdownGenerator()
    )
    
    # 4. Execute the Crawl
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=profile_url, config=run_config)
        if result.success:
            content = result.markdown.raw_markdown if hasattr(result.markdown, 'raw_markdown') else str(result.markdown)
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[Success] Profile saved securely to {output_filename}")
            return True
        else:
            print(f"[Error] Failed to fetch profile: {result.error_message}")
            return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloud_fetcher.py <linkedin_url>")
        sys.exit(1)
        
    target_url = sys.argv[1]
    asyncio.run(fetch_linkedin_profile(target_url))
