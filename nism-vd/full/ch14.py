from summary_lib import *

def add(chap, sub):
    chap(14, "Understanding the Index", "5", 3)
    sub("What an index is & why it matters", 4,
      L("Statistical indicator of changes in the economy or specific areas; in markets, a portfolio of securities representing a market or part of it",
        "Expressed as change from a base value — % change matters more than the number",
        "Stock index = average share price movement; broad indices should represent typical portfolio returns",
        "Significance: (1) indicator of market/sector performance (2) <b>benchmark</b> for portfolios (3) <b>underlying for derivatives</b>"))
    sub("Market-cap weighted index (worked example)", 5,
      F("Market cap = shares outstanding × price  (5 crore shares × ₹120 = ₹600 crore)\nIndex value = (Current index market cap ÷ Base market cap) × Base index value\n5 stocks, base 100 on 1 Jan 1995: base m-cap ₹18,800 lakh → now ₹42,500 lakh\nIndex = 42,500 ÷ 18,800 × 100 = 226.06 (+126.06%)") +
      T(["Stock","Old price","Shares (lakh)","Old m-cap","Old wt","New price","New m-cap","New wt"],
        [["AZ","150","20","3,000","0.16","650","13,000","0.31"],["BY","300","12","3,600","0.19","450","5,400","0.13"],
         ["CX","450","16","7,200","0.38","600","9,600","0.23"],["DW","100","30","3,000","0.16","350","10,500","0.25"],
         ["EU","250","8","2,000","0.11","500","4,000","0.09"]]) +
      K("Sensex and Nifty were earlier full market-cap weighted"))
    sub("Free-float market-cap index", 5,
      L("Free float = shares readily available for trading (vs promoters, institutions, corporates holdings)",
        "Weights by free-float market cap = price × shares × free-float factor",
        "Most global indices incl. <b>Sensex, Nifty and SX40</b> moved to free-float basis") +
      F("Same 5 stocks with free-float factors 0.6, 0.5, 0.5, 0.7, 0.8\nBase FF m-cap ₹10,900 lakh → now ₹25,850 lakh\nIndex = 25,850 ÷ 10,900 × 100 = 237.15"))
    sub("Price-weighted index", 5,
      F("Price index = Sum of prices ÷ Number of stocks\nBase = (150+300+450+100+250) ÷ 5 = 250 ; Now = (650+450+600+350+500) ÷ 5 = 510 → +104%\nWeights by price: AZ 0.12, BY 0.24, CX 0.36, DW 0.08, EU 0.20") +
      K("Higher-priced stocks have more influence","Examples: <b>Dow Jones Industrial Average, Nikkei 225</b>"))
    sub("Equal-weighted & capped indices", 4,
      F("4 stocks, ₹30,000 each (weight 0.25) on 1 Jan 1995 → total 1,20,000 → now 1,46,000\nIndex = 146,000 ÷ 120,000 × 100 = 121.67 (+21.67% = Σ price change × old weight)") +
      K("After moves, weights drift (P, R above 25%; Q, S below) → rebalance: sell risers, buy fallers","Capped indices: float-adjusted with a maximum weight per stock"))
    sub("Attributes of a good index", 4,
      K("Reflects market behaviour","Computed by independent third party, free of participant influence","Professionally maintained"))
    sub("Impact cost & bid-ask spread", 5,
      L("Liquidity = large orders executed without moving prices",
        "Bid-ask spread = best sell − best buy (₹4.50 − ₹4.00 = ₹0.50); buy &amp; sell 100 shares immediately → lose ₹50 — the transaction cost for a small trade",
        "Bigger order (3,000 shares) hits deeper levels → higher cost",
        "<b>Ideal price</b> = average of best bid and best offer",
        "<b>Impact cost</b> = % degradation of actual price vs ideal price; varies with size; differs for buy and sell side; arises from lack of liquidity — not actually paid as a fee") +
      F("Bids 9.80/9.70/9.60, offers 9.90 (1,000) / 10.00 (1,500) / 10.10\nBuy 1,500: ideal = (9.80 + 9.90) ÷ 2 = 9.85\nActual = (1,000 × 9.90 + 500 × 10.00) ÷ 1,500 = 9.9333\nImpact cost = (9.9333 − 9.85) ÷ 9.85 × 100 = 0.84%") +
      TRAP("Impact cost is HIGH when liquidity is poor."))
    sub("Beta, PRI, TRI", 3,
      KV([("Beta","Movement of a stock's/portfolio's returns relative to market returns"),
          ("Price Return Index","Only price changes; ignores dividends/interest"),
          ("Total Return Index","Price moves + dividends reinvested in the overall index (not the paying stock)")]))
    sub("Index management", 4,
      KV([("Managers","BSE indices: <b>Asia Index Pvt Ltd</b>; NSE indices: <b>NSE Indices Limited</b>"),
          ("Regulation","SEBI (Index Providers) Regulations, 2024 — transparency &amp; accountability"),
          ("Construction","Choose stocks + calculation method"),
          ("Maintenance","Adjust for corporate actions: bonus, rights, split, consolidation, mergers — triggered by events"),
          ("Revision","Change composition (replace stocks) — continuous exercise"),
          ("Index Committee","Final decision on inclusion/removal")]) +
      K("Good index = trade-off between diversification and liquidity","10 → 20 stocks: sharp risk reduction; 50 → 100: very little; beyond 100: almost none"))
    sub("Derivatives on non-benchmark indices (SEBI 30 Oct 2025)", 4,
      T(["Prudential norm","Limit"],
        [["Minimum constituents","14"],["Top constituent weight","≤ 20%"],["Top 3 combined weight","≤ 45%"],["Weights","Descending structure"]]) +
      T(["Index","Deadline","Mode"],
        [["BANKEX (BSE), FINNIFTY (NSE)","31 Dec 2025","Single tranche"],["BANKNIFTY (NSE)","31 Mar 2026","Four monthly tranches"]]) +
      F("Tranche adjustment = (actual − desired weight) ÷ remaining tranches\nMonth 1: 28% → (28 − 20)/4 = 2% → 26%\nMonth 2: drifted 25.5% → (25.5 − 20)/3 = 1.83% → 23.67%\nMonth 3: 23% → (23 − 19.5)/2 = 1.75% → 21.25%\nMonth 4: 20.9% → (20.9 − 18.5)/1 = 2.4% → 18.5%"))
    sub("Major Indian indices", 3,
      K("BSE Sensex","BSE Sensex Next 50","BSE 100","BSE 200","BSE 500","BSE Bankex","SX 40","Nifty 50","Nifty Next 50","Nifty 100","Nifty 200","Nifty 500","Nifty Bank"))
    sub("Applications & types of indices", 4,
      T(["Application","Point"],
        [["Index funds","Hold index stocks in index proportions (Sensex fund → 30 stocks); small tracking error from expenses &amp; cash for redemptions"],
         ["Index derivatives","Index futures &amp; options — most popular worldwide; hedge market risk"],
         ["ETFs","Basket traded like a stock; intraday; small denomination; low cost"]]) +
      T(["Type","Examples"],
        [["Broad market","BSE Sensex, Nifty 50"],["Sectoral","BSE Bankex, Nifty IT"],["Market cap","Large/mid/small cap (e.g. Nifty Midcap 100)"],
         ["Thematic &amp; factor","ESG/sustainability, dividend yield, volatility (India VIX)"]]))
