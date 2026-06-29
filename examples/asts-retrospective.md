# ASTS Investment Retrospective

> 研究教育用途；不是买入、卖出、持有建议，也不提供目标价或未来收益预测。本文遵循本仓库的 `Investment Retrospective Skill`：先识别价格异常，再做基准比较，最后才讨论归因与叙事。

## 0. Scope

- 公司：AST SpaceMobile, Inc.
- 股票代码：ASTS
- 研究区间：2024-01-02 至 2026-06-29
- 完整收盘价截止：2026-06-26；2026-06-29 仅作信息截止日，不把盘中价格纳入事件收益
- 主题：低轨卫星直连普通手机（direct-to-device / D2D）
- 核心问题：市场何时从“融资与发射执行可能失败”转向“运营商、监管者与真实网络部署共同验证商业化路径”？这次转变是基本面确认、预期重置，还是主要由高贝塔与资金流推动？
- 基准：QQQ；航天主题 ETF UFO、ARKX；等权同业篮子 GSAT、IRDM、RKLB
- 同业限制：没有与 ASTS 完全同构的上市公司。GSAT 更接近卫星直连，IRDM 是成熟 MSS，RKLB 偏航天基础设施，因此同业篮子只能控制部分航天主题 beta。
- 回报口径：未复权 regular-session close-to-close；T+1 从 T-1 收盘到有效 T0 收盘；T+5/T+20 以相同基准价计算至第 5/20 个交易日收盘。

## 0.1 First-read Finding Card

- **Sharp finding:** ASTS 的巨大重估不是“卫星发射成功”的简单故事，而是市场逐步降低了融资失败、运营商不付费、美国监管路径不成立这三个失败概率。
- **Strongest evidence:** AT&T 正式协议、Verizon 1 亿美元承诺、Vodafone 客户侧测试、FCC 商业许可。
- **Most misleading false signal:** 单纯发射成功。Block 1 发射成功后 T+20 反而明显跑输基准。
- **Current classification:** Level 3 — externally validated candidate commercial-pathway shift。
- **Still unproven:** 不是 Level 4/5，因为缺少 SpaceMobile 服务收入、可靠估值重估、一致预期修订、连续覆盖和单位经济性。
- **Fact confidence:** High
- **Reaction confidence:** High for the principal abnormal windows
- **Causal Attribution confidence:** Medium；W2 的幅度可能受定位/动量放大，W5 是不可拆分的多事件簇。

### Executive Attribution Takeaway

| 窗口 | 价格异常 | 最受证据支持的发现 | 当时真正改变的假设 | Reaction confidence | Causal attribution confidence |
|---|---:|---|---|---|---|
| W1，2024-05-16 | 1D +68.62%；5D +94.77% | AT&T 正式商用协议触发预期重置 | 商业伙伴从 MOU 变成正式客户；融资与美国落地路径同时改善 | High | Medium（T+20 被 W2 污染） |
| W2，2024-05-29 | 1D +69.23%；20D +110.69% | 最强的外部商业验证窗口 | Verizon 的 1 亿美元承诺表明两家美国头部运营商愿意共同采用 AST 架构 | High | Medium；事件证据强，但价格幅度可能受定位与动量放大 |
| W3，2024-08-15 | 1D +50.70%；20D +28.74% | 发射执行风险显著下降 | 五颗卫星已到发射场、FCC 初始许可、9 月发射时间更确定 | High | Medium |
| W5，2025-01-30 起 | 5D +39.45%；20D +47.18% | 客户侧技术验证 + 美国测试许可的事件簇 | Block 1 从“已入轨硬件”变成客户与监管可实际测试的网络 | High | Medium；多事件重叠，不能拆分单一催化剂 |
| W9，2026-04-20 | 1D -5.30%；5D -10.67% | 单次发射失败造成执行风险重估 | 多发射商策略降低但没有消除任务失败和部署延期风险 | High | Medium-High |
| W10，2026-04-22 | 1D +5.81%；5D -10.16%；20D +10.11% | 监管基本面改善，但没有形成持续的独立重估 | 美国商业许可从主要待决项变为获批；价格却很快被部署风险与板块波动覆盖 | Medium | Low-Medium |
| W11，2026-06-17 | 1D +3.87%；5D -17.31%；T+20 Pending | 三星同箭成功是经营进展，不是即时正向叙事确认 | 生产与发射吞吐改善；市场仍要求后续展开、在轨测试和连续发射 | High（负向跟随） | Pending |

**当前结论：** ASTS 已经完成了从“公司自述的技术项目”到“运营商、监管机构和发射伙伴外部验证的候选商业网络”的叙事升级，适合归类为 **Level 3：Externally validated candidate shift**。现有公开数据不足以升级为 Level 4/5：缺少可靠的历史一致预期与远期估值数据库，而且截至 2026 年一季度，公司仍未确认任何 SpaceMobile 服务收入。事实置信度 High；主要拐点的反应置信度 High；整体因果归因置信度 Medium。

## 1. Original Market Fear

### 1.1 被记录下来的恐惧

2024 年初的核心恐惧不是“技术完全不可行”，而是以下三个互相强化的问题：

1. **融资/稀释风险。** 2024-01-18 公司一边公布 AT&T、Google、Vodafone 的战略承诺，一边启动 1 亿美元普通股发行；次日 ASTS 下跌 25.72%。这说明市场把战略背书与低价融资压力同时计价。[S1]
2. **重复延期与供应链执行风险。** 2024-04-01 公司把首批五颗商业卫星运往发射场的预期移至 7–8 月；2024-04-02 股价下跌 23.57% 至 2.01 美元。同期行业报道和分析师评论把担忧明确指向供应商问题、发射延期及收入延后。[S2][S3]
3. **商业协议能否从 MOU 变为付款与收入。** 当时网络尚未上线，2023 年收入为零；因此运营商兴趣是否能变成正式协议、预付款、频谱接入和真实用户服务，是商业模式可行性的关键假设。[S2]

