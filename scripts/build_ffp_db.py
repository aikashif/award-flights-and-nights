"""Build the frequent flyer program database.

One source of truth for the column list and the program data.
Outputs:
  data/ffp_database.xlsx   (Programs, Parameters, Sources sheets)
  docs/ffp-parameters.md   (column list)

Values marked with "?" at the start need a check against the official
program site. The script removes the "?" and fills those cells yellow.
"""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent.parent
USD_INR = 88  # exchange rate used for all INR values

SURCHARGE_SCALE = "Very high / High / Medium / Low / Very low"

# Each column: (name, description, type, {program_key: value})
CATEGORIES = [
    ("A. Program identity", [
        ("program_name", "Name of the program", "text"),
        ("currency_name", "Name of the points (Avios, miles, points)", "text"),
        ("owner_airline", "Airline or group that runs the program", "text"),
        ("other_airlines_using_currency", "Other airlines that use the same currency", "list"),
        ("alliance", "Star Alliance, oneworld, SkyTeam or none", "enum"),
        ("home_country", "Country of the owner airline", "text"),
        ("main_hubs", "Hub airports", "list"),
        ("points_value_inr", f"Our estimate of the value of 1 point, in INR (USD 1 = INR {USD_INR})", "number"),
        ("website_and_app_quality", "How easy the website and app are to use", "rating 1-10"),
        ("program_source_url", "Official program page used for the data", "text"),
    ]),
    ("B. Points expiry and account rules", [
        ("expiry_policy", "Fixed term, activity based or no expiry", "enum"),
        ("expiry_months", "Months until points expire", "number"),
        ("how_to_keep_points_alive", "Activities that reset the expiry date", "text"),
        ("expired_points_reinstatement", "Can you get expired points back, and the fee", "text"),
        ("family_pooling", "Can a household pool points in one account", "yes/no"),
        ("family_pooling_rules", "Number of members, relation rules, fees", "text"),
    ]),
    ("C. Earning on flights", [
        ("earn_model", "Distance based, revenue based or fare class based", "enum"),
        ("earn_rate_own_flights", "Points per USD (or % of distance) on own flights", "text"),
        ("earn_by_cabin_and_fare_class", "Earn rate for each cabin and fare class", "text"),
        ("basic_economy_earns", "Do the lowest fares earn points", "yes/no"),
        ("minimum_points_per_flight", "Minimum points for a short flight", "number"),
        ("earn_on_partner_airlines", "How points are earned on partner flights", "text"),
        ("best_partner_to_credit", "Partner flights that earn the most", "text"),
        ("earn_on_award_tickets", "Do award tickets earn points or status", "yes/no"),
        ("elite_bonus_earn", "Extra % earned by each status tier", "text"),
        ("retro_credit_window_days", "Days after the flight to claim missing points", "number"),
        ("points_posting_time_days", "Days for points to post after the flight", "number"),
        ("status_credits_earned_on_partners", "Do partner flights count towards status", "yes/no"),
        ("earn_on_paid_upgrades_and_ancillaries", "Do paid seats, upgrades or bags earn points", "yes/no"),
        ("promo_frequency_flights", "How often the program runs bonus earn offers", "text"),
    ]),
    ("D. Earning off flights", [
        ("cobrand_credit_cards", "Co-branded credit cards and their countries", "list"),
        ("cobrand_card_earn_rate", "Points per unit of spend on the best co-brand card", "text"),
        ("cobrand_card_key_perks", "Welcome bonus, companion ticket, lounge visits", "text"),
        ("bank_transfer_partners", "Bank programs that transfer in (Amex, Chase, Citi, Capital One, Bilt, HDFC, Axis and others)", "list"),
        ("bank_transfer_ratios", "Ratio for each bank partner", "text"),
        ("bank_transfer_time", "Time for a bank transfer to arrive", "text"),
        ("transfer_bonus_frequency", "How often banks offer transfer bonuses", "text"),
        ("hotel_transfer_partners_in", "Hotel programs that transfer in, with ratio", "list"),
        ("hotel_stay_earn", "Points earned for hotel stays at partners", "text"),
        ("car_rental_earn", "Car rental partners and earn rates", "text"),
        ("shopping_portal", "Name of the online shopping portal", "text"),
        ("dining_program", "Dining rewards program", "text"),
        ("other_earn_partners", "Other partners (fuel, telecom, retail, surveys)", "list"),
        ("buy_points_price_inr", "Normal price to buy 1 point, in INR", "number"),
        ("buy_points_sale_price_inr", "Usual sale price for 1 point, in INR, and how often", "text"),
        ("buy_points_annual_limit", "Maximum points you can buy in one year", "number"),
    ]),
    ("E. Elite status", [
        ("tier_names", "Names of the status tiers, lowest to highest", "list"),
        ("qualification_metric", "What counts: miles, segments, status credits, spend, points", "text"),
        ("qualification_thresholds", "Threshold for each tier", "text"),
        ("qualification_period", "Calendar year, membership year or rolling", "enum"),
        ("alliance_tier_mapping", "Alliance status for each tier", "text"),
        ("lounge_access_by_tier", "Lounge access for each tier, and guests", "text"),
        ("extra_baggage_by_tier", "Extra baggage for each tier", "text"),
        ("priority_services_by_tier", "Priority check-in, security, boarding", "text"),
        ("complimentary_upgrades", "Free upgrades and who gets them", "text"),
        ("free_seat_selection_by_tier", "Free seat selection, including exit rows", "text"),
        ("fee_waivers_by_tier", "Change, cancel or award fees waived for each tier", "text"),
        ("extra_award_space_for_elites", "Do elites see more award seats", "yes/no"),
        ("tier_benefit_one_liners", "One line summary of the benefits of each tier", "text"),
        ("status_match_or_challenge", "Does the program offer a status match or challenge", "text"),
        ("lifetime_status", "Lifetime status rules", "text"),
        ("soft_landing", "Do you drop one tier only when you fail to requalify", "yes/no"),
    ]),
    ("F. Award pricing", [
        ("award_pricing_model_own_flights", "Fixed chart, dynamic or hybrid for own flights", "enum"),
        ("award_pricing_model_partners", "Fixed chart, dynamic or hybrid for partner flights", "enum"),
        ("award_chart_published", "Is the award chart public", "yes/no"),
        ("award_chart_basis", "Zone based, distance based or revenue based", "enum"),
        ("distance_bands", "Distance bands, if the chart is distance based", "text"),
        ("peak_offpeak_pricing", "Does the price change on peak dates", "text"),
        ("economy_price_range", "Points for one-way economy", "text"),
        ("premium_economy_price_range", "Points for one-way premium economy", "text"),
        ("business_price_range", "Points for one-way business", "text"),
        ("first_price_range", "Points for one-way first", "text"),
        ("one_way_awards_allowed", "Can you book one-way awards at half the round-trip price", "yes/no"),
        ("round_trip_discount", "Is a round trip cheaper than two one-ways", "yes/no"),
        ("mixed_cabin_pricing", "How the price is set when cabins are mixed", "text"),
        ("cash_plus_points", "Can you pay part cash and part points", "text"),
        ("minimum_points_to_redeem", "Minimum points needed for any redemption", "number"),
        ("sweet_spots_india", "Best value redemptions to, from or within India (50% of sweet spots)", "list"),
        ("sweet_spots_global", "Best value redemptions elsewhere (50% of sweet spots)", "list"),
        ("last_devaluation", "Date and size of the last devaluation, and how much notice", "text"),
    ]),
    ("G. Taxes, surcharges and fees on awards", [
        ("surcharges_own_flights", "Fuel or carrier surcharges on own flights, and typical amount", "text"),
        ("surcharges_partner_flights", "Surcharges on partner flights, by partner", "text"),
        ("surcharge_free_partners", "Partners with no surcharges", "list"),
        ("surcharge_varies_by_origin", "Do surcharges change with the departure country", "text"),
        ("sample_taxes_long_haul_business", "Taxes and fees on a sample long haul business award", "text"),
        ("award_booking_fee", "Fee to issue an award ticket", "text"),
        ("phone_booking_fee", "Fee to book by phone", "text"),
        ("close_in_booking_fee", "Fee for awards booked close to departure", "text"),
        ("partner_award_booking_fee", "Extra fee for partner awards", "text"),
        ("taxes_payable_currencies", "Currencies and cards accepted for taxes", "text"),
    ]),
    ("H. Surcharge ranking", [
        ("surcharge_rank_own_flights", f"Surcharge level on own flights ({SURCHARGE_SCALE})", "enum"),
        ("surcharge_rank_partner_flights", f"Typical surcharge level on partner flights ({SURCHARGE_SCALE})", "enum"),
        ("surcharge_rank_india_routes", f"Surcharge level on awards to or from India ({SURCHARGE_SCALE})", "enum"),
        ("surcharge_rank_overall", f"Overall surcharge level for the program ({SURCHARGE_SCALE})", "enum"),
    ]),
    ("I. Award availability and booking", [
        ("booking_window_own_days", "Days before departure that own award seats open", "number"),
        ("booking_window_partner_days", "Days before departure that partner seats can be booked", "number"),
        ("saver_space_own_flights", "How easy it is to find low price seats on own flights", "rating 1-10"),
        ("premium_cabin_release_to_partners", "Does the airline release business and first seats to partners", "text"),
        ("partner_awards_online", "Can you book partner awards online, and which partners", "text"),
        ("partners_phone_only", "Partners you can book by phone only", "list"),
        ("award_hold", "Can you hold an award, and for how many days", "text"),
        ("award_waitlist", "Can you waitlist an award", "yes/no"),
        ("award_calendar_search", "Does the website show a calendar of award prices", "yes/no"),
        ("third_party_search_tools", "Tools that show this program's award space", "list"),
        ("upgrade_with_points", "Can you upgrade a paid ticket with points, and the cost", "text"),
        ("upgrade_on_partners", "Can you upgrade on partner airlines with points", "yes/no"),
        ("seat_selection_on_awards", "Is seat selection free on award tickets", "text"),
        ("baggage_on_awards", "Baggage allowance on award tickets", "text"),
    ]),
    ("J. Routing rules", [
        ("stopover_one_way", "Stopover allowed on a one-way award, and the cost", "text"),
        ("stopover_round_trip", "Number of stopovers allowed on a round trip, and the cost", "text"),
        ("stopover_max_hours_layover", "Maximum hours before a connection counts as a stopover", "number"),
        ("open_jaw_allowed", "Is an open jaw allowed, and the rules", "text"),
        ("max_segments", "Maximum flights in one award", "number"),
        ("max_permitted_mileage_rule", "Rule on routing distance", "text"),
        ("mix_partners_on_one_award", "Can you mix airlines on one award", "yes/no"),
        ("routing_restrictions", "Other routing rules (backtracking, region transit)", "text"),
        ("married_segment_logic", "Does the program price connecting flights as one unit", "yes/no"),
        ("multi_city_online_booking", "Can you book multi city awards online", "yes/no"),
    ]),
    ("K. Changes and cancellations", [
        ("award_date_change_fee", "Fee to change the date of an award", "text"),
        ("award_reissue_fee", "Fee to change the route or the airline", "text"),
        ("award_cancel_redeposit_fee", "Fee to cancel an award and get the points back", "text"),
        ("cancel_deadline", "Last time before departure that you can cancel", "text"),
        ("no_show_penalty", "What you lose if you do not fly", "text"),
        ("taxes_refund_on_cancel", "Are taxes and surcharges refunded", "yes/no"),
        ("free_cancel_24_hours", "Free cancel within 24 hours of booking", "yes/no"),
        ("schedule_change_rights", "What you can do when the airline changes the schedule", "text"),
        ("paid_ticket_change_fee", "Change fee on paid tickets", "text"),
        ("paid_ticket_cancel_fee", "Cancel fee on paid tickets", "text"),
    ]),
    ("L. Family and other passengers", [
        ("book_awards_for_others", "Can you book awards for anyone", "yes/no"),
        ("nominee_limit", "Limit on named people, and the fee to change them", "text"),
        ("lap_infant_award_cost", "Cost for a lap infant on an award", "text"),
        ("child_award_discount", "Discount for children on awards", "text"),
        ("companion_voucher", "Companion or 2-for-1 voucher, and how to get it", "text"),
        ("family_account", "Is there a family account", "yes/no"),
        ("group_award_limit", "Maximum passengers on one award booking", "number"),
    ]),
    ("M. Other redemptions and partnerships", [
        ("points_transfer_out", "Can points move to other programs, and the ratio", "text"),
        ("transfer_points_to_other_member", "Can you move points to another member's account in the same program, and the fee and limit", "text"),
        ("linked_programs", "Programs you can link to", "list"),
        ("non_flight_redemptions", "Hotels, cars, shopping, gift cards, lounge passes, charity", "list"),
        ("non_flight_redemption_value_inr", "Value of 1 point on non flight redemptions, in INR", "number"),
        ("non_alliance_partners", "Airline partners outside the alliance", "list"),
    ]),
    ("N. Product and comfort ratings (our scores)", [
        ("comfort_scores", "Scores for economy, premium economy, business, first, food, entertainment, wifi, lounges", "rating 1-10 each"),
        ("operations_scores", "Scores for on-time performance, network size, customer service", "rating 1-10 each"),
        ("overall_value_score", "Our overall score for value of the points", "rating 1-10"),
    ]),
    ("O. Remarks and data control", [
        ("final_remarks", "Restrictions and anything that does not fit another column (for example who can join, join fee, residency rules)", "text"),
        ("data_last_checked", "Date we last checked the data", "date"),
    ]),
]

