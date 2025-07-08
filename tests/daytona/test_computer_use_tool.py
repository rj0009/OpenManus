from app.tool.computer_use_tool import ComputerUseTool
from app.daytona.sandbox import create_sandbox,start_supervisord_session
import asyncio

async def main():
    # 创建沙箱和工具
    sandbox = create_sandbox(password="123456")
    base_url=sandbox.get_preview_link(8000)
    print(f"Sandbox base URL: {base_url}")

    print(f"Sandbox ID: {sandbox.id}")
    computer_tool = ComputerUseTool.create_with_sandbox(sandbox)

    # 执行截图操作
    result = await computer_tool.execute(action="screenshot")
    print(result)

    # 清理资源（可选）
    await computer_tool.cleanup()

if __name__ == "__main__":
    asyncio.run(main())  # 运行异步主函数
