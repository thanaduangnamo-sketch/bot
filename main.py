import discord
from discord import app_commands
from discord.ext import commands

# ตั้งค่า Bot ตามปกติ
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.default())

    async def setup_hook(self):
        # Sync คำสั่ง Slash กับ Discord
        await self.tree.sync()

bot = MyBot()

@bot.tree.command(name="setup_ticket", description="ตั้งค่าระบบ Ticket ในห้องที่เลือก")
@app_commands.describe(channel="เลือกห้องที่ต้องการให้แสดงปุ่ม Ticket")
async def setup_ticket(interaction: discord.Interaction, channel: discord.TextChannel):
    # ตรวจสอบสิทธิ์
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("คุณไม่มีสิทธิ์ใช้งานคำสั่งนี้", ephemeral=True)
        return

    embed = discord.Embed(
        title="ระบบ Ticket Support",
        description="กดปุ่มด้านล่างเพื่อเปิด Ticket ตามประเภทที่ต้องการ",
        color=discord.Color.blue()
    )
    
    # ส่ง Embed และ View ไปที่ห้องที่เลือก
    await channel.send(embed=embed, view=TicketView())
    await interaction.response.send_message(f"ตั้งค่าระบบ Ticket ในห้อง {channel.mention} เรียบร้อยแล้ว!", ephemeral=True)

# (ส่วนของ TicketView ใช้ Class เดิมจากที่ให้ไปก่อนหน้านี้ได้เลยครับ)

import os # เพิ่มบรรทัดนี้ที่ด้านบนสุดของไฟล์

# เปลี่ยนบรรทัดสุดท้ายเป็นอันนี้
bot.run(os.environ['MTUxMDQ3NTU3MjY4MDMzMTQzNw.GVhshp.HQwgahROh9JUhKc0y6rocEpd5yNlKMtVnwlPoo'])
