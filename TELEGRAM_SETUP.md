# 🤖 Telegram Bot Setup Guide

Complete guide to run YouTube Auto-Clip Bot on Telegram.

## 🚀 Quick Start (5 minutes)

### Step 1: Create Telegram Bot

1. Open Telegram
2. Search for **@BotFather**
3. Send `/start`
4. Send `/newbot`
5. Follow prompts:
   ```
   What should your bot be called?
   → YouTubeClipBot
   
   Give your bot a username (must end with 'bot')
   → youtube_clip_bot_123
   ```
6. **Copy the API TOKEN** (look for: "Use this token to access the HTTP API")

### Step 2: Add Token to .env

```bash
# Edit .env file
nano .env
```

Add this line:
```env
TELEGRAM_BOT_TOKEN=your_token_here_from_botfather
```

Save and exit: `Ctrl+X`, `Y`, `Enter`

### Step 3: Install Dependencies

```bash
pip install python-telegram-bot
```

### Step 4: Run Bot

```bash
python telegram_runner.py
```

You should see:
```
✅ Checking requirements...
✅ Checking API configuration...
🚀 Starting Telegram Bot...
🤖 Telegram Bot Started!
```

### Step 5: Test Bot

1. Open Telegram
2. Search for your bot username: `youtube_clip_bot_123`
3. Send `/start`
4. You should see welcome message!

---

## 📋 Available Commands

```
/start        → Welcome message with main menu
/help         → Show all commands and usage
/status       → Check bot status
/settings     → Configure bot settings
/history      → View processing history
/cancel       → Cancel current operation
```

---

## 🎬 How to Use

### Method 1: Send YouTube URL

1. Copy YouTube video link
2. Send to bot: `https://youtube.com/watch?v=...
3. Bot will:
   - Download video
   - Detect best clips
   - Generate titles with GLM 4
   - Send results

### Method 2: Upload Video File

1. Send video file to bot
2. Bot will:
   - Analyze video
   - Detect clips
   - Generate titles
   - Send results

---

## 🔧 Configuration

### Customize Settings

```bash
# In Telegram, send:
/settings
```

You can customize:
- Clip minimum duration
- Clip maximum duration
- Title style (engaging/professional/clickbait)
- Scene sensitivity
- Video quality

---

## 📊 Example Interaction

```
You: /start
Bot: 🎬 Welcome to YouTube Auto-Clip Bot!
     [Shows welcome message with buttons]

You: https://youtube.com/watch?v=...
Bot: 🎬 Processing Started!
     [Shows progress steps]
     Step 1: Downloading from YouTube... ✓
     Step 2: Analyzing content... ✓
     Step 3: Detecting clips... ✓
     Step 4: Generating titles... ✓

Bot: ✅ Processing Complete!
     Found 5 clips
     Generated 5 titles:
     1. You Won't Believe What Happened Next!
     2. Epic Moment Everyone Should See
     3. This Will Change Everything
     4. The Ultimate Guide to Success
     5. Mind-Blowing Content Revealed

You: [Click "Download Clips"]
Bot: [Sends download links]
```

---

## 🆘 Troubleshooting

### Bot not responding

**Check if bot is running:**
```bash
# Look for process
ps aux | grep telegram

# If not running, start it:
python telegram_runner.py
```

**Check API token:**
```bash
echo $TELEGRAM_BOT_TOKEN
```

### "TELEGRAM_BOT_TOKEN not found"

1. Make sure `.env` file exists
2. Verify token is added correctly
3. No quotes needed around token

### Bot stops running

**Keep bot running in background:**

```bash
# Terminal 1: Start bot
nohup python telegram_runner.py &

# Terminal 2: Check logs
tail -f logs/telegram_bot.log
```

### Processing takes too long

Normal times:
- 1 min video: 5-10 minutes
- 5 min video: 15-25 minutes
- 10 min video: 30-60 minutes

Depends on:
- Video length
- Phone/computer performance
- GLM API response time

---

## 🌟 Advanced Features

### Multiple Videos at Once

Send multiple URLs - bot queues them:
```
You: Video 1 URL
You: Video 2 URL
You: Video 3 URL
Bot: Processing all in queue...
```

### Save Processing History

```
/history
```

View all processed videos and reprocess anytime.

### Customize Output

In `/settings`, you can choose:
- Number of clips to extract
- Number of titles to generate
- Video quality
- Sensitivity of clip detection

---

## 📱 Using on Phone

### Termux on Android

```bash
# Install Termux
# Then:

cd youtube-auto-clip-bot
source venv/bin/activate
python telegram_runner.py
```

Bot runs 24/7 on phone!

### Keep Bot Running

1. Install termux-wake-lock
2. Or disable phone sleep in settings
3. Keep phone plugged in
4. Use persistent notification

---

## 🔒 Security

### Protect Your API Key

✅ DO:
- Keep `.env` file private
- Never share TELEGRAM_BOT_TOKEN
- Use `.gitignore` to hide .env
- Regenerate token if leaked

❌ DON'T:
- Commit .env to GitHub
- Share token publicly
- Use old tokens

---

## 📈 Monitor Bot Performance

### Check Logs

```bash
# View recent logs
tail -f logs/telegram_bot.log

# Search for errors
grep ERROR logs/telegram_bot.log

# Count successful processes
grep "Processing Complete" logs/telegram_bot.log | wc -l
```

### Monitor Status

In Telegram:
```
/status
```

Shows:
- Bot online status
- API connections
- Processing queue
- Performance metrics

---

## 🚀 Deploy to Cloud (Optional)

### Run on Server 24/7

```bash
# Using nohup
nohup python telegram_runner.py > bot.log 2>&1 &

# Using screen
screen -S telegram_bot
python telegram_runner.py
# Press Ctrl+A, then D to detach

# Using systemd (Linux)
# Create /etc/systemd/system/telegram-bot.service
```

---

## 💡 Tips & Tricks

### Speed Up Processing

1. Use lower video quality (480p instead of 1080p)
2. Reduce clip duration limits
3. Disable unnecessary detection methods

### Better Titles

1. Make sure GLM API is working: `/status`
2. Provide clear video context
3. Use specific keywords in URL

### Save Bandwidth

1. Reuse downloaded videos
2. Store clips locally
3. Use shorter videos for testing

---

## 📞 Support

For issues:

1. Check logs: `tail -f logs/telegram_bot.log`
2. Run `/help` in Telegram
3. Check `.env` configuration
4. Restart bot: `Ctrl+C` then `python telegram_runner.py`

---

## ✅ Checklist

- [ ] Got Telegram bot token from @BotFather
- [ ] Added token to .env file
- [ ] Installed python-telegram-bot
- [ ] Got GLM API key from https://open.bigmodel.cn/
- [ ] Started bot with `python telegram_runner.py`
- [ ] Found bot in Telegram
- [ ] Sent `/start` successfully
- [ ] Ready to process videos!

---

## 🎉 You're Ready!

Your Telegram bot is now running! 🎬

**Next steps:**
1. Send a YouTube URL to test
2. Wait for processing to complete
3. Receive titles and clips
4. Share amazing content!

Happy clipping! ✨
