# 🔐 Password Book - GitHub 部署指南

## 当前状态
- ✅ 代码已准备好：`/Users/linus/Documents/Codex/password-book/`
- ❌ 网络无法连接 GitHub（需要手动操作）

---

## 📤 第一步：推送代码到 GitHub

### 方法一：使用 GitHub Desktop（推荐新手）
1. 下载安装 [GitHub Desktop](https://desktop.github.com/)
2. 登录你的 GitHub 账号 (dachui77)
3. 点击 `File` → `Add local repository`
4. 选择文件夹：`/Users/linus/Documents/Codex/password-book/`
5. 点击 `Continue`
6. 点击 `Publish repository`
   - Repository name: `password-book`
   - Keep this code private（可选）
   - 点击 `Publish repository`

### 方法二：使用终端命令
```bash
cd /Users/linus/Documents/Codex/password-book

# 配置 Git 用户信息（如果还没配置）
git config --global user.name "dachui77"
git config --global user.email "你的邮箱@example.com"

# 推送代码（需要 GitHub Token）
git push -u origin main
```

**获取 GitHub Token：**
1. 打开 https://github.com/settings/tokens
2. 点击 `Generate new token (classic)`
3. 勾选 `repo` 权限
4. 点击 `Generate token`
5. 复制生成的 Token（只显示一次！）

**使用 Token 推送：**
```bash
git push https://dachui77:YOUR_TOKEN@github.com/dachui77/password-book.git
```

---

## 🌐 第二步：启用 GitHub Pages

### 自动启用（推荐）
1. 打开 https://github.com/dachui77/password-book/settings/pages
2. 在 "Source" 下选择 `Deploy from a branch`
3. 选择分支：`main`
4. 选择文件夹：`/ (root)`
5. 点击 `Save`

### 手动启用（创建 gh-pages 分支）
```bash
cd /Users/linus/Documents/Codex/password-book

# 创建 gh-pages 分支并推送
git checkout -b gh-pages
git push -u origin gh-pages

# 切回 main 分支
git checkout main
```

启用后，你的网站将在：
- `https://dachui77.github.io/password-book/`

---

## 🔗 第三步：配置二级域名

### 需要的 DNS 记录

访问你的域名注册商（如 Cloudflare、Namecheap、GoDaddy 等），添加以下 DNS 记录：

#### A 记录方式（推荐）
```
类型: A
名称: password-book
值: 185.199.108.153
TTL: 自动或 300
```

然后添加以下 CNAME 记录：
```
类型: CNAME
名称: password-book.test260326.eu.cc
值: dachui77.github.io.
```

#### 或者 CNAME 方式
```
类型: CNAME
名称: password-book
值: dachui77.github.io.
```

### GitHub Pages 自定义域名配置

1. 打开 https://github.com/dachui77/password-book/settings/pages
2. 在 "Custom domain" 输入：`password-book.test260326.eu.cc`
3. 点击 `Save`
4. 勾选 `Enforce HTTPS`（如果可用）

### 等待 DNS 生效
- DNS 传播通常需要 5-30 分钟
- 可以使用 `dig password-book.test260326.eu.cc` 检查

---

## 📁 第四步：确保文件正确

确认仓库根目录包含以下文件：
```
password-book/
├── index.html      # 主应用文件
├── README.md       # 项目说明
└── .github/
    └── ISSUE_TEMPLATE/
        └── feature_request.md
```

**重要：** 确保 `index.html` 在仓库根目录，不是子文件夹。

---

## ✅ 验证部署

访问以下地址验证：
1. GitHub Pages: https://dachui77.github.io/password-book/
2. 自定义域名: https://password-book.test260326.eu.cc

如果看到登录页面，说明部署成功！

---

## 🐛 故障排除

### 问题 1：显示 404
- 检查是否启用了 GitHub Pages
- 检查 `index.html` 是否在根目录
- 等待 5-10 分钟让 Pages 部署完成

### 问题 2：DNS 解析失败
- 检查 DNS 记录是否正确
- 等待 DNS 传播（最长 48 小时）
- 尝试使用 `185.199.108.153` 等 GitHub Pages IP

### 问题 3：HTTPS 证书错误
- 在 GitHub Pages 设置中勾选 `Enforce HTTPS`
- 等待证书签发（可能需要几分钟）

---

## 📞 需要帮助？

如果遇到问题，可以在 GitHub Issue 中提问。
