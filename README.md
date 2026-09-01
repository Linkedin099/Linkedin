# LinkedIn Cloud Scraper Architecture

This repository contains an AI-Agent optimized, 100% free, zero-IP-risk infrastructure for scraping LinkedIn profiles using GitHub Actions and Crawl4AI.

## Why this is safe:
1. **Zero Home IP Risk:** The scraper runs inside a GitHub Actions runner (an ephemeral Ubuntu server hosted by Microsoft). LinkedIn never sees your home IP address.
2. **Zero Primary Account Risk:** By using a dummy "Burner" account cookie, your main professional network is completely shielded from bans.

---

## 🛠️ Setup Instructions

### 1. Push to GitHub
Create a private repository on GitHub and push this code to it:
- `cloud_fetcher.py`
- `.github/workflows/scrape.yml`

### 2. Get a Burner `li_at` Cookie
1. Create a secondary "Burner" LinkedIn account. 
2. Log into this account using an Incognito window or separate browser profile.
3. Once logged in, right-click anywhere on the page -> **Inspect** to open Developer Tools.
4. Go to the **Application** tab (Chrome/Edge) or **Storage** tab (Firefox).
5. On the left sidebar, click **Cookies** -> `https://www.linkedin.com`.
6. Find the row named `li_at`. 
7. Double-click its **Value**, copy it, and keep it safe.

### 3. Add the Secret to GitHub
1. Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Click **New repository secret**.
3. **Name:** `LI_AT_COOKIE`
4. **Secret:** Paste the long cookie value you copied earlier.
5. Click **Add secret**.

### 4. Local Automation Setup (Optional but Recommended)
To allow your local AI agent to trigger the scrape automatically without you clicking buttons:
1. Generate a **GitHub Personal Access Token (PAT)** (classic) with `repo` permissions.
2. On your local machine, set the following environment variables:
   - `GITHUB_PAT`: Your personal access token
   - `GITHUB_OWNER`: Your GitHub username
   - `GITHUB_REPO`: The name of the repository where you pushed this code

---

## 🚀 How to Use (Triggering the Scrape)

### Method 1: Fully Automated (Zero-Click)
Once your environment variables are set, just ask your agent or run this command in your terminal:
```bash
python auto_fetch.py "https://www.linkedin.com/in/target-profile/"
```
*The script will silently trigger the cloud workflow, wait for it to finish (usually ~45 seconds), download the artifact, and unpack `profile_data.md` right into this directory.*

### Method 2: Manual Trigger
If you prefer not to use the Python script:
1. Go to your GitHub repository's **Actions** tab.
2. Click on **Stealth LinkedIn Fetcher** on the left menu.
3. Click the **Run workflow** dropdown button.
4. Paste the Target LinkedIn Profile URL in the box.
5. Click **Run workflow**.

Wait ~30 seconds for the action to finish. At the bottom of the completed workflow run, you will see an **Artifact** named `linkedin-profile-markdown`. 

Download it, extract `profile_data.md`, and drop it into your Antigravity IDE for your AI agent to analyze securely!
