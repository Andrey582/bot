import vk_api
import random

import sel

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random.randint(-2000000000, 2000000000)})


# API-ключ созданный ранее
token = "430728c88b0dd724dec66b18422cb96c339c1030787eb8fa71d338cc2eebc61c02e6b8e2b49f67aff6990"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

write_msg(4658426, sel.Get_Page())
#write_msg(505191416, sel.Get_Page())