"""Build the NISM V-D quiz bank (Ch15, Ch16, Ch13, Ch20) and inject it into quiz.html.

Run: python3 nism-vd/build_quiz.py  (derivatives quiz)
Numerical questions compute their answers here, so the key is exact.
"""
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from quiz_lib import make_bank, inr, num, build

BANK, Q = make_bank()

# =====================================================================
# CH 13  BASICS OF DERIVATIVES
# =====================================================================
C = 13
Q(C,"S","A derivative is a contract whose value depends on:",
  "The value of an underlying asset, index or rate",
  "By definition a derivative 'derives' its value from an underlying: a share, index, commodity, currency or interest rate.",
  ("The credit rating of the exchange","The exchange's rating has no link to a contract's value."),
  ("Its own demand and supply only","Trading moves the price around, but without the underlying the contract has no value."),
  ("The face value printed on the contract","Derivatives have a notional value; no printed face value sets their price."))
Q(C,"S","Under which law are derivatives included in the definition of 'securities' in India?",
  "Securities Contracts (Regulation) Act, 1956 (amended 1999)",
  "The 1999 amendment to SCRA added derivatives to the definition of securities. That made exchange trading legal.",
  ("SEBI Act, 1992","The SEBI Act set up SEBI. The definition of securities sits in SCRA."),
  ("Companies Act, 2013","The Companies Act governs companies, not the definition of traded derivatives."),
  ("FEMA, 1999","FEMA covers foreign exchange, not the definition of securities."))
Q(C,"S","Which was the first exchange-traded derivative product in India?",
  "Index futures (June 2000)",
  "Sequence: index futures Jun 2000 → index options Jun 2001 → stock options Jul 2001 → stock futures Nov 2001.",
  ("Stock futures","Stock futures came last, in Nov 2001."),
  ("Index options","Index options started in June 2001, one year after index futures."),
  ("Stock options","Stock options started in July 2001."))
Q(C,"S","Which committee recommended the regulatory framework for derivatives trading in India?",
  "L.C. Gupta Committee",
  "L.C. Gupta = framework for derivatives trading. J.R. Varma = risk containment (margins).",
  ("J.R. Varma Committee","Varma worked on risk containment and margins, not the overall framework."),
  ("Narasimham Committee","Narasimham worked on banking sector reforms."),
  ("Kelkar Committee","Kelkar worked on tax reforms."))
Q(C,"S","The J.R. Varma Committee is mainly linked with:",
  "Risk containment measures such as margins for derivatives",
  "Varma recommended the margin and risk-containment system for exchange-traded derivatives.",
  ("Launch of mutual funds in India","Unrelated. Mutual funds are under SEBI (MF) Regulations, 1996."),
  ("The overall framework for derivatives trading","That was the L.C. Gupta Committee."),
  ("Taxation of derivatives","Tax is set by the Income Tax Act, not this committee."))
Q(C,"S","The main difference between a forward and a futures contract is that a futures contract is:",
  "Standardised and traded on an exchange",
  "Futures: standard terms, exchange-traded, daily MTM, clearing corporation guarantee. Forwards: custom, OTC.",
  ("Customised to the needs of the two parties","That describes a forward."),
  ("Always settled by delivery","Many futures (e.g. index futures) are cash settled."),
  ("Free of any margin requirement","Futures need initial margin and daily MTM."))
Q(C,"S","Ignoring costs, trading in derivatives is described as a:",
  "Zero-sum game",
  "One side's gain equals the other side's loss. No new wealth is created by the contract itself.",
  ("Positive-sum game","Derivatives don't create wealth; they transfer risk."),
  ("Negative-sum game","It becomes negative-sum only after costs. The question says ignore costs."),
  ("Wealth-creating activity","Wealth is only moved between the two sides."))
Q(C,"S","A hedger uses derivatives to:",
  "Reduce an existing price risk",
  "A hedger already has exposure (holds or will hold the asset) and takes an opposite derivative position to cut risk.",
  ("Take extra risk for profit","That is a speculator."),
  ("Earn riskless profit from price gaps","That is an arbitrageur."),
  ("Increase leverage on a view","Leverage on a view is speculation."))
Q(C,"S","An arbitrageur in derivatives markets:",
  "Profits from price differences between markets with little or no risk",
  "Buy where cheap, sell where expensive, at the same time. This keeps prices across markets in line.",
  ("Takes large directional bets","That is a speculator."),
  ("Reduces risk on assets they hold","That is a hedger."),
  ("Only buys options","Arbitrage uses any instrument; it is about mispricing."))
Q(C,"S","What role does a speculator play in derivatives markets?",
  "Takes on risk and adds liquidity",
  "Speculators take the other side of hedgers' trades. They bear the risk hedgers want to shed and make the market liquid.",
  ("Removes price risk from the market","Speculators take risk, they don't remove it."),
  ("Guarantees settlement of trades","The clearing corporation guarantees settlement."),
  ("Sets the exchange's margin rates","Margins are set by the exchange/clearing corporation."))
Q(C,"S","In exchange-traded derivatives, counterparty risk is removed because:",
  "The clearing corporation becomes the counterparty to both sides (novation)",
  "Novation: the clearing corporation is buyer to every seller and seller to every buyer, so traders don't face each other.",
  ("The exchange insures every trader's profit","The guarantee is for settlement, not for profit."),
  ("SEBI pays any defaulted amount","SEBI regulates; it does not pay defaults."),
  ("Brokers carry no positions","Brokers' positions have nothing to do with counterparty risk."))
Q(C,"S","A swap is a contract to:",
  "Exchange a series of cash flows between two parties",
  "Example: interest rate swap — one side pays fixed, the other pays floating, on a notional amount.",
  ("Buy an asset at today's price for future delivery","That is a forward."),
  ("Get the right to buy an asset","That is a call option."),
  ("Buy shares on margin","That is margin trading, not a swap."))
Q(C,"S","The buyer of an option has:",
  "A right but not an obligation",
  "The buyer pays the premium and can choose to exercise. The seller has the obligation.",
  ("An obligation but no right","That describes the option seller (writer)."),
  ("Both a right and an obligation","Both obligations exist in futures, not for an option buyer."),
  ("Neither a right nor an obligation","The buyer paid a premium for the right."))
Q(C,"S","In an option contract, the premium is paid by:",
  "The option buyer to the option seller",
  "The buyer pays the premium for the right. The seller receives it for taking the obligation.",
  ("The option seller to the buyer","Reversed. The seller receives the premium."),
  ("Both parties to the exchange","The exchange charges fees, but the premium goes buyer → seller."),
  ("The clearing corporation","The clearing corporation guarantees settlement; it doesn't pay premium."))
Q(C,"S","SPAN is a system used to calculate:",
  "Initial margin",
  "SPAN estimates the worst likely one-day loss of a portfolio under many price and volatility scenarios. That sets initial margin.",
  ("Daily mark-to-market profit and loss","MTM is just today's settlement price minus yesterday's. No SPAN needed."),
  ("Option premium","Premium comes from the market (or a pricing model like Black-Scholes)."),
  ("Securities transaction tax","STT is a fixed rate set by law."))
Q(C,"S","Daily settlement of profits and losses on futures positions is called:",
  "Mark-to-market (MTM)",
  "Each day the position is valued at the settlement price; the gain or loss is paid in cash.",
  ("Novation","Novation means the clearing corporation becomes the counterparty."),
  ("Exercise","Exercise applies to options."),
  ("Rollover","Rollover means moving a position to the next expiry."))
Q(C,"S","Which of these is an OTC derivative?",
  "An interest rate swap negotiated between two banks",
  "OTC = negotiated directly between two parties, not on an exchange.",
  ("Nifty index futures","Traded on NSE: exchange-traded."),
  ("Stock options on NSE","Exchange-traded."),
  ("Interest rate futures on NSE","Exchange-traded."))
Q(C,"S","Which of these is NOT an economic function of derivatives markets?",
  "Guaranteeing returns to investors",
  "Derivatives help price discovery, risk transfer and liquidity. Nothing guarantees returns.",
  ("Price discovery","Futures prices reflect expected prices: a real function."),
  ("Transfer of risk","Hedgers pass risk to speculators: a real function."),
  ("Improving liquidity in the underlying market","Derivatives draw more participants: a real function."))
Q(C,"S","The underlying of a derivative can be:",
  "All of these: shares, indices, commodities, currencies and interest rates",
  "Any asset or rate with a measurable price can be an underlying.",
  ("Only equity shares","Too narrow."),
  ("Only commodities","Too narrow."),
  ("Only stock indices","Too narrow."))
Q(C,"S","Exchange-traded equity derivatives in India are regulated by:",
  "SEBI",
  "SEBI regulates the securities markets, including equity derivatives on NSE/BSE.",
  ("RBI","RBI regulates OTC interest rate and currency derivatives, not exchange equity derivatives."),
  ("Ministry of Corporate Affairs","MCA administers company law."),
  ("AMFI","AMFI is the mutual fund industry body."))
Q(C,"S","OTC interest rate derivatives in India are regulated by:",
  "RBI",
  "RBI regulates OTC interest rate derivatives such as IRS and FRA.",
  ("SEBI","SEBI regulates exchange-traded products. OTC rate derivatives are RBI's."),
  ("IRDAI","IRDAI regulates insurance."),
  ("PFRDA","PFRDA regulates pensions."))
Q(C,"S","Leverage in derivatives arises because:",
  "A small margin controls a large position",
  "You pay, say, 15% margin but gain or lose on 100% of the contract value.",
  ("The exchange lends money to traders","The exchange lends nothing; margin is a deposit."),
  ("Derivatives have no price risk","They have full price risk on the notional value."),
  ("Premiums are refunded at expiry","Premiums are never refunded."))
Q(C,"S","Compared with OTC derivatives, exchange-traded derivatives have:",
  "Higher transparency and liquidity",
  "Prices and volumes are public, and standard contracts attract many traders.",
  ("Customised terms","Customisation is an OTC feature."),
  ("Higher counterparty risk","Lower: the clearing corporation guarantees."),
  ("No margin requirement","Exchange-traded products always require margins."))
Q(C,"S","The notional value of a futures position equals:",
  "Futures price × lot size × number of lots",
  "Notional value = the full value of the underlying the contract controls.",
  ("Margin paid","Margin is only a fraction of notional value."),
  ("Premium × lot size","Premium applies to options, and it isn't the notional value."),
  ("Spot price ÷ lot size","Dividing by lot size makes no sense here."))
Q(C,"S","The Settlement Guarantee Fund is maintained by:",
  "The clearing corporation",
  "The SGF lets the clearing corporation complete settlement even if a member defaults.",
  ("SEBI","SEBI supervises but doesn't keep the SGF."),
  ("Each stock broker separately","It's a common fund at the clearing corporation."),
  ("The Ministry of Finance","Not involved in settlement."))
Q(C,"S","The world's earliest organised futures exchange was:",
  "Chicago Board of Trade (1848)",
  "CBOT started organised grain futures trading in 1848.",
  ("NSE","NSE started in the 1990s."),
  ("London Stock Exchange","LSE is a stock exchange, not the first futures exchange."),
  ("Bombay Stock Exchange","BSE (1875) is the oldest in Asia, but not a futures pioneer."))
