from app.tool.sb_shell_tool import SandboxShellTool
from app.tool.sb_vision_tool import SandboxVisionTool
from app.daytona.sandbox import create_sandbox
import asyncio



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
    sb_vision_tool = SandboxVisionTool(sandbox)

    # 执行终端命令
    result = await sb_shell_tool.execute(action="execute_command", command="curl -O http://img.netbian.com/file/2025/0716/091412RIFD9.jpg")
    print(result)
    # 执行see_image操作
    result = await sb_vision_tool.execute(action="see_image", file_path="091412RIFD9.jpg")
    print(result)

    # 清理资源（可选）
    # await sb_shell_tool.cleanup()

if __name__ == "__main__":
    asyncio.run(main())