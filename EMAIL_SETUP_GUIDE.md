# Password Book 邮件日报配置指南

## 收件人
- dacuiw448@gmail.com
- liushu@163.com

## 配置步骤

### 第一步：获取 Gmail 应用专用密码

1. 打开浏览器访问：**https://myaccount.google.com/apppasswords**
2. 登录你的 Gmail 账号（dacuiw448@gmail.com）
3. 在"应用"下拉菜单选择 **"其他（自定义名称）"**
4. 输入名称：`PasswordBook`
5. 点击 **"生成"**
6. 复制生成的 **16 位密码**（格式如：`abcd efgh ijkl mnop`）

### 第二步：修改配置文件

打开文件：`/Users/linus/Documents/Codex/password-book/.env`

将这一行：
```
EMAIL_PASSWORD=YOUR_APP_PASSWORD_HERE
```

改为你的 16 位应用密码（去掉空格）：
```
EMAIL_PASSWORD=abcdefghijklmnop
```

### 第三步：测试发送

在项目目录下运行：
```bash
cd /Users/linus/Documents/Codex/password-book
python3 send_report.py
```

应该看到输出：
```
✓ 邮件已发送至: dacuiw448@gmail.com, liushu@163.com
```

### 第四步：每日自动发送日报

之后每天工作结束时运行：
```bash
./auto_report.sh
```

---

## 常见问题

**Q: 找不到应用专用密码入口？**
A: 确保你的 Google 账号开启了 2FA（两步验证），然后访问 https://myaccount.google.com/apppasswords

**Q: 发送失败？**
A: 检查密码是否正确（16位，无空格），确认账号已开启 SMTP 访问

**Q: 如何更换邮箱？**
A: 修改 `.env` 文件中的 `EMAIL_SENDER` 即可

---

*创建时间: 2026-09-22*