Q(C,"S","In a cash-settled derivative:",
  "Only the price difference is paid; the underlying is not delivered",
  "Index futures and index options in India are cash settled — an index can't be delivered.",
  ("The underlying is always delivered","That is physical settlement."),
  ("The buyer pays the full contract value","Only the difference changes hands."),
  ("No settlement happens at expiry","Cash settlement happens at expiry."))
Q(C,"S","Physical settlement of a derivative means:",
  "The underlying asset is delivered against payment",
  "Stock futures and stock options in India are physically settled at expiry.",
  ("Only the price difference is paid","That is cash settlement."),
  ("The contract is cancelled","Settlement completes the contract."),
  ("Margins are refunded","Margins are released, but delivery is the point."))
Q(C,"S","Which participant helps keep prices in different markets in line with each other?",
  "Arbitrageur",
  "Arbitrageurs buy in the cheap market and sell in the dear market until the gap closes.",
  ("Hedger","Hedgers cut their own risk; they don't target price gaps."),
  ("Speculator","Speculators bet on direction."),
  ("Custodian","Custodians hold assets; they don't trade."))

Q(C,"S","Which of these is exchange-traded?",
  "Stock futures on NSE",
  "Stock futures are standard contracts traded on NSE/BSE and cleared by the clearing corporation.",
  ("A forward contract between an importer and a bank","Forwards are OTC."),
  ("An interest rate swap between two companies","Swaps are mostly OTC."),
  ("A forward rate agreement","FRAs are OTC."))
Q(C,"H","An option buyer pays ₹12,000 premium for one lot. The underlying moves sharply against the position. What is the most the buyer can lose?",
  "₹12,000","An option buyer's loss is capped at the premium paid. No margin calls.",
  ("Unlimited","That's an option seller (for calls)."),
  ("The full contract value","The buyer only risks the premium."),
  ("₹12,000 plus daily MTM losses","Option buyers have no MTM; the premium is paid in full upfront."))
# Ch13 harder
for cv, m, mv in [(20, 15, 3), (16, 12.5, -2), (25, 12, 4)]:
    cvr = cv * 1e5
    margin = cvr * m / 100
    pl = cvr * mv / 100
    ret = pl / margin * 100
    Q(C,"H",f"A futures contract has a value of {inr(cvr)} and the margin is {m}%. The price moves {mv:+}%. What is the return on the margin money?",
      f"{ret:+.1f}%",
      f"Margin = {inr(margin)}. P&L = {mv:+}% × {inr(cvr)} = {inr(pl)}. Return = P&L ÷ margin = {ret:+.1f}%. Leverage = 100 ÷ {m} = {100/m:.1f}×.",
      (f"{mv:+.1f}%","That is the price move. You paid only the margin, so your return is magnified."),
      (f"{mv*m:+.1f}%","You multiplied by the margin rate. Divide by it instead."),
      (f"{mv/m*10:+.1f}%","Wrong scaling. Return = price move ÷ margin rate."))
for fp, lot in [(24800, 75), (51200, 30)]:
    nv = fp * lot
    Q(C,"H",f"An index futures contract trades at {num(fp,0)} with a lot size of {lot}. What is the notional value of one lot?",
      inr(nv),
      f"Notional = price × lot = {num(fp,0)} × {lot} = {inr(nv)}.",
      (inr(nv/10),"Off by a factor of 10. Check your multiplication."),
      (inr(nv*10),"Off by a factor of 10. Check your multiplication."),
      (inr(fp),"That is just the index level, not the value of one lot."))
Q(C,"H","A trader has ₹3 lakh. The margin on stock futures is 15%. What is the largest notional position the trader can take?",
  "₹20 lakh","Position = cash ÷ margin rate = 3,00,000 ÷ 0.15 = ₹20,00,000.",
  ("₹45,000","You multiplied by 15%. Divide instead."),
  ("₹3.45 lakh","Margin isn't added on top. Divide cash by the margin rate."),
  ("₹2 lakh","Off by a factor of 10."))
Q(C,"H","A jeweller must buy gold in 3 months and buys gold futures today. Gold rises 8% by then. What is the net effect?",
  "The futures gain offsets the higher purchase cost, so the price is roughly locked",
  "This is a long (buying) hedge. Higher cash price is paid, but the futures profit makes up for it.",
  ("The jeweller loses 8% on the futures","Long futures gain when price rises."),
  ("The jeweller gains 8% overall","The gain is offset by the higher cost of gold. Net ≈ locked price."),
  ("The hedge fails because gold rose","A hedge works both ways; the point is to lock the price."))
Q(C,"H","Which statement is TRUE?",
  "In futures both parties have obligations; in options only the seller has an obligation",
  "Futures: both must perform. Options: buyer has the right, seller has the obligation.",
  ("In options both parties have obligations","The option buyer only has a right."),
  ("In futures only the buyer has an obligation","Both buyer and seller of futures are obliged."),
  ("Option buyers must pay margin daily","Option buyers pay the full premium upfront; sellers pay margin."))
Q(C,"H","Which statement about the clearing corporation is NOT true?",
  "It guarantees profits to all traders",
  "It guarantees settlement of trades, not anyone's profit.",
  ("It acts as counterparty to every trade","True: novation."),
  ("It collects margins from members","True."),
  ("It runs daily mark-to-market settlement","True."))
Q(C,"H","An investor fully hedges a share portfolio with futures. What does the hedge do?",
  "Removes both the downside and the upside",
  "A futures hedge locks the value: losses and gains on shares are offset by the futures.",
  ("Removes only the downside","Only an options hedge (protective put) keeps the upside."),
  ("Removes only the upside","It removes both."),
  ("Doubles the exposure","An opposite position reduces, not doubles, exposure."))
Q(C,"H","A share trades at ₹500 on NSE and ₹502 on BSE at the same moment. What does an arbitrageur do?",
  "Buy on NSE and sell on BSE, earning ₹2 per share before costs",
  "Buy cheap, sell dear, at the same time.",
  ("Buy on BSE and sell on NSE","That locks in a ₹2 loss."),
  ("Buy on both exchanges","That is a directional bet, not arbitrage."),
  ("Wait for prices to equalise","Arbitrage acts now, while the gap exists."))
Q(C,"H","An exporter must sell USD 1,37,500 on an exact date that doesn't match exchange contract sizes or expiries. Which product suits best?",
  "An OTC forward contract with a bank",
  "Forwards can be customised to the exact amount and date.",
  ("Exchange currency futures","Standard lots and expiry dates won't match exactly."),
  ("Index options","An equity index doesn't hedge currency risk."),
  ("Stock futures","Wrong underlying."))
Q(C,"H","Which risk is NOT removed by trading on an exchange instead of OTC?",
  "Market (price) risk",
  "The clearing corporation removes counterparty risk. Your position can still lose if the price moves against you.",
  ("Counterparty default risk","Removed by novation."),
  ("Settlement risk","Covered by the clearing corporation and SGF."),
  ("Risk of non-transparent prices","Exchange prices are public."))
Q(C,"H","SPAN margin is based on:",
  "The worst likely loss of the whole portfolio under many scenarios",
  "SPAN tests price and volatility scenarios and charges the worst one-day loss. It looks at the whole portfolio, so offsetting positions need less margin.",
  ("A flat percentage of each contract","Exposure margin is a flat %, but SPAN is scenario-based."),
  ("The trader's annual income","Income is irrelevant."),
  ("The option premium only","Premium is not the margin basis."))
Q(C,"H","Day 1 MTM is a loss of ₹40,000 and Day 2 MTM is a gain of ₹15,000 on the same futures position. What is the net cash outflow over two days?",
  "₹25,000","Cash flows: −40,000 + 15,000 = −25,000.",
  ("₹55,000","You added the gain as a loss."),
  ("₹40,000","You ignored the Day 2 gain."),
  ("₹15,000","That is only Day 2."))
Q(C,"H","Why do forward contracts carry more default risk than futures?",
  "There is no daily MTM, so losses build up till maturity",
  "With MTM, losses are paid daily and stay small. A forward's loss grows unpaid until the end.",
  ("Forwards are always larger","Size is not the reason."),
  ("Forwards are regulated by SEBI","Regulation isn't the reason, and most forwards are OTC."),
  ("Forwards have no underlying","They do have an underlying."))
Q(C,"H","The exchange raises the margin on index futures. What is the likely effect?",
  "Leverage falls and speculative positions tend to shrink",
  "Higher margin = more cash per contract = less leverage.",
  ("Leverage rises","Higher margin means lower leverage."),
  ("Index futures stop trading","Trading continues; it just needs more cash."),
  ("Option premiums double","No direct link."))
Q(C,"H","A company with a floating-rate loan fears rates will rise. Which swap position hedges this?",
  "Pay fixed, receive floating",
  "The floating receipt from the swap offsets the floating loan payment, leaving a fixed cost.",
  ("Pay floating, receive fixed","That adds more floating exposure."),
  ("Pay floating, receive floating","No hedge; it does nothing useful."),
  ("Buy index futures","Equity futures don't hedge interest rates."))
Q(C,"H","A hedger gains ₹5 lakh on a futures position. Ignoring costs, what happens on the other side?",
  "The counterparties lose ₹5 lakh in total",
  "Zero-sum: total gains equal total losses.",
  ("The exchange pays the ₹5 lakh","The exchange passes cash between members; it doesn't fund profits."),
  ("No one loses because the hedger was hedging","Purpose doesn't change the zero-sum nature."),
  ("SEBI pays from the investor protection fund","Not how MTM works."))

# =====================================================================
# CH 15  FORWARDS AND FUTURES
# =====================================================================
C = 15
Q(C,"S","A forward contract is traded:",
  "Over the counter, between two parties",
  "Forwards are private, custom contracts. No exchange, no daily MTM.",
  ("On a stock exchange","Futures are exchange-traded; forwards are not."),
  ("Only through the clearing corporation","The clearing corporation handles exchange trades."),
  ("Only by RBI","Anyone with a counterparty can enter a forward."))
Q(C,"S","In exchange-traded futures, who bears the counterparty risk?",
  "The clearing corporation",
  "Through novation the clearing corporation stands between buyer and seller.",
  ("The buyer","The buyer faces the clearing corporation, not the seller."),
  ("The seller","Same: the seller faces the clearing corporation."),
  ("SEBI","SEBI regulates, it doesn't guarantee trades."))
Q(C,"S","Basis is defined as:",
  "Spot price − futures price",
  "Basis = Spot − Futures. In a normal (contango) market, basis is negative.",
  ("Futures price − spot price","Sign reversed. NISM defines basis as spot minus futures."),
  ("Futures price × lot size","That's notional value."),
  ("Spot price ÷ futures price","Basis is a difference, not a ratio."))
Q(C,"S","At expiry of a futures contract, the basis is:",
  "Zero",
  "Convergence: on expiry day futures settle at the spot price, so spot − futures = 0.",
  ("Equal to the cost of carry","Carry shrinks to zero as time to expiry shrinks to zero."),
  ("Always negative","Negative basis is normal before expiry, not at expiry."),
  ("Equal to the initial margin","Margin is unrelated to basis."))
