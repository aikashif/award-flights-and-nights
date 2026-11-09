# Frequent flyer program database: parameters

This file lists the columns for the frequent flyer program (FFP) database. Each row in the database is one program. The data is in `data/ffp_database.xlsx`.

There are 146 columns in 15 groups. `scripts/build_ffp_db.py` makes this file and the Excel file, so change the columns there.

All money values are in INR (USD 1 = INR 88). Surcharge ranks use a five point scale: Very high / High / Medium / Low / Very low.

## A. Program identity (10)

| # | Column | What it records | Type |
|---|---|---|---|
| 1 | program_name | Name of the program | text |
| 2 | currency_name | Name of the points (Avios, miles, points) | text |
| 3 | owner_airline | Airline or group that runs the program | text |
| 4 | other_airlines_using_currency | Other airlines that use the same currency | list |
| 5 | alliance | Star Alliance, oneworld, SkyTeam or none | enum |
| 6 | home_country | Country of the owner airline | text |
| 7 | main_hubs | Hub airports | list |
| 8 | points_value_inr | Our estimate of the value of 1 point, in INR (USD 1 = INR 88) | number |
| 9 | website_and_app_quality | How easy the website and app are to use | rating 1-10 |
| 10 | program_source_url | Official program page used for the data | text |

## B. Points expiry and account rules (6)

| # | Column | What it records | Type |
|---|---|---|---|
| 11 | expiry_policy | Fixed term, activity based or no expiry | enum |
| 12 | expiry_months | Months until points expire | number |
| 13 | how_to_keep_points_alive | Activities that reset the expiry date | text |
| 14 | expired_points_reinstatement | Can you get expired points back, and the fee | text |
| 15 | family_pooling | Can a household pool points in one account | yes/no |
| 16 | family_pooling_rules | Number of members, relation rules, fees | text |

## C. Earning on flights (14)

| # | Column | What it records | Type |
|---|---|---|---|
| 17 | earn_model | Distance based, revenue based or fare class based | enum |
| 18 | earn_rate_own_flights | Points per USD (or % of distance) on own flights | text |
| 19 | earn_by_cabin_and_fare_class | Earn rate for each cabin and fare class | text |
| 20 | basic_economy_earns | Do the lowest fares earn points | yes/no |
| 21 | minimum_points_per_flight | Minimum points for a short flight | number |
| 22 | earn_on_partner_airlines | How points are earned on partner flights | text |
| 23 | best_partner_to_credit | Partner flights that earn the most | text |
| 24 | earn_on_award_tickets | Do award tickets earn points or status | yes/no |
| 25 | elite_bonus_earn | Extra % earned by each status tier | text |
| 26 | retro_credit_window_days | Days after the flight to claim missing points | number |
| 27 | points_posting_time_days | Days for points to post after the flight | number |
| 28 | status_credits_earned_on_partners | Do partner flights count towards status | yes/no |
| 29 | earn_on_paid_upgrades_and_ancillaries | Do paid seats, upgrades or bags earn points | yes/no |
| 30 | promo_frequency_flights | How often the program runs bonus earn offers | text |

## D. Earning off flights (16)

| # | Column | What it records | Type |
|---|---|---|---|
| 31 | cobrand_credit_cards | Co-branded credit cards and their countries | list |
| 32 | cobrand_card_earn_rate | Points per unit of spend on the best co-brand card | text |
| 33 | cobrand_card_key_perks | Welcome bonus, companion ticket, lounge visits | text |
| 34 | bank_transfer_partners | Bank programs that transfer in (Amex, Chase, Citi, Capital One, Bilt, HDFC, Axis and others) | list |
| 35 | bank_transfer_ratios | Ratio for each bank partner | text |
| 36 | bank_transfer_time | Time for a bank transfer to arrive | text |
| 37 | transfer_bonus_frequency | How often banks offer transfer bonuses | text |
| 38 | hotel_transfer_partners_in | Hotel programs that transfer in, with ratio | list |
| 39 | hotel_stay_earn | Points earned for hotel stays at partners | text |
| 40 | car_rental_earn | Car rental partners and earn rates | text |
| 41 | shopping_portal | Name of the online shopping portal | text |
| 42 | dining_program | Dining rewards program | text |
| 43 | other_earn_partners | Other partners (fuel, telecom, retail, surveys) | list |
| 44 | buy_points_price_inr | Normal price to buy 1 point, in INR | number |
| 45 | buy_points_sale_price_inr | Usual sale price for 1 point, in INR, and how often | text |
| 46 | buy_points_annual_limit | Maximum points you can buy in one year | number |

## E. Elite status (16)

