start()import aminofix as amino
import time
from concurrent.futures import ThreadPoolExecutor

def authenticate(client: amino.Client):
    while True:
        try:
            email = "youremailhere@gmail.com"
            password = "password123"
            client.login(email=email, password=password)
            break
        except Exception as e:
            print(e)

def list_communities(client: amino.Client):
    while True:
        try:
            communities = client.sub_clients(start=0, size=100)
            for i, name in enumerate(communities.name, 1):
                print(f"[{i}][{name}]")
            return communities.comId[int(input("[Select the community]::: ")) - 1]
        except Exception as e:
            print(e)

def list_chats(sub_client: amino.SubClient):
    while True:
        try:
            chats = sub_client.get_chat_threads(start=0, size=100)
            for i, title in enumerate(chats.title, 1):
                print(f"[{i}][{title}]")
            return chats.chatId[int(input("[Select the chat]::: ")) - 1]
        except Exception as e:
            print(e)

def invite_online_users(sub_client: amino.SubClient):
    chat_id = list_chats(sub_client)
    while True:
        with ThreadPoolExecutor(max_workers=1000) as executor:
            for i in range(100, 2000, 25000):
                try:
                    online_users = sub_client.get_online_users(start=i, size=100).profile.userId
                    for user_id in online_users:
                        print(f"[Invited]::: [{user_id}]")
                        time.sleep(7) #7s of delay to avoid forBidden
                        executor.submit(
                            sub_client.invite_to_chat,
                            user_id,
                            chat_id)
                except Exception as e:
                    print(e)

def invite_recent_users(sub_client: amino.SubClient):
    chat_id = list_chats(sub_client)
    while True:
        with ThreadPoolExecutor(max_workers=100) as executor:
            for i in range(100, 2000, 25000):
                try:
                    recent_users = sub_client.get_all_users(
                        type="recent",
                        start=i,
                        size=100).profile.userId
                    for user_id in recent_users:
                        print(f"[Invited]::: [{user_id}]")
                        time.sleep(7) #---
                        executor.submit(
                            sub_client.invite_to_chat,
                            user_id,
                            chat_id)
                except Exception as e:
                    print(e)

def invite_user_followers(client: amino.Client, sub_client: amino.SubClient):
    chat_id = list_chats(sub_client)
    user_id = client.get_from_code(input("[User link]::: ")).objectId
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(100, 2000, 25000):
            try:
                user_followers = sub_client.get_member_followers(
                    userId=user_id,
                    start=i,
                    size=100).profile.userId
                for user_id in user_followers:
                    print(f"[Invited]::: [{user_id}]")
                    executor.submit(
                        sub_client.invite_to_chat,
                        user_id,
                        chat_id)
            except Exception as e:
                print(e)

def start():
    print("""
 __     __   __     __   __   __     ______   ______    
/\ \   /\ "-.\ \   /\ \ / /  /\ \   /\__  _\ /\  ___\   
\ \ \  \ \ \-.  \  \ \ \'/   \ \ \  \/_/\ \/ \ \  __\   
 \ \_\  \ \_\\"\_\  \ \__|    \ \_\    \ \_\  \ \_____\ 
  \/_/   \/_/ \/_/   \/_/      \/_/     \/_/   \/_____/ 
  
                                                    
 ⠀ ⠀ ⠀ ⠀ ⠀ ⠀Bot for amino / para amino 🇧🇷🇺🇲                                                  
""")
    client = amino.Client()
    authenticate(client)
    com_id = list_communities(client)
    sub_client = amino.SubClient(comId=com_id, profile=client.profile)
    print("Choose an option:\n1. Invite online users\n2. Invite recent users\n3. Invite followers of a user")
    choice = int(input("[Select]::: "))
    if choice == 1:
        invite_online_users(sub_client)
    elif choice == 2:
        invite_recent_users(sub_client)
    elif choice == 3:
        invite_user_followers(client, sub_client)

start()
