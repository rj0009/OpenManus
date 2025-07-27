import asyncio

from app.daytona.sandbox import create_sandbox
from app.tool.sb_shell_tool import SandboxShellTool


async def main():
    # 创建沙箱和工具
    sandbox = create_sandbox(password="123456")
    # base_url=sandbox.get_preview_link(8000)
    # print(f"Sandbox base URL: {base_url}")

    print(f"Sandbox ID: {sandbox.id}")

    vnc_link = sandbox.get_preview_link(6080)
    website_link = sandbox.get_preview_link(8080)
    print(f"VNC Link: {vnc_link}")
    print(f"Website Link: {website_link}")
    sb_shell_tool = SandboxShellTool(sandbox)

    # 执行截图操作
    result = await sb_shell_tool.execute(action="execute_command", command="pwd")
    print(result)

    # 清理资源（可选）
    # await sb_shell_tool.cleanup()


if __name__ == "__main__":
    print("123")
    asyncio.run(main())