### 1.2 恐惧门槛检查

- 至少两个同期指标：1 月股权融资后的异常下跌；4 月再次延迟后的异常下跌。
- 与经营/估值假设直接相连：延期推迟发射与潜在收入；低价发行提高未来融资与稀释风险。
- 不是两个媒体重复同一来源：公司 SEC 披露、市场价格、分析师/行业报道构成不同证据层。
- 结论：这是 **documented fear — High confidence**，不是从后来的股价上涨倒推出来的故事。

### 1.3 后来是否解决

| 恐惧 | 后续证据 | 状态 |
|---|---|---|
| 五颗 Block 1 无法按新计划完成并发射 | 2024-09-12 五颗卫星成功发射，随后完成阵列展开 | Resolved for Block 1 |
| 技术只能停留在公司演示 | Vodafone、AT&T、Verizon、Rakuten 均参与普通手机视频/宽带测试；FCC 后续批准商业 SCS | Partially resolved；规模化容量仍待验证 |
| 美国没有商业监管路径 | FCC 于 2026-04 批准最多 248 颗星座及 SCS 商业服务 | Largely resolved for authorization；仍需满足许可条件与运营合规 |
| 资金不足以建设星座 | 2026-03-31 现金、现金等价物及受限现金约 34.59 亿美元；公司称足以覆盖未来 12 个月，并认为约 90 颗星座已获资金覆盖 | Partially resolved；融资结构、受限现金、债务、稀释和超支风险仍在 |
| 正式服务能否产生可持续收入 | 2025 年收入 7,091.8 万美元、2026Q1 收入 1,473.5 万美元，但来源主要是网关设备与美国政府项目；截至 2026Q1 尚无 SpaceMobile 服务收入 | Unresolved |

## 2. Event Timeline

| 日期 | 事件 | 类型 | 当时可知的信息 | 证据等级 |
|---|---|---|---|---|
| 2024-01-18 | 战略投资/商业承诺与 1 亿美元股权发行同时公布 | 融资、伙伴 | 战略背书改善，但低价股权融资说明资金缺口仍大 | Tier 1 / Grade A |
| 2024-04-01 | 首五颗卫星运往发射场预期移至 7–8 月 | 执行、延期 | 供应链与制造节奏仍是硬约束 | Tier 1 + Tier 2 / Grade A-B |
| 2024-05-15 | AT&T 签署至 2030 年的正式商业协议 | 客户验证 | MOU 升级为 definitive agreement；首五颗卫星仍以 7–8 月交付为目标 | Tier 1 customer-side / Grade A |
| 2024-05-29 | Verizon 战略合作并承诺 1 亿美元 | 客户、融资 | 包含商业预付款和可转债；美国两大运营商共同支持 AST 路径 | Tier 1 / Grade A |
| 2024-08-14 | 首五颗卫星抵达发射场、FCC 初始许可、9 月上半月发射 | 执行、监管 | 4 月最主要的延期恐惧被具体里程碑反驳 | Tier 1 / Grade A |
| 2024-09-12 | 五颗 Block 1 BlueBird 成功入轨 | 发射 | 单次任务成功，但仍需展开、测试、许可和更多卫星 | Tier 1 / Grade A |
| 2025-01-29 至 01-31 | Vodafone 普通手机视频通话；FCC 给予美国测试 STA | 客户技术验证、监管 | Block 1 真正连接客户网络；美国可用 AT&T/Verizon 频谱测试 | Tier 1 customer + regulator context / Grade A-B |
| 2025-10-08 | Verizon 签署正式商业协议，目标 2026 年服务 | 客户、商业化 | 2024 战略合作升级为正式服务关系 | Tier 1 / Grade A |
| 2025-10-29 | stc 签署 10 年协议并承诺 1.75 亿美元预付款 | 客户、商业化 | 外部需求扩展到 MENA；形成有金额的商业承诺 | Tier 1 / Grade A |
| 2025-12-23 | BlueBird 6 成功入轨；其后展开 Block 2 大型阵列 | 发射、技术 | 下一代卫星从计划变成在轨硬件 | Tier 1 launch provider / Grade A |
| 2026-04-19 | BlueBird 7 被运载火箭送入过低轨道，将再入；预计保险赔付 | 负面执行 | 多发射商不能消除单任务失败；单星损失不等于平台失败 | Tier 1 filing / Grade A |
| 2026-04-21/22 | FCC 批准最多 248 颗星座及美国 SCS 商业服务 | 监管 | 美国核心监管“是否获批”问题显著下降 | Tier 1 regulator / Grade A |
| 2026-06-17 | SpaceX 一箭发射并部署 BlueBird 8、9、10 | 制造与发射吞吐 | 首次一次部署三颗 Block 2；仍需阵列展开和在轨测试 | Tier 1 launch provider / Grade A |

## 3. Event Window Map