Q(C,"S","A market where futures prices are higher than the spot price is in:",
  "Contango",
  "Contango = futures > spot (normal, because of carrying cost). Backwardation = futures < spot.",
  ("Backwardation","Backwardation is futures below spot."),
  ("Convergence","Convergence is futures moving to spot near expiry."),
  ("Arbitrage","Arbitrage is a trade, not a market state."))
Q(C,"S","Index futures may trade below spot (backwardation) when:",
  "The expected dividend yield is higher than the interest rate",
  "Fair futures ≈ Spot × (1 + r − d). If d > r, futures fall below spot.",
  ("Interest rates are very high","High r pushes futures above spot."),
  ("Time to expiry is long","Longer time magnifies the carry, whichever way it points."),
  ("Margins are high","Margins don't enter the fair-value formula."))
Q(C,"S","For index futures, the cost of carry equals:",
  "Interest cost minus dividend yield",
  "Holding the index costs interest but earns dividends; net carry = r − d.",
  ("Interest cost plus dividend yield","Dividends reduce carry; you receive them."),
  ("Brokerage plus STT","Transaction costs aren't the carry in the pricing model."),
  ("Initial margin rate","Margin is not part of fair value."))
Q(C,"S","Futures are trading above their fair value. What does an arbitrageur do?",
  "Buy in the spot market and sell futures (cash-and-carry)",
  "Sell the overpriced futures, buy the cheaper spot, carry it to expiry.",
  ("Sell spot and buy futures","That's reverse cash-and-carry, used when futures are cheap."),
  ("Buy both spot and futures","Two long positions is a directional bet."),
  ("Sell both spot and futures","Two short positions is a directional bet."))
Q(C,"S","Reverse cash-and-carry arbitrage involves:",
  "Selling the spot and buying futures",
  "Used when futures are below fair value: buy the cheap futures, sell (short) the spot.",
  ("Buying spot and selling futures","That's normal cash-and-carry."),
  ("Buying a call and a put","That's a straddle."),
  ("Buying futures only","One leg alone isn't arbitrage."))
Q(C,"S","An investor holds a share portfolio and fears the market will fall. Which futures trade hedges the risk?",
  "Sell index futures",
  "Short hedge: losses on shares are offset by gains on the short futures.",
  ("Buy index futures","That doubles the long exposure."),
  ("Buy more shares","More exposure, not a hedge."),
  ("Do nothing; futures can't hedge shares","Index futures are the standard tool for this."))
Q(C,"S","An investor will receive cash in one month and wants to invest in equities. She fears the market will rise before then. She should:",
  "Buy index futures now",
  "Long (anticipatory) hedge: if the market rises, the futures gain offsets the higher buying price.",
  ("Sell index futures now","That gains if the market falls — the opposite of her risk."),
  ("Sell call options","That gives premium but loses if the market rises."),
  ("Wait for the cash","Waiting leaves her fully exposed to a rise."))
Q(C,"S","The payoff of a long futures position is:",
  "Linear, with unlimited profit and unlimited loss",
  "Every ₹1 move in price gives ₹1 × lot profit or loss. No cap on either side.",
  ("Limited loss, unlimited profit","That's a long call."),
  ("Limited profit, unlimited loss","That's a short call."),
  ("Fixed regardless of price","Futures P&L moves with the price."))
Q(C,"S","Index futures in India are settled:",
  "In cash",
  "An index can't be delivered, so only the price difference is paid.",
  ("By physical delivery of all index shares","Impossible in practice. Index futures are cash settled."),
  ("At the buyer's choice","No choice; settlement is fixed by the exchange."),
  ("In gold","No."))
Q(C,"S","Stock futures in India are settled at expiry by:",
  "Physical delivery of the shares",
  "SEBI moved all stock derivatives to physical settlement in phases from 2018–19.",
  ("Cash only","Stock futures were cash settled earlier, but now they're physically settled."),
  ("Delivery of index units","No."),
  ("Settlement in the next month's contract","Expired contracts settle; they don't roll automatically."))
Q(C,"S","How often are futures positions marked to market?",
  "Daily",
  "Gains and losses are settled every trading day at the daily settlement price.",
  ("Weekly","Too slow. MTM is daily."),
  ("Only at expiry","That would be a forward."),
  ("Monthly","Too slow."))
Q(C,"S","Futures price rises and open interest rises. This usually signals:",
  "Long build-up (bullish)",
  "New buyers are opening positions and pushing price up.",
  ("Short build-up","That's price falling with OI rising."),
  ("Short covering","That's price rising with OI falling."),
  ("Long unwinding","That's price falling with OI falling."))
Q(C,"S","Futures price falls and open interest rises. This usually signals:",
  "Short build-up (bearish)",
  "New sellers are opening positions and pushing price down.",
  ("Long build-up","That's price up, OI up."),
  ("Short covering","That's price up, OI down."),
  ("Long unwinding","That's price down, OI down."))
Q(C,"S","Futures price rises and open interest falls. This usually signals:",
  "Short covering",
  "Shorts buy back to close positions, so OI drops while price rises.",
  ("Long build-up","That needs rising OI."),
  ("Short build-up","That needs falling price and rising OI."),
  ("Long unwinding","That needs falling price."))
Q(C,"S","Futures price falls and open interest falls. This usually signals:",
  "Long unwinding",
  "Longs sell to close positions; price falls and OI drops.",
  ("Short build-up","That needs rising OI."),
  ("Short covering","That needs rising price."),
  ("Long build-up","That needs rising price and OI."))
Q(C,"S","Equity futures in India follow a contract cycle of:",
  "Three months (near, middle and far month)",
  "At any time, three monthly contracts are available.",
  ("One month only","Three months are available."),
  ("Six months","That's longer than the standard cycle."),
  ("Twelve months","Not for stock and index futures."))
Q(C,"S","In a futures contract, who deposits initial margin?",
  "Both the buyer and the seller",
  "Both sides have obligations, so both post margin. (In options, only the seller does.)",
  ("Only the buyer","Both."),
  ("Only the seller","That's options."),
  ("Neither","Margin is always required."))
Q(C,"S","Why does the futures price usually stay above the spot price?",
  "Because of the cost of carry (interest on money)",
  "Buying futures instead of spot saves interest, so futures carry that interest in the price.",
  ("Because buyers expect prices to rise","Expectations don't set fair value; arbitrage ties futures to spot + carry."),
  ("Because of high margins","Margins don't set the price."),
  ("Because futures have lower risk","Futures carry the same price risk."))
Q(C,"S","As expiry approaches, the futures price:",
  "Moves towards the spot price",
  "Carry shrinks as time shrinks; at expiry, futures = spot.",
  ("Moves away from the spot price","Opposite of convergence."),
  ("Becomes fixed","It keeps trading till expiry."),
  ("Doubles","No."))
Q(C,"S","The fair value of a futures contract depends on all of the following EXCEPT:",
  "The trader's view of the future spot price",
  "Fair value = spot, interest rate, time and dividends. Personal views don't enter the formula.",
  ("Spot price","Core input."),
  ("Interest rate","Core input."),
  ("Expected dividends","Core input for index and stock futures."))
Q(C,"S","A trader is bullish on a stock but has limited capital. Which trade gives the most exposure per rupee?",
  "Buy stock futures",
  "Futures need only margin, so the same capital controls a larger position.",
  ("Buy shares in the cash market","Full payment needed: less exposure per rupee."),
  ("Sell stock futures","That's bearish."),
  ("Buy a put option","That's bearish."))
Q(C,"S","Margin money in futures is best described as:",
  "A performance guarantee deposit",
  "Margin is a deposit to make sure you can meet losses; it is not a part payment for the asset.",
  ("Part payment for the asset","You don't pay for the asset until delivery (if any)."),
  ("A fee to the exchange","Fees are separate; margin is returned when you close."),
  ("Premium paid to the seller","Premium belongs to options."))
Q(C,"S","A long futures position has an MTM loss today. The trader must:",
  "Pay the loss in cash to the clearing corporation",
  "MTM losses are paid in cash, usually next day.",
  ("Wait until expiry to pay","That's a forward."),
  ("Receive cash from the clearing corporation","Receiving is for MTM gains."),
  ("Exercise the contract","Exercise applies to options."))
Q(C,"S","Open interest in futures means:",
  "The number of contracts still outstanding (not closed)",
  "Each open contract has one long and one short; OI counts them once.",
  ("The number of contracts traded today","That's volume."),
  ("The interest rate in the futures price","Unrelated."),
  ("The total margin collected","Unrelated."))
Q(C,"S","A calendar spread in futures means:",
  "Buying one month's futures and selling another month's futures on the same underlying",
  "A bet on the price gap between two expiries, not on direction.",
  ("Buying futures on two different stocks","That's an inter-commodity/pair trade."),
  ("Buying a call and a put","That's a straddle."),
  ("Buying spot and selling futures","That's cash-and-carry."))
Q(C,"S","A forward contract has low liquidity mainly because:",
  "Its terms are customised for the two parties",
  "A custom contract is hard to transfer to someone else.",
  ("It is exchange-traded","Forwards are OTC."),
  ("It is marked to market daily","Forwards are not marked to market daily."),
  ("It has no underlying","It has one."))
Q(C,"S","When a stock crosses 95% of its market-wide position limit (MWPL):",
  "It enters a ban period: only trades that reduce positions are allowed",
  "No fresh positions in that stock's F&O until OI falls below 80% of MWPL.",
  ("Trading in the stock's shares stops","The cash market continues."),
  ("All positions are cancelled","Existing positions stay; only new ones are blocked."),
  ("Margins are refunded","No."))
Q(C,"S","Hedging with futures generally:",
  "Removes both downside and upside",
  "The futures gain/loss offsets the asset's loss/gain. You lock the value.",
  ("Removes only downside","That needs a put option."),
  ("Increases profit potential","It reduces it."),
  ("Removes basis risk","Basis risk remains."))

def f_simple(S, r, m):
    return S * (1 + r/100 * m/12)
for S, r, m in [(2000, 10, 3), (1500, 8, 6), (5000, 6, 2)]:
    F = f_simple(S, r, m)
    Q(C,"S",f"Spot price is ₹{num(S,0)}, the interest rate is {r}% a year and there are no dividends. Using simple interest, what is the fair price of a {m}-month futures?",
      f"₹{num(F)}",
      f"F = S × (1 + r × t) = {num(S,0)} × (1 + {r/100} × {m}/12) = ₹{num(F)}.",
      (f"₹{num(S*(1+r/100))}","You used a full year. Use t = months ÷ 12."),
      (f"₹{num(S*(1+r/100*1/12))}","You used 1 month instead of the stated period."),
      (f"₹{num(S,2)}","Futures trade at spot + carry, not at spot."))
for S, D, r, m in [(1000, 20, 12, 3), (2400, 30, 8, 6)]:
    F = (S - D) * (1 + r/100*m/12)
    Q(C,"S",f"A stock trades at ₹{num(S,0)}. A dividend of ₹{D} is due before expiry (ignore discounting). The interest rate is {r}% a year. What is the fair price of a {m}-month futures (simple interest)?",
      f"₹{num(F)}",
      f"Remove the dividend first: ({num(S,0)} − {D}) × (1 + {r/100} × {m}/12) = ₹{num(F)}.",
      (f"₹{num(f_simple(S,r,m))}","You ignored the dividend. The futures buyer doesn't get it, so subtract it."),
      (f"₹{num((S+D)*(1+r/100*m/12))}","You added the dividend. It should be subtracted."),
      (f"₹{num(S-D)}","You removed the dividend but forgot the interest."))
