# Frequent flyer program database: parameters

This file lists the columns for the frequent flyer program (FFP) database. Each row in the database is one program, for example Air India Maharaja Club, British Airways Club or Air Canada Aeroplan.

There are 142 columns in 13 groups. For each column, the table gives the column name, what it records and the type of value.

Value types:

- `text`: free text
- `list`: values separated by semicolons
- `yes/no`: yes, no or partial
- `number`: a number with the unit in the column name
- `enum`: one value from a fixed set (the set is in the description)
- `rating 1-10`: our score, 10 is best

## A. Program identity (12)

| # | Column | What it records | Type |
|---|---|---|---|
| 1 | program_name | Name of the program | text |
| 2 | currency_name | Name of the points (Avios, miles, points) | text |
| 3 | owner_airline | Airline or group that runs the program | text |
| 4 | other_airlines_using_currency | Other airlines that use the same currency (for example Avios at BA, Iberia, Qatar, Aer Lingus, Finnair) | list |
| 5 | alliance | Star Alliance, oneworld, SkyTeam or none | enum |
| 6 | home_country | Country of the owner airline | text |
| 7 | main_hubs | Hub airports | list |
| 8 | join_fee_and_age | Fee to join and minimum age | text |
| 9 | membership_open_to | Who can join (any country, residents only) | text |
| 10 | points_value_cents | Our estimate of the value of 1 point, in US cents | number |
| 11 | website_and_app_quality | How easy the website and app are to use | rating 1-10 |
| 12 | program_source_url | Official program page used for the data | text |

## B. Points expiry and account rules (7)

| # | Column | What it records | Type |
|---|---|---|---|
| 13 | expiry_policy | Fixed term, activity based or no expiry | enum |
| 14 | expiry_months | Months until points expire | number |
| 15 | how_to_keep_points_alive | Activities that reset the expiry date | text |
| 16 | expired_points_reinstatement | Can you get expired points back, and the fee | text |
| 17 | family_pooling | Can a household pool points in one account | yes/no |
| 18 | family_pooling_rules | Number of members, relation rules, fees | text |
| 19 | points_transfer_to_other_member | Can you move points to another member, and the fee and limit | text |

## C. Earning on flights (14)

| # | Column | What it records | Type |
|---|---|---|---|
| 20 | earn_model | Distance based, revenue based or fare class based | enum |
| 21 | earn_rate_own_flights | Points per USD (or % of distance) on own flights | text |
| 22 | earn_by_cabin_and_fare_class | Earn rate for each cabin and fare class | text |
| 23 | basic_economy_earns | Do the lowest fares earn points | yes/no |
| 24 | minimum_points_per_flight | Minimum points for a short flight | number |
| 25 | earn_on_partner_airlines | How points are earned on partner flights | text |
| 26 | best_partner_to_credit | Partner flights that earn the most | text |
| 27 | earn_on_award_tickets | Do award tickets earn points or status | yes/no |
| 28 | elite_bonus_earn | Extra % earned by each status tier | text |
| 29 | retro_credit_window_days | Days after the flight to claim missing points | number |
| 30 | points_posting_time_days | Days for points to post after the flight | number |
| 31 | status_credits_earned_on_partners | Do partner flights count towards status | yes/no |
| 32 | earn_on_paid_upgrades_and_ancillaries | Do paid seats, upgrades or bags earn points | yes/no |
| 33 | promo_frequency_flights | How often the program runs bonus earn offers | text |

## D. Earning off flights (16)

| # | Column | What it records | Type |
|---|---|---|---|
| 34 | cobrand_credit_cards | Co-branded credit cards and their countries | list |
| 35 | cobrand_card_earn_rate | Points per unit of spend on the best co-brand card | text |
| 36 | cobrand_card_key_perks | Welcome bonus, companion ticket, lounge visits | text |
| 37 | bank_transfer_partners | Bank programs that transfer in (Amex MR, Chase UR, Citi, Capital One, Bilt, HDFC, Axis and others) | list |
| 38 | bank_transfer_ratios | Ratio for each bank partner | text |
| 39 | bank_transfer_time | Time for a bank transfer to arrive (instant, hours, days) | text |
| 40 | transfer_bonus_frequency | How often banks offer transfer bonuses | text |
| 41 | hotel_transfer_partners_in | Hotel programs that transfer in, with ratio (for example Marriott Bonvoy 3:1) | list |
| 42 | hotel_stay_earn | Points earned for hotel stays at partners | text |
| 43 | car_rental_earn | Car rental partners and earn rates | text |
| 44 | shopping_portal | Name and link of the online shopping portal (for example Avios eStore, AAdvantage eShopping) | text |
| 45 | dining_program | Dining rewards program | text |
| 46 | other_earn_partners | Other partners (fuel, telecom, retail, surveys) | list |
| 47 | buy_points_price | Normal price to buy points, cents per point | number |
| 48 | buy_points_sale_price | Usual sale price, cents per point, and how often | text |
| 49 | buy_points_annual_limit | Maximum points you can buy in one year | number |