| ID | Anchor | 披露时间 | Effective T0 | Pre-event fear/setup | 主要归因测试 |
|---|---|---|---|---|---|
| W0 | 2024Q4/FY23 update：再次延期 | 2024-04-01 after close | 2024-04-02 | 延期、融资、收入推迟 | 是否出现公司特定下跌 |
| W1 | AT&T 正式商业协议 + Q1 update | 2024-05-15 after close | 2024-05-16 | MOU 能否转正式客户 | 是否相对市场/航天/同业持续异常上涨 |
| W2 | Verizon 1 亿美元战略承诺 | 2024-05-29 07:30 ET | 2024-05-29 | 是否只有 AT&T 单一伙伴 | 第二家美国头部运营商是否构成独立验证 |
| W3 | Q2 update / 发射就绪 | 2024-08-14 after close | 2024-08-15 | 首五颗是否再次延期 | 发射准备、FCC 许可、生产是否降低执行风险 |
| W4 | Block 1 发射成功 | 2024-09-12 pre-market | 2024-09-12 | 发射硬失败风险 | 成功发射是否带来正向跟随，还是 sell-the-news |
| W5 | Vodafone 视频通话 + FCC STA 事件簇 | 2025-01-29 after close 起 | 2025-01-30 | 在轨硬件能否连接真实客户网络 | 客户侧演示与监管许可是否形成联合验证 |
| W6 | Verizon 正式商业协议 | 2025-10-08 pre-market | 2025-10-08 | 战略关系能否转正式服务 | T+20 是否保持异常收益 |
| W7 | stc 10 年协议 + 1.75 亿美元预付款 | 2025-10-29 pre-market | 2025-10-29 | 海外需求和付款意愿 | 金额明确的合同是否改变市场模型 |
| W8 | BlueBird 6 成功发射 | 2025-12-23 late evening | 2025-12-24 | Block 2 是否能真正入轨 | 即时与 20 日反应是否一致 |
| W9 | BlueBird 7 入轨失败 | 2026-04-19 weekend | 2026-04-20 | 单任务失败与部署延期 | 是否出现持续的公司特定负收益 |
| W10 | FCC 商业 SCS 授权 | 2026-04-21 order / 04-22 release | 2026-04-22 | 美国商业许可是否获批 | 监管利好是否产生持续异常收益 |
| W11 | BlueBird 8–10 成功部署 | 2026-06-17 pre-market | 2026-06-17 | BB7 后制造与发射节奏 | 三星同箭是否恢复执行信心；T+20 Pending |

## 4. Claim Ledger

| Claim ID | Window | Claim class | Claim | Source | Fact confidence | Reaction confidence | Causal Attribution confidence |
|---|---|---|---|---|---|---|---|
| C0F | W0 | Fact | 2024-04-02 ASTS 下跌 23.57%，同期公司披露首五颗卫星运往发射场推迟到 7–8 月 | S2, S3, S16 | High | High | Medium-High |
| C1F | W1 | Fact | AT&T 与 ASTS 签署至 2030 年的正式商业协议 | S4 | High | N/A | N/A |
| C1I | W1 | Inference | 正式协议降低了商业模式和融资尾部风险 | S4, S5, S16 | Medium | High | Medium |
| C2F | W2 | Fact | Verizon 承诺 1 亿美元，其中包括商业预付款和可转债 | S6 | High | N/A | N/A |
| C2I | W2 | Attribution hypothesis | 第二家美国头部运营商的独立验证是 2024 年最强重估催化剂；价格幅度可能受定位与动量放大 | S6, S16 | Medium-High | High | Medium |
| C3F | W3 | Fact | 首五颗卫星已到 Cape Canaveral，获 FCC 初始许可并计划 9 月上半月发射 | S7 | High | N/A | N/A |
| C4I | W4 | Reaction | 发射成功并未形成正向跟随，T+20 明显跑输所有基准 | S8, S16 | High | High | Low-Medium |
| C5F | W5 | Customer validation | Vodafone 使用普通 4G/5G 手机通过五颗 BlueBird 完成无地面覆盖地区的视频通话 | S9 | High | N/A | N/A |
| C5I | W5 | Attribution hypothesis | 客户验证与 FCC STA 共同推动 5–20 日重估，但多事件重叠，不能把全部收益归给该事件簇或其中任一事件 | S9, S10, S16 | High | High | Medium |
| C6F | W6 | Fact | Verizon 正式协议拟于 2026 年开始提供 AST 服务 | S11 | High | N/A | N/A |
| C6I | W6 | Reaction | 5 日异常收益强，但 20 日绝对收益转负，因此不是持续确认 | S16 | High | High | Low-Medium |
| C7F | W7 | Fact | stc 10 年协议包含 1.75 亿美元未来服务预付款 | S12 | High | N/A | N/A |
| C7I | W7 | Reaction | 重要商业事实没有形成正向价格跟随；“好消息=上涨”的简单规则失效 | S12, S16 | High | High | Low |
| C9F | W9 | Fact | BB7 被送入过低轨道，将再入；卫星成本预计由保险赔偿 | S14 | High | N/A | N/A |
| C9I | W9 | Attribution hypothesis | -10.67% 的 5 日反应主要反映部署节奏风险，不等于技术平台失效 | S14, S16 | Medium-High | High | Medium-High |
| C10F | W10 | Fact | FCC 授权最多 248 颗星座并允许以 700/800 MHz 频谱提供 SCS | S15 | High | N/A | N/A |
| C10I | W10 | Reaction | 监管基本面改善真实存在，但 5/20 日相对表现不支持一次持续重估 | S15, S16 | High | Medium | Low-Medium |
| C11F | W11 | Fact | SpaceX 成功部署 BB8、BB9、BB10 | S17 | High | N/A | N/A |
| C11I | W11 | Reaction | 正常发射已不再自动构成正向意外，市场要求展开、测试与后续节奏 | S16, S17 | Medium | High | Pending |

## 5. Price Reaction & Relative Return Map

同业篮子为 GSAT、IRDM、RKLB 等权算术平均。表中“超额”均为 ASTS 回报减去对应基准回报。W1 与 W2 的窗口重叠，W1 的 T+20 包含 W2，不能视为 AT&T 事件的纯净因果收益。