for S, F in [(24500, 24650), (1810, 1798)]:
    b = S - F
    Q(C,"S",f"Spot Nifty/stock price is {num(S,0)} and the near-month futures is {num(F,0)}. What is the basis?",
      f"{b:+,.0f}",
      f"Basis = Spot − Futures = {num(S,0)} − {num(F,0)} = {b:+,.0f}.",
      (f"{-b:+,.0f}","Sign reversed. Basis = spot − futures."),
      ("0","Basis is zero only at expiry."),
      (f"{S+F:,.0f}","Basis is a difference, not a sum."))
for P, beta, F, lot in [(1.5e7, 1.25, 25000, 75), (3e7, 0.8, 24000, 50), (9e6, 1.5, 22500, 40)]:
    cv = F*lot; n = P*beta/cv
    Q(C,"S",f"A portfolio worth {inr(P)} has a beta of {beta}. Index futures trade at {num(F,0)} with a lot size of {lot}. How many lots should be sold to hedge fully?",
      f"{n:.0f} lots",
      f"Lot value = {num(F,0)} × {lot} = {inr(cv)}. Lots = Portfolio × β ÷ lot value = {inr(P)} × {beta} ÷ {inr(cv)} = {n:.0f}.",
      (f"{P/cv:.0f} lots","You ignored beta. Multiply portfolio value by beta."),
      (f"{P/beta/cv:.0f} lots","You divided by beta. Multiply instead."),
      (f"{n*lot:.0f} lots","You multiplied by lot size twice."))
for side, lots, entry, exitp, lot in [("bought",2,1200,1185,500),("sold",3,850,838,600),("bought",1,3150,3201,250)]:
    sign = 1 if side=="bought" else -1
    pl = sign*(exitp-entry)*lots*lot
    Q(C,"S",f"A trader {side} {lots} lot(s) of stock futures at ₹{num(entry,0)}, lot size {lot}. The settlement price today is ₹{num(exitp,0)}. What is today's MTM?",
      f"{'Gain' if pl>0 else 'Loss'} of {inr(abs(pl))}",
      f"MTM = {'(settle − entry)' if sign>0 else '(entry − settle)'} × lot × lots = {inr(pl)}.",
      (f"{'Loss' if pl>0 else 'Gain'} of {inr(abs(pl))}","Right size, wrong sign. A long gains when price rises; a short gains when price falls."),
      (f"{'Gain' if pl>0 else 'Loss'} of {inr(abs(pl)/lots)}" if lots>1 else f"{'Gain' if pl>0 else 'Loss'} of {inr(abs(pl)*2)}","Check the number of lots."),
      (f"{'Gain' if pl>0 else 'Loss'} of {inr(abs(exitp-entry)*lots)}","You forgot to multiply by lot size."))
for S, F, r, m in [(1000, 1040, 12, 3), (2500, 2560, 6, 2)]:
    fair = f_simple(S, r, m); prof = F - fair
    Q(C,"S",f"Spot is ₹{num(S,0)}, {m}-month futures is ₹{num(F,0)} and the interest rate is {r}% a year (simple). Ignoring costs, what arbitrage profit per share is available?",
      f"₹{num(prof)} by buying spot and selling futures",
      f"Fair value = {num(S,0)} × (1 + {r/100} × {m}/12) = {num(fair)}. Futures is ₹{num(prof)} too high → cash-and-carry.",
      (f"₹{num(F-S)} by buying spot and selling futures","That's the raw gap. You forgot the interest cost of carrying the spot."),
      (f"₹{num(prof)} by selling spot and buying futures","Wrong direction. Futures is overpriced, so sell it."),
      ("No arbitrage is available","Futures is above fair value, so cash-and-carry pays."))

# Ch15 harder
for S, r, t in [(1000, 8, 0.5), (2500, 7, 0.25)]:
    F = S*math.exp(r/100*t)
    Q(C,"H",f"Spot is ₹{num(S,0)}, interest is {r}% a year (continuously compounded), time to expiry {t} years, no dividends. What is the fair futures price?",
      f"₹{num(F)}",
      f"F = S × e^(rt) = {num(S,0)} × e^({r/100*t:.4f}) = ₹{num(F)}.",
      (f"₹{num(S*(1+r/100*t))}","That's simple interest. The question says continuous compounding."),
      (f"₹{num(S*math.exp(r/100))}","You used a full year instead of t."),
      (f"₹{num(S*math.exp(-r/100*t))}","You discounted instead of compounding."))
for S, r, d, m in [(20000, 7, 2, 3), (24000, 6.5, 1.5, 2)]:
    t = m/12; F = S*math.exp((r-d)/100*t)
    Q(C,"H",f"Nifty spot is {num(S,0)}, risk-free rate {r}%, dividend yield {d}% (both continuous). What is the fair price of the {m}-month futures?",
      f"{num(F)}",
      f"F = S × e^((r − d) × t) = {num(S,0)} × e^({(r-d)/100:.3f} × {t:.4f}) = {num(F)}.",
      (f"{num(S*math.exp(r/100*t))}","You ignored the dividend yield."),
      (f"{num(S*math.exp((r+d)/100*t))}","You added dividend yield. It reduces carry."),
      (f"{num(S*math.exp((r-d)/100))}","You used a full year."))
for S, F, m in [(4000, 4060, 3), (1200, 1209, 1)]:
    rr = (F/S-1)*12/m*100
    Q(C,"H",f"Spot is ₹{num(S,0)} and the {m}-month futures is ₹{num(F,0)}. No dividends. What annual interest rate (simple) is implied?",
      f"{rr:.1f}%",
      f"Return for the period = {F-S}/{S} = {(F/S-1)*100:.2f}%. Annualise: × 12/{m} = {rr:.1f}%.",
      (f"{(F/S-1)*100:.2f}%","Not annualised."),
      (f"{rr/2:.1f}%","Check the annualising factor: multiply by 12 ÷ months."),
      (f"{rr*2:.1f}%","Check the annualising factor."))
for S, F, r, m, cost in [(800, 815, 9, 1, 4), (1500, 1530, 8, 2, 6)]:
    fair = f_simple(S, r, m); net = F - fair - cost
    Q(C,"H",f"Spot ₹{num(S,0)}, {m}-month futures ₹{num(F,0)}, interest {r}% a year (simple), total transaction costs ₹{cost} per share. What is the net arbitrage profit per share?",
      f"₹{num(net)}",
      f"Fair = {num(S,0)} × (1 + {r/100} × {m}/12) = {num(fair)}. Gross = {num(F-fair)}. Net = gross − {cost} = ₹{num(net)}.",
      (f"₹{num(F-S)}","Raw gap: you ignored both interest and costs."),
      (f"₹{num(F-fair)}","You ignored transaction costs."),
      (f"₹{num(F-S-cost)}","You ignored the interest cost of carrying the spot."))
for P, b0, b1, F, lot in [(5e7, 1.4, 0.8, 25000, 75), (2e7, 0.9, 1.2, 20000, 60), (6e7, 1.1, 0, 25000, 60)]:
    cv = F*lot; n = (b1-b0)*P/cv
    act = "Buy" if n > 0 else "Sell"
    Q(C,"H",f"A {inr(P)} portfolio has beta {b0}. The manager wants beta {b1}. Index futures: {num(F,0)}, lot {lot}. What should the manager do?",
      f"{act} {abs(n):.0f} lots",
      f"Lots = (target β − current β) × P ÷ lot value = ({b1} − {b0}) × {inr(P)} ÷ {inr(cv)} = {n:+.0f}. Negative = sell, positive = buy.",
      (f"{'Sell' if n>0 else 'Buy'} {abs(n):.0f} lots","Right size, wrong direction. To cut beta, sell; to raise it, buy."),
      (f"{act} {b0*P/cv:.0f} lots" if b1 != 0 else f"{act} {P/cv:.0f} lots","You used the full beta (or ignored beta) instead of the change in beta."),
      (f"{act} {abs(b1-b0)*P/F:.0f} lots","You divided by the index level only. Divide by lot value (price × lot)."))
for entry, d1, d2, d3, lot in [(2000, 1980, 2010, 1995, 250), (1500, 1540, 1512, 1521, 400), (900, 905, 890, 880, 1000)]:
    m3 = (d3-d2)*lot; cum = (d3-entry)*lot
    Q(C,"H",f"A trader buys 1 lot of futures at ₹{entry} (lot {lot}). Settlement prices: Day 1 ₹{d1}, Day 2 ₹{d2}, Day 3 ₹{d3}. What is the MTM cash flow on Day 3?",
      f"{inr(m3)}",
      f"Day 3 MTM = (Day 3 − Day 2) × lot = ({d3} − {d2}) × {lot} = {inr(m3)}. Each day settles against the previous day's price.",
      (f"{inr(cum)}","That's the cumulative P&L since entry, not Day 3's MTM."),
      (f"{inr(-m3)}","Sign reversed. A long gains when price rises."),
      (f"{inr((d2-d1)*lot)}","That's Day 2's MTM. Day 3 compares Day 3 with Day 2."))
for port, idx in [(-6, -5), (-3, -4)]:
    net = (port - idx)
    Q(C,"H",f"A ₹1 crore portfolio (beta 1) is fully hedged by selling Nifty futures. Nifty falls {abs(idx)}%; the portfolio falls {abs(port)}%. Ignoring basis, what is the net result?",
      f"{'Loss' if net<0 else 'Gain'} of about {inr(abs(net)*1e5)}",
      f"Portfolio: {port}% = {inr(port*1e5)}. Futures gain: {abs(idx)}% = {inr(abs(idx)*1e5)}. Net = {inr(net*1e5)}. The hedge removes market risk, not stock-specific risk.",
      ("Zero: the hedge is perfect","The portfolio moved differently from the index. That gap is not hedged."),
      (f"Loss of {inr(abs(port)*1e5)}","You forgot the futures gain."),
      (f"Gain of {inr(abs(idx)*1e5)}","You forgot the portfolio loss."))
for b0, b1 in [(-50, -20), (-30, -55)]:
    ch = b1 - b0
    Q(C,"H",f"A hedger holds shares and is short futures. The basis (spot − futures) moves from {b0} to {b1}. What is the effect on the hedger per unit?",
      f"{'Gain' if ch>0 else 'Loss'} of {abs(ch)}",
      f"Long spot + short futures gains when basis (S − F) increases (strengthens). Change = {b1} − ({b0}) = {ch:+}.",
      (f"{'Loss' if ch>0 else 'Gain'} of {abs(ch)}","Direction reversed. A short hedger gains when basis strengthens."),
      ("No effect: the hedge is perfect","Basis risk remains even in a hedge."),
      (f"{'Gain' if ch>0 else 'Loss'} of {abs(b0)+abs(b1)}","Basis change is the difference, not the sum."))
