# 邮件日报配置说明

## 功能说明
每天工作结束后，自动发送工作日志到邮箱：
- 你的邮箱@gmail.com
- 收件人邮箱@example.com

## 配置步骤

### 1. 获取 Gmail 应用密码
1. 访问 https://myaccount.google.com/apppasswords
2. 登录您的 Gmail 账号
3. 在"应用"下拉菜单选择"其他（自定义名称）"
4. 输入名称：`PasswordBook`
5. 点击"生成"
6. 复制生成的 16 位密码（格式：`abcd efgh ijkl mnop`）

### 2. 运行配置脚本
```bash
cd <项目目录>/
./setup_email.sh
```

### 3. 输入邮箱信息
```
输入您的 Gmail 地址: your_email@gmail.com
输入应用专用密码: abcd efgh ijkl mnop
```

### 4. 测试发送
```bash
source ~/.password_book_env
python3 send_report.py
```

## 使用方法

### 手动发送日报
```bash
cd <项目目录>/
./auto_report.sh
```

### 发送到指定邮箱
```bash
# 临时设置环境变量
export EMAIL_SENDER='your@gmail.com'
export EMAIL_PASSWORD='abcd efgh ijkl mnop'
python3 send_report.py /path/to/project "今日工作摘要"
```

## 邮件内容
- 主题：`[密码本日报] 标题 - YYYY-MM-DD`
- 正文：工作日志内容
- 附件：WORK_LOG.md

## 注意事项
1. Gmail 需要开启"不安全应用访问"或使用应用专用密码
2. 163 邮箱可能需要开启 SMTP 服务
3. 应用密码比普通密码更安全，建议定期更换（切勿提交到仓库）

---
*配置时间: 2026-09-22*
