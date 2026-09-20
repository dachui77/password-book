#!/bin/bash
echo "🔐 Password Book - 打开方法"
echo ""
echo "请在浏览器地址栏粘贴以下路径："
echo ""
echo "file:///Users/linus/Documents/Codex/password-book/index.html"
echo ""
echo "按 Enter 访问"
echo ""
echo "登录密码: admin123"
echo ""
echo "按任意键复制路径到剪贴板..."
read -n 1
echo "file:///Users/linus/Documents/Codex/password-book/index.html" | pbcopy
echo "✅ 路径已复制到剪贴板，请粘贴到浏览器地址栏"
