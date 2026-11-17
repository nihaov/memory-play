# 熟人局 · Memory Play

用 Agent 对你的记忆，玩点只有你才懂的。

「熟人局」是一组适合休息时打开的创意玩法。它把 Agent 已经知道的那些小事变成插画、建议和短故事。你可以自己挑，也可以让 Agent 给你个惊喜。

## 安装

运行下面的命令，在安装器中选择 Codex 或 Claude Code。加上 `-g` 可在不同项目中使用。

```sh
npx skills add nihaov/memory-play --skill memory-play -g
```

试着说：

- “熟人局，给我个惊喜。”
- “熟人局，把我的脑内世界画出来。”
- “熟人局，给我未来的人生提十条建议。”
- “熟人局，把我最近的日子拍成一部冷幽默纪录片。”

随机抽取或点名时，熟人局会先亮出选中玩法的提示词，再给你结果。比如抽中「脑内世界」时会看到：

> **基于你对我的了解，把我脑中的世界画成一幅图画。**

有可用的记忆时，Agent 可以从里面取材。也可以在当前对话里给它几个关键词。画图玩法需要宿主提供图像工具，纯文本环境会生成生图提示词。

## 更新玩法

公开玩法写在 [docs/catalog.json](docs/catalog.json)，由 [GitHub Pages](https://nihaov.github.io/memory-play/catalog.json) 发布。每次打开熟人局都会尝试读取最新版，网络受限时会用随包安装的入门玩法。目录请求只下载公开玩法，用户的个人上下文由各自的 Agent 使用。

新增玩法时，在目录中加入唯一的 `id`、中英文 `title`、要高亮展示的中英文 `user_prompt`，以及指导 Agent 创作的 `prompt`。玩法更新在 Pages 部署后生效。若修改了 Skill 本身，使用 `npx skills update` 更新安装的版本。
