# 📰 NewsWeaver

A powerful multi-source tech news aggregator that automatically collects articles from the web's most popular tech communities and commits them to Git. NewsWeaver weaves together the best tech news from diverse sources, creating a comprehensive feed of trending articles.

## 🌟 Features

- **Multi-Source Aggregation**: Scrapes from 7+ popular tech news sources
- **Automatic Git Integration**: Each new article creates a unique Git commit
- **Duplicate Detection**: Prevents duplicate articles from being saved
- **Multiple Parsers**: Supports HTML, JSON APIs, and RSS/Atom feeds
- **Error Handling**: Robust error handling with graceful fallbacks
- **Logging**: Beautiful, informative console output with progress tracking
- **JSON Storage**: Articles stored in structured JSON format
- **User-Agent Support**: Proper headers to bypass anti-bot detection

## 📚 Supported News Sources

NewsWeaver aggregates from these sources:

| Source | Type | Feed |
|--------|------|------|
| 🔥 **Hacker News - Top** | HTML Scraping | `https://news.ycombinator.com/` |
| 🔥 **Hacker News - Newest** | HTML Scraping | `https://news.ycombinator.com/newest` |
| 🔴 **Reddit - r/programming** | JSON API | `/r/programming/.json` |
| 🔴 **Reddit - r/technology** | JSON API | `/r/technology/.json` |
| 💻 **Dev.to - Top Articles** | REST API | `dev.to/api/articles` |
| 💥 **Product Hunt** | RSS Feed | `producthunt.com/feed.xml` |
| 📊 **ArXiv AI Papers** | RSS Feed | `arxiv.org/rss/cs.AI/recent` |

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Git
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/NewsWeaver.git
cd NewsWeaver
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Initialize Git repository** (if not already done)
```bash
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Usage

Simply run the scraper:

```bash
python scraper.py
```

### Example Output

```
============================================================
>>> Multi-Source News Scraper Started
============================================================

[*] Scraping: Hacker News - Top
    URL: https://news.ycombinator.com/
    [+] Found 30 articles

[*] Scraping: Reddit - r/programming
    URL: https://www.reddit.com/r/programming/.json
    [+] Found 25 articles

[*] Scraping: Dev.to - Top Articles
    URL: https://dev.to/api/articles?top=7
    [+] Found 7 articles

...

============================================================
[SUMMARY] 6 sources succeeded, 1 source failed
[TOTAL] 89 articles collected
============================================================

[*] Processing 89 articles...
    [+] Committing: [Hacker News] New AI breakthrough announced...
    [+] Committing: [Reddit - r/programming] Python tips and tricks...
    [+] Committing: [Dev.to] Getting started with Rust...
    ...

[RESULTS] 45 new articles, 44 duplicates

[*] Pushing 45 new commits...
[+] Push successful!
```

## 📁 Project Structure

```
NewsWeaver/
├── scraper.py          # Main scraper module
├── requirements.txt    # Python dependencies
├── data.json           # Collected articles (generated)
├── README.md           # This file
└── .git/               # Git repository
```

## 💾 Data Format

Articles are stored in `data.json` with the following structure:

```json
[
  {
    "title": "Revolutionary AI Model Achieves 99% Accuracy",
    "url": "https://example.com/article-1",
    "timestamp": "2026-03-07T14:23:45.123456",
    "source": "Hacker News"
  },
  {
    "title": "Python 3.11 Performance Improvements",
    "url": "https://reddit.com/r/programming/comments/xyz123",
    "timestamp": "2026-03-07T14:24:12.654321",
    "source": "Reddit - r/programming"
  }
]
```

## 🔧 Configuration

### Adding New Sources

Edit the `SOURCES` list in `scraper.py`:

```python
SOURCES = [
    {
        "url": "https://your-news-source.com/feed",
        "parser": "rss",  # or "hn", "reddit", "devto"
        "name": "Your News Source"
    },
    # ... more sources
]
```

### Supported Parsers

- `hn` - Hacker News HTML scraper
- `reddit` - Reddit JSON API parser
- `devto` - Dev.to REST API parser
- `rss` - RSS/Atom feed parser

### Timeout Configuration

Modify the timeout in `fetch_data()`:

```python
response = requests.get(url, timeout=10, headers=default_headers)
```

## 🔄 How It Works

### 1. **Fetching**
   - Sends HTTP requests to each configured news source
   - Includes proper User-Agent headers
   - 10-second timeout per request

### 2. **Parsing**
   - Routes content to appropriate parser based on source type
   - Extracts title, URL, timestamp, and source information
   - Handles errors gracefully

### 3. **Deduplication**
   - Loads existing articles from `data.json`
   - Checks if article URL already exists
   - Only processes new articles

### 4. **Saving & Committing**
   - Appends new article to JSON file
   - Creates Git commit for each article
   - Includes article title in commit message

### 5. **Pushing**
   - Pushes all new commits to remote repository
   - Provides summary of operations

## 📦 Dependencies

```
requests         - HTTP library for fetching web pages
beautifulsoup4   - HTML/XML parsing
feedparser       - RSS/Atom feed parsing
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

