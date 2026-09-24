#!/bin/bash
echo "🔐 Password Book 服务器启动脚本"
echo ""
echo "步骤1: 关闭旧服务器"
kill 98728 2>/dev/null
sleep 1

echo "步骤2: 启动新服务器"
cd /Users/linus/Documents/Codex/password-book
python3 -m http.server 8000 &
sleep 2

echo ""
echo "✅ 服务器已启动!"
echo "📍 访问地址: http://localhost:8000"
echo "🔑 登录密码: admin123"
echo ""
echo "请按 Cmd+Shift+R 强制刷新浏览器"
