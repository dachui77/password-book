# 🔐 Password Book 使用说明

## 服务器问题解决方案

由于权限限制，需要在你的终端中手动重启服务器。

### 步骤1: 打开终端

按 `Cmd + 空格`，输入 `terminal`，回车

### 步骤2: 执行以下命令

```bash
# 关闭旧服务器
kill 98728

# 进入项目目录
cd /Users/linus/Documents/Codex/password-book

# 启动新服务器
python3 -m http.server 8000
```

### 步骤3: 刷新浏览器

在浏览器中按 `Cmd + Shift + R` 强制刷新

### 步骤4: 登录应用

- 访问地址: http://localhost:8000
- 登录密码: admin123

---

## 如果还是看不到更新

### 清除浏览器缓存

1. 按 `Cmd + Shift + Delete`
2. 选择「缓存的图像和文件」
3. 点击清除

### 或使用无痕模式

- Chrome: `Cmd + Shift + N`
- Safari: `Cmd + Shift + P`

---

## 当前已实现功能

✅ 5分类系统（网站/邮箱/社交/软件/其它）  
✅ 密码生成器（8-24位，字符选项）  
✅ 密码强度指示  
✅ 2FA双因素认证  
✅ 用户名自动补全  
✅ 导入/导出功能  
✅ 邮件日报配置  

---

*如有疑问，请告诉我你看到的具体界面内容*
