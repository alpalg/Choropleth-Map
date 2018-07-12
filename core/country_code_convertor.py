# DataMaps expects in ISO Alpha-3
# Becouse I created dict with ISO Alpha-3 and ISO Alpha-2 format
# Data was taken from Wikipedia

# ISO Alpha-3
country_codes_alpha_3 = ['ZWE', 'ZMB', 'ZAF', 'YEM', 'WSM', 'WLF', 'VUT', 'VNM', 'VIR', 'VGB', 'VEN', 'VCT', 'VAT',
                         'UZB', 'USA', 'URY', 'UMI', 'UKR', 'UGA', 'TZA', 'TWN', 'TUV', 'TUR', 'TUN', 'TTO', 'TON',
                         'TLS', 'TKM', 'TKL', 'TJK', 'THA', 'TGO', 'TCD', 'TCA', 'SYR', 'SYC', 'SWZ', 'SWE', 'SVN',
                         'SVK', 'SUR', 'STP', 'SSD', 'SRB', 'SPM', 'SOM', 'SMR', 'SLV', 'SLE', 'SLB', 'SJM', 'SHN',
                         'SGS', 'SGP', 'SEN', 'SDN', 'SAU', 'RWA', 'RUS', 'ROU', 'REU', 'QAT', 'PYF', 'PSE', 'PRY',
                         'PRT', 'PRK', 'PRI', 'POL', 'PNG', 'PLW', 'PHL', 'PER', 'PCN', 'PAN', 'PAK', 'OMN', 'NZL',
                         'NRU', 'NPL', 'NOR', 'NLD', 'NIU', 'NIC', 'NGA', 'NFK', 'NER', 'NCL', 'NAM', 'MYT', 'MYS',
                         'MWI', 'MUS', 'MTQ', 'MSR', 'MRT', 'MOZ', 'MNP', 'MNG', 'MNE', 'MMR', 'MLT', 'MLI', 'MKD',
                         'MHL', 'MEX', 'MDV', 'MDG', 'MDA', 'MCO', 'MAR', 'MAF', 'MAC', 'LVA', 'LUX', 'LTU', 'LSO',
                         'LKA', 'LIE', 'LCA', 'LBY', 'LBR', 'LBN', 'LAO', 'KWT', 'KOR', 'KNA', 'KIR', 'KHM', 'KGZ',
                         'KEN', 'KAZ', 'JPN', 'JOR', 'JEY', 'JAM', 'ITA', 'ISR', 'ISL', 'IRQ', 'IRN', 'IRL', 'IOT',
                         'IND', 'IMN', 'IDN', 'HUN', 'HTI', 'HRV', 'HND', 'HMD', 'HKG', 'GUY', 'GUM', 'GUF', 'GTM',
                         'GRL', 'GRD', 'GRC', 'GNQ', 'GNB', 'GMB', 'GLP', 'GIN', 'GIB', 'GHA', 'GGY', 'GEO', 'GBR',
                         'GAB', 'FSM', 'FRO', 'FRA', 'FLK', 'FJI', 'FIN', 'ETH', 'EST', 'ESP', 'ESH', 'ERI', 'EGY',
                         'ECU', 'DZA', 'DOM', 'DNK', 'DMA', 'DJI', 'DEU', 'CZE', 'CYP', 'CYM', 'CXR', 'CUB', 'CRI',
                         'CPV', 'COM', 'COL', 'COK', 'COG', 'COD', 'CMR', 'CIV', 'CHN', 'CHL', 'CHE', 'CCK', 'CAN',
                         'CAF', 'BWA', 'BVT', 'BTN', 'BRN', 'BRB', 'BRA', 'BOL', 'BMU', 'BLZ', 'BLR', 'BLM', 'BIH',
                         'BHS', 'BHR', 'BGR', 'BGD', 'BFA', 'BEN', 'BEL', 'BDI', 'AZE', 'AUT', 'AUS', 'ATG', 'ATF',
                         'ATA', 'ASM', 'ARM', 'ARG', 'ARE', 'ANT', 'AND', 'ALB', 'ALA', 'AIA', 'AGO', 'AFG', 'ABW',
                         'XKX']

# ISO Alpha-2 || Some values were corrected because 'countrycodes' 
#    not accords to current geopolitical map. 
country_codes_alpha_2 = ['ZW', 'ZM', 'ZA', 'RY', 'WS', 'WF', 'VU', 'VN', 'VI', 'VG', 'VE', 'VC', 'VA', 'UZ', 'US', 'UY',
                         'UM', 'UA', 'UG', 'TZ', 'TW', 'TV', 'TR', 'TN', 'TT', 'TO', 'TP', 'TM', 'TK', 'TJ', 'TH', 'TG',
                         'TD', 'TC', 'SY', 'SC', 'SZ', 'SE', 'SI', 'SK', 'SR', 'ST', 'SS', 'YF', 'PM', 'SO', 'SM', 'SV',
                         'SL', 'SB', 'SJ', 'SH', 'GS', 'SG', 'SN', 'SD', 'SA', 'RW', 'RU', 'RO', 'RE', 'QA', 'PF', 'PS',
                         'PY', 'PT', 'KP', 'PR', 'PL', 'PG', 'PW', 'PH', 'PE', 'PN', 'PA', 'PK', 'OM', 'NZ', 'NR', 'NP',
                         'NO', 'NL', 'NU', 'NI', 'NG', 'NF', 'NE', 'NC', 'NA', 'YT', 'MY', 'MW', 'MU', 'MQ', 'MS', 'MR',
                         'MZ', 'MP', 'MN', 'ME', 'MM', 'MT', 'ML', 'MK', 'MH', 'MX', 'MV', 'MG', 'MD', 'MC', 'MA', 'MF',
                         'MO', 'LV', 'LU', 'LT', 'LS', 'LK', 'LI', 'LC', 'LY', 'LR', 'LB', 'LA', 'KW', 'KR', 'KN', 'KI',
                         'KH', 'KG', 'KE', 'KZ', 'JP', 'JO', 'JE', 'JM', 'IT', 'IL', 'IS', 'IQ', 'IR', 'IE', 'IO', 'IN',
                         'IM', 'ID', 'HU', 'HT', 'HR', 'HN', 'HM', 'HK', 'GY', 'GU', 'GF', 'GT', 'GL', 'GD', 'GR', 'GQ',
                         'GW', 'GM', 'GP', 'GN', 'GI', 'GH', 'GG', 'GE', 'GB', 'GA', 'FM', 'FO', 'FR', 'FK', 'FJ', 'FI',
                         'ET', 'EE', 'ES', 'EH', 'ER', 'EG', 'EC', 'DZ', 'DO', 'DK', 'DM', 'DJ', 'DE', 'CZ', 'CY', 'KY',
                         'CX', 'CU', 'CR', 'CV', 'KM', 'CO', 'CK', 'CG', 'ZR', 'CM', 'CI', 'CN', 'CL', 'CH', 'CC', 'CA',
                         'CF', 'BW', 'BV', 'BT', 'BN', 'BB', 'BR', 'BO', 'BM', 'BZ', 'BY', 'BL', 'BA', 'BS', 'BH', 'BG',
                         'BD', 'BF', 'BJ', 'BE', 'BI', 'AZ', 'AT', 'AU', 'AG', 'TF', 'AQ', 'AS', 'AM', 'AR', 'AE', 'AN',
                         'AD', 'AL', 'AX', 'AI', 'AO', 'AF', 'AW', 'XK']

# Was created the dict to create a correspondence between formats.
country_codes = dict(zip(country_codes_alpha_2, country_codes_alpha_3))