Q(C,"H","Why is the futures price NOT a forecast of the future spot price?",
  "Arbitrage ties it to spot plus the cost of carry",
  "If futures drift from spot + carry, arbitrageurs trade the gap away. So futures reflect carry, not a forecast.",
  ("Because futures are illiquid","Index futures are very liquid."),
  ("Because SEBI fixes futures prices","Prices are set by the market."),
  ("Because futures ignore interest rates","Interest is a key input."))
Q(C,"H","Basis risk arises mainly when:",
  "The hedge instrument differs from the asset, or the hedge is closed before expiry",
  "If the asset and futures don't move one-for-one, or you exit before convergence, the hedge is imperfect.",
  ("The futures is held to expiry on the same asset","Then basis converges to zero — no basis risk."),
  ("Margins are paid on time","Margin timing isn't basis risk."),
  ("The trader uses options","Options have their own risks; the question is about futures hedges."))
Q(C,"H","Hedging a mid-cap portfolio with Nifty 50 futures is an example of:",
  "A cross hedge",
  "The hedge instrument (Nifty 50) differs from the asset (mid-caps), so basis risk is higher.",
  ("A perfect hedge","Different assets — not perfect."),
  ("Cash-and-carry arbitrage","That needs spot and futures on the same asset."),
  ("A calendar spread","That uses two expiries of the same futures."))
Q(C,"H","Rolling over a futures position means:",
  "Closing the near-month contract and opening the next-month contract",
  "Done near expiry to keep the exposure. The cost is the price gap between the two months.",
  ("Converting futures into options","Not possible."),
  ("Doubling the position","Rollover keeps the size the same."),
  ("Paying MTM late","No."))
Q(C,"H","Price rises sharply while open interest falls steadily. How should this rally be read?",
  "Short covering — the rally may be weak and not driven by fresh buying",
  "Rising price with falling OI = shorts buying back, not new longs.",
  ("Strong long build-up","Long build-up needs rising OI."),
  ("Short build-up","That needs falling price."),
  ("Long unwinding","That needs falling price."))
Q(C,"H","Index futures trade below spot during dividend season. Most likely reason:",
  "Expected dividends exceed the interest cost (backwardation)",
  "F = S × (1 + r − d). When d is high, F can fall below S.",
  ("Arbitrageurs have left the market","Arbitrage keeps futures near fair value, which here is below spot."),
  ("Interest rates have risen","Higher rates push futures up."),
  ("Margins have fallen","Margins don't enter fair value."))
Q(C,"H","An investor will receive a bonus next month and plans to buy an index fund. She buys index futures now. The market falls 6%. What happens?",
  "She loses on futures, but buys the index cheaper — net price ≈ locked",
  "A long hedge locks the price both ways: the futures loss is matched by the cheaper purchase.",
  ("She gains on futures and buys cheaper","Long futures lose when the market falls."),
  ("She loses 12% in total","The futures loss is offset by the cheaper buying price."),
  ("Her hedge was wrong because the market fell","A hedge locks the price; direction doesn't make it wrong."))
Q(C,"H","An arbitrage mutual fund mainly does cash-and-carry trades. Its return should be close to:",
  "The short-term interest rate",
  "Cash-and-carry earns the carry — roughly the money-market rate — with no market risk.",
  ("The Nifty return","Market risk is hedged away."),
  ("Twice the Nifty return","No leverage like that."),
  ("Zero","It earns the carry."))
Q(C,"H","Other things equal, if interest rates rise, the fair value of stock futures will:",
  "Rise",
  "F = S × (1 + r × t). Higher r → higher F.",
  ("Fall","Higher carry raises F."),
  ("Stay the same","r is a direct input."),
  ("Become equal to spot","Only at expiry."))
Q(C,"H","A portfolio is fully beta-hedged with index futures. What return should it earn, ignoring alpha and costs?",
  "Roughly the risk-free rate",
  "Market risk is removed; holding a riskless position should earn the risk-free rate (via the futures' carry).",
  ("The market return","Market exposure is removed."),
  ("Zero, always","The futures carry gives about the risk-free rate."),
  ("Twice the market return","No."))
Q(C,"H","A calendar spread needs lower margin than an outright futures position because:",
  "The long and short legs offset most of the price risk",
  "Both legs move with the same underlying, so the net risk is small.",
  ("Calendar spreads are not marked to market","Both legs are marked to market."),
  ("The exchange gives a discount to all traders","Not a discount — it's lower risk."),
  ("Calendar spreads cannot lose money","They can lose if the gap moves against you."))
Q(C,"H","Which is the BEST reason for an investor to hedge with futures rather than sell the shares?",
  "To keep the shares (and avoid sale costs or tax) while removing market risk for a period",
  "Selling triggers costs and capital gains tax; a futures hedge removes risk temporarily.",
  ("Futures hedges remove all risk","Basis and stock-specific risk remain."),
  ("Futures don't need margin","They do."),
  ("Futures guarantee a profit","No."))

# =====================================================================
# CH 16  OPTIONS
# =====================================================================
C = 16
for q, r, w, a, b, c in [
  ("A call option gives its buyer the right to:","Buy the underlying at the strike price","A call = right to buy.",
   ("Sell the underlying at the strike price","That's a put."),("Buy at the market price on expiry","The strike price, not the market price, is fixed."),("Receive dividends","Option holders don't get dividends.")),
  ("A put option gives its buyer the right to:","Sell the underlying at the strike price","A put = right to sell.",
   ("Buy the underlying at the strike price","That's a call."),("Receive the premium","The seller receives the premium."),("Vote at company meetings","Options carry no voting rights.")),
  ("A European option can be exercised:","Only on the expiry date","European = expiry only. American = any time up to expiry.",
   ("At any time up to expiry","That's American."),("Only before expiry","Exercise is allowed on expiry."),("Only in Europe","It's a style name, not a place.")),
  ("An American option can be exercised:","At any time up to and including expiry","American = any time. European = only on expiry.",
   ("Only on expiry","That's European."),("Only after expiry","Options expire worthless after expiry."),("Only in the USA","It's a style name.")),
  ("Index options traded in India are:","European style","Index (and stock) options in India are European.",
   ("American style","Not in India."),("Exercisable any day","That's American."),("Never exercised","They are exercised at expiry if ITM (cash settled).")),
  ("A call option is in-the-money when:","Spot price > strike price","Exercising a call at K when S > K gives S − K.",
   ("Spot price < strike price","That's OTM for a call (ITM for a put)."),("Spot price = strike price","That's ATM."),("Premium > strike price","Moneyness compares S and K.")),
  ("A put option is in-the-money when:","Spot price < strike price","A put lets you sell at K when the market is lower.",
   ("Spot price > strike price","That's OTM for a put."),("Spot price = strike price","That's ATM."),("Strike price is zero","Not meaningful.")),
  ("An option is at-the-money when:","Spot price equals strike price","ATM: S = K, for both calls and puts.",
   ("Spot is far above strike","Deep ITM call / deep OTM put."),("Premium is zero","Premium of ATM options is all time value, not zero."),("It has expired","Expiry is unrelated to moneyness.")),
  ("The intrinsic value of an out-of-the-money option is:","Zero","Intrinsic value = max(0, S − K) for calls, max(0, K − S) for puts. OTM → 0.",
   ("Negative","Intrinsic value can't be negative."),("Equal to its premium minus strike","Not a valid formula."),("Equal to the strike price","No.")),
  ("At expiry, the time value of an option is:","Zero","At expiry, only intrinsic value remains.",
   ("Equal to premium","At expiry premium = intrinsic value."),("At its highest","Time value is highest with more time left."),("Negative","Time value can't be negative for these options.")),
  ("Option premium is made up of:","Intrinsic value + time value","Premium = IV + TV.",
   ("Strike price + spot price","No."),("Margin + brokerage","No."),("Intrinsic value − time value","Time value is added.")),
  ("The maximum loss for a call option buyer is:","The premium paid","The buyer can let the option lapse; loss is capped at premium.",
   ("Unlimited","That's the call seller."),("Strike price","The buyer never loses the strike."),("Strike minus premium","That's a put seller's max loss.")),
  ("The maximum loss for a call option seller (writer) is:","Unlimited","If the price keeps rising, the call writer keeps losing.",
   ("The premium received","That's the max profit."),("Strike price","No cap at the strike."),("Strike minus premium","That's for a put writer.")),
  ("The maximum profit for a put option buyer is:","Strike price − premium","The best case is the price going to zero: profit = K − 0 − premium.",
   ("Unlimited","A price can't fall below zero."),("Premium paid","That's the max loss."),("Strike price + premium","Premium is a cost, so subtract it.")),
  ("The breakeven for a call option buyer is:","Strike + premium","The price must rise above K by the premium to recover it.",
   ("Strike − premium","That's a put."),("Strike","At K the option is worth zero; premium is lost."),("Premium only","Breakeven is a price level.")),
  ("The breakeven for a put option buyer is:","Strike − premium","The price must fall below K by the premium.",
   ("Strike + premium","That's a call."),("Strike","At K the put is worthless."),("Spot + premium","Not a breakeven formula.")),
  ("If volatility of the underlying rises (other things equal):","Both call and put premiums rise","More volatility = more chance of big moves = options worth more.",
   ("Call premium rises, put premium falls","Volatility helps both."),("Both premiums fall","Opposite."),("No effect","Volatility is a key input.")),
  ("For calls on the same stock and expiry, a higher strike price means:","Lower call premium","A higher K is harder to reach, so the call is worth less.",
   ("Higher call premium","Opposite. Higher K raises put premium."),("Same premium","Strike matters."),("Zero premium","Not necessarily zero.")),
  ("If the spot price rises (other things equal), the put premium:","Falls","A put gains from falling prices; a rise hurts it.",
   ("Rises","That's a call."),("Stays the same","Spot is a key input."),("Becomes negative","Premiums can't be negative.")),
  ("The delta of a call option lies between:","0 and +1","Call value rises with spot; at most one-for-one.",
   ("−1 and 0","That's a put."),("−1 and +1","Too wide for a call alone."),("1 and 2","Delta of a single call can't exceed 1.")),
  ("The delta of a put option lies between:","−1 and 0","Put value falls as spot rises.",
   ("0 and +1","That's a call."),("1 and 2","No."),("Always exactly −0.5","Only around ATM.")),
  ("An at-the-money call has a delta of about:","0.5","ATM: roughly 50% chance of finishing ITM; delta ≈ 0.5.",
   ("1.0","That's deep ITM."),("0","That's deep OTM."),("−0.5","That's an ATM put.")),
  ("Gamma is highest for:","At-the-money options, especially near expiry","Delta changes fastest around the strike.",
   ("Deep in-the-money options","Their delta is stable near 1."),("Deep out-of-the-money options","Their delta is stable near 0."),("Options with long expiry","Gamma rises as expiry nears.")),
  ("Theta measures:","The fall in option value as time passes","Time decay. Negative for buyers, positive for sellers.",
   ("Sensitivity to volatility","That's vega."),("Sensitivity to spot price","That's delta."),("Sensitivity to interest rates","That's rho.")),
  ("Vega measures the change in option premium for a change in:","Volatility","Vega = premium change per 1% change in volatility.",
   ("Spot price","That's delta."),("Time","That's theta."),("Interest rate","That's rho.")),
  ("Rho measures sensitivity of option value to:","Interest rates","Rho is positive for calls, negative for puts.",
   ("Dividends","No standard Greek for this here."),("Volatility","That's vega."),("Delta","That's gamma.")),
  ("In exchange-traded options, margin is paid by:","The option seller","The buyer's risk is capped at the premium paid; the seller has open-ended risk.",
   ("The option buyer","Buyer pays premium, not margin."),("Both buyer and seller","That's futures."),("No one","Sellers must pay margin.")),
  ("The option writer:","Receives the premium and takes on the obligation","Writer = seller.",
   ("Pays the premium","That's the buyer."),("Has the right to exercise","That's the buyer."),("Pays no margin","Writers pay margin.")),
  ("Put-call parity relates:","Call price, put price, spot price and present value of strike","C + PV(K) = P + S for European options.",
   ("Only call and put prices","S and PV(K) are needed too."),("Strike and margin","Margin is not in parity."),("Volume and open interest","No.")),
  ("Which Black-Scholes input cannot be observed directly in the market?","Volatility","Spot, strike, time and rate are known. Volatility must be estimated (or implied).",
   ("Spot price","Observed on screen."),("Strike price","Set in the contract."),("Time to expiry","Known from the expiry date.")),
  ("Stock options in India are settled at expiry by:","Physical delivery","ITM stock options lead to delivery of shares.",
   ("Cash only","Index options are cash settled; stock options are physical."),("Delivery of index units","No."),("The buyer's choice","No.")),
  ("Buying a put option expresses a view that is:","Bearish","A long put gains when the price falls.",
   ("Bullish","That's a long call."),("Neutral","That's selling options."),("Volatility-neutral","Long options gain from higher volatility.")),
  ("Selling a put option expresses a view that is:","Neutral to bullish","The writer keeps the premium if the price stays above K.",
   ("Strongly bearish","A falling price hurts the put writer."),("Bearish with limited risk","Put writer risk is large."),("Neutral to bearish","A fall hurts the put writer.")),
  ("An option buyer exercises the option when it is:","In-the-money","Exercise only makes sense when it gives a positive payoff.",
   ("Out-of-the-money","Exercise would lose money."),("At-the-money only","Payoff is zero at ATM."),("Never","ITM options are exercised.")),
]:
    Q(C,"S",q,r,w,a,b,c)

for K, P, ST, lot in [(25000, 180, 25400, None), (1200, 45, 1180, None), (500, 18, 530, None)]:
    pay = max(0, ST-K); pr = pay - P
    Q(C,"S",f"You buy a call with strike {num(K,0)} at a premium of {P}. On expiry the spot is {num(ST,0)}. What is your profit or loss per unit?",
      f"{pr:+,.0f}",
      f"Payoff = max(0, {num(ST,0)} − {num(K,0)}) = {pay}. Profit = payoff − premium = {pr:+,.0f}.",
      (f"{pay:+,.0f}" if pay != 0 else f"{-P-(K-ST):+,.0f}","That's the payoff before premium." if pay != 0 else "A call buyer's loss is capped at the premium; the option just lapses."),
      (f"{pay+P:+,.0f}","You added the premium. It's a cost — subtract it.") if pay else ("0","The option lapses, but the premium you paid is lost."),
      (f"{-pr:+,.0f}","Sign reversed."))
for K, P, ST in [(1000, 30, 940), (24000, 150, 24100)]:
    pay = max(0, K-ST); pr = pay - P
    Q(C,"S",f"You buy a put with strike {num(K,0)} at a premium of {P}. On expiry the spot is {num(ST,0)}. What is your profit or loss per unit?",
      f"{pr:+,.0f}",
      f"Payoff = max(0, {num(K,0)} − {num(ST,0)}) = {pay}. Profit = {pay} − {P} = {pr:+,.0f}.",
      (f"{pay:+,.0f}" if pay else f"{-(ST-K)-P:+,.0f}","That's the payoff before premium." if pay else "A put buyer's loss is capped at the premium."),
      (f"{pay+P:+,.0f}","Premium is a cost. Subtract it.") if pay else ("0","The put lapses, but the premium you paid is lost."),
      (f"{-pr:+,.0f}","Sign reversed."))
for S, K, prem, typ in [(520, 500, 32, "call"), (520, 500, 6, "put")]:
    iv = max(0, S-K) if typ=="call" else max(0, K-S); tv = prem - iv
    Q(C,"S",f"Spot is ₹{S}. A {typ} with strike ₹{K} trades at ₹{prem}. What are its intrinsic value and time value?",
      f"IV ₹{iv}, TV ₹{tv}",
      f"IV = {'max(0, S − K)' if typ=='call' else 'max(0, K − S)'} = {iv}. TV = premium − IV = {prem} − {iv} = {tv}.",
      (f"IV ₹{abs(S-K)}, TV ₹{prem-abs(S-K)}" if typ=="put" else f"IV ₹{prem}, TV ₹0","For a put, IV = K − S; here that's negative, so IV = 0." if typ=="put" else "Premium isn't all intrinsic value; some is time value."),
      (f"IV ₹{tv}, TV ₹{iv}","You swapped the two."),
      (f"IV ₹{prem}, TV ₹{abs(S-K)}","IV comes from S and K, not the premium."))
for K, P, typ in [(24000, 150, "put"), (1200, 45, "call")]:
    be = K-P if typ=="put" else K+P
    Q(C,"S",f"What is the breakeven price at expiry for the buyer of a {typ} with strike {num(K,0)} bought at a premium of {P}?",
      f"{num(be,0)}",
      f"{'Put' if typ=='put' else 'Call'} breakeven = K {'−' if typ=='put' else '+'} premium = {num(be,0)}.",
      (f"{num(K+P if typ=='put' else K-P,0)}","Wrong sign. Calls: K + P. Puts: K − P."),
      (f"{num(K,0)}","At the strike the option is worth zero; the premium is lost."),
      (f"{num(K+2*P if typ=='call' else K-2*P,0)}","Premium counts once."))

# Ch16 harder
for K, P, ST, lot in [(1500, 40, 1620, 400), (24500, 210, 24900, 75)]:
    loss = (ST-K-P)*lot
    Q(C,"H",f"You SELL a call (strike {num(K,0)}) at a premium of {P}, lot size {lot}. On expiry the spot is {num(ST,0)}. What is your profit or loss on one lot?",
      f"Loss of {inr(loss)}",
      f"Writer pays max(0, S − K) = {ST-K} and keeps {P}. Net per unit = −{ST-K-P}. × {lot} = −{inr(loss)}.",
      (f"Gain of {inr(P*lot)}","You assumed the option lapses. It's ITM, so the writer pays out."),
      (f"Loss of {inr((ST-K)*lot)}","You forgot the premium received."),
      (f"Loss of {inr((ST-K+P)*lot)}","The premium was received, so it reduces the loss."))
Q(C,"H","You sell a put (strike 1,000) for ₹25. On expiry the stock is at ₹1,060. Your result per share?",
  "Profit of ₹25","The put expires OTM (S > K), so it lapses and you keep the premium.",
  ("Profit of ₹60","The writer's profit is capped at the premium."),
  ("Loss of ₹35","The put is OTM; no payout."),
  ("Profit of ₹85","The premium is the only income."))
for d, mv, typ in [(0.6, 10, "call"), (-0.4, 15, "put")]:
    ch = d*mv
    Q(C,"H",f"A {typ} option has a delta of {d}. The spot rises by ₹{mv}. Roughly how does the premium change?",
      f"{'Rises' if ch>0 else 'Falls'} by ₹{abs(ch):.0f}",
      f"Change ≈ delta × spot change = {d} × {mv} = {ch:+.0f}.",
      (f"{'Falls' if ch>0 else 'Rises'} by ₹{abs(ch):.0f}","Sign reversed. Call delta is positive; put delta negative."),
      (f"{'Rises' if ch>0 else 'Falls'} by ₹{mv}","That assumes delta = 1."),
      (f"{'Rises' if ch>0 else 'Falls'} by ₹{abs(mv/d):.0f}","You divided by delta. Multiply."))
Q(C,"H","You hold 10 lots of Nifty calls (lot 75), each with delta 0.5. How many lots of Nifty futures should you sell to be delta-neutral?",
  "5 lots","Delta exposure = 10 × 75 × 0.5 = 375 units = 5 lots. Futures delta = 1.",
  ("10 lots","That assumes delta = 1."),
  ("20 lots","You divided by delta."),
  ("Buy 5 lots","Long calls have positive delta; you need to sell futures."))
for C_, S_, PVK in [(50, 1000, 980), (120, 2400, 2350)]:
    P_ = C_ + PVK - S_
    Q(C,"H",f"European options, same strike and expiry. Call = ₹{C_}, spot = ₹{S_}, present value of strike = ₹{PVK}. By put-call parity, what is the put price?",
      f"₹{P_}",
      f"C + PV(K) = P + S → P = C + PV(K) − S = {C_} + {PVK} − {S_} = {P_}.",
      (f"₹{C_ - PVK + S_}","Wrong rearrangement. P = C + PV(K) − S."),
      (f"₹{C_}","Put and call are equal only when S = PV(K)."),
      (f"₹{S_ - PVK}","You left out the call price."))
Q(C,"H","An option has theta of −5 per day. Other things equal, roughly how much value does it lose over 4 days?",
  "About ₹20","Theta × days = −5 × 4 = −20.",
  ("About ₹5","That's one day."),
  ("About ₹1.25","You divided by days."),
  ("It gains ₹20","Negative theta means a loss in value."))
Q(C,"H","An option has vega of 8 (per 1% volatility). Implied volatility rises from 14% to 17%. Roughly how does the premium change?",
  "Rises by about ₹24","Vega × change in vol = 8 × 3 = 24.",
  ("Falls by ₹24","Higher volatility raises premium."),
  ("Rises by ₹8","That's for a 1% change."),
  ("Rises by ₹136","You multiplied by the full 17%."))
Q(C,"H","A call has delta 0.50 and gamma 0.02. The spot rises by ₹10. What is the new delta (approximately)?",
  "0.70","New delta ≈ 0.50 + gamma × change = 0.50 + 0.02 × 10 = 0.70.",
  ("0.52","You added gamma only once, not × 10."),
  ("0.30","Rising spot increases a call's delta."),
  ("0.50","Gamma changes delta."))
