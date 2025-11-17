import webbrowser
webbrowser.open("https://t.me/nobi_shops")

import asyncio
import random
from telethon import TelegramClient
from telethon.tl.functions.messages import ReportRequest
from telethon.tl.types import (
    InputReportReasonSpam, 
    InputReportReasonViolence,
    InputReportReasonPornography,
    InputReportReasonChildAbuse,
    InputReportReasonOther
)

API_ID = YOUR_API_ID 
apihash = "YOUR_API_HASH "

class ziddi:
    def __init__(self, api_id, api_hash):
        self.client = TelegramClient('session', api_id, api_hash)
        self.report_reasons = {
            '1': InputReportReasonSpam(),
            '2': InputReportReasonViolence(), 
            '3': InputReportReasonPornography(),
            '4': InputReportReasonChildAbuse(),
            '5': InputReportReasonOther()
        }

    async def start(self):
        await self.client.start()
        print("Telegram'a bağlandı ✓")

    async def report_channel(self):
        channel_link = input("Channel links: ").strip() # by @meta_server
        
        try:
            channel = await self.client.get_entity(channel_link)
            print(f" channel found: {channel.title}")
            

            print("\nTelegram: @meta_server \ @nobi_shops")
            print("1. Spam")
            print("2. Violence")
            print("3. Pornography")
            print("4. child abuse")
            print("5. Other")
            
            choice = input("Your choice (1-5): ").strip()
            if choice not in self.report_reasons:
                print("invalid selection")
                return
            
            reason = self.report_reasons[choice]
            description = ""
            
            if choice == '5':
                description = input("Explanation: ").strip()

            
            messages = await self.client.get_messages(channel, limit=10)
            
            if not messages:
                print("There are no messages in the channel.")
                return

            print(f"{len(messages)} message found.")
            
            success_count = 0
            total_reports = 0
            
            for msg_num, message in enumerate(messages, 1):
                if message.id is None:
                    continue
                
                
                
                
                reports_for_this_msg = random.randint(10, 20)
                
                for report_num in range(1, reports_for_this_msg + 1):
                    try:
                        wait_time = random.uniform(3, 8)
                        await asyncio.sleep(wait_time)
                        

                        result = await self.client(ReportRequest(
                            peer=channel,
                            id=[message.id],
                            reason=reason,
                            message=description
                        ))
                        
                        success_count += 1
                        total_reports += 1
                        
                        if report_num % 5 == 0:
                            print(f"   {report_num}/{reports_for_this_msg} report sent ✅ ") #@meta_server
                            
                    except Exception as e:
                        ''
                        await asyncio.sleep(10)  
                
                

            print(f"Telegram: @meta_server | @nobi_shops !")
            print(f"Total {total_reports} report sent ✅")
            print(f"Channel: {channel.title}")

        except Exception as e:
            ''

    async def stop(self):
        await self.client.disconnect()

async def main():
    bot = ziddi(API_ID, apihash)
    
    try:
        await bot.start()
        await bot.report_channel()
    except KeyboardInterrupt:
        ''
    except Exception as e:
        ''
    finally:
        await bot.stop()
        ''

if __name__ == '__main__':
    asyncio.run(main())
    
    
    
    # tg @meta_server / @nobi_shops
