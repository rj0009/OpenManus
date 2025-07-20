from app.tool.sb_files_tool import SandboxFilesTool
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

    sb_files_tool = SandboxFilesTool(sandbox)


    # 执行创建文件操作
    result = await sb_files_tool.execute(action="create_file", file_path="src/a.txt", file_contents="aaaaa1111")
    print(result)
    # 执行字符串替换操作
    # result = await sb_files_tool.execute(action="str_replace", file_path="src/a.txt", old_str="aaaaa", new_str="bbbbb")
    # print(result)
    # 执行全文件重写操作
    result = await sb_files_tool.execute(action="full_file_rewrite", file_path="src/a.txt", file_contents="1234567")
    print(result)
    # 执行删除文件操作
    # result = await sb_files_tool.execute(action="delete_file", file_path="src/a.txt")
    # print(result)
    # 清理资源（可选）
    # await sb_shell_tool.cleanup()

if __name__ == "__main__":
    asyncio.run(main())