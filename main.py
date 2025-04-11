#coded by wezaxy.
from wezaxy.test import test
import json
import asyncio

async def main():
    while True:
        with open('config.json', 'r') as fs:
            config = json.load(fs)

        use_proxy = config.get('use_proxy', False)
        username = config.get('username')
        password = config.get('password')
        language = config.get('language')
        group_messages = config.get('group_messages')

        if not username or not password or not language:
            print("Required information is empty in config.json")
            break

        if use_proxy:
                with open('proxies.txt', 'r') as proxy_file:
                    proxies = proxy_file.read().splitlines()
                for proxy in proxies:

                    result = await test(username, password, language, proxy,group_messages)
                    print("the last dm message that came in:",result)

        else:
            
            result = await test(username, password, language, None,group_messages)
            print("the last dm message that came in:",result)
        if use_proxy is False:
         await asyncio.sleep(2) 

if __name__ == "__main__":
    asyncio.run(main())