for q, r, w, a, b, c in [
  ("Which option has the highest time value, other things equal?","An at-the-money option","Uncertainty of finishing ITM is greatest at the strike.",
   ("A deep in-the-money option","Mostly intrinsic value."),("A deep out-of-the-money option","Small chance of value; small time value."),("An expired option","Time value is zero at expiry.")),
  ("A deep in-the-money call option behaves most like:","A long futures position (delta near 1)","Its value moves almost one-for-one with spot.",
   ("A short put","A short put has positive delta but different payoff."),("A long put","Opposite direction."),("Cash","It still moves with the spot.")),
  ("Near expiry, what happens to the premium of an out-of-the-money option?","It decays quickly towards zero","Time value collapses fastest near expiry; OTM options have only time value.",
   ("It rises steadily","Theta works against it."),("It stays constant","Theta reduces it."),("It becomes equal to strike","No.")),
  ("A large dividend is expected before expiry. Effect on option premiums?","Call premium falls, put premium rises","The share price drops by the dividend on ex-date, which hurts calls and helps puts.",
   ("Call rises, put falls","Opposite."),("Both rise","Dividends hurt calls."),("No effect","Dividends lower the expected price.")),
  ("Interest rates rise (other things equal). Effect on option premiums?","Call premium rises, put premium falls","Higher rates cut the present value of the strike paid later — good for calls, bad for puts.",
   ("Call falls, put rises","Opposite."),("Both rise","Puts fall."),("Both fall","Calls rise.")),
  ("Spot is ₹1,050. A put has a strike of ₹1,100. This put is:","In-the-money by ₹50","Put is ITM when S < K: 1,100 − 1,050 = 50.",
   ("Out-of-the-money by ₹50","For a put, S < K is ITM."),("At-the-money","S ≠ K."),("Worthless","It has ₹50 intrinsic value.")),
  ("Long stock + long put (same quantity) has a payoff shape like:","A long call","Downside is floored at the strike; upside open. That is a call's shape.",
   ("A short call","Short call has capped upside, unlimited downside."),("A long put","Long put gains from falls only."),("A short put","Short put has unlimited downside.")),
  ("Long call + short put, same strike and expiry, is equal to:","A long futures position (synthetic long)","From put-call parity: C − P = S − PV(K). Payoff is linear like futures.",
   ("A short futures position","That's short call + long put."),("A straddle","A straddle is long call + long put."),("Cash","It moves with the market.")),
  ("Why must option sellers pay margin while buyers don't?","Sellers face large or unlimited losses; buyers' loss is capped at the premium already paid","The clearing corporation needs cover for the seller's open-ended risk.",
   ("Sellers earn more money","Income isn't the reason."),("Buyers are always retail","Buyer type doesn't matter."),("SEBI taxes sellers","Margin isn't a tax.")),
  ("You hold a long call on a stock that finishes ITM at expiry. Under physical settlement you:","Pay the strike price and receive the shares","Long call → right to buy at K.",
   ("Receive the strike price and deliver shares","That's a short call."),("Receive cash only","Stock options are physically settled."),("Lose the premium and nothing else","ITM options are exercised.")),
  ("Which Greek is the same for a call and a put with the same strike and expiry?","Gamma","Call and put deltas differ by 1 (from parity), so their rate of change (gamma) is the same. Vega is also the same.",
   ("Delta","Call delta is positive, put delta negative."),("Rho","Call rho positive, put rho negative."),("Intrinsic value","Depends on S vs K.")),
  ("Implied volatility rises before company results. What happens to option premiums?","Both call and put premiums rise","Higher implied volatility raises all option prices.",
   ("Only calls rise","Puts also rise."),("Both fall","Opposite."),("Only puts rise","Calls also rise.")),
  ("Compare an American and a European option with the same terms:","The American option is worth at least as much","It has every right the European has, plus early exercise.",
   ("The European is always worth more","Fewer rights can't be worth more."),("They are always equal","They can differ (e.g. puts, dividends)."),("The American is always worth double","No.")),
]:
    Q(C,"H",q,r,w,a,b,c)
Q(C,"H","You bought a call (strike ₹500) for ₹20. On expiry the stock is at ₹510. What should you do, and what is your result per share?",
  "Exercise; net loss of ₹10","Exercise recovers ₹10 of the ₹20 premium. Not exercising loses all ₹20.",
  ("Let it lapse; loss of ₹20","Exercising gives ₹10 back. Always exercise if ITM, even below breakeven."),
  ("Exercise; profit of ₹10","Payoff is ₹10, but you paid ₹20."),
  ("Exercise; profit of ₹30","Premium is a cost."))

# =====================================================================
# CH 20  EXCHANGE TRADED INTEREST RATE FUTURES (+ bond basics it needs)
# =====================================================================
C = 20
for q, r, w, a, b, c in [
  ("Bond prices and yields move:","In opposite directions","Higher yield = future cash flows discounted more = lower price.",
   ("In the same direction","Opposite."),("Independently","They are mathematically linked."),("Only when RBI changes repo","They move every day in the market.")),
  ("A bank holding G-secs fears interest rates will rise. Which IRF trade hedges the risk?","Sell interest rate futures","Rates up → bond and futures prices fall → short futures gain.",
   ("Buy interest rate futures","That adds to the loss if rates rise."),("Buy more G-secs","More exposure."),("Do nothing","That leaves the risk open.")),
  ("An insurer will invest in bonds in 2 months and fears rates will fall. Which IRF trade hedges this?","Buy interest rate futures","Rates fall → bond prices rise → long futures gain, offsetting the higher purchase price.",
   ("Sell interest rate futures","That gains if rates rise — not the risk here."),("Sell bonds now","It has no bonds yet."),("Buy equity index futures","Wrong underlying.")),
  ("The underlying for bond futures traded on Indian exchanges is:","Government of India securities","Bond futures in India are on GOI securities.",
   ("Corporate bonds","Not the underlying for exchange IRF."),("Equity shares","No."),("Bank fixed deposits","No.")),
  ("The underlying for T-bill futures in India is:","The 91-day Treasury bill","Exchange T-bill futures are on the 91-day T-bill.",
   ("The 10-year G-sec","That's for bond futures."),("Commercial paper","No."),("Call money","No.")),
  ("T-bill futures are quoted as:","100 minus the annualised discount yield","Quote = 100 − yield. Yield up → quote down, like a price.",
   ("The yield itself","Quoting as 100 − yield makes the quote move like a price."),("100 plus the yield","Wrong sign."),("Face value of the T-bill","No.")),
  ("'Cheapest to deliver' (CTD) means:","The bond in the deliverable basket that costs the short least to deliver","The short chooses the bond; it picks the cheapest one.",
   ("The bond with the lowest coupon always","Coupon alone doesn't decide; price and conversion factor do."),("The bond the buyer prefers","The short chooses."),("The cheapest T-bill","CTD applies to bond futures.")),
  ("Why do physically settled bond futures use a conversion factor?","To make different deliverable bonds comparable with the notional bond","Each bond in the basket has a different coupon and maturity; CF adjusts for that.",
   ("To convert rupees into dollars","No."),("To calculate margin","Margin is separate."),("To convert yield into duration","No.")),
  ("A deliverable bond has a coupon higher than the notional coupon. Its conversion factor is:","Greater than 1","Higher coupon = worth more than the notional bond at the notional yield.",
   ("Less than 1","That's for coupon below notional."),("Exactly 1","Only if coupon equals notional."),("Zero","No.")),
  ("Invoice price paid by the long when a bond is delivered equals:","Futures settlement price × conversion factor + accrued interest","The long pays the futures price adjusted for the bond, plus interest accrued.",
   ("Futures price only","Ignores CF and accrued interest."),("Bond's market price","Delivery is at the futures-based invoice."),("Futures price − accrued interest","Accrued interest is added.")),
  ("In a physically settled bond futures contract, the choice of which bond to deliver belongs to:","The seller (short)","The delivery option is with the short.",
   ("The buyer (long)","The long accepts what's delivered."),("The exchange","The exchange sets the basket only."),("RBI","No.")),
  ("If interest rates rise, a short position in interest rate futures will:","Gain","Rates up → futures price down → short gains.",
   ("Lose","That's a long position."),("Not change","IRF prices react to rates."),("Be cancelled","No.")),
  ("A long position in bond futures profits when:","Interest rates fall","Rates down → bond prices up → long gains.",
   ("Interest rates rise","That hurts the long."),("Equity markets rise","Wrong underlying."),("Inflation rises","Higher inflation usually lifts yields — bad for longs.")),
  ("PVBP (or DV01) measures:","The change in price for a 1 basis point change in yield","PVBP = price value of a basis point (0.01%).",
   ("The bond's coupon","No."),("Accrued interest","No."),("Credit rating","No.")),
  ("Modified duration tells you:","The approximate % change in price for a 1% change in yield","%ΔP ≈ −MD × Δy.",
   ("The bond's maturity in years","That's maturity, not modified duration."),("The coupon rate","No."),("The time to next coupon","No.")),
  ("Who can trade exchange-traded interest rate futures in India?","All of these: banks, primary dealers, mutual funds, FPIs and retail investors","IRF is open to a wide range of participants.",
   ("Only banks","Too narrow."),("Only RBI","RBI regulates; it doesn't trade for profit."),("Only foreign investors","Too narrow.")),
  ("A debt mutual fund mainly uses IRF to:","Manage portfolio duration and hedge interest rate risk","Selling IRF cuts duration; buying adds duration — without selling bonds.",
   ("Increase equity exposure","IRF is a rate product."),("Pay dividends","No."),("Avoid NAV calculation","No.")),
  ("Compared with OTC interest rate swaps, exchange-traded IRF are:","Standardised and guaranteed by a clearing corporation","Exchange products: standard terms, MTM, central counterparty.",
   ("Customised to each client","That's OTC."),("Free of margins","Margins apply."),("Unregulated","Regulated by RBI and SEBI.")),
  ("Gross basis in bond futures is:","Cash bond price − (futures price × conversion factor)","This measures how expensive a bond is to deliver. The CTD has the lowest net cost.",
   ("Futures price − spot price","For bond futures, the CF adjustment is needed."),("Coupon − yield","No."),("Accrued interest × CF","No.")),
  ("Other things equal, a bond with a longer duration:","Changes more in price for a given yield change","Duration = price sensitivity.",
   ("Changes less in price","Opposite."),("Never changes in price","No."),("Has no interest rate risk","It has more.")),
  ("Exchange-traded interest rate derivatives in India are regulated by:","RBI and SEBI jointly","RBI sets the rules for interest rate products; SEBI regulates the exchange.",
   ("Only SEBI","RBI also has a role."),("Only RBI","SEBI regulates exchanges."),("IRDAI","Insurance regulator.")),
  ("Which is a key advantage of hedging a bond portfolio with IRF instead of selling bonds?","Lower cost and speed; the bonds are kept","Futures are liquid and cheap to trade; the fund keeps its holdings.",
   ("It removes all risk","Basis risk remains."),("No margin is needed","Margin is needed."),("It increases yield","Hedging doesn't raise yield.")),
]:
    Q(C,"S",q,r,w,a,b,c)
for y in [6.40, 7.15]:
    Q(C,"S",f"The 91-day T-bill futures implies an annualised yield of {y:.2f}%. What is its quoted price?",
      f"{100-y:.2f}",
      f"Quote = 100 − yield = 100 − {y:.2f} = {100-y:.2f}.",
      (f"{100+y:.2f}","Wrong sign. Subtract the yield."),
      (f"{y:.2f}","The quote isn't the yield itself."),
      (f"{100-y/4:.2f}","Don't de-annualise the yield in the quote."))
for md, dy in [(6, 0.25), (4.5, -0.40)]:
    ch = -md*dy
    Q(C,"S",f"A bond has a modified duration of {md}. Yields {'rise' if dy>0 else 'fall'} by {abs(dy):.2f}%. What is the approximate change in price?",
      f"{ch:+.2f}%",
      f"%ΔP ≈ −MD × Δy = −{md} × ({dy:+.2f}) = {ch:+.2f}%.",
      (f"{-ch:+.2f}%","Sign reversed. Price moves opposite to yield."),
      (f"{-dy:+.2f}%","You ignored duration."),
      (f"{ch*100:+.2f}%","Units: Δy is already in %, don't multiply by 100."))
