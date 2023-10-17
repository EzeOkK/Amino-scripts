import aminofix as amino
import time

print(
    f"""
 __      __     ______      __         __        
/\ \  __/\ \   /\  _  \    /\ \       /\ \       
\ \ \/\ \ \ \  \ \ \L\ \   \ \ \      \ \ \      
 \ \ \ \ \ \ \  \ \  __ \   \ \ \  __  \ \ \  __ 
  \ \ \_/ \_\ \  \ \ \/\ \   \ \ \L\ \  \ \ \L\ \
   \ `\___x___/   \ \_\ \_\   \ \____/   \ \____/
    '\/__//__/     \/_/\/_/    \/___/     \/___/ 
                                                 
                                                     

 ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀spam !! 🇧🇷/🇺🇲
""")

client = amino.Client()

email = "you@gmail.com"
password = "senha123"
client.login(email=email, password=password)

link_info = client.get_from_code(input("-- User link::: "))
com_id = link_info.comId
user_id = link_info.objectId

sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = "--"

while True:
    try:
        sub_client.comment(message, userId=user_id)
        print("-- Comment is sent...")
        time.sleep(7) # 7 s to avoid forBidden and punishments from communities.
    except Exception as e:
        print(e)
