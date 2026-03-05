from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
collection = db['your_collection']

async def delete_edited_messages(message):
    # Check if the message is edited and user is not authenticated
    if message.edit_date and not is_authenticated_user(message.from_user.id):
        # Delete the message from MongoDB
        collection.delete_one({'message_id': message.message_id})

        # Send the popup to the user with inline buttons
        await message.reply(
            'This message has been deleted. If you need support, click below:',
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('Support Chat', url='http://support_chat_link'), InlineKeyboardButton('Updates', url='http://updates_link')]
            ])
        )

def is_authenticated_user(user_id):
    # Logic to check if user is authenticated
    return user_id in AUTHORIZED_USER_IDS
