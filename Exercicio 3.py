import pulp as pl

prob = pl.LpProblem('mochila', pl.LpMaximize)

pesos = [541,766,1307,529,798,1327,294,925,1219,630,651,1281,512,883,1395,297,500,797,337,699,1036,572,645,1217,572,
635,1207,146,373,519,62,963,1025,371,798,1169,721,742,1463,51,636,687,242,952,1194,248,501,749,506,823,1329,244,722,
966,442,627,1069,216,457,673,418,670,1088,544,1083,1627,327,892,1219,656,754,1410,442,579,1021,144,1002,1146,332,1041,
1373,366,827,1193,748,956,1704,527,705,1232,147,424,571,56,150,206,309,331,640,389,501,890,245,821,1066,190,275,465,
235,796,1031,303,575,878,214,855,1069,467,751,1218,379,900,1279,521,996,1517,554,646,1200,338,482,820,294,586,880,746,
761,1507,834,896,1730,163,191,354,624,879,1503,224,443,667,356,518,874,383,418,801,358,922,1280,279,842,1121,829,856,
1685,137,249,386,647,934,1581,167,791,958,220,686,906,93,519,612,325,947,1272,372,654,1026,452,960,1412,39,493,532,
265,588,853,121,605,726,74,758,832,207,643,850,110,461,571,441,580,1021,136,222,358,302,421,723,762,958,1720,174,296,
470,602,636,1238,291,650,941,701,934,1635,353,907,1260,607,974,1581,297,405,702,279,402,681,720,742,1462,255,477,732,
129,769,898,679,752,1431,608,638,1246,356,690,1046,312,581,893,626,824,1450,450,783,1233,392,571,963,208,629,837,281,
886,1167,292,1014,1306,248,896,1144,664,843,1507,202,461,663,73,783,856,429,901,1330,608,810,1418]

valores = [461,700,919,541,771,1169,273,829,1013,620,676,893,605,872,963,309,546,568,279,744,1002,478,715,730,
535,719,1098,216,425,551,109,948,1014,353,821,936,706,833,1204,109,562,603,264,899,985,333,591,645,471,804,977,
320,669,751,350,707,854,229,429,581,506,690,1163,575,994,1080,293,893,915,726,744,1292,456,569,969,110,907,989,
322,950,1235,418,909,947,834,987,1791,507,703,1118,178,402,517,123,167,276,379,391,489,295,586,641,219,826,856,
130,227,286,293,710,756,227,573,581,247,759,900,423,670,956,430,974,1149,492,963,1155,567,677,862,244,501,511,
203,646,827,742,773,1237,897,967,1562,150,207,344,679,958,1085,196,447,474,434,458,738,382,434,726,439,978,1118,
223,841,932,853,877,1374,137,340,353,549,982,1493,233,864,1027,249,772,975,105,590,592,269,916,993,454,560,925,
417,885,1263,116,468,478,362,496,823,187,622,779,170,847,941,131,668,699,124,406,508,375,492,649,234,283,459,378,
443,696,841,966,1510,240,309,365,673,729,974,288,619,748,674,844,1420,288,972,1247,527,912,1301,274,457,489,250,
311,388,625,813,1028,348,535,798,173,858,899,729,815,1046,546,720,847,400,687,1023,365,494,687,563,749,833,388,
837,1094,302,556,697,160,682,723,305,792,1075,254,966,1030,186,929,1068,659,853,1176,192,555,633,158,716,797,467,
983,1448,643,899,971]

S = [str(i+1) for i in range(len(pesos))]

V = dict(zip(S, valores))
P = dict(zip(S, pesos))

P_MAX = 65423

x = pl.LpVariable.dicts('x', S, lowBound=0, cat=pl.LpInteger)

prob += pl.lpSum([V[i]*x[i] for i in S])

for i in S:
    prob += pl.lpSum([P[i] * x[i] for i in S]) <= P_MAX

prob.solve()

print("total revenue:", prob.objective.value())


