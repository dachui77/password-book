#!/bin/bash
echo "🔐 Password Book - 访问方式"
echo ""
echo "方式一：直接访问（推荐）"
echo "  浏览器打开: http://localhost:18923"
echo ""
echo "方式二：file 协议"
echo "  浏览器打开: file:///Users/linus/Documents/Codex/password-book/index.html"
echo ""
echo "方式三：局域网访问（手机/平板）"
echo "  浏览器打开: http://192.168.3.229:18923"
echo ""
echo "登录密码: admin123"
echo ""
echo "按 Enter 复制地址..."
read -n 1
echo "http://localhost:18923" | pbcopy
echo ""
echo "✅ 地址已复制到剪贴板"
