from aiogram import Router, F
from aiogram.types import Message
from utils.storage import user_languages
from utils.texts import texts
from utils.ai import get_ai_response

router = Router()

@router.message()
async def chat_handler(message: Message):
    user_id = message.from_user.id
    lang = user_languages.get(user_id, "uz") # Default to Uzbek
    
    if message.text:
        # Send a "typing" action to make it feel real
        await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
        
        # Get response from AI
        response_text = await get_ai_response(message.text)
        
        # Check for forwarding tag
        if "||FORWARD:" in response_text:
            try:
                # Extract parts
                parts = response_text.split("||FORWARD:")
                clean_response = parts[0].strip()
                forward_content = parts[1].replace("||", "").strip()
                
                # Send to admin
                import os
                ADMIN_ID = os.getenv("ADMIN_ID")
                if ADMIN_ID:
                    user_info = f"@{message.from_user.username}" if message.from_user.username else f"ID: {message.from_user.id}"
                    admin_msg = f"📩 **Yangi xabar**\n👤 Kimdan: {user_info} ({message.from_user.full_name})\n📝 Xabar: {forward_content}"
                    await message.bot.send_message(chat_id=ADMIN_ID, text=admin_msg)
                
                await message.answer(clean_response)
            except Exception as e:
                print(f"Forwarding error: {e}")
                # Fallback: send original response
                await message.answer(response_text.replace("||FORWARD:", "").replace("||", ""))
        else:
            await message.answer(response_text)
    else:
        await message.answer(texts[lang]["pardon"])
