#!/bin/bash
# 邮箱配置助手
echo "=================================="
echo "  密码本项目邮件配置"
echo "=================================="
echo ""
echo "请准备您的 Gmail 邮箱信息："
echo ""
echo "1. 访问 https://myaccount.google.com/apppasswords"
echo "2. 生成一个应用专用密码（应用选择：其他（自定义名称）= PasswordBook）"
echo "3. 复制生成的 16 位密码"
echo ""
read -p "输入您的 Gmail 地址: " EMAIL
read -s -p "输入应用专用密码: " PASSWORD
echo ""
echo ""
echo "正在保存配置..."
echo "EMAIL_SENDER=$EMAIL" >> ~/.password_book_env
echo "EMAIL_PASSWORD=$PASSWORD" >> ~/.password_book_env
echo ""
echo "✓ 配置已保存到 ~/.password_book_env"
echo ""
echo "使用方法："
echo "  source ~/.password_book_env && python3 send_report.py"
echo ""