| Window | Horizon | ASTS | QQQ | UFO | Peer basket | Excess vs QQQ | Excess vs UFO | Excess vs peers |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| W1 AT&T | 1D | +68.62% | -0.20% | +1.25% | -1.04% | +68.82 pp | +67.37 pp | +69.66 pp |
|  | 5D | +94.77% | +0.62% | +0.00% | -2.53% | +94.15 pp | +94.77 pp | +97.30 pp |
|  | 20D | +317.57% | +5.26% | +0.00% | -5.81% | +312.31 pp | +317.57 pp | +323.38 pp |
| W2 Verizon | 1D | +69.23% | -0.70% | +2.00% | -0.68% | +69.94 pp | +67.23 pp | +69.91 pp |
|  | 5D | +62.66% | -1.16% | +2.81% | -0.05% | +63.82 pp | +59.85 pp | +62.72 pp |
|  | 20D | +110.69% | +4.50% | -1.50% | -1.58% | +106.19 pp | +112.19 pp | +112.27 pp |
| W3 launch-ready | 1D | +50.70% | +2.53% | +6.01% | +6.65% | +48.17 pp | +44.69 pp | +44.04 pp |
|  | 5D | +75.11% | +4.27% | +14.29% | +18.55% | +70.84 pp | +60.81 pp | +56.56 pp |
|  | 20D | +28.74% | +2.27% | +6.83% | +9.57% | +26.47 pp | +21.91 pp | +19.17 pp |
| W4 Block 1 launch | 1D | -3.98% | +0.98% | -0.49% | -0.99% | -4.96 pp | -3.49 pp | -2.99 pp |
|  | 5D | +1.43% | +0.60% | +1.96% | +2.05% | +0.83 pp | -0.52 pp | -0.62 pp |
|  | 20D | -18.96% | +5.23% | +2.61% | +17.07% | -24.20 pp | -21.57 pp | -36.03 pp |
| W5 Vodafone/FCC cluster | 1D | +2.77% | +0.43% | +1.59% | -2.21% | +2.34 pp | +1.18 pp | +4.97 pp |
|  | 5D | +39.45% | +1.16% | +3.76% | +0.75% | +38.29 pp | +35.68 pp | +38.70 pp |
|  | 20D | +47.18% | -3.95% | -2.26% | -8.79% | +51.13 pp | +49.44 pp | +55.97 pp |
| W6 Verizon definitive | 1D | +8.63% | +1.15% | +3.02% | +4.00% | +7.48 pp | +5.60 pp | +4.63 pp |
|  | 5D | +26.42% | -1.08% | +2.97% | +2.54% | +27.50 pp | +23.45 pp | +23.88 pp |
|  | 20D | -6.29% | +2.44% | -8.69% | -2.99% | -8.73 pp | +2.40 pp | -3.30 pp |
| W7 stc | 1D | +2.94% | +0.45% | -0.71% | +0.31% | +2.49 pp | +3.65 pp | +2.63 pp |
|  | 5D | -9.93% | -2.16% | -6.29% | +1.30% | -7.77 pp | -3.64 pp | -11.23 pp |
|  | 20D | -28.62% | -3.80% | -14.05% | +2.50% | -24.83 pp | -14.58 pp | -31.12 pp |
| W8 BB6 | 1D | -8.89% | +0.29% | -0.20% | -0.62% | -9.19 pp | -8.70 pp | -8.27 pp |
|  | 5D | -15.22% | -1.25% | -3.74% | -5.02% | -13.97 pp | -11.49 pp | -10.20 pp |
|  | 20D | +32.57% | +0.10% | +16.94% | +13.62% | +32.47 pp | +15.63 pp | +18.95 pp |
| W9 BB7 failure | 1D | -5.30% | -0.32% | -0.24% | +1.89% | -4.98 pp | -5.06 pp | -7.18 pp |
|  | 5D | -10.67% | +2.32% | -6.69% | -3.57% | -12.99 pp | -3.98 pp | -7.11 pp |
|  | 20D | -2.17% | +9.26% | +2.85% | +16.34% | -11.43 pp | -5.03 pp | -18.52 pp |
| W10 FCC commercial | 1D | +5.81% | +1.67% | +1.32% | -0.25% | +4.14 pp | +4.49 pp | +6.06 pp |
|  | 5D | -10.16% | +2.05% | -6.70% | -7.04% | -12.21 pp | -3.46 pp | -3.12 pp |
|  | 20D | +10.11% | +8.88% | +6.47% | +16.74% | +1.23 pp | +3.64 pp | -6.63 pp |
| W11 BB8–10 | 1D | +3.87% | -1.01% | -0.43% | +2.40% | +4.87 pp | +4.30 pp | +1.46 pp |
|  | 5D | -17.31% | -2.64% | -9.36% | -6.86% | -14.68 pp | -7.95 pp | -10.46 pp |
|  | 20D | Pending | Pending | Pending | Pending | Pending | Pending | Pending |

### Price anomaly summary

- 2024-04-02 的 2.01 美元到 2024-08-21 的 36.44 美元，涨幅约 **1,713%**。这一重估发生在正式 SpaceMobile 服务收入出现之前，也发生在首五颗商业卫星真正发射之前。
- 最强的正向异常不是“火箭发射成功”，而是 **AT&T/Verizon 外部商业验证 + 发射准备可信度上升**。
- 实际 Block 1 发射成功后，T+20 反而跑输 QQQ 24.20 个百分点、跑输同业 36.03 个百分点；这是典型的“事实改善但价格已提前计价”。
- 2026-05-28 收盘高点为 133.09 美元；到 2026-06-26 收盘 71.45 美元回撤约 46.3%。这显示当前价格仍是高预期、高波动资产，不能把经营进展线性映射为股价。

## 6. Candidate Driver Attribution Matrix