## 🎯 Use Cases

- **Tech Blog**: Curate a daily tech news feed
- **Research**: Track trends in tech and AI
- **Portfolio**: Showcase automated data collection
- **Notifications**: Setup webhooks to notify on new articles
- **Archives**: Build a searchable archive of tech news
- **Learning**: Understand web scraping and Git automation

## 🔐 Git Integration

Each article creates a unique commit:

```bash
git log --oneline | head -10

abc1234 Add article: Revolutionary AI Model Achieves 99% Accuracy
def5678 Add article: Python 3.11 Performance Improvements
ghi9012 Add article: New Kubernetes Release Announced
```

This creates a detailed history of discovered articles, making it easy to:
- Track when articles were discovered
- See what was trending in the tech world
- Rollback unwanted articles
- Create branches for further analysis

## 🚨 Troubleshooting

### No articles found
- Check internet connection
- Verify news sources are still accessible
- Check console output for specific errors
- Some sites may require additional headers

### Git commit fails
- Ensure git is configured: `git config user.name "Your Name"`
- Check repository is properly initialized: `git init`
- Verify write permissions in directory

### API rate limiting
- Reddit limits requests to the `.json` endpoint
- Add delays between requests if needed:
```python
import time
time.sleep(2)  # Wait 2 seconds between requests
```

### Missing dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📊 Statistics

After running NewsWeaver regularly, you can analyze:

```python
import json

with open('data.json') as f:
    articles = json.load(f)

# Count by source
sources = {}
for article in articles:
    source = article['source']
    sources[source] = sources.get(source, 0) + 1

print(f"Total articles: {len(articles)}")
for source, count in sorted(sources.items(), key=lambda x: x[1], reverse=True):
    print(f"  {source}: {count}")
```

## 🔮 Future Enhancements

- [ ] Filter articles by keywords
- [ ] Support for more news sources (Medium, HackerEarth, etc.)
- [ ] Email digest notifications
- [ ] Web dashboard for browsing articles
- [ ] Category/tagging system
- [ ] Search functionality
- [ ] Scheduled automatic runs (cron jobs)
- [ ] Database support (SQLite, PostgreSQL)

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-source`)
3. Add your changes
4. Commit with clear messages
5. Push to the branch
6. Open a Pull Request

### Adding a New Source

1. Add to `SOURCES` list with URL and parser type
2. Create parser function if needed (e.g., `parse_techcrunch()`)
3. Add parser to `parse_html()` function
4. Test and verify articles are extracted correctly

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created by: **You** 🚀

## 🙏 Acknowledgments

- Powered by incredible tech communities
- Built with Python, BeautifulSoup, and Feedparser
- Uses Git for version control
- Special thanks to Hacker News, Reddit, Dev.to, Product Hunt, and ArXiv

## 📞 Support

Having issues? Here are some resources:

- 🐛 [Open an Issue](https://github.com/yourusername/NewsWeaver/issues)
- 💬 [Discussions](https://github.com/yourusername/NewsWeaver/discussions)
- 📖 [Documentation](README.md)

---

**Happy news weaving!** 📰✨

Made with ❤️ for the tech community
