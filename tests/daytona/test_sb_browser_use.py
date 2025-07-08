from app.tool.sb_browser_tool import SandboxBrowserTool
from app.daytona.sandbox import create_sandbox,start_supervisord_session
import asyncio
from app.utils.logger import logger
from daytona import DaytonaConfig, Daytona
import json
async def main():
    # 创建沙箱和工具
    # sandbox = create_sandbox(password="123456")
    config = DaytonaConfig(
        api_key="dtn_bedf8ed9953f0b5c410c042090e1002a56ba8129b573c92f5607aef04b08c82a",
        api_url="https://app.daytona.io/api",
        target="us"
    )
    daytona = Daytona(config)
    sandbox = daytona.find_one("84fd0b0c-de80-4d2f-b395-e27317248655")
    sandbox.start()
    vnc_link = sandbox.get_preview_link(6080)
    website_link = sandbox.get_preview_link(8080)
    print(f"VNC Link: {vnc_link}")
    print(f"Website Link: {website_link}")
    # sandbox.start()
    # base_url=sandbox.get_preview_link(8000)
    # print(f"Sandbox base URL: {base_url}")

    # print(f"Sandbox ID: {sandbox.id}")
    tool = SandboxBrowserTool(sandbox)

    # # 执行截图操作
    result = await tool.execute(action="navigate_to",url="https://www.google.com")
    print(result)

    # endpoint = "navigate_to"
    # method = "POST"
    # params = {
    #     "url": "https://www.google.com"
    # }
    # url = f"http://localhost:8003/api/automation/{endpoint}"
    # curl_cmd = f"curl -s -X {method} '{url}' -H 'Content-Type: application/json'"
    # json_data = json.dumps(params)
    # curl_cmd += f" -d '{json_data}'"
    # logger.debug(f"Executing curl command: {curl_cmd}")
    # response = sandbox.process.exec(curl_cmd, timeout=30)
    # print(f"Response: {response}")


    # response = sandbox.process.exec("ls -la")
    # print(response.result)
    # 清理资源（可选）
    # await computer_tool.cleanup()

if __name__ == "__main__":
    asyncio.run(main())  # 运行异步主函数