| Window | Candidate driver | Driver / finding type | 证据 | 替代解释 | Score (0–4) | Fact | Reaction | Causal |
|---|---|---|---|---|---:|---|---|---|
| W0 | 再次延期 | Fundamental deterioration / expectation reset | 公司时间表 + 异常下跌 + 分析师关注 | 融资压力、微盘股波动 | 3 | H | H | M-H |
| W1 | AT&T 正式协议 | Customer validation / expectation reset | 客户侧公告 + 公司披露 + 三层基准 | 后续 Verizon 事件污染 T+20 | 3 | H | H | M |
| W2 | Verizon 1 亿美元承诺 | External validation / financing risk reduction | 独立客户、明确金额、持续超额收益 | 短挤压、定位与动量可能放大幅度 | 4 | H | H | M |
| W3 | 发射就绪与 FCC 初始许可 | Execution risk reduction | 卫星到场、许可、生产信息、持续超额收益 | 主要仍是管理层披露；高动量 | 3 | H | H | M |
| W4 | Block 1 发射 | Fundamental improvement but sell-the-news | 发射事实可靠；20 日负超额 | 获利回吐、拥挤交易、板块切换 | 2 | H | H | L-M |
| W5 | 客户视频 + FCC STA | External technology/regulatory validation | Vodafone 客户侧验证、监管许可、20 日超额 | 多事件重叠、空头回补；无法拆分各事件贡献 | 4（仅对联合证据栈） | H | H | M |
| W6 | Verizon 正式协议 | Commercial validation | 5 日强超额 | T+20 反转、已预期 | 2 | H | H immediate / L sustained | L-M |
| W7 | stc 预付款 | Commercial validation without rerating | 明确合同和预付款 | 整体风险偏好、融资、已计价 | 2 | H | H negative | L |
| W8 | BB6 成功 | Fundamental improvement / mean reversion | 发射方确认；20 日恢复 | 立即 sell-the-news、航天板块上涨 | 2 | H | M | L-M |
| W9 | BB7 失败 | Execution setback | SEC 直接披露、保险、5/20 日相对落后 | 市场/航天板块波动 | 3 | H | H | M-H |
| W10 | FCC 商业许可 | Policy/regulatory improvement | FCC 原始命令 | 5 日反转、同业 20 日更强 | 2 | H | M | L-M |
| W11 | BB8–10 成功部署 | Execution recovery | SpaceX 部署确认 | T+20 缺失、sell-the-news、板块波动 | 1–2 | H | H | Pending |

## 7. Valuation Re-rating Layer

### 可验证快照

- Nasdaq 在 2026-06-29 盘中给出的 ASTS 市值约 **307.5 亿美元**。[S18]
- 公司 2026 年收入指导为 **1.5–2.0 亿美元**，且约一半预计来自已有合同 backlog；2026Q1 实际收入为 1,473.5 万美元。[S19]
- 仅作量纲检查，当前市值约为管理层 2026 收入指导的 **154–205 倍**。这不是 EV/NTM Revenue，也不是同业可比估值，不能据此判断合理价值。
- 截至 2026Q1 公司仍亏损，Forward P/E 不适用；截至 2026Q1 尚无 SpaceMobile 服务收入。[S19][S20]

### 不能验证的部分

| 项目 | 状态 | 结论 |
|---|---|---|
| 历史 EV/NTM Revenue（各事件 T-20 与 T+20） | Pending | 无可靠 point-in-time 一致预期和净债务快照 |
| 同业中位数与溢价/折价 | Pending | 商业模式差异大，peer selection 会强烈改变结论 |
| FY+1/FY+2 收入与 EPS 修订 | Pending | 缺少历史 sell-side consensus 数据 |
| 目标价/评级与估值框架变化 | Pending | 公开摘要不完整，不能拼接成可靠时间序列 |
| 估值扩张与盈利预测上调分解 | Pending | 无法把涨幅可靠拆成 estimate revision 与 multiple expansion |

因此，本文只支持“价格与预期发生巨大重估”，**不支持把它正式分类为已验证的 valuation rerating 或 market-model shift**。

## 8. Narrative Shift Map

### Phase 0 — 2024Q1：融资与执行危机

- **支持证据：** 低价股权发行、首五颗卫星再次延期、2024-04-02 公司特定暴跌。
- **当时可知：** 技术演示存在，但发射、资金和商业合同仍可能阻止规模化。
- **未证明：** 技术或商业模式已经失败。

### Phase 1 — 2024-05 至 2024-08：运营商验证与发射可信度重估

- **支持证据：** AT&T 正式协议；Verizon 1 亿美元承诺；卫星到发射场、FCC 初始许可、9 月窗口。
- **价格证据：** W1、W2、W3 都是极强且跨基准的股票特定异常窗口。
- **未证明：** 服务收入、连续覆盖、规模化生产、长期单位经济性。

### Phase 2 — 2024-09 至 2025Q1：从“要发射”到“客户网络可用”

- **支持证据：** Block 1 入轨并展开；Vodafone 普通手机视频；FCC STA；AT&T/Verizon/Rakuten 后续测试。
- **关键区别：** 发射本身没有持续正向回报；客户侧实际使用与监管许可的事件簇才产生更强跟随。
- **未证明：** 规模化并发容量和商业付费。

### Phase 3 — 2025H2：合同金额和下一代卫星

- **支持证据：** Verizon 正式协议；stc 10 年、1.75 亿美元预付款；累计签约收入承诺超过 12 亿美元；BB6 成功入轨并展开。[S12][S13]
- **价格证据：** 好消息后的跟随并不稳定，说明市场已经从“是否存在需求”转向“何时交付容量与收入”。
- **未证明：** 合同承诺的收入确认节奏、服务毛利、终端用户采用率。

