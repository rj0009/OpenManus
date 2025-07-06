from app.tool.sb_shell_tool import SandboxShellTool
from app.daytona.sandbox import create_sandbox
import asyncio

async def main():
    # 创建沙箱和工具
    sandbox = create_sandbox(password="123456")
    base_url=sandbox.get_preview_link(8000)
    print(f"Sandbox base URL: {base_url}")

    print(f"Sandbox ID: {sandbox.id}")
    sb_shell_tool = SandboxShellTool.create_with_sandbox(sandbox)

    # 执行截图操作
    result = await sb_shell_tool.execute(action="execute_command", command="ls")
    print(result)

    # 清理资源（可选）
    await sb_shell_tool.cleanup()

if __name__ == "__main__":
    print("123")
    asyncio.run(main())