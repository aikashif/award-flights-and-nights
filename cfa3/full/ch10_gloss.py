from summary_lib import *
from helpers import P

G = [
("Active risk","SD of active returns (tracking error)"),("Active Share","½ Σ |portfolio wt − benchmark wt|"),("Activist strategy","Buy minority stake, push for change"),
("Agency trade","Broker finds the other side; risk stays with manager"),("Algorithmic trading","Programmed rules for profit-seeking or execution"),("Alpha decay","Loss of alpha after the decision → urgency"),
("Alpha skills","Factor timing and security selection"),("Altman z-score","Reduced-form default score; &gt; 3 safe, &lt; 1.8 distress"),("Arrival price","Price when order reaches the market"),
("Asset swap spread (ASW)","Coupon − interpolated swap rate"),("Attribution analysis","Finds sources of return/tracking error"),("Authorised participant","Creates/redeems ETF shares in kind"),
("Average daily volume (ADV)","Base for relative order size"),("Basis point value (BPV)","Value change for 1 bp = MD × V × 0.0001"),("Bear flattener / steepener","Short / long rates rise more"),
("Best execution","Best overall result for client, not just price"),("BEMC","Best execution monitoring committee"),("Bottom-up","Pick individual securities"),
("Bull flattener / steepener","Long / short rates fall more"),("Butterfly strategy","Body (bullet) vs wings (barbell)"),("Buy and hold","Extend duration, low turnover"),
("Callable bond","Bond + short call; negative convexity at low yields"),("Capacity and scalability","How much AUM a strategy can absorb"),("Carry trade","Borrow low-rate, invest high-rate currency"),
("CDS basis","CDS spread − z-spread"),("CDS curve trade","Buy/sell protection at different tenors"),("CDS long/short","Buy protection on one name, sell on another"),
("CDS spread","Fair periodic premium for protection"),("Cell matching","Stratified sampling by risk cells"),("Closet indexer","Low Active Share, low active risk, active fees"),
("Clustering","ML grouping of trades to pick algorithms"),("Conditional VaR (CVaR)","Average loss beyond VaR"),("Contingent immunisation","Active while surplus &gt; 0, then immunise"),
("Contrarian investing","Against sentiment; depressed cyclicals"),("Covered interest parity (CIRP)","Hedged foreign return = domestic rate"),("Credit barbell","Long Treasuries + short-dated corporates"),
("Credit cycle","Growth/default cycle that shapes spread curves"),("Credit default swap (CDS)","Insurance on an issuer's default"),("Credit loss rate","Historical % lost to default"),
("Credit migration","Rating downgrade risk"),("Credit spread curve","Spread vs maturity"),("Dark pools","Venues without pre-trade transparency"),
("Data mining / overfitting","Searching data until something works"),("Decision price","Price when PM decides"),("Deep-value investing","Very low P/B, often distressed"),
("Default intensity","Periodic POD in reduced-form models"),("Delay cost","Arrival − decision price × filled shares"),("Derivatives overlay","Derivatives added to adjust exposures"),
("Direct market access (DMA)","Buy side trades on exchange via broker tech"),("Discount margin (DM)","Required margin over MRR for an FRN"),("Duration matching","Match BPVs of assets and liabilities"),
("Duration times spread (DTS)","EffSpreadDur × spread"),("Effective spread duration / convexity","Price sensitivity to spread changes"),("Electronic trading","Order-driven limit order books"),
("Empirical duration","Regression-based rate sensitivity; &lt; analytical for HY"),("Enhanced indexing","Match risk factors, not every holding"),("ESG rating / techniques","Screening, ratings, direct funding"),
("Evaluated / matrix pricing","Price from similar traded bonds"),("Event-driven","Trade around corporate events"),("Excess spread","Spread − widening loss − expected default loss"),
("Execution cost","Delay + trading cost"),("Factor bets","Factor exposures different from benchmark"),("Factor weightings","Building block 1"),
("Fixed fees","Commissions, explicit fees"),("Fixed-fixed cross-currency swap","Hedge a foreign coupon bond"),("Forward rate bias","UIRP fails → carry earns"),
("Full replication","Hold every index constituent"),("Fundamental approach","Judgment-based decisions"),("Fundamental law","E(R_A) = IC √BR σ_A TC"),
("GARP","Growth at a reasonable price (PEG)"),("G-spread","YTM − interpolated govt YTM"),("Green bond","Funds environmental projects"),
("Growth trap","Growth already priced in; shortfall hurts"),("Heuristic risk constraints","Rule-of-thumb limits, no forecasts"),("High-quality value","Value + financial strength (Buffett)"),
("High-touch","Human-intermediated trading"),("Historical simulation","VaR from past factor moves"),("Holdings-based style","Aggregate stock styles (style box)"),
("Idiosyncratic risk","Stock-specific (luck)"),("Immunisation","Lock a future value regardless of rates"),("Implementation shortfall (IS)","Paper − actual return"),
("Income investing","High dividend yield and growth"),("Incremental VaR (IVaR)","VaR change from adding/removing a position"),("Information coefficient (IC)","Correlation of forecasts/scores and later returns"),
("Information leakage","Market learns your intention"),("Intraday benchmarks","VWAP, TWAP"),("I-spread","YTM − interpolated swap rate"),
("Key rate duration","Sensitivity to one maturity's yield"),("LASSO","ML method to cut variables"),("Limited legal liability","Long loss capped at price paid"),
("Long extension (130/30)","Net 100% long with some shorts"),("Look-ahead bias","Using data not yet available"),("Loss given default (LGD)","1 − recovery rate"),
("Macaulay duration","PV-weighted average time to cash flows"),("Market impact","Price move caused by your trade"),("Market-adjusted cost","Arrival cost − β × index cost"),
("Market microstructure strategy","Millisecond imbalances, HFT"),("Market-neutral","Net beta ≈ 0"),("Modified duration","Macaulay ÷ (1 + periodic yield)"),
("Money duration","Duration × value; BPV"),("Monte Carlo","VaR from simulated model paths"),("Multi-factor model","Several factors explain returns"),
("OAS","Option-removed spread over a rate tree — best measure"),("Opportunity cost","Unfilled shares × (close − decision)"),("Optimisation","Minimise tracking error with constraints"),
("Pairs trading","Long/short two correlated stocks on divergence"),("Parametric VaR","Normal-distribution VaR"),("Payer / receiver swaption","Right to pay / receive fixed"),
("Pearson vs Spearman IC","Raw vs rank correlation (robust to outliers)"),("Position sizing","Building block 3"),("Post-trade benchmark","Closing price"),
("Pre-trade benchmarks","Decision, previous close, open, arrival"),("Price target benchmark","Manager's fair value"),("Principal (broker risk) trade","Dealer takes the risk"),
("Probability of default (POD)","Chance of missed payment"),("Pure index","Full replication"),("Putable bond","Bond + long put; price floor"),
("Quantitative approach","Rules from data"),("Quoted margin (QM)","Fixed margin in FRN coupon"),("Quote-driven","Dealer markets"),
("Receive-fixed swap","Adds duration"),("Reduced-form model","Macro + ratios → default intensity"),("Relative value","Low multiples vs peers"),
("Relative VaR","VaR of returns vs benchmark"),("Repo carry trade","Borrow short via repo, buy longer bonds"),("RFQ","Request-for-quote market"),
("Risk arbitrage","Merger arbitrage"),("Risk models","Vendor variance/correlation estimates"),("Rolling down the curve","Earn rolldown on steep segments"),
("Screening","Exclude by ESG/other criteria"),("Sector rotator","Moderate Active Share, high active risk"),("Securities lending","Fee income cuts tracking error"),
("Slippage","Execution price − midquote at entry"),("Smart beta","Rule-based factor exposures"),("Smart order router (SOR)","Routes small orders to best venue"),
("Special situations","Spin-offs, mergers, divestitures"),("Statistical arbitrage","Mean-reversion trades on price data"),("Stratified sampling","Sample within risk strata"),
("Stress testing","Extreme scenarios on assets and liabilities"),("Structural model","Distance to default (EDF, DRSK)"),("Structural risk","Curve twists hurting immunisation"),
("Survivorship bias","Testing only surviving firms"),("Swap fixed rate (SFR)","Fixed leg rate; swaption strike"),("Systematic rebalancing","Calendar or percent-range rules"),
("Top-down","Macro view drives allocation"),("Total return swap (TRS)","Receive index return, pay MRR + spread"),("Trader's dilemma","Impact (fast) vs execution risk (slow)"),
("Transfer coefficient (TC)","How fully insights reach the portfolio"),("Uncovered interest parity (UIRP)","High-rate currencies should fall"),("Value trap","Cheap for a reason"),
("Value at risk (VaR)","Minimum loss at a probability"),("VWAP / TWAP","Volume- / time-weighted average price"),("Well-constructed portfolio","Promised traits, efficient, low cost"),
("Yield spread","YTM − nearest on-the-run govt YTM"),("Z-spread","Spread over govt spot curve"),("Zero-discount margin (Z-DM)","DM using forward MRR curve"),
]

