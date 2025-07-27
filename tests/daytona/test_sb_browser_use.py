import asyncio
import json

from daytona import Daytona, DaytonaConfig

from app.daytona.sandbox import create_sandbox, start_supervisord_session
from app.tool.sb_browser_tool import SandboxBrowserTool
from app.utils.logger import logger


async def main():
    # 创建沙箱和工具
    sandbox = create_sandbox(password="123456")
    # config = DaytonaConfig(
    #     api_key="",
    #     api_url="https://app.daytona.io/api",
    #     target="us"
    # )
    # daytona = Daytona(config)
    # sandbox = daytona.find_one("201415a9-28ad-4b6d-8756-13b1e34a70c3")
    # if sandbox.state == "archived" or sandbox.state == "stopped":
    #     logger.info(f"Sandbox is in {sandbox.state} state. Starting...")
    #     try:
    #         daytona.start(sandbox)
    #         start_supervisord_session(sandbox)
    #         # Wait a moment for the sandbox to initialize
    #         # sleep(5)
    #         # Refresh sandbox state after starting
    #         # sandbox = daytona.get(sandbox.id)
    #     except Exception as e:
    #         logger.error(f"Error starting sandbox: {e}")
    #         raise e

    # sandbox.start()
    vnc_link = sandbox.get_preview_link(6080)
    website_link = sandbox.get_preview_link(8080)
    computer_link = sandbox.get_preview_link(8000)
    print(f"VNC Link: {vnc_link}")
    print(f"Website Link: {website_link}")
    print(f"Computer Link: {computer_link}")
    # sandbox.start()
    # base_url=sandbox.get_preview_link(8000)
    # print(f"Sandbox base URL: {base_url}")

    # print(f"Sandbox ID: {sandbox.id}")
    tool = SandboxBrowserTool(sandbox)

    # # 执行截图操作
    result, tooresult = await tool.execute(
        action="navigate_to", url="https://www.github.com"
    )
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
    # await computer_tool.cleanup()

if __name__ == "__main__":
    asyncio.run(main())  # 运行异步主函数
    # await computer_tool.cleanup()

if __name__ == "__main__":
    asyncio.run(main())  # 运行异步主函数
    # await computer_tool.cleanup()

if __name__ == "__main__":
    asyncio.run(main())  # 运行异步主函数