INR = lambda usd_cents: round(usd_cents / 100 * USD_INR, 2)  # noqa: E731

ALASKA = {
    "program_name": "Atmos Rewards (Alaska Airlines and Hawaiian Airlines; replaced Alaska Mileage Plan in Aug 2025)",
    "currency_name": "Atmos points",
    "owner_airline": "Alaska Air Group (Alaska Airlines, Hawaiian Airlines, Horizon Air)",
    "other_airlines_using_currency": "Hawaiian Airlines; Horizon Air",
    "alliance": "oneworld",
    "home_country": "United States",
    "main_hubs": "Seattle (SEA); Portland (PDX); San Francisco (SFO); Los Angeles (LAX); Anchorage (ANC); Honolulu (HNL)",
    "points_value_inr": f"{INR(1.5)} (about 1.5 US cents)",
    "website_and_app_quality": "?8",
    "program_source_url": "https://www.alaskaair.com/atmosrewards",
    "expiry_policy": "No expiry",
    "expiry_months": "Not applicable",
    "how_to_keep_points_alive": "Not needed; points do not expire",
    "expired_points_reinstatement": "Not applicable",
    "family_pooling": "?Check",
    "family_pooling_rules": "?Check official terms",
    "earn_model": "Distance based in 2026; from 1 Jan 2027 the member chooses distance, price paid or segments",
    "earn_rate_own_flights": "2026: 100% of miles flown on most fares. 2027 choices: 1 point per mile, 5 points per USD 1 of fare (no taxes), or 500 points per segment",
    "earn_by_cabin_and_fare_class": "2026: 100% most main cabin; up to 150% full fare economy; up to 200% first class (J)",
    "basic_economy_earns": "No. Saver (X) fares booked on or after 11 Jun 2026 for travel on or after 1 Aug 2026 earn no points and no status points",
    "minimum_points_per_flight": "?500",
    "earn_on_partner_airlines": "Distance x fare class % from each partner's earn chart",
    "best_partner_to_credit": "?American Airlines, Qatar Airways, Cathay Pacific, JAL in premium cabins",
    "earn_on_award_tickets": "No",
    "elite_bonus_earn": "Silver 25%; Gold 50%; Platinum 100%; Titanium 150%",
    "retro_credit_window_days": "?Check",
    "points_posting_time_days": "?3 to 7 for Alaska and Hawaiian; longer for partners",
    "status_credits_earned_on_partners": "Yes",
    "earn_on_paid_upgrades_and_ancillaries": "?Check",
    "promo_frequency_flights": "Communities challenges (6 communities from 1 Oct 2026, bonus for destinations flown 1 Oct 2026 to 31 Dec 2027)",
    "cobrand_credit_cards": "Atmos Rewards Ascent Visa (US, Bank of America); Atmos Rewards Summit Visa Infinite (US, Bank of America); business card refresh late 2026. No India card",
    "cobrand_card_earn_rate": "?Check per card",
    "cobrand_card_key_perks": "Summit: partner booking fee waived; Global Companion Award (?check value). Ascent: companion fare (?check)",
    "bank_transfer_partners": "Bilt (US); Bank of America transfers planned for 2027. No Indian bank partners",
    "bank_transfer_ratios": "Bilt 1:1",
    "bank_transfer_time": "?Instant to 1 day",
    "transfer_bonus_frequency": "?Occasional Bilt bonuses",
    "hotel_transfer_partners_in": "?Marriott Bonvoy 3:1 (5,000 bonus per 60,000)",
    "hotel_stay_earn": "?Check hotel partners on official site",
    "car_rental_earn": "?Check car partners on official site",
    "shopping_portal": "?Atmos Rewards shopping portal",
    "dining_program": "?Atmos Rewards Dining",
    "other_earn_partners": "?Check official site",
    "buy_points_price_inr": "?Check base price on official site",
    "buy_points_sale_price_inr": f"{INR(1.98)} (1.98 US cents) with 90% bonus in recent sale; sales run several times a year",
    "buy_points_annual_limit": "?Check",
    "tier_names": "Silver; Gold; Platinum; Titanium",
    "qualification_metric": "Status points (2026: distance based; 2027: member chooses distance, price paid or segments)",
    "qualification_thresholds": "Silver 20,000; Gold 40,000; Platinum 80,000; Titanium 135,000 status points",
    "qualification_period": "Calendar year (resets to zero on 1 Jan)",
    "alliance_tier_mapping": "Silver = oneworld Ruby; Gold = Sapphire; Platinum = Emerald; Titanium = Emerald",
    "lounge_access_by_tier": "Gold: oneworld Sapphire lounges on international oneworld trips; Platinum and Titanium: oneworld Emerald lounges (?check guest rules)",
    "extra_baggage_by_tier": "Silver 1; Gold 2; Platinum 3; Titanium 3 free checked bags (for companions on same booking)",
    "priority_services_by_tier": "Priority check-in and boarding from Silver; priority security from Gold (?check)",
    "complimentary_upgrades": "Space-available upgrades on Alaska and Hawaiian; Titanium can get long haul lie-flat upgrades. Priority: Titanium > Platinum > Gold > Silver",
    "free_seat_selection_by_tier": "?Preferred seats from Silver; Premium Class seats from Gold (check)",
    "fee_waivers_by_tier": "Gold and higher: same-day flight changes free (?check)",
    "extra_award_space_for_elites": "No",
    "tier_benefit_one_liners": "Silver: 25% bonus, 1 free bag, oneworld Ruby. Gold: 50% bonus, 2 bags, same-day change, oneworld Sapphire lounges. Platinum: 100% bonus, 3 bags, better upgrades, oneworld Emerald lounges. Titanium: 150% bonus, top upgrade priority incl. long haul lie-flat",
    "status_match_or_challenge": "?Check (Alaska has run status matches in the past)",
    "lifetime_status": "?Check (Mileage Plan had Million Miler; check Atmos rules)",
    "soft_landing": "?Check",
    "award_pricing_model_own_flights": "Dynamic",
    "award_pricing_model_partners": "Hybrid: distance based chart by region gives the floor; price can go higher with demand",
    "award_chart_published": "Yes (partners)",
    "award_chart_basis": "Distance based within regions",
    "distance_bands": "?Check official partner chart",
    "peak_offpeak_pricing": "Dynamic on own flights; partner chart price is the lowest level",
    "economy_price_range": "Partners from 4,500 points (shortest band); Alaska from 5,000; Asia sale from 20,000",
    "premium_economy_price_range": "?Check",
    "business_price_range": "JAL US West Coast to Japan 60,000; US East Coast to Japan 75,000; Cathay from 75,000; Qatar US East Coast to Doha 70,000",
    "first_price_range": "Cathay First 110,000 to 130,000 (sources differ)",
    "one_way_awards_allowed": "Yes",
    "round_trip_discount": "No",
    "mixed_cabin_pricing": "?Priced at highest cabin on the long segment (check)",
    "cash_plus_points": "?Check",
    "minimum_points_to_redeem": "4,500",
    "sweet_spots_india": (
        "1) Global Getaways sale: Mumbai from 30,000 points one-way (travel to 12 May 2027). "
        "2) Cathay Pacific business US or Canada to Delhi, Mumbai, Bengaluru, Chennai or Hyderabad via Hong Kong, with free Hong Kong stopover (from 75,000 to Asia; check India band). "
        "3) JAL business US to Delhi or Bengaluru via Tokyo, with free Tokyo stopover (from 60,000 to Japan; check India band). "
        "4) Qatar Airways Qsuite US to India via Doha, with free Doha stopover (rare saver space; check price)"
    ),
    "sweet_spots_global": (
        "1) JAL business US West Coast to Japan 60,000. "
        "2) Qatar Airways Qsuite US East Coast to Doha 70,000. "
        "3) Cathay Pacific First 110,000 to 130,000. "
        "4) Hawai'i from 11,500 points one-way in Global Getaways sale"
    ),
    "last_devaluation": "2026: Saver X fares stop earning (1 Aug 2026); partner booking fee up from USD 12.50 to USD 20 (1 Jul 2026); higher Platinum and Titanium thresholds",
    "surcharges_own_flights": "None",
    "surcharges_partner_flights": "British Airways about USD 1,000 on transatlantic; Icelandair, Hainan, Royal Air Maroc also add surcharges; most others none",
    "surcharge_free_partners": "American Airlines; Aer Lingus; Condor; ?Qatar Airways; ?Cathay Pacific; ?JAL; ?Starlux (check)",
    "surcharge_varies_by_origin": "Only government taxes change by country (for example UK APD); carrier surcharges depend on the partner",
    "sample_taxes_long_haul_business": "?USD 50 to 200 on surcharge free partners (check per route)",
    "award_booking_fee": "None on Alaska and Hawaiian",
    "phone_booking_fee": "?Check",
    "close_in_booking_fee": "None",
    "partner_award_booking_fee": "USD 20 per person each way from 1 Jul 2026 (was USD 12.50); not refunded; waived for Summit Visa cardholders",
    "taxes_payable_currencies": "USD by card",
    "surcharge_rank_own_flights": "Very low",
    "surcharge_rank_partner_flights": "Low",
    "surcharge_rank_india_routes": "Low (avoid British Airways via London: High)",
    "surcharge_rank_overall": "Low",
    "booking_window_own_days": "?330",
    "booking_window_partner_days": "?Varies by partner (about 330 to 361)",
    "saver_space_own_flights": "?6",
    "premium_cabin_release_to_partners": "Yes, Alaska and Hawaiian space bookable by oneworld partners",
    "partner_awards_online": "Yes, most partners online at alaskaair.com",
    "partners_phone_only": "?Check",
    "award_hold": "No",
    "award_waitlist": "No",
    "award_calendar_search": "Yes",
    "third_party_search_tools": "seats.aero; AwardFares; point.me; Roame",
    "upgrade_with_points": "?Check",
    "upgrade_on_partners": "No",
    "seat_selection_on_awards": "Free on Alaska and Hawaiian awards (?check Saver); partners per partner rules",
    "baggage_on_awards": "Same as the fare and cabin booked",
    "stopover_one_way": "Yes, 1 free stopover up to 14 days at a partner hub on international one-way awards. Not inside one region (for example intra-Asia)",
    "stopover_round_trip": "2 free stopovers (1 each way)",
    "stopover_max_hours_layover": "24 (international, ?check)",
    "open_jaw_allowed": "?Yes on round trips (check)",
    "max_segments": "?Check",
    "max_permitted_mileage_rule": "?Check",
    "mix_partners_on_one_award": "?Sources differ; check",
    "routing_restrictions": "No stopovers inside one international region; companion awards no stopover",
    "married_segment_logic": "?Check",
    "multi_city_online_booking": "?Check",
    "award_date_change_fee": "None",
    "award_reissue_fee": "None (partner booking fee not charged again)",
    "award_cancel_redeposit_fee": "None; points and taxes come back; partner booking fee not refunded",
    "cancel_deadline": "Before departure",
    "no_show_penalty": "?Check",
    "taxes_refund_on_cancel": "Yes",
    "free_cancel_24_hours": "Yes",
    "schedule_change_rights": "?Check",
    "paid_ticket_change_fee": "None on Main and First (not Saver)",
    "paid_ticket_cancel_fee": "None on Main and First, credit given; Saver not refundable",
    "book_awards_for_others": "Yes",
    "nominee_limit": "No limit",
    "lap_infant_award_cost": "Taxes only on long haul international awards on Alaska or Hawaiian ticket stock (027); call to add. Free on US domestic",
    "child_award_discount": "None",
    "companion_voucher": "Summit Visa: Global Companion Award; Ascent Visa: companion fare (?check details)",
    "family_account": "?Check",
    "group_award_limit": "?Check",
    "points_transfer_out": "?Check (no regular transfer out)",
    "transfer_points_to_other_member": "?Yes, for a fee; check fee and yearly limit",
    "linked_programs": "HawaiianMiles merged 1:1 into Atmos points",
    "non_flight_redemptions": "?Hotels; cars; check official site",
    "non_flight_redemption_value_inr": "?Check",
    "non_alliance_partners": "Aer Lingus; Condor; Hainan; Icelandair; LATAM; Porter; Starlux; ?Singapore Airlines; ?El Al (check list)",
    "comfort_scores": "?Economy 7; Premium economy 7; Business (Hawaiian A330 / 787 lie-flat) 7; First (domestic) 6; Food 6; Entertainment 6; Wifi 8 (free Starlink from 2026); Lounges 6",
    "operations_scores": "?On-time 8; Network 6; Customer service 8",
    "overall_value_score": "?8",
    "final_remarks": (
        "Anyone can join, free, from any country. No Indian co-brand card or Indian bank transfer partner, "
        "so earning from India is hard (buy points in sales or credit partner flights). "
        "Program changes a lot in 2026 and 2027; yellow cells need a check on alaskaair.com. "
        f"INR values use USD 1 = INR {USD_INR}."
    ),
    "data_last_checked": "2026-11-09",
}