### Phase 4 — 2026：监管许可与工业化部署

- **支持证据：** FCC 商业 SCS 授权；BB8–10 三星同箭；BB11–33 处于不同生产阶段的管理层披露；2026 年收入指导 1.5–2.0 亿美元。[S15][S17][S19]
- **反证/限制：** BB7 因运载火箭入轨异常损失；截至 2026-06-17 只有九颗商业 BlueBird 在轨（5 颗 Block 1、BB6、BB8–10），而公司仍以 2026 年约 45 颗在轨为目标。达到目标还需要约 36 颗，节奏非常激进。
- **未证明：** 45 颗目标、连续服务、服务收入和长期回报率。

### Narrative shift classification

| Level | 当前状态 | 理由 |
|---|---|---|
| Level 0 — No shift | Rejected | W1/W2/W3/W5 存在强公司特定反应 |
| Level 1 — Reaction only | Exceeded | 不只是价格；有运营商、监管者和发射伙伴外部证据 |
| Level 2 — Company-framed candidate | Exceeded | 已有客户侧与监管侧验证 |
| Level 3 — Externally validated candidate | **Supported** | AT&T、Verizon、Vodafone、stc、Rakuten、FCC、ISRO、SpaceX 等独立层共同验证 |
| Level 4 — Market-model shift | Pending | 缺少可靠历史估值和一致预期修订数据 |
| Level 5 — Confirmed narrative shift | Not supported | 尚无 SpaceMobile 服务收入与连续覆盖的长期经营跟随 |

## 9. True Signal vs Noise

### True signals

| Signal | Date | 为什么重要 | 当时可知 | 后来强化 | 替代解释/限制 |
|---|---|---|---|---|---|
| AT&T 正式商业协议 | 2024-05-15 | 直接测试 MOU 能否变正式客户 | 协议至 2030；AT&T 董事席位与技术合作 | Verizon、Vodafone、stc 后续正式化 | W1 T+20 被 W2 污染 |
| Verizon 1 亿美元承诺 | 2024-05-29 | 独立验证美国双运营商路径并缓解融资风险 | 明确商业预付款与可转债 | 2025 年正式商业协议 | 空头回补可能放大涨幅，但无法解释全部跨基准异常 |
| 卫星到场 + 发射许可 | 2024-08-14 | 直接反驳 4 月延期恐惧 | 硬件已到发射场，发射窗口明确 | 9 月成功发射 | 管理层信息仍占主导 |
| Vodafone 视频 + FCC STA | 2025-01-29/31 | 客户与监管两条独立证据证明 Block 1 可进入真实网络 | 普通手机视频、美国可测试 | Rakuten、AT&T、Verizon测试，2026 FCC 商业许可 | 多事件簇，无法精确拆因 |
| BB7 失败后的多发射商恢复 | 2026-04 至 06 | 验证单点失败是否可被部署体系吸收 | BB7 损失但有保险；BB8–10 随后成功部署 | 尚需后续展开和连续发射 | 只有短期证据，T+20 Pending |

### Possible signals / too uncertain

| Signal | 分类 | 缺失确认 |
|---|---|---|
| 超过 12 亿美元 aggregate contracted revenue commitments | Possible signal | 需要合同分拆、可撤销/条件条款、收入确认时间与现金回收 |
| 2026 年约 45 颗卫星在轨目标 | Too uncertain | 需要按月生产完成、运输、发射槽位、展开与在轨验收 |
| 98.9 Mbps Block 1 峰值速度 | Possible signal | 需要多用户并发、持续覆盖、边缘条件、真实商业网络吞吐 |
| “约 90 颗星座已获资金覆盖” | Possible signal | 管理层估算；需要完整现金用途、受限现金、债务、地面站、频谱费与超支敏感性 |
| FCC 授权后全球许可会快速复制 | Too uncertain | 各国监管、频谱和运营商安排不同，不能由美国自动外推 |

### Noise or weaker signals

- 单纯的“火箭发射成功”标题：W4、W8、W11 显示正常发射常常已被计价，甚至出现 sell-the-news。
- 没有金额、期限、地域和服务条件的 MOU：可以生成研究问题，但不能等同订单或 backlog。
- 单日航天板块上涨：ASTS 是高 beta、高波动股票，必须看 UFO/ARKX 与同业。
- 仅由管理层给出的 TAM、峰值速度或生产目标：在客户、监管和长期经营结果验证前只能算候选信号。
- 社交媒体发射倒计时、卫星照片和未核实的发射清单：只能做情绪背景，不支持事实归因。

## 10. Lessons Learned

1. **最强重估常发生在硬件完成之前。** ASTS 2024 年最强窗口来自客户承诺与执行可信度，而不是 9 月实际发射。未来类似公司要观察“谁愿意签正式协议并付款”，而不只是技术演示。
2. **客户侧验证比公司自述更有权重。** AT&T、Vodafone、Verizon、Rakuten 的官方材料把技术从管理层 claim 提升为外部验证；但仍不能替代规模化单位经济性。
3. **事件成功不等于股价正收益。** Block 1、BB6、BB8–10 的发射窗口都出现弱跟随或负跟随。若预期已充分进入价格，事实改善可以与价格下跌同时发生。
4. **重叠事件会制造虚假的单一催化剂故事。** W1 的 T+20 包含 W2；W5 同时包含 Vodafone 与 FCC。归因应对事件簇打分，而不是把全段涨幅塞给一个标题。
5. **融资风险可以从“生存风险”转为“资本结构风险”。** 现金大幅增加降低短期生存风险，但可转债、注册直接发行、受限现金和频谱付款仍影响稀释与资本回报。
6. **监管许可消除的是一个 gate，不是交付本身。** FCC 授权降低“能不能在美国商用”的风险，但没有自动带来持续异常回报；市场随即转向卫星数量、容量和收入。
7. **当叙事领先财务结果时，价格对二阶信息更敏感。** 截至 2026Q1 尚无 SpaceMobile 服务收入，当前定价主要依赖未来部署、合同转收入与规模化能力。