COV = [
("P1 Index-based equity","P1.a–f","Factor strategies (3 types) · pooled/derivatives/separate · replication/sampling/optimisation · tracking error · lending, proxy voting"),
("P2 Active equity strategies","P2.a–i","Fundamental vs quant · bottom-up value/growth sub-styles · top-down, smart beta · factor/hedged portfolio · factor timing · activists · stat arb, microstructure · event-driven · building fundamental and quant strategies · IC · pitfalls · style box, returns-based style"),
("P3 Portfolio construction","P3.a–h","Return sources · building blocks · fundamental law · approaches · objectives · Active Share vs active risk · manager types · risk budgeting (absolute, relative) · risk level · heuristic vs formal · market impact, scale · well-constructed · long/short"),
("P4 LDI &amp; index fixed income","P4.a–g","Durations · portfolio statistics · curve shifts · single/multiple liability rules · cash-flow vs duration matching · futures, swaps, swaptions, collars · contingent immunisation · DB pensions · LDI risks · bond indexing · vehicles · benchmark choice"),
("P5 Yield curve strategies","P5.a–g","Curve changes · 5-step decomposition · static strategies · level, slope, curvature trades · embedded and stand-alone options · KRDs · currency: unhedged, CIRP/UIRP, cross-currency swaps, carry · scenario evaluation"),
("P6 Credit strategies","P6.a–k","POD/LGD/CVA · credit cycle · empirical duration · all spread measures, OAS · FRN DM/Z-DM · spread duration, DTS, excess spread · structural/reduced models · relative value · top-down, factor, ESG · liquidity · VaR family · CDS pricing and trades · static/dynamic curve strategies · global/EM · structured · analytics"),
("P7 Trade execution","P7.a–i","Motivations · inputs, trader's dilemma · benchmarks · strategies by trade type · execution methods · algorithms · markets · IS and decomposition · market-adjusted cost, added value · trade policy"),
("P8 Institutional case","P8.a–g","Liquidity tools · illiquidity premium · QU endowment facts, SAA, liquidity profiles · ethics in manager selection · ETF vs futures vs TRS · cash vs derivatives rebalancing · ESG policy and Portro response"),
]

def add(chap, sub):
    chap("G", "Glossary of Index Terms & Coverage Check", "reference", 4)
    half = (len(G) + 1) // 2
    sub("Glossary (part 1)", 4, T(["Term","Meaning"], [[a, b] for a, b in G[:half]]))
    sub("Glossary (part 2)", 4, T(["Term","Meaning"], [[a, b] for a, b in G[half:]]))
    sub("Coverage check: every LOS in the Schweser notes", 4,
      P("Every reading, LOS, worked example, Professor's Note and module-quiz answer in the source was checked against this summary. Exhibits that are images in the source (some tables) are rebuilt from the text and standard curriculum content.") +
      T(["Reading","LOS","Covered in this summary"], [list(r) for r in COV]))
