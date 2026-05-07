# vX.Y.Z

## 本次更新

- 
- 
- 

## 当前支持环境

- 平台：`Windows x64`
- 游戏渠道：`Steam 版 龙吟立志传`
- 游戏运行时：`Unity IL2CPP`
- 加载器（二选一，不要叠装）：
  - `BepInEx-Unity.IL2CPP-win-x64-6.0.0-be.755+3fab71a.zip`
  - `MelonLoader 0.7.x x64 IL2CPP`

## 当前功能

- `=` 键开关
- 武学经验倍率（读书）
- 武学经验倍率（实战）
- 技艺经验倍率
- 好感增长倍率
- 门派&官府功绩倍率
- 抄书效率与花费调整

## 说明

- 当前实现优先保证实际入账生效与启动稳定性。
- 武学经验与技艺经验倍率对走同一套入账路径的 NPC 同样生效，属于当前版本设计行为。

## 安装方式

BepInEx 路径：

1. 先安装固定版本的 `BepInEx`
2. 先单独启动一次游戏，确认 `BepInEx` 能正常生成日志
3. 将 `RisingFame.dll` 放入 `BepInEx/plugins/`
4. 手动启动游戏测试

MelonLoader 路径：

1. 先安装 `MelonLoader 0.7.x` x64 IL2CPP
2. 先单独启动一次游戏，确认 `MelonLoader/Latest.log` 已生成、Il2Cpp 程序集已生成
3. 将 MelonLoader 资产 `RisingFame.dll` 放入 `Mods/`
4. 手动启动游戏测试；倍率可在 `UserData/RisingFame.cfg` 调整

## QA / 反馈时请提供

1. 加载器日志：BepInEx 用户提供 `BepInEx/LogOutput.log`，MelonLoader 用户提供 `MelonLoader/Latest.log`
2. 游戏根目录截图
3. 你下载的加载器安装包完整文件名