PROGRAMS = [ALASKA]

SOURCES = [
    "https://www.alaskaair.com/atmosrewards",
    "https://news.alaskaair.com/loyalty/introducing-atmos-rewards/",
    "https://www.alaskaair.com/atmosrewards/content/partners/airlines/qatar-airways",
    "https://en.wikipedia.org/wiki/Atmos_Rewards",
    "https://awardwallet.com/news/alaska-atmos-rewards/2026-program-changes/",
    "https://awardfares.com/blog/atmos-rewards-guide/",
    "https://awardfares.com/blog/atmos-rewards-sweet-spots/",
    "https://thepointsparty.com/articles/alaska-airlines-atmos-rewards-2026-changes",
    "https://www.insideflyer.com/posts/atmos-rewards-status-spans-four-elite-tiers/",
    "https://www.insideflyer.com/posts/alaska-now-charges-only-taxes-for-lap-infants-on-award-flights/",
    "https://awardtravelfinder.com/cancellation-fees/alaska-airlines",
    "https://onemileatatime.com/guides/redeem-alaska-atmos-rewards-points/",
    "https://onemileatatime.com/deals/buy-alaska-atmos-rewards-points/",
    "https://onemileatatime.com/deals/alaska-atmos-rewards-global-getaways/",
    "https://upgradedpoints.com/travel/airlines/airline-fuel-surcharges/",
    "https://awardlocker.com/value/alaska-mileage-plan",
    "https://flightpoints.com/blogs/best-oneworld-sweet-spots/",
    "https://www.nerdwallet.com/travel/learn/guide-to-atmos-rewards",
]