Q(C,"S","A bond position has face value ₹1 crore, price 100 and modified duration 8. What is its PVBP?",
  "₹8,000","PVBP = MD × value × 0.0001 = 8 × 1,00,00,000 × 0.0001 = ₹8,000.",
  ("₹80,000","That's 10 bps, not 1 bp."),
  ("₹800","Off by a factor of 10."),
  ("₹8,00,000","That's 1%, i.e. 100 bps."))
for n, p0, p1, side in [(50, 99.80, 99.20, "sold"), (30, 101.25, 101.70, "bought")]:
    per = (p0-p1 if side=="sold" else p1-p0)/100*2e5; tot = per*n
    Q(C,"S",f"A trader {side} {n} bond futures contracts at {p0:.2f} and closed them at {p1:.2f}. Contract size is ₹2 lakh face value. What is the profit or loss?",
      f"{'Profit' if tot>0 else 'Loss'} of {inr(abs(tot))}",
      f"Per contract: {abs(p1-p0):.2f}% of ₹2,00,000 = {inr(abs(per))}. × {n} = {inr(abs(tot))}. {'Short gains as price falls.' if side=='sold' else 'Long gains as price rises.'}",
      (f"{'Loss' if tot>0 else 'Profit'} of {inr(abs(tot))}","Direction reversed."),
      (f"{'Profit' if tot>0 else 'Loss'} of {inr(abs(per))}","That's one contract."),
      (f"{'Profit' if tot>0 else 'Loss'} of {inr(abs(p1-p0)*n)}","You didn't scale by contract size."))

# Ch20 harder
for V, mdp, F, mdf in [(100e7, 5, 100, 7), (50e7, 6, 98, 7.5)]:
    cv = F/100*2e5; n = mdp*V/(mdf*cv)
    Q(C,"H",f"A {inr(V)} bond portfolio has modified duration {mdp}. Bond futures trade at {F} (contract ₹2 lakh face), futures duration {mdf}. How many contracts hedge the portfolio fully?",
      f"Sell about {n:,.0f}",
      f"Contract value = {F}% × 2,00,000 = {inr(cv)}. N = (MDp × Vp) ÷ (MDf × Vf) = ({mdp} × {inr(V)}) ÷ ({mdf} × {inr(cv)}) ≈ {n:,.0f}. Sell to hedge.",
      (f"Buy about {n:,.0f}","Direction reversed. A long bond holder sells futures."),
      (f"Sell about {V/cv:,.0f}","You ignored the duration ratio."),
      (f"Sell about {mdf*V/(mdp*cv):,.0f}","You flipped the duration ratio."))
for pp, pf in [(400000, 160), (250000, 125)]:
    n = pp/pf
    Q(C,"H",f"A portfolio's PVBP is {inr(pp)}. One bond futures contract has a PVBP of ₹{pf}. How many contracts hedge the portfolio?",
      f"Sell {n:,.0f}",
      f"N = PVBP portfolio ÷ PVBP futures = {inr(pp)} ÷ {pf} = {n:,.0f}. Sell to hedge a long bond position.",
      (f"Buy {n:,.0f}","Direction reversed."),
      (f"Sell {n/100:,.0f}","Off by 100."),
      (f"Sell {n*10:,.0f}","Off by 10."))
for V, md0, md1, mdf in [(200e7, 4, 6, 8), (80e7, 7, 5, 6.4)]:
    cv = 2e5; n = (md1-md0)*V/(mdf*cv)
    Q(C,"H",f"A {inr(V)} debt fund has modified duration {md0} and wants {md1}. Futures: duration {mdf}, contract value ₹2 lakh. What should the fund do?",
      f"{'Buy' if n>0 else 'Sell'} {abs(n):,.0f} contracts",
      f"N = (target − current) × V ÷ (MDf × Vf) = ({md1} − {md0}) × {inr(V)} ÷ ({mdf} × 2,00,000) = {n:+,.0f}. Positive = buy (adds duration).",
      (f"{'Sell' if n>0 else 'Buy'} {abs(n):,.0f} contracts","Wrong direction. Buying futures adds duration; selling cuts it."),
      (f"{'Buy' if n>0 else 'Sell'} {md1*V/(mdf*cv):,.0f} contracts","You used the target duration, not the change."),
      (f"{'Buy' if n>0 else 'Sell'} {abs(md1-md0)*V/cv:,.0f} contracts","You ignored the futures duration."))
for F, cf, ai in [(98.50, 1.0320, 1.20), (101.10, 0.9650, 0.85)]:
    inv = F*cf + ai
    Q(C,"H",f"Futures settlement price {F:.2f}, conversion factor {cf:.4f}, accrued interest {ai:.2f}. What invoice price does the long pay (per ₹100 face)?",
      f"{inv:.3f}",
      f"Invoice = F × CF + AI = {F:.2f} × {cf:.4f} + {ai:.2f} = {inv:.3f}.",
      (f"{F*cf:.3f}","You forgot accrued interest."),
      (f"{F+ai:.3f}","You forgot the conversion factor."),
      (f"{F*cf-ai:.3f}","Accrued interest is added, not subtracted."))
Q(C,"H","Futures price 99.00. Bond A: price 104.00, CF 1.0500. Bond B: price 99.00, CF 0.9950. Which is cheapest to deliver?",
  "Bond A (cost 0.05)","Delivery cost = price − F × CF. A: 104.00 − 103.95 = 0.05. B: 99.00 − 98.505 = 0.495. Lowest = A.",
  ("Bond B, because its price is lower","Price alone is misleading; adjust by CF."),
  ("Bond B (cost 0.05)","Recheck: B's cost is 0.495."),
  ("Both equal","They differ."))
for q, r, w, a, b, c in [
  ("The CTD bond is the one with:","The highest implied repo rate","Buying the CTD and delivering it into futures gives the best return.",
   ("The lowest implied repo rate","That's the most expensive to deliver."),("The longest maturity always","Not always."),("The highest coupon always","Not always.")),
  ("A trader expects the yield curve to steepen (long yields rise more than short yields). Using futures, the trader should:","Buy short-tenor futures and sell long-tenor futures","Long yields up → long-tenor futures fall (short gains). Short tenor relatively firmer.",
   ("Sell short-tenor and buy long-tenor futures","That's a flattening trade."),("Buy both","Directional, not a curve trade."),("Sell both","Directional, not a curve trade.")),
  ("A trader expects the yield curve to flatten. The futures trade is:","Sell short-tenor futures and buy long-tenor futures","Flattening: short yields up relative to long yields.",
   ("Buy short-tenor, sell long-tenor","That's a steepener."),("Buy T-bill futures only","Single leg is directional."),("Sell equity futures","Wrong market.")),
  ("When does cash-and-carry arbitrage in bond futures make sense?","When the implied repo rate is higher than the actual repo (borrowing) rate","Buy the bond with borrowed money, sell futures, deliver: earn implied repo, pay actual repo.",
   ("When implied repo is below actual repo","Then reverse cash-and-carry is better."),("When yields are falling","Direction doesn't matter for arbitrage."),("Never","It's a standard trade.")),
  ("A treasurer expects short-term rates to rise. Which T-bill futures trade fits?","Sell T-bill futures","Quote = 100 − yield. Yield up → quote down → short gains.",
   ("Buy T-bill futures","That gains if rates fall."),("Buy long-dated bonds","More rate risk."),("Do nothing","Leaves the view unused.")),
  ("For the same size of yield change, a plain bond's price rises more than it falls. This is due to:","Positive convexity","Duration gives a straight-line estimate; convexity adds the curve.",
   ("Negative duration","Duration is positive."),("Credit risk","Unrelated."),("Accrued interest","Unrelated.")),
  ("A bond hedge with IRF is not perfect mainly because of:","Basis risk between the portfolio's bonds and the futures underlying","Different bonds don't move exactly together.",
   ("Daily MTM","MTM doesn't make a hedge imperfect."),("High liquidity","Liquidity helps hedging."),("Clearing corporation guarantee","That removes counterparty risk.")),
  ("A fund manager wants to cut duration quickly without selling bonds. The best tool is to:","Sell interest rate futures","Short futures carry negative duration, lowering portfolio duration.",
   ("Buy interest rate futures","That adds duration."),("Buy long-dated G-secs","Adds duration."),("Buy equity futures","Wrong market.")),
  ("Duration estimates of price change are least accurate for:","Large yield changes","Convexity makes the price curve bend; the straight-line estimate drifts.",
   ("Small yield changes","Duration works well for small moves."),("Zero-coupon bonds only","Accuracy issue is about size of move."),("Short-dated T-bills","They have low convexity.")),
  ("Interest rate options on bonds: a CALL option gains when:","Interest rates fall (bond prices rise)","Option on a bond price: call gains when price rises, i.e. when rates fall.",
   ("Interest rates rise","That's when a put on bond price gains."),("Equity markets rise","Wrong market."),("Inflation rises","Usually lifts yields — bad for calls on bonds.")),
  ("A bank has a fixed-rate bond portfolio funded by floating-rate deposits. Rates are expected to rise. Which combination hedges?","Sell IRF or pay fixed in an IRS","Both gain when rates rise.",
   ("Buy IRF or receive fixed in an IRS","Both gain when rates fall."),("Buy more fixed-rate bonds","More exposure."),("Buy a cap on deposits only","Not the standard answer here; and it's one-sided.")),
]:
    Q(C,"H",q,r,w,a,b,c)
for md, dy, P in [(7.2, 0.50, 102), (5.5, -0.30, 98.5)]:
    ch = -md*dy/100*P
    Q(C,"H",f"A bond priced at {P} has modified duration {md}. Yield {'rises' if dy>0 else 'falls'} by {abs(dy)*100:.0f} bps. What is the approximate new price?",
      f"{P+ch:.2f}",
      f"ΔP ≈ −MD × Δy × P = −{md} × {dy/100:+.4f} × {P} = {ch:+.2f}. New price = {P+ch:.2f}.",
      (f"{P-ch:.2f}","Direction reversed. Yield up → price down."),
      (f"{P+ch*100:.2f}","Units error: 50 bps = 0.005, not 0.5."),
      (f"{P-md*dy:.2f}","You treated the % change as a rupee change; multiply by price."))

# =====================================================================
# BUILD
# =====================================================================
build(BANK, [15, 16, 13, 20],
      {15: "Forwards & Futures", 16: "Options", 13: "Basics of Derivatives", 20: "Exchange Traded IR Futures"},
      {15: 15, 16: 13, 13: 10, 20: 10},
      title="NISM V-D Practice Quiz", eyebrow="NISM-Series-V-D · derivatives practice simulation",
      sub="Top 4 derivatives chapters by marks. 5 questions for every expected exam question: 3 at exam level, 2 harder. Instant answer and reason after each click. Skip any question and come back to it later. Your time is recorded.",
      storage_key="nismvd-attempts-v1", out_name="quiz.html")