| # | Column | What it records | Type |
|---|---|---|---|
| 47 | tier_names | Names of the status tiers, lowest to highest | list |
| 48 | qualification_metric | What counts: miles, segments, status credits, spend, points | text |
| 49 | qualification_thresholds | Threshold for each tier | text |
| 50 | qualification_period | Calendar year, membership year or rolling | enum |
| 51 | alliance_tier_mapping | Alliance status for each tier | text |
| 52 | lounge_access_by_tier | Lounge access for each tier, and guests | text |
| 53 | extra_baggage_by_tier | Extra baggage for each tier | text |
| 54 | priority_services_by_tier | Priority check-in, security, boarding | text |
| 55 | complimentary_upgrades | Free upgrades and who gets them | text |
| 56 | free_seat_selection_by_tier | Free seat selection, including exit rows | text |
| 57 | fee_waivers_by_tier | Change, cancel or award fees waived for each tier | text |
| 58 | extra_award_space_for_elites | Do elites see more award seats | yes/no |
| 59 | tier_benefit_one_liners | One line summary of the benefits of each tier | text |
| 60 | status_match_or_challenge | Does the program offer a status match or challenge | text |
| 61 | lifetime_status | Lifetime status rules | text |
| 62 | soft_landing | Do you drop one tier only when you fail to requalify | yes/no |

## F. Award pricing (18)

| # | Column | What it records | Type |
|---|---|---|---|
| 63 | award_pricing_model_own_flights | Fixed chart, dynamic or hybrid for own flights | enum |
| 64 | award_pricing_model_partners | Fixed chart, dynamic or hybrid for partner flights | enum |
| 65 | award_chart_published | Is the award chart public | yes/no |
| 66 | award_chart_basis | Zone based, distance based or revenue based | enum |
| 67 | distance_bands | Distance bands, if the chart is distance based | text |
| 68 | peak_offpeak_pricing | Does the price change on peak dates | text |
| 69 | economy_price_range | Points for one-way economy | text |
| 70 | premium_economy_price_range | Points for one-way premium economy | text |
| 71 | business_price_range | Points for one-way business | text |
| 72 | first_price_range | Points for one-way first | text |
| 73 | one_way_awards_allowed | Can you book one-way awards at half the round-trip price | yes/no |
| 74 | round_trip_discount | Is a round trip cheaper than two one-ways | yes/no |
| 75 | mixed_cabin_pricing | How the price is set when cabins are mixed | text |
| 76 | cash_plus_points | Can you pay part cash and part points | text |
| 77 | minimum_points_to_redeem | Minimum points needed for any redemption | number |
| 78 | sweet_spots_india | Best value redemptions to, from or within India (50% of sweet spots) | list |
| 79 | sweet_spots_global | Best value redemptions elsewhere (50% of sweet spots) | list |
| 80 | last_devaluation | Date and size of the last devaluation, and how much notice | text |

## G. Taxes, surcharges and fees on awards (10)

| # | Column | What it records | Type |
|---|---|---|---|
| 81 | surcharges_own_flights | Fuel or carrier surcharges on own flights, and typical amount | text |
| 82 | surcharges_partner_flights | Surcharges on partner flights, by partner | text |
| 83 | surcharge_free_partners | Partners with no surcharges | list |
| 84 | surcharge_varies_by_origin | Do surcharges change with the departure country | text |
| 85 | sample_taxes_long_haul_business | Taxes and fees on a sample long haul business award | text |
| 86 | award_booking_fee | Fee to issue an award ticket | text |
| 87 | phone_booking_fee | Fee to book by phone | text |
| 88 | close_in_booking_fee | Fee for awards booked close to departure | text |
| 89 | partner_award_booking_fee | Extra fee for partner awards | text |
| 90 | taxes_payable_currencies | Currencies and cards accepted for taxes | text |

## H. Surcharge ranking (4)

| # | Column | What it records | Type |
|---|---|---|---|
| 91 | surcharge_rank_own_flights | Surcharge level on own flights (Very high / High / Medium / Low / Very low) | enum |
| 92 | surcharge_rank_partner_flights | Typical surcharge level on partner flights (Very high / High / Medium / Low / Very low) | enum |
| 93 | surcharge_rank_india_routes | Surcharge level on awards to or from India (Very high / High / Medium / Low / Very low) | enum |
| 94 | surcharge_rank_overall | Overall surcharge level for the program (Very high / High / Medium / Low / Very low) | enum |

## I. Award availability and booking (14)

