import aiohttp ,asyncio
async def gpt4o(message,lang):
    session = aiohttp.ClientSession()
    headers = {"content-type":"application/json","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","origin":"https://www.blackbox.ai","referer":"https://www.blackbox.ai/chat/",}
    async with session.post('https://www.blackbox.ai/api/chat',json={"messages":[{"role":"user","content":f"always speak {lang}","id":None},{"id":None,"createdAt":"","content":"Of course! I will communicate in English. How can I assist you today?","role":"assistant"},{"id":None,"content":message,"role":"user"}],"id":None,"previewToken":None,"userId":None,"codeModelMode":True,"agentMode":{},"trendingAgentMode":{},"isMicMode":False,"userSystemPrompt":None,"maxTokens":1024,"playgroundTopP":0.9,"playgroundTemperature":0.5,"isChromeExt":False,"githubToken":"","clickedAnswer2":False,"clickedAnswer3":False,"clickedForceWebSearch":False,"visitFromDelta":False,"mobileClient":False,"userSelectedModel":"gpt-4o","validated":"00f37b34-a166-4efb-bce5-1312d87f2f94","imageGenerationMode":False,"webSearchModePrompt":False},headers=headers)as res:
        resp = await res.text()
    await session.close()
    print(resp)
    return resp
