#!/usr/bin/env python
"""
Telegram Bot Runner Script
Simple script to start the Telegram bot
"""

import os
import sys
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/telegram_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def check_requirements():
    """Check if all requirements are installed"""
    print("\n🔍 Checking requirements...")
    
    requirements = {
        'python-telegram-bot': 'telegram',
        'python-dotenv': 'dotenv',
        'zhipu-ai': 'zhipuai',
        'pyyaml': 'yaml'
    }
    
    missing = []
    for package, import_name in requirements.items():
        try:
            __import__(import_name)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing.append(package)
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        print(f"\nInstall with: pip install {' '.join(missing)}")
        return False
    
    print("\n✅ All requirements satisfied!")
    return True

def check_api_key():
    """Check if API key is configured"""
    print("\n🔐 Checking API configuration...")
    
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    glm_api_key = os.getenv('GLM_API_KEY')
    
    if not telegram_token:
        print("❌ TELEGRAM_BOT_TOKEN not found in .env")
        print("   Get it from: https://t.me/BotFather")
        return False
    else:
        print("✅ TELEGRAM_BOT_TOKEN configured")
    
    if not glm_api_key:
        print("⚠️  GLM_API_KEY not found (titles won't work)")
        print("   Get it from: https://open.bigmodel.cn/")
        return False
    else:
        print("✅ GLM_API_KEY configured")
    
    return True

def setup_logging():
    """Setup logging directory"""
    os.makedirs('logs', exist_ok=True)
    logger.info("✅ Logging directory ready")

def main():
    """Main runner function"""
    print("\n" + "="*60)
    print("🤖 YouTube Auto-Clip Bot - Telegram Edition")
    print("="*60)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check API key
    if not check_api_key():
        print("\n❌ Please configure API keys in .env file")
        sys.exit(1)
    
    # Setup logging
    setup_logging()
    
    # Run bot
    print("\n" + "="*60)
    print("🚀 Starting Telegram Bot...")
    print("="*60)
    
    try:
        from src.telegram_bot import TelegramYouTubeBot
        
        bot = TelegramYouTubeBot()
        bot.run()
        
    except KeyboardInterrupt:
        print("\n✅ Bot stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