HEAD_FILL = PatternFill("solid", start_color="1F3864")
CAT_FILL = PatternFill("solid", start_color="D9E1F2")
CHECK_FILL = PatternFill("solid", start_color="FFF2CC")
HEAD_FONT = Font(bold=True, color="FFFFFF")
WRAP = Alignment(wrap_text=True, vertical="top")


def columns():
    n = 0
    for cat, cols in CATEGORIES:
        for name, desc, typ in cols:
            n += 1
            yield n, cat, name, desc, typ


def build_xlsx(path):
    wb = Workbook()

    ws = wb.active
    ws.title = "Programs"
    cols = list(columns())
    ws.cell(row=1, column=1, value="category")
    ws.cell(row=2, column=1, value="column")
    for i, (_, cat, name, _, _) in enumerate(cols, start=2):
        ws.cell(row=1, column=i, value=cat).fill = CAT_FILL
        c = ws.cell(row=2, column=i, value=name)
        c.fill, c.font = HEAD_FILL, HEAD_FONT
        ws.column_dimensions[get_column_letter(i)].width = 28
    for r, prog in enumerate(PROGRAMS, start=3):
        ws.cell(row=r, column=1, value=r - 2)
        for i, (_, _, name, _, _) in enumerate(cols, start=2):
            val = prog.get(name, "")
            cell = ws.cell(row=r, column=i)
            if isinstance(val, str) and val.startswith("?"):
                val, cell.fill = val[1:], CHECK_FILL
            cell.value = val
            cell.alignment = WRAP
        ws.row_dimensions[r].height = 150
    ws.column_dimensions["A"].width = 10
    ws.freeze_panes = "C3"

    # Same data, one row per parameter: easier to read on screen.
    pv = wb.create_sheet("Program view")
    head = ["#", "category", "column", "description", "type"] + [p["currency_name"] for p in PROGRAMS]
    for j, h in enumerate(head, start=1):
        c = pv.cell(row=1, column=j, value=h)
        c.fill, c.font = HEAD_FILL, HEAD_FONT
    for n, cat, name, desc, typ in cols:
        row = [n, cat, name, desc, typ]
        for j, v in enumerate(row, start=1):
            pv.cell(row=n + 1, column=j, value=v).alignment = WRAP
        for k, prog in enumerate(PROGRAMS):
            val = prog.get(name, "")
            cell = pv.cell(row=n + 1, column=6 + k)
            if isinstance(val, str) and val.startswith("?"):
                val, cell.fill = val[1:], CHECK_FILL
            cell.value, cell.alignment = val, WRAP
    for letter, w in zip("ABCDEF", (5, 26, 32, 45, 12, 70)):
        pv.column_dimensions[letter].width = w
    pv.freeze_panes = "D2"

    src = wb.create_sheet("Sources and key")
    src.append(["Key"])
    src.append(["Yellow cell", "Value needs a check on the official program site"])
    src.append(["INR rate", f"USD 1 = INR {USD_INR}"])
    src.append(["Surcharge scale", SURCHARGE_SCALE])
    src.append([])
    src.append(["Sources (Atmos Rewards)"])
    for s in SOURCES:
        src.append([s])
    src["B2"].fill = CHECK_FILL
    src.column_dimensions["A"].width = 80
    src.column_dimensions["B"].width = 60

    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)


def build_md(path):
    total = sum(len(c) for _, c in CATEGORIES)
    lines = [
        "# Frequent flyer program database: parameters",
        "",
        "This file lists the columns for the frequent flyer program (FFP) database. "
        "Each row in the database is one program. The data is in `data/ffp_database.xlsx`.",
        "",
        f"There are {total} columns in {len(CATEGORIES)} groups. "
        "`scripts/build_ffp_db.py` makes this file and the Excel file, so change the columns there.",
        "",
        f"All money values are in INR (USD 1 = INR {USD_INR}). "
        "Surcharge ranks use a five point scale: " + SURCHARGE_SCALE + ".",
        "",
    ]
    n = 0
    for cat, cols in CATEGORIES:
        lines += [f"## {cat} ({len(cols)})", "", "| # | Column | What it records | Type |", "|---|---|---|---|"]
        for name, desc, typ in cols:
            n += 1
            lines.append(f"| {n} | {name} | {desc} | {typ} |")
        lines.append("")
    path.write_text("\n".join(lines))


if __name__ == "__main__":
    build_xlsx(ROOT / "data" / "ffp_database.xlsx")
    build_md(ROOT / "docs" / "ffp-parameters.md")
    print("done")