## 11. Future Watchlist Rules

### Rule A — 合同升级门槛

只有同时看到 `definitive agreement + 对手方官方确认 + 金额/期限/地域/收入机制至少两项 + 后续履约`，才把 MOU 升级为 true signal。

### Rule B — 发射执行门槛

不要只记录发射。按 `生产完成 → 交付发射场 → 成功部署 → 阵列展开 → 在轨测试 → 网络接入 → 服务收入` 逐级记录；任何一级都不能替代下一级。

### Rule C — 商业化门槛

把网关设备收入、政府工程/测试收入和 SpaceMobile 服务收入分开。只有服务收入、活跃用户/流量、收入分成和毛利开始出现，才算核心商业模型进入财务验证。

### Rule D — 融资质量门槛

每季同时跟踪：非受限现金、受限现金、债务本金、潜在稀释、经营现金流、资本化卫星投入、未来发射承诺和频谱年度付款。只看“现金很多”会遗漏资本结构成本。

### Rule E — 叙事升级门槛

从 Level 3 升到 Level 4/5 至少需要：历史一致预期上修、远期倍数相对同业扩张、服务收入开始、连续覆盖形成、合同转收入、生产/发射节奏持续兑现。

## 12. Open Questions

- BB8–10 是否已完成阵列展开和在轨验收？W11 的 T+20/T+60 回报如何？
- 2026 年约 45 颗在轨目标在 BB7 损失后是否仍可实现？每月需要多少颗完成、运输和发射？
- 超过 12 亿美元 contracted commitments 中，多少是无条件、不可撤销、已收现金或满足收入确认标准？
- 2026 年 1.5–2.0 亿美元收入中，SpaceMobile 服务收入占比会是多少？截至 2026Q1 仍为零。
- AT&T、Verizon、Vodafone/SatCo、stc 的收入分成、定价和最低承诺是什么？
- 一颗 Block 2 在多用户、边缘波束、拥塞和恶劣环境下的可交付容量是多少？
- 90 颗星座的 2,100–2,300 万美元平均单星直接材料与发射成本，是否包含地面站、频谱、人员、保险、返工和失败冗余？
- Ligado 频谱交易的监管条件、最低年度付款和长期现金成本如何影响资本回报？
- 可靠的 point-in-time FY+1/FY+2 一致预期、EV/NTM Revenue、目标价与评级时间序列是什么？
- 期权隐含波动、短仓、ETF 流入和成交量在 W1/W2/W3/W5 中贡献了多少幅度？

## 13. Final Retrospective Takeaway

ASTS 的案例说明，一家尚未产生核心服务收入的资本密集型公司，也可能在“外部验证堆栈”快速改善时发生巨大重估：正式客户、预付款、监管许可和可见的发射执行共同降低失败概率。2024 年真正的拐点不是卫星飞上天，而是 AT&T 与 Verizon 先后把关系从意向升级为正式、带资金承诺的合作；随后客户测试和 FCC 授权证明这不是纯粹的价格故事。不过，2025–2026 的事件窗口也表明，市场已经把问题从“技术是否存在”推进到“能否按时部署足够容量并产生服务收入”。因此，最合适的结论是 **外部验证的候选叙事转变，而非已确认的商业模式与估值转变**。

## 14. Source Register