| # | Column | What it records | Type |
|---|---|---|---|
| 95 | booking_window_own_days | Days before departure that own award seats open | number |
| 96 | booking_window_partner_days | Days before departure that partner seats can be booked | number |
| 97 | saver_space_own_flights | How easy it is to find low price seats on own flights | rating 1-10 |
| 98 | premium_cabin_release_to_partners | Does the airline release business and first seats to partners | text |
| 99 | partner_awards_online | Can you book partner awards online, and which partners | text |
| 100 | partners_phone_only | Partners you can book by phone only | list |
| 101 | award_hold | Can you hold an award, and for how many days | text |
| 102 | award_waitlist | Can you waitlist an award | yes/no |
| 103 | award_calendar_search | Does the website show a calendar of award prices | yes/no |
| 104 | third_party_search_tools | Tools that show this program's award space | list |
| 105 | upgrade_with_points | Can you upgrade a paid ticket with points, and the cost | text |
| 106 | upgrade_on_partners | Can you upgrade on partner airlines with points | yes/no |
| 107 | seat_selection_on_awards | Is seat selection free on award tickets | text |
| 108 | baggage_on_awards | Baggage allowance on award tickets | text |

## J. Routing rules (10)

| # | Column | What it records | Type |
|---|---|---|---|
| 109 | stopover_one_way | Stopover allowed on a one-way award, and the cost | text |
| 110 | stopover_round_trip | Number of stopovers allowed on a round trip, and the cost | text |
| 111 | stopover_max_hours_layover | Maximum hours before a connection counts as a stopover | number |
| 112 | open_jaw_allowed | Is an open jaw allowed, and the rules | text |
| 113 | max_segments | Maximum flights in one award | number |
| 114 | max_permitted_mileage_rule | Rule on routing distance | text |
| 115 | mix_partners_on_one_award | Can you mix airlines on one award | yes/no |
| 116 | routing_restrictions | Other routing rules (backtracking, region transit) | text |
| 117 | married_segment_logic | Does the program price connecting flights as one unit | yes/no |
| 118 | multi_city_online_booking | Can you book multi city awards online | yes/no |

## K. Changes and cancellations (10)

| # | Column | What it records | Type |
|---|---|---|---|
| 119 | award_date_change_fee | Fee to change the date of an award | text |
| 120 | award_reissue_fee | Fee to change the route or the airline | text |
| 121 | award_cancel_redeposit_fee | Fee to cancel an award and get the points back | text |
| 122 | cancel_deadline | Last time before departure that you can cancel | text |
| 123 | no_show_penalty | What you lose if you do not fly | text |
| 124 | taxes_refund_on_cancel | Are taxes and surcharges refunded | yes/no |
| 125 | free_cancel_24_hours | Free cancel within 24 hours of booking | yes/no |
| 126 | schedule_change_rights | What you can do when the airline changes the schedule | text |
| 127 | paid_ticket_change_fee | Change fee on paid tickets | text |
| 128 | paid_ticket_cancel_fee | Cancel fee on paid tickets | text |

## L. Family and other passengers (7)

| # | Column | What it records | Type |
|---|---|---|---|
| 129 | book_awards_for_others | Can you book awards for anyone | yes/no |
| 130 | nominee_limit | Limit on named people, and the fee to change them | text |
| 131 | lap_infant_award_cost | Cost for a lap infant on an award | text |
| 132 | child_award_discount | Discount for children on awards | text |
| 133 | companion_voucher | Companion or 2-for-1 voucher, and how to get it | text |
| 134 | family_account | Is there a family account | yes/no |
| 135 | group_award_limit | Maximum passengers on one award booking | number |

## M. Other redemptions and partnerships (6)

| # | Column | What it records | Type |
|---|---|---|---|
| 136 | points_transfer_out | Can points move to other programs, and the ratio | text |
| 137 | transfer_points_to_other_member | Can you move points to another member's account in the same program, and the fee and limit | text |
| 138 | linked_programs | Programs you can link to | list |
| 139 | non_flight_redemptions | Hotels, cars, shopping, gift cards, lounge passes, charity | list |
| 140 | non_flight_redemption_value_inr | Value of 1 point on non flight redemptions, in INR | number |
| 141 | non_alliance_partners | Airline partners outside the alliance | list |

## N. Product and comfort ratings (our scores) (3)

| # | Column | What it records | Type |
|---|---|---|---|
| 142 | comfort_scores | Scores for economy, premium economy, business, first, food, entertainment, wifi, lounges | rating 1-10 each |
| 143 | operations_scores | Scores for on-time performance, network size, customer service | rating 1-10 each |
| 144 | overall_value_score | Our overall score for value of the points | rating 1-10 |

## O. Remarks and data control (2)

| # | Column | What it records | Type |
|---|---|---|---|
| 145 | final_remarks | Restrictions and anything that does not fit another column (for example who can join, join fee, residency rules) | text |
| 146 | data_last_checked | Date we last checked the data | date |