## E. Elite status (16)

| # | Column | What it records | Type |
|---|---|---|---|
| 50 | tier_names | Names of the status tiers, lowest to highest | list |
| 51 | qualification_metric | What counts: miles, segments, status credits, spend, points | text |
| 52 | qualification_thresholds | Threshold for each tier | text |
| 53 | qualification_period | Calendar year, membership year or rolling | enum |
| 54 | alliance_tier_mapping | Alliance status for each tier (for example Star Gold, oneworld Emerald) | text |
| 55 | lounge_access_by_tier | Lounge access for each tier, and guests | text |
| 56 | extra_baggage_by_tier | Extra baggage for each tier | text |
| 57 | priority_services_by_tier | Priority check-in, security, boarding | text |
| 58 | complimentary_upgrades | Free upgrades and who gets them | text |
| 59 | free_seat_selection_by_tier | Free seat selection, including exit rows | text |
| 60 | fee_waivers_by_tier | Change, cancel or award fees waived for each tier | text |
| 61 | extra_award_space_for_elites | Do elites see more award seats | yes/no |
| 62 | tier_benefit_one_liners | One line summary of the benefits of each tier | text |
| 63 | status_match_or_challenge | Does the program offer a status match or challenge | text |
| 64 | lifetime_status | Lifetime status rules | text |
| 65 | soft_landing | Do you drop one tier only when you fail to requalify | yes/no |

## F. Award pricing (17)

| # | Column | What it records | Type |
|---|---|---|---|
| 66 | award_pricing_model_own_flights | Fixed chart, dynamic or hybrid for own flights | enum |
| 67 | award_pricing_model_partners | Fixed chart, dynamic or hybrid for partner flights | enum |
| 68 | award_chart_published | Is the award chart public | yes/no |
| 69 | award_chart_basis | Zone based, distance based or revenue based | enum |
| 70 | distance_bands | Distance bands, if the chart is distance based | text |
| 71 | peak_offpeak_pricing | Does the price change on peak dates, and the peak calendar | text |
| 72 | economy_price_range | Points for one-way economy (short, medium, long haul) | text |
| 73 | premium_economy_price_range | Points for one-way premium economy | text |
| 74 | business_price_range | Points for one-way business | text |
| 75 | first_price_range | Points for one-way first | text |
| 76 | one_way_awards_allowed | Can you book one-way awards at half the round-trip price | yes/no |
| 77 | round_trip_discount | Is a round trip cheaper than two one-ways | yes/no |
| 78 | mixed_cabin_pricing | How the price is set when cabins are mixed | text |
| 79 | cash_plus_points | Can you pay part cash and part points, and the value | text |
| 80 | minimum_points_to_redeem | Minimum points needed for any redemption | number |
| 81 | sweet_spots | Best value redemptions, with route, cabin and price | list |
| 82 | last_devaluation | Date and size of the last devaluation, and how much notice | text |

## G. Taxes, surcharges and fees on awards (10)

| # | Column | What it records | Type |
|---|---|---|---|
| 83 | surcharges_own_flights | Fuel or carrier surcharges on own flights, and typical amount | text |
| 84 | surcharges_partner_flights | Surcharges on partner flights, by partner | text |
| 85 | surcharge_free_partners | Partners with no surcharges | list |
| 86 | surcharge_varies_by_origin | Do surcharges change with the departure country (for example UK APD, Hong Kong) | text |
| 87 | sample_taxes_long_haul_business | Taxes and fees on a sample long haul business award | text |
| 88 | award_booking_fee | Fee to issue an award ticket | text |
| 89 | phone_booking_fee | Fee to book by phone | text |
| 90 | close_in_booking_fee | Fee for awards booked close to departure, and the cut off | text |
| 91 | partner_award_booking_fee | Extra fee for partner awards | text |
| 92 | taxes_payable_currencies | Currencies and cards accepted for taxes | text |

## H. Award availability and booking (14)

| # | Column | What it records | Type |
|---|---|---|---|
| 93 | booking_window_own_days | Days before departure that own award seats open (for example 355, 360) | number |
| 94 | booking_window_partner_days | Days before departure that partner seats can be booked | number |
| 95 | saver_space_own_flights | How easy it is to find saver seats on own flights | rating 1-10 |
| 96 | premium_cabin_release_to_partners | Does the airline release business and first seats to partners | text |
| 97 | partner_awards_online | Can you book partner awards online, and which partners | text |
| 98 | partners_phone_only | Partners you can book by phone only | list |
| 99 | award_hold | Can you hold an award, and for how many days | text |
| 100 | award_waitlist | Can you waitlist an award | yes/no |
| 101 | award_calendar_search | Does the website show a calendar of award prices | yes/no |
| 102 | third_party_search_tools | Tools that show this program's award space (seats.aero, ExpertFlyer, point.me) | list |
| 103 | upgrade_with_points | Can you upgrade a paid ticket with points, from which fares, and the cost | text |
| 104 | upgrade_on_partners | Can you upgrade on partner airlines with points | yes/no |
| 105 | seat_selection_on_awards | Is seat selection free on award tickets | text |
| 106 | baggage_on_awards | Baggage allowance on award tickets | text |