| ID | 日期 | 来源 | Tier / proximity / grade | 支持窗口/用途 | 限制 |
|---|---|---|---|---|---|
| S1 | 2024-01-18 | [SEC：战略承诺与计划中的 1 亿美元普通股发行](https://www.sec.gov/Archives/edgar/data/1780312/000149315224002914/form8-k.htm) | 1 / direct / A | W0；融资恐惧 | 不能解释价格幅度 |
| S2 | 2024-04-01 | [SEC：FY2023/Q4 业务更新](https://www.sec.gov/Archives/edgar/data/1780312/000095017024039386/asts-ex99_1.htm) | 1 / direct / A | W0；现金、时间表 | 管理层披露 |
| S3 | 2024-04-02 | [Space Intel Report：Block 1 延期与供应链问题](https://www.spaceintelreport.com/direct-to-device-startup-ast-spacemobile-delays-next-launch-by-6-months-solicits-export-credit-agency-financing/) | 2 / near-direct / B | W0；同期恐惧 | 付费墙、部分二手解释 |
| S4 | 2024-05-15 | [AT&T：与 AST SpaceMobile 的正式商业协议](https://about.att.com/story/2024/ast-spacemobile-commercial-agreement.html) | 1 customer / direct / A | W1；外部客户验证 | 商业经济条款有限 |
| S5 | 2024-05-15 | [SEC：ASTS 2024Q1 业务更新](https://www.sec.gov/Archives/edgar/data/1780312/000095017024060494/asts-ex99_1.htm) | 1 / direct / A | W1；现金、卫星进度 | 管理层披露 |
| S6 | 2024-05-29 | [Nasdaq/Business Wire：Verizon 1 亿美元战略伙伴关系](https://www.nasdaq.com/press-release/ast-spacemobile-and-verizon-announce-plans-target-100-percent-geographical-coverage) | 1 joint release / direct / A | W2；客户与融资 | 联合新闻稿仍带宣传性 |
| S7 | 2024-08-14 | [SEC：2024Q2 业务更新](https://www.sec.gov/Archives/edgar/data/1780312/000095017024097095/asts-ex99_1.htm) | 1 / direct / A | W3；到场、许可、生产 | 未来目标是 management claim |
| S8 | 2024-09-12 | [ASTS：首五颗商业卫星成功发射](https://s24.q4cdn.com/538403808/files/doc_news/AST-SpaceMobile-Announces-Successful-Orbital-Launch-of-Its-First-Five-Commercial-Satellites-2024.pdf) | 1 / direct / A | W4；发射事实 | 不等于在轨服务成功 |
| S9 | 2025-01-29 | [Vodafone：普通手机从无覆盖地区完成卫星视频通话](https://www.vodafone.com/news/newsroom/technology/vodafone-makes-historic-satellite-video-call-from-a-smartphone) | 1 customer / direct / A | W5；技术外部验证 | 单次演示不证明规模容量 |
| S10 | 2025-01-31 | [Via Satellite：FCC 批准 AT&T/Verizon 测试](https://www.satellitetoday.com/connectivity/2025/01/31/fcc-approves-ast-spacemobile-testing-in-the-us-with-verizon-and-att/) | 2 / near-direct / B | W5；监管事件簇 | 非 FCC 原始命令 |
| S11 | 2025-10-08 | [AP：Verizon 与 ASTS 正式商业协议](https://apnews.com/article/88e8780d32b973333fad262665527199) | 2 / near-direct / B | W6；客户商业化 | 未披露财务条款 |
| S12 | 2025-11-10 | [SEC：Q3 更新，Verizon/stc 合同、1.75 亿美元预付款、累计承诺](https://www.sec.gov/Archives/edgar/data/1780312/000119312525274360/asts-ex99_1.htm) | 1 / direct / A | W6/W7；商业承诺 | aggregate commitment 不等于已确认收入 |
| S13 | 2026-03-02 | [SEC：FY2025/Q4 结果，7,091.8 万美元收入与 12 亿美元承诺](https://www.sec.gov/Archives/edgar/data/1780312/000178031226000005/asts-ex99_1.htm) | 1 / direct / A | Phase 3；后续经营证据 | 主要收入不是 SpaceMobile 服务 |
| S14 | 2026-04-20 | [SEC：BlueBird 7 入轨异常、再入与保险](https://www.sec.gov/Archives/edgar/data/1780312/000149315226018012/form8-k.htm) | 1 / direct / A | W9；负面执行 | 后续保险回收金额/时间未确认 |
| S15 | 2026-04-21 | [FCC：DA 26-391 Order and Authorization](https://docs.fcc.gov/public/attachments/DA-26-391A1.pdf) | 1 regulator / direct / A | W10；商业 SCS 许可 | 有条件授权；不保证商业成功 |
| S16 | 2024-01 至 2026-06 | [Nasdaq 历史行情 API（ASTS；其余代码使用同一接口）](https://api.nasdaq.com/api/quote/ASTS/historical?assetclass=stocks&fromdate=2024-01-01&todate=2026-06-29&limit=5000) | 4 / direct market / A | 全部窗口；价格与成交日 | 价格证明反应，不证明原因；未复权 |
| S17 | 2026-06-17 | [SpaceX：BlueBird 8–10 launch and deployment](https://www.spacex.com/launches/bluebird8-10) | 1 launch provider / direct / A | W11；三星部署 | 尚不证明阵列展开与商业运行 |
| S18 | 2026-06-29 | [Nasdaq：ASTS 市场摘要](https://api.nasdaq.com/api/quote/ASTS/summary?assetclass=stocks) | 4 / direct market / A | 当前市值快照 | 盘中数据会变化 |
| S19 | 2026-05-11 | [SEC：2026Q1 业务更新与收入指导](https://www.sec.gov/Archives/edgar/data/1780312/000119312526216946/asts-ex99_1.htm) | 1 / direct / A | 当前经营、制造、指导 | 未来目标是管理层声明 |
| S20 | 2026-05-11 | [SEC：2026Q1 10-Q](https://www.sec.gov/Archives/edgar/data/1780312/000119312526216950/asts-20260331.htm) | 1 / direct / A | 现金、成本、收入结构、无服务收入 | 仅截至 2026-03-31 |
| S21 | 2025-12-23 | [ISRO：LVM3-M6 / BlueBird Block-2 成功入轨](https://www.isro.gov.in/ISRO_EN/LVM3_M6_BlueBird_Block2_Mission.html) | 1 launch provider / direct / A | W8；BB6 发射 | 页面日期与任务执行时区需谨慎 |

### 14.1 Required Source Backlog

| Backlog | 数据 | 用途 | 当前状态/限制 |
|---|---|---|---|
| B1 | Point-in-time sell-side FY+1/FY+2 revenue/EPS/EBITDA | 检验 Level 4 market-model shift | Pending；公开摘要不足 |
| B2 | 历史 EV/NTM Revenue、净债务、同业中位数 | 估值重估分解 | Pending；需专业数据库 |
| B3 | 期权隐含波动、短仓、借券费、ETF 流量 | 测试 W1/W2/W3/W5 的 short squeeze/flow | Pending |
| B4 | 各正式商业协议全文或关键经济条款 | 拆分 12 亿美元 commitments 的质量 | 多数未公开 |
| B5 | BB8–10 展开、在轨测试与 FCC 状态 | 完成 W11 T+20/T+60 | Pending |
| B6 | 2026 每次生产/发射清单 | 测试约 45 颗目标 | 动态更新中 |
| B7 | 服务收入、用户、流量、毛利与 MNO 分成 | 验证核心商业模型 | 尚未披露/尚未产生 |
| B8 | Ligado 频谱交易最终监管状态与现金付款时间表 | 评估频谱价值与资本成本 | 交易结构复杂，仍需持续核验 |
