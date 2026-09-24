#!/bin/bash
# Password Book 本地服务器启动脚本（macOS / Linux）
# Windows 用户请直接运行： node server.js
echo "🔐 Password Book 服务器启动脚本"
echo ""

cd "$(dirname "$0")" || exit 1

echo "正在启动本地服务器（端口 3457）..."
node server.js &
sleep 2

echo ""
echo "✅ 服务器已启动"
echo "📍 访问地址: http://127.0.0.1:3457"
echo ""
echo "提示：登录密码请在应用内「设置」中自行修改，不要使用默认值"