## I. Routing rules (10)

| # | Column | What it records | Type |
|---|---|---|---|
| 107 | stopover_one_way | Stopover allowed on a one-way award, and the cost | text |
| 108 | stopover_round_trip | Number of stopovers allowed on a round trip, and the cost | text |
| 109 | stopover_max_hours_layover | Maximum hours before a connection counts as a stopover | number |
| 110 | open_jaw_allowed | Is an open jaw allowed, and the rules | text |
| 111 | max_segments | Maximum flights in one award | number |
| 112 | max_permitted_mileage_rule | Rule on routing distance | text |
| 113 | mix_partners_on_one_award | Can you mix airlines on one award | yes/no |
| 114 | routing_restrictions | Other routing rules (backtracking, region transit, gateway) | text |
| 115 | married_segment_logic | Does the program price connecting flights as one unit | yes/no |
| 116 | multi_city_online_booking | Can you book multi city awards online | yes/no |

## J. Changes and cancellations (10)

| # | Column | What it records | Type |
|---|---|---|---|
| 117 | award_date_change_fee | Fee to change the date of an award | text |
| 118 | award_reissue_fee | Fee to change the route or the airline | text |
| 119 | award_cancel_redeposit_fee | Fee to cancel an award and get the points back | text |
| 120 | cancel_deadline | Last time before departure that you can cancel | text |
| 121 | no_show_penalty | What you lose if you do not fly | text |
| 122 | taxes_refund_on_cancel | Are taxes and surcharges refunded | yes/no |
| 123 | free_cancel_24_hours | Free cancel within 24 hours of booking | yes/no |
| 124 | schedule_change_rights | What you can do when the airline changes the schedule | text |
| 125 | paid_ticket_change_fee | Change fee on paid tickets | text |
| 126 | paid_ticket_cancel_fee | Cancel fee on paid tickets | text |

## K. Family and other passengers (7)

| # | Column | What it records | Type |
|---|---|---|---|
| 127 | book_awards_for_others | Can you book awards for anyone | yes/no |
| 128 | nominee_limit | Limit on named people, and the fee to change them | text |
| 129 | lap_infant_award_cost | Cost for a lap infant on an award (10% of fare, taxes only, points) | text |
| 130 | child_award_discount | Discount for children on awards | text |
| 131 | companion_voucher | Companion or 2-for-1 voucher, and how to get it | text |
| 132 | family_account | Is there a family account | yes/no |
| 133 | group_award_limit | Maximum passengers on one award booking | number |

## L. Other redemptions and partnerships (5)

| # | Column | What it records | Type |
|---|---|---|---|
| 134 | points_transfer_out | Can points move to other programs (hotels, other airlines), and the ratio | text |
| 135 | linked_programs | Programs you can link to (for example BA and Iberia Avios combine, hotel status links) | list |
| 136 | non_flight_redemptions | Hotels, cars, shopping, gift cards, lounge passes, charity | list |
| 137 | non_flight_redemption_value_cents | Value per point on non flight redemptions, in US cents | number |
| 138 | non_alliance_partners | Airline partners outside the alliance | list |

## M. Product and comfort ratings (our scores) (4)

These scores are for the airline that runs the program. Rate partners in a separate airline table.

| # | Column | What it records | Type |
|---|---|---|---|
| 139 | comfort_scores | One score each for economy seat, premium economy seat, business seat, first seat, food, entertainment, wifi, lounges | rating 1-10 each |
| 140 | operations_scores | One score each for on-time performance, network size, customer service | rating 1-10 each |
| 141 | overall_value_score | Our overall score for value of the points | rating 1-10 |
| 142 | data_last_checked | Date we last checked the data | date |

## Notes for the database build

Some columns hold several values, for example `comfort_scores` and the per tier columns. In the spreadsheet we can split them into one column for each value. For example, `comfort_scores` becomes 8 columns, and the total goes past 160. A database can also keep them in extra tables:

- `tiers` table: one row for each program and tier
- `transfer_partners` table: one row for each program and partner, with the ratio and time
- `sweet_spots` table: one row for each sweet spot, with route, cabin, price and taxes
- `airlines` table: comfort scores for each airline, so a partner score shows when you book on that partner

Award space itself (dates, seats, routes) changes every day. Keep it in a separate table that links to this one by `program_name`.
