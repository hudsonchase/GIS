# coding: utf-8
import arcpy
fc = 'airports'
cursor = arcpy.da.SearchCursor(fc,['*'])
for row in cursor:
    print(row)
# (1, (-130.01252746616962, 55.904338836668046), 0.0, 0.0, 5.0, '4Z7', 'Seaplane Base', 'Hyder', 319.0, ' ', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (2, (-158.53256225574347, 56.30786895728659), 0.0, 0.0, 6.0, 'KCL', 'Airport', 'Chignik Lagoon', 2697.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (3, (-161.15107727069946, 64.93807220426885), 0.0, 0.0, 7.0, 'KKA', 'Airport', 'Koyuk', 2346.0, 'AK', 'Nome Census Area', '02180', '02')
# (4, (-164.52558898964014, 67.74520873999143), 0.0, 0.0, 8.0, 'KVL', 'Airport', 'Kivalina', 3313.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (5, (-131.68510436997065, 55.34780883790762), 0.0, 0.0, 10.0, '5KE', 'Seaplane Base', 'Ketchikan Harbor', 46644.0, 'AK', 'Ketchikan Gateway Borough', '02130', '02')
# (6, (-131.57806396458028, 55.13104629555016), 0.0, 0.0, 666.0, 'MTM', 'Seaplane Base', 'Metlakatla', 15387.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (7, (-133.24333190904036, 55.29632186925892), 0.0, 0.0, 667.0, 'KWF', 'Seaplane Base', 'Waterfall', 2018.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (8, (-131.71374511694358, 55.35556793221434), 0.0, 0.0, 668.0, 'KTN', 'Airport', 'Ketchikan', 132451.0, 'AK', 'Ketchikan Gateway Borough', '02130', '02')
# (9, (-132.39752197266085, 55.537414550641074), 0.0, 0.0, 669.0, 'KXA', 'Seaplane Base', 'Kasaan', 455.0, ' ', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (10, (-132.6460876461279, 55.48158645644986), 0.0, 0.0, 670.0, 'HYL', 'Seaplane Base', 'Hollis', 4170.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (11, (-133.14779663041014, 55.47883224491221), 0.0, 0.0, 671.0, 'CGA', 'Seaplane Base', 'Craig', 5898.0, ' ', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (12, (-132.53668212897702, 55.687961578264265), 0.0, 0.0, 672.0, 'KTB', 'Seaplane Base', 'Thorne Bay', 5210.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (13, (-132.84196472179445, 56.00324249274689), 0.0, 0.0, 673.0, 'KCC', 'Seaplane Base', 'Coffman Cove', 705.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (14, (-132.25502014156626, 55.739635467402934), 0.0, 0.0, 674.0, '84K', 'Seaplane Base', 'Meyers Chuck', 341.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (15, (-133.0760040284631, 55.57923507713713), 0.0, 0.0, 675.0, 'AKW', 'Airport', 'Klawock', 3900.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (16, (-131.80113220238917, 55.9163017273429), 0.0, 0.0, 676.0, '78K', 'Seaplane Base', 'Yes Bay Lodge', 941.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (17, (-132.36982727021234, 56.484325408990514), 0.0, 0.0, 677.0, 'WRG', 'Airport', 'Wrangell', 13895.0, 'AK', 'Wrangell-Petersburg Census Area', '02280', '02')
# (18, (-132.94528198247747, 56.801651001392656), 0.0, 0.0, 678.0, 'PSG', 'Airport', 'Petersburg James A. Johnson', 21047.0, 'AK', 'Wrangell-Petersburg Census Area', '02280', '02')
# (19, (-133.94561767581507, 56.972995757848025), 0.0, 0.0, 679.0, 'KAE', 'Seaplane Base', 'Kake', 3466.0, 'AK', 'Wrangell-Petersburg Census Area', '02280', '02')
# (20, (-135.36160278334177, 57.04713821455704), 0.0, 0.0, 680.0, 'SIT', 'Airport', 'Sitka Rocky Gutierrez', 68659.0, 'AK', 'Sitka Borough', '02220', '02')
# (21, (-134.58509826677158, 57.503555298238496), 0.0, 0.0, 681.0, 'AGN', 'Seaplane Base', 'Angoon', 2865.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (22, (-134.89790344209013, 58.254386901634234), 0.0, 0.0, 682.0, 'FNR', 'Seaplane Base', 'Funter Bay', 303.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (23, (-135.21844482396943, 57.779659271258424), 0.0, 0.0, 683.0, 'TKE', 'Seaplane Base', 'Tenakee', 1072.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (24, (-134.7559509276931, 58.127441406595665), 0.0, 0.0, 684.0, 'HWI', 'Seaplane Base', 'Hawk Inlet', 1073.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (25, (-135.4096984858964, 58.09609222447665), 0.0, 0.0, 685.0, 'HNH', 'Airport', 'Hoonah', 9126.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (26, (-134.57627868651213, 58.35496139555204), 0.0, 0.0, 686.0, 'JNU', 'Airport', 'Juneau International', 377559.0, 'AK', 'Juneau Borough', '02110', '02')
# (27, (-136.23626708985427, 57.955173492462734), 0.0, 0.0, 687.0, 'PEC', 'Seaplane Base', 'Pelican', 1022.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (28, (-136.34739685018445, 58.19518280014614), 0.0, 0.0, 688.0, 'ELV', 'Seaplane Base', 'Elfin Cove', 1325.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (29, (-135.44903564427955, 58.42049789426244), 0.0, 0.0, 689.0, 'EXI', 'Seaplane Base', 'Excursion Inlet', 1972.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (30, (-135.70738220222682, 58.424381255890296), 0.0, 0.0, 690.0, 'GST', 'Airport', 'Gustavus', 11570.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (31, (-135.52210998518763, 59.24522781361276), 0.0, 0.0, 691.0, 'HNS', 'Airport', 'Haines', 11060.0, 'AK', 'Haines Borough', '02100', '02')
# (32, (-135.31565856938744, 59.46006011947901), 0.0, 0.0, 692.0, 'SGY', 'Airport', 'Skagway', 36554.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (33, (-139.66023254429643, 59.50336074839987), 0.0, 0.0, 693.0, 'YAK', 'Airport', 'Yakutat', 14702.0, 'AK', 'Yakutat Borough', '02282', '02')
# (34, (-141.66177368151017, 59.96901702881286), 0.0, 0.0, 694.0, '19AK', 'Airport', 'Icy Bay', 455.0, 'AK', 'Valdez-Cordova Census Area', '02261', '02')
# (35, (-154.24784851060025, 56.899486541670626), 0.0, 0.0, 695.0, 'ALZ', 'Seaplane Base', 'Alitak', 313.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (36, (-154.1825561526443, 56.938690185803466), 0.0, 0.0, 696.0, 'AKK', 'Airport', 'Akhiok', 1037.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (37, (-153.32060241696794, 57.73037338252561), 0.0, 0.0, 697.0, 'WSJ', 'Seaplane Base', 'San Juan/Uganik Bay', 335.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (38, (-153.26974487302743, 57.21810150108348), 0.0, 0.0, 698.0, '6R7', 'Airport', 'Old Harbor', 1082.0, ' ', 'Kodiak Island Borough', '02150', '02')
# (39, (-153.97842407221313, 57.53510665874535), 0.0, 0.0, 699.0, '2A3', 'Airport', 'Larsen Bay', 2855.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (40, (-152.39138793940185, 57.78083419774009), 0.0, 0.0, 700.0, 'T44', 'Seaplane Base', 'Trident Basin', 2625.0, ' ', 'Kodiak Island Borough', '02150', '02')
# (41, (-152.49385070834347, 57.74996948220587), 0.0, 0.0, 701.0, 'ADQ', 'Airport', 'Kodiak', 80107.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (42, (-152.5005035403061, 57.92287445089522), 0.0, 0.0, 702.0, '4K5', 'Airport', 'Ouzinkie', 661.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (43, (-152.8460998536253, 57.88537597622036), 0.0, 0.0, 703.0, 'ORI', 'Airport', 'Port Lions', 1499.0, ' ', 'Kodiak Island Borough', '02150', '02')
# (44, (-145.4776458743576, 60.49183273279442), 0.0, 0.0, 704.0, 'CDV', 'Airport', 'Merle K. (Mudhole) Smith', 20648.0, 'AK', 'Valdez-Cordova Census Area', '02261', '02')
# (45, (-160.51770019500796, 55.31502914467933), 0.0, 0.0, 705.0, 'SDP', 'Airport', 'Sand Point', 4366.0, 'AK', 'Aleutians East Borough', '02013', '02')
# (46, (-159.48866271950888, 55.897533416733836), 0.0, 0.0, 706.0, 'KIB', 'Seaplane Base', 'Ivanof Bay', 277.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (47, (-159.1585845948032, 55.9080619813754), 0.0, 0.0, 707.0, 'AK5', 'Airport', 'Perryville', 1111.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (48, (-158.59092712428733, 56.317829132408576), 0.0, 0.0, 708.0, 'KCG', 'Airport', 'Chignik Fisheries', 1416.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (49, (-158.77536010748295, 56.25504684433645), 0.0, 0.0, 709.0, 'A79', 'Airport', 'Chignik Lake', 635.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (50, (-158.37322998037925, 56.311462402667814), 0.0, 0.0, 710.0, 'AJC', 'Airport', 'Chignik', 1819.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (51, (-154.45037841822938, 57.56706237782652), 0.0, 0.0, 711.0, 'KYK', 'Airport', 'Karluk', 910.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (52, (-151.83154296853314, 59.34825897207395), 0.0, 0.0, 712.0, 'PGM', 'Airport', 'Port Graham', 1481.0, 'AK', 'Kenai Peninsula Borough', '02122', '02')
# (53, (-151.70405578574588, 59.44244003268142), 0.0, 0.0, 713.0, 'SOV', 'Airport', 'Seldovia', 5534.0, 'AK', 'Kenai Peninsula Borough', '02122', '02')
# (54, (-151.92515563962104, 59.352149963550005), 0.0, 0.0, 714.0, 'KEB', 'Airport', 'English Bay', 1153.0, 'AK', 'Kenai Peninsula Borough', '02122', '02')
# (55, (-151.47657775915624, 59.64555740355138), 0.0, 0.0, 715.0, 'HOM', 'Airport', 'Homer', 32859.0, 'AK', 'Kenai Peninsula Borough', '02122', '02')
# (56, (-149.41880798320184, 60.12693786588983), 0.0, 0.0, 716.0, 'SWD', 'Airport', 'Seward', 1213.0, 'AK', 'Kenai Peninsula Borough', '02122', '02')
# (57, (-149.1257934570024, 60.9660949703067), 0.0, 0.0, 717.0, 'AQY', 'Airport', 'Girdwood', 2420.0, 'AK', 'Anchorage Borough', '02020', '02')
# (58, (-146.2483673095037, 61.13394927983546), 0.0, 0.0, 718.0, 'VDZ', 'Airport', 'Valdez', 21536.0, 'AK', 'Valdez-Cordova Census Area', '02261', '02')
# (59, (-144.42709350566074, 61.58285903891357), 0.0, 0.0, 719.0, 'CXC', 'Airport', 'Chitina', 451.0, ' ', 'Valdez-Cordova Census Area', '02261', '02')
# (60, (-145.45663452146596, 62.15488815346555), 0.0, 0.0, 720.0, 'GKN', 'Airport', 'Gulkana', 708.0, 'AK', 'Valdez-Cordova Census Area', '02261', '02')
# (61, (-142.52192688002145, 63.13382339503369), 0.0, 0.0, 721.0, '5TE', 'Airport', 'Tetlin', 787.0, 'AK', 'Southeast Fairbanks Census Area', '02240', '02')
# (62, (-162.2662200926831, 55.116348266159605), 0.0, 0.0, 722.0, 'KVC', 'Airport', 'King Cove', 2777.0, 'AK', 'Aleutians East Borough', '02013', '02')
# (63, (-162.72425842288789, 55.20560073888305), 0.0, 0.0, 723.0, 'CDB', 'Airport', 'Cold Bay', 9909.0, 'AK', 'Aleutians East Borough', '02013', '02')
# (64, (-163.41032409637992, 54.84744644179989), 0.0, 0.0, 724.0, 'KFP', 'Airport', 'False Pass', 498.0, 'AK', 'Aleutians East Borough', '02013', '02')
# (65, (-158.63182067908105, 56.95943450929525), 0.0, 0.0, 725.0, 'PTH', 'Airport', 'Port Heiden', 1694.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (66, (-157.56744384735563, 57.58037948652412), 0.0, 0.0, 726.0, 'PNP', 'Airport', 'Pilot Point', 1037.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (67, (-157.38098144503763, 58.18837356528786), 0.0, 0.0, 727.0, 'EII', 'Airport', 'Egegik', 1879.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (68, (-155.77738952630557, 58.55484390232431), 0.0, 0.0, 728.0, '5Z9', 'Seaplane Base', 'Lake Brooks', 5251.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (69, (-156.86521911576955, 59.11816406222175), 0.0, 0.0, 729.0, 'KLL', 'Airport', 'Levelock', 1157.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (70, (-156.64921569834578, 58.67680358921433), 0.0, 0.0, 730.0, 'AKN', 'Airport', 'King Salmon', 48743.0, 'AK', 'Bristol Bay Borough', '02060', '02')
# (71, (-157.00825500476464, 58.7034378048109), 0.0, 0.0, 731.0, 'WSN', 'Airport', 'South Naknek Nr 2', 1176.0, 'AK', 'Bristol Bay Borough', '02060', '02')
# (72, (-157.0071411134716, 58.73426818872599), 0.0, 0.0, 732.0, '4AK9', 'Airport', 'Tibbetts', 487.0, 'AK', 'Bristol Bay Borough', '02060', '02')
# (73, (-155.1212768554425, 58.98207855218351), 0.0, 0.0, 733.0, 'LKK', 'Airport', 'Kulik Lake', 3178.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (74, (-154.802703857497, 59.432643890303325), 0.0, 0.0, 734.0, '9K2', 'Airport', 'Kokhanok', 2283.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (75, (-154.12384033176588, 59.789608002107684), 0.0, 0.0, 735.0, '4K0', 'Airport', 'Pedro Bay', 676.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (76, (-155.90327453629078, 59.32373428361035), 0.0, 0.0, 736.0, 'IGG', 'Airport', 'Igiugig', 1330.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (77, (-154.8396911620175, 59.979042053148305), 0.0, 0.0, 737.0, '5NN', 'Airport', 'Nondalton', 1845.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (78, (-154.3188781735888, 60.20433425861921), 0.0, 0.0, 738.0, 'TPO', 'Airport', 'Port Alsworth', 282.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (79, (-151.03244018596578, 60.47613906846328), 0.0, 0.0, 739.0, 'SXQ', 'Airport', 'Soldotna', 2508.0, 'AK', 'Kenai Peninsula Borough', '02122', '02')
# (80, (-151.24752807645953, 60.57199859585859), 0.0, 0.0, 740.0, 'ENA', 'Airport', 'Kenai Municipal', 106530.0, 'AK', 'Kenai Peninsula Borough', '02122', '02')
# (81, (-151.13807678201783, 61.07666397096557), 0.0, 0.0, 741.0, 'TYE', 'Airport', 'Tyonek', 8780.0, 'AK', 'Kenai Peninsula Borough', '02122', '02')
# (82, (-151.79891967730123, 60.81554794268345), 0.0, 0.0, 742.0, '5AK0', 'Airport', 'Trading Bay Production', 400.0, 'AK', 'Kenai Peninsula Borough', '02122', '02')
# (83, (-151.0438995363345, 61.17221832241768), 0.0, 0.0, 743.0, 'BLG', 'Airport', 'Beluga', 2570.0, 'AK', 'Kenai Peninsula Borough', '02122', '02')
# (84, (-149.84616088851416, 61.214378357375324), 0.0, 0.0, 744.0, 'MRI', 'Airport', 'Merrill Field', 2240.0, ' ', 'Anchorage Borough', '02020', '02')
# (85, (-149.9719390869193, 61.18000412029397), 0.0, 0.0, 745.0, 'LHD', 'Seaplane Base', 'Lake Hood', 26733.0, 'AK', 'Anchorage Borough', '02020', '02')
# (86, (-149.79386901854033, 61.2530632015056), 0.0, 0.0, 746.0, 'EDF', 'Airport', 'Elmendorf Air Force Base', 2104.0, 'AK', 'Anchorage Borough', '02020', '02')
# (87, (-149.08882141127907, 61.594741821577884), 0.0, 0.0, 747.0, 'PAQ', 'Airport', 'Palmer Municipal', 683.0, 'AK', 'Matanuska-Susitna Borough', '02170', '02')
# (88, (-150.05166625979004, 61.75441741942842), 0.0, 0.0, 748.0, 'UUO', 'Airport', 'Willow', 1595.0, 'AK', 'Matanuska-Susitna Borough', '02170', '02')
# (89, (-147.16886901839047, 61.93699646011862), 0.0, 0.0, 749.0, 'AZK', 'Airport', 'Skelton', 300.0, ' ', 'Matanuska-Susitna Borough', '02170', '02')
# (90, (-143.00611877416208, 63.2954826356152), 0.0, 0.0, 750.0, 'TKJ', 'Airport', 'Tok', 1816.0, 'AK', 'Southeast Fairbanks Census Area', '02240', '02')
# (91, (-141.15092468222826, 64.77639007594132), 0.0, 0.0, 751.0, 'EAA', 'Airport', 'Eagle', 483.0, 'AK', 'Southeast Fairbanks Census Area', '02240', '02')
# (92, (-165.78530883823228, 54.13246536298618), 0.0, 0.0, 752.0, 'KQA', 'Seaplane Base', 'Akutan', 2313.0, ' ', 'Aleutians East Borough', '02013', '02')
# (93, (-166.54350280720877, 53.900138854724446), 0.0, 0.0, 753.0, 'DUT', 'Airport', 'Unalaska', 31988.0, 'AK', 'Aleutians West Census Area', '02016', '02')
# (94, (-158.55883789095589, 58.811191558743474), 0.0, 0.0, 754.0, 'KKU', 'Airport', 'Ekuk', 648.0, 'AK', 'Dillingham Census Area', '02070', '02')
# (95, (-158.54522705108752, 58.84230422995631), 0.0, 0.0, 755.0, 'CLP', 'Airport', 'Clarks Point', 2029.0, 'AK', 'Dillingham Census Area', '02070', '02')
# (96, (-159.04997253420507, 58.988964081027575), 0.0, 0.0, 756.0, '17Z', 'Airport', 'Manokotak', 2855.0, 'AK', 'Dillingham Census Area', '02070', '02')
# (97, (-157.47441101055966, 59.353996277106546), 0.0, 0.0, 757.0, 'KEK', 'Airport', 'Ekwok', 973.0, 'AK', 'Dillingham Census Area', '02070', '02')
# (98, (-158.50334167447866, 59.04541397097802), 0.0, 0.0, 758.0, 'DLG', 'Airport', 'Dillingham', 45173.0, 'AK', 'Dillingham Census Area', '02070', '02')
# (99, (-157.25947570803746, 59.72664260846966), 0.0, 0.0, 759.0, 'JZZ', 'Airport', 'Koliganek', 1855.0, 'AK', 'Dillingham Census Area', '02070', '02')
# (100, (-151.19136047380678, 61.96529388460516), 0.0, 0.0, 760.0, 'SKW', 'Airport', 'Skwentna', 287.0, 'AK', 'Matanuska-Susitna Borough', '02170', '02')
# (101, (-150.09368896467396, 62.32049941981245), 0.0, 0.0, 761.0, 'TKA', 'Airport', 'Talkeetna', 13589.0, 'AK', 'Matanuska-Susitna Borough', '02170', '02')
# (102, (-148.91064453132003, 63.73259735078716), 0.0, 0.0, 762.0, 'INR', 'Airport', 'McKinley National Park', 725.0, ' ', 'Denali Borough', '02068', '02')
# (103, (-161.81967163044138, 59.01135635371281), 0.0, 0.0, 763.0, 'PTU', 'Airport', 'Platinum', 510.0, 'AK', 'Bethel Census Area', '02050', '02')
# (104, (-161.58139038086136, 59.117275237961906), 0.0, 0.0, 764.0, 'GNU', 'Airport', 'Goodnews', 1596.0, 'AK', 'Bethel Census Area', '02050', '02')
# (105, (-160.27304077181415, 59.075622558234556), 0.0, 0.0, 765.0, 'A63', 'Airport', 'Twin Hills', 524.0, 'AK', 'Dillingham Census Area', '02070', '02')
# (106, (-160.39692688027128, 59.05284118667146), 0.0, 0.0, 766.0, 'TOG', 'Airport', 'Togiak', 3845.0, 'AK', 'Dillingham Census Area', '02070', '02')
# (107, (-156.5881805420983, 61.78987503020852), 0.0, 0.0, 767.0, 'SRV', 'Airport', 'Stony River 2', 347.0, ' ', 'Bethel Census Area', '02050', '02')
# (108, (-157.15570068343976, 61.70931243931767), 0.0, 0.0, 768.0, 'SLQ', 'Airport', 'Sleetmute', 671.0, ' ', 'Bethel Census Area', '02050', '02')
# (109, (-154.36396789580172, 63.01744842520469), 0.0, 0.0, 769.0, '5NI', 'Airport', 'Nikolai', 356.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (110, (-150.99395751932403, 63.54171371491606), 0.0, 0.0, 770.0, '5Z5', 'Airport', 'Kantishna', 1556.0, 'AK', 'Denali Borough', '02068', '02')
# (111, (-152.30067443887424, 63.88056564348972), 0.0, 0.0, 771.0, 'MHM', 'Airport', 'Minchumina', 254.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (112, (-148.96897888226957, 63.866207122560695), 0.0, 0.0, 772.0, 'HRR', 'Airport', 'Healy River', 482.0, 'AK', 'Denali Borough', '02068', '02')
# (113, (-147.10150146492063, 64.66566467328607), 0.0, 0.0, 773.0, 'EIL', 'Airport', 'Eielson Air Force Base', 1740.0, 'AK', 'Fairbanks North Star Borough', '02090', '02')
# (114, (-147.61444091761422, 64.83750152617455), 0.0, 0.0, 774.0, 'FBK', 'Airport', 'Wainwright Army Air Field', 775.0, 'AK', 'Fairbanks North Star Borough', '02090', '02')
# (115, (-147.85966491720214, 64.81367492655664), 0.0, 0.0, 775.0, 'FAI', 'Airport', 'Fairbanks International', 393381.0, 'AK', 'Fairbanks North Star Borough', '02090', '02')
# (116, (-144.07580566370038, 65.83049011272857), 0.0, 0.0, 776.0, 'CRC', 'Airport', 'Circle City', 465.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (117, (-143.73594665541378, 66.6496887203582), 0.0, 0.0, 777.0, 'CIK', 'Airport', 'Chalkyitsik', 1312.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (118, (-174.20634460441994, 52.22034835839008), 0.0, 0.0, 778.0, 'AKA', 'Airport', 'Atka', 397.0, 'AK', 'Aleutians West Census Area', '02016', '02')
# (119, (-161.8794860838157, 59.75700759862184), 0.0, 0.0, 779.0, 'AQH', 'Airport', 'Quinhagak', 1666.0, 'AK', 'Bethel Census Area', '02050', '02')
# (120, (-162.0056152345554, 60.21590423549213), 0.0, 0.0, 780.0, 'EEK', 'Airport', 'Eek', 1408.0, ' ', 'Bethel Census Area', '02050', '02')
# (121, (-162.8817291258984, 59.95950698865664), 0.0, 0.0, 781.0, 'DUY', 'Airport', 'Kongiganak', 3349.0, 'AK', 'Bethel Census Area', '02050', '02')
# (122, (-163.1675567631341, 59.876449584880504), 0.0, 0.0, 782.0, 'A85', 'Airport', 'Kwigillingok', 3047.0, ' ', 'Bethel Census Area', '02050', '02')
# (123, (-162.6670074465364, 60.3353462217508), 0.0, 0.0, 783.0, 'A61', 'Airport', 'Tuntutuliak', 3342.0, 'AK', 'Bethel Census Area', '02050', '02')
# (124, (-161.2270202636742, 60.90481185927996), 0.0, 0.0, 784.0, 'AKI', 'Airport', 'Akiak', 1373.0, 'AK', 'Bethel Census Area', '02050', '02')
# (125, (-161.44534301736633, 60.804252624159346), 0.0, 0.0, 785.0, 'KWT', 'Airport', 'Kwethluk', 2293.0, 'AK', 'Bethel Census Area', '02050', '02')
# (126, (-160.9684143070746, 61.09676361095194), 0.0, 0.0, 786.0, 'TLT', 'Airport', 'Tuluksak', 2775.0, 'AK', 'Bethel Census Area', '02050', '02')
# (127, (-161.7767333986274, 60.703689575013925), 0.0, 0.0, 787.0, 'PKA', 'Airport', 'Napaskiak', 748.0, 'AK', 'Bethel Census Area', '02050', '02')
# (128, (-161.43507385227645, 60.90786361691244), 0.0, 0.0, 788.0, 'KKI', 'Seaplane Base', 'Akiachak', 2250.0, 'AK', 'Bethel Census Area', '02050', '02')
# (129, (-161.96951293937062, 60.69118881241383), 0.0, 0.0, 789.0, 'WNA', 'Airport', 'Napakiak', 1236.0, 'AK', 'Bethel Census Area', '02050', '02')
# (130, (-161.8379974368322, 60.77977752701133), 0.0, 0.0, 790.0, 'BET', 'Airport', 'Bethel', 125885.0, 'AK', 'Bethel Census Area', '02050', '02')
# (131, (-159.5430450437937, 61.58159637457311), 0.0, 0.0, 791.0, 'ANI', 'Airport', 'Aniak', 16471.0, 'AK', 'Bethel Census Area', '02050', '02')
# (132, (-160.34132385221397, 61.53627395637807), 0.0, 0.0, 792.0, 'KLG', 'Airport', 'Kalskag', 4549.0, 'AK', 'Bethel Census Area', '02050', '02')
# (133, (-157.34793090838468, 61.7876434326983), 0.0, 0.0, 793.0, 'RDV', 'Airport', 'Red Devil', 250.0, 'AK', 'Bethel Census Area', '02050', '02')
# (134, (-158.13711547819673, 61.86902236968666), 0.0, 0.0, 794.0, 'CJX', 'Airport', 'Crooked Creek', 720.0, 'AK', 'Bethel Census Area', '02050', '02')
# (135, (-155.60575866672906, 62.95287322981574), 0.0, 0.0, 795.0, 'MCG', 'Airport', 'McGrath', 4954.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (136, (-152.10939025845363, 65.17439269976336), 0.0, 0.0, 796.0, 'TAL', 'Airport', 'Ralph M. Calhoun Memorial', 4653.0, ' ', 'Yukon-Koyukuk Census Area', '02290', '02')
# (137, (-149.36996459958658, 65.14370727577023), 0.0, 0.0, 797.0, '51Z', 'Airport', 'Minto', 393.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (138, (-150.142807006638, 65.50786590548722), 0.0, 0.0, 798.0, 'RMP', 'Airport', 'Rampart', 1087.0, ' ', 'Yukon-Koyukuk Census Area', '02290', '02')
# (139, (-149.09591674835923, 66.0090026853257), 0.0, 0.0, 799.0, 'SVS', 'Airport', 'Stevens Village', 2212.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (140, (-147.40121459947414, 66.36154937760176), 0.0, 0.0, 800.0, 'WBQ', 'Airport', 'Beaver', 2676.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (141, (-145.82403564422955, 66.27399444538742), 0.0, 0.0, 801.0, 'Z91', 'Airport', 'Birch Creek', 744.0, ' ', 'Yukon-Koyukuk Census Area', '02290', '02')
# (142, (-145.2504119876231, 66.57148742720307), 0.0, 0.0, 802.0, 'FYU', 'Airport', 'Fort Yukon', 11392.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (143, (-146.41377258343795, 67.02269744882824), 0.0, 0.0, 803.0, 'VEE', 'Airport', 'Venetie', 2274.0, ' ', 'Yukon-Koyukuk Census Area', '02290', '02')
# (144, (-176.64602661113918, 51.877964019623846), 0.0, 0.0, 804.0, 'ADK', 'Airport', 'Adak Naval Air Facility', 2698.0, ' ', 'Aleutians West Census Area', '02016', '02')
# (145, (-169.6637420652441, 56.57735443086233), 0.0, 0.0, 805.0, 'PBV', 'Airport', 'Saint George', 1007.0, 'AK', 'Aleutians West Census Area', '02016', '02')
# (146, (-170.22044372569735, 57.16733169590111), 0.0, 0.0, 806.0, 'SNP', 'Airport', 'Saint Paul Island', 4712.0, 'AK', 'Aleutians West Census Area', '02016', '02')
# (147, (-164.65621948284283, 60.92365264895062), 0.0, 0.0, 807.0, 'WWT', 'Seaplane Base', 'Newtok', 1683.0, 'AK', 'Bethel Census Area', '02050', '02')
# (148, (-164.03051757852342, 59.93295288107066), 0.0, 0.0, 808.0, 'IIK', 'Airport', 'Kipnuk', 4677.0, 'AK', 'Bethel Census Area', '02050', '02')
# (149, (-164.285629272373, 60.14922714191914), 0.0, 0.0, 809.0, 'CFK', 'Airport', 'Chefornak', 3049.0, 'AK', 'Bethel Census Area', '02050', '02')
# (150, (-164.68563842757135, 60.47032547034422), 0.0, 0.0, 810.0, 'IGT', 'Airport', 'Nightmute', 1537.0, 'AK', 'Bethel Census Area', '02050', '02')
# (151, (-165.11396789590165, 60.53337478601759), 0.0, 0.0, 811.0, 'OOK', 'Airport', 'Toksook Bay', 3938.0, 'AK', 'Bethel Census Area', '02050', '02')
# (152, (-165.27313232449714, 60.57559585526457), 0.0, 0.0, 812.0, '4KA', 'Airport', 'Tununak', 1826.0, 'AK', 'Bethel Census Area', '02050', '02')
# (153, (-162.27313232419738, 60.866744995085526), 0.0, 0.0, 813.0, '4A2', 'Airport', 'Atmautluak', 2065.0, 'AK', 'Bethel Census Area', '02050', '02')
# (154, (-162.4391174315242, 60.90582656884112), 0.0, 0.0, 814.0, '16A', 'Airport', 'Nunapitchuk', 2502.0, ' ', 'Bethel Census Area', '02050', '02')
# (155, (-162.52481079138488, 60.87202072127934), 0.0, 0.0, 815.0, 'Z09', 'Airport', 'Kasigluk', 2439.0, 'AK', 'Bethel Census Area', '02050', '02')
# (156, (-161.31947326617825, 61.77967453015549), 0.0, 0.0, 816.0, 'RSH', 'Airport', 'Russian Mission', 2470.0, ' ', 'Wade Hampton Census Area', '02270', '02')
# (157, (-162.06904602015769, 61.8659210207386), 0.0, 0.0, 817.0, 'MLL', 'Airport', 'Marshall', 2662.0, 'AK', 'Wade Hampton Census Area', '02270', '02')
# (158, (-162.8929290767155, 61.93396377530803), 0.0, 0.0, 818.0, '0AK', 'Airport', 'Pilot Station', 4703.0, 'AK', 'Wade Hampton Census Area', '02270', '02')
# (159, (-159.7749481197599, 62.18829727140201), 0.0, 0.0, 819.0, '4Z4', 'Airport', 'Holy Cross', 1510.0, ' ', 'Yukon-Koyukuk Census Area', '02290', '02')
# (160, (-159.56906127945444, 62.69511795003342), 0.0, 0.0, 820.0, 'SHX', 'Airport', 'Shageluk', 788.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (161, (-160.18989563017917, 62.64858245881345), 0.0, 0.0, 821.0, 'ANV', 'Airport', 'Anvik', 649.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (162, (-160.0649108883268, 62.89456176751162), 0.0, 0.0, 822.0, 'KGX', 'Airport', 'Grayling', 1095.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (163, (-156.9374237061391, 64.73617553717133), 0.0, 0.0, 823.0, 'GAL', 'Airport', 'Edward G. Pitka Sr.', 10027.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (164, (-155.4698944087999, 64.72721862773756), 0.0, 0.0, 824.0, 'RBY', 'Airport', 'Ruby', 1941.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (165, (-151.5280609128808, 66.9152832033572), 0.0, 0.0, 825.0, 'BTT', 'Airport', 'Bettles', 3900.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (166, (-152.62222290046645, 66.55194091793908), 0.0, 0.0, 826.0, '6A8', 'Airport', 'New Allakaket', 1901.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (167, (-150.64379882835323, 66.81288146960418), 0.0, 0.0, 827.0, 'PPC', 'Airport', 'Prospect Creek', 2419.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (168, (-150.20657348667703, 67.25163269009664), 0.0, 0.0, 828.0, 'CXF', 'Airport', 'Coldfoot', 631.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (169, (-145.57611084024305, 68.11608123775898), 0.0, 0.0, 829.0, 'ARC', 'Airport', 'Arctic Village', 2296.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (170, (-166.27061462366592, 60.371421814265375), 0.0, 0.0, 830.0, 'MYU', 'Airport', 'Mekoryuk', 1954.0, ' ', 'Bethel Census Area', '02050', '02')
# (171, (-166.14677429160025, 61.524181366377036), 0.0, 0.0, 831.0, 'HPB', 'Airport', 'Hooper Bay', 5319.0, ' ', 'Wade Hampton Census Area', '02270', '02')
# (172, (-163.68205261223824, 62.09536361723718), 0.0, 0.0, 832.0, 'MOU', 'Airport', 'Mountain Village', 5523.0, 'AK', 'Wade Hampton Census Area', '02270', '02')
# (173, (-165.5837249760268, 61.53363418536941), 0.0, 0.0, 833.0, 'VAK', 'Airport', 'Chevak', 4404.0, 'AK', 'Wade Hampton Census Area', '02270', '02')
# (174, (-165.57374572718354, 61.84453964269039), 0.0, 0.0, 834.0, 'SCM', 'Airport', 'Scammon Bay', 2864.0, 'AK', 'Wade Hampton Census Area', '02270', '02')
# (175, (-163.30210876450784, 62.06048583984966), 0.0, 0.0, 835.0, 'KSM', 'Airport', "Saint Mary's", 8281.0, 'AK', 'Wade Hampton Census Area', '02270', '02')
# (176, (-164.8477783207129, 62.52055740320168), 0.0, 0.0, 836.0, 'SXP', 'Airport', 'Sheldon Point', 1376.0, 'AK', 'Wade Hampton Census Area', '02270', '02')
# (177, (-162.11036682127175, 63.49005126965045), 0.0, 0.0, 837.0, '5S8', 'Airport', 'Saint Michael', 2123.0, ' ', 'Nome Census Area', '02180', '02')
# (178, (-162.28274536100957, 63.51591873136442), 0.0, 0.0, 838.0, 'WBB', 'Airport', 'Stebbins', 2407.0, 'AK', 'Nome Census Area', '02180', '02')
# (179, (-160.79895019489555, 63.88835906941557), 0.0, 0.0, 839.0, 'UNK', 'Airport', 'Unalakleet', 8467.0, ' ', 'Nome Census Area', '02180', '02')
# (180, (-161.2025299068297, 64.36263275170018), 0.0, 0.0, 840.0, '38A', 'Airport', 'Shaktoolik', 1756.0, 'AK', 'Nome Census Area', '02180', '02')
# (181, (-158.74414062469006, 64.32572174116547), 0.0, 0.0, 841.0, 'KAL', 'Airport', 'Kaltag', 2192.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (182, (-158.07319641108546, 64.72982025130364), 0.0, 0.0, 842.0, 'NUL', 'Airport', 'Nulato', 3529.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (183, (-156.3874969480257, 65.7005538943468), 0.0, 0.0, 843.0, 'HSL', 'Airport', 'Huslia', 3443.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (184, (-154.2631835936479, 66.0411224362515), 0.0, 0.0, 844.0, 'HUS', 'Airport', 'Hughes', 1095.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
# (185, (-151.74168395974692, 68.1343231203158), 0.0, 0.0, 845.0, 'AKP', 'Airport', 'Anaktuvuk Pass', 3653.0, 'AK', 'North Slope Borough', '02185', '02')
# (186, (-149.49002075175625, 68.4790649409943), 0.0, 0.0, 846.0, 'GBH', 'Airport', 'Galbraith Lake', 1200.0, 'AK', 'North Slope Borough', '02185', '02')
# (187, (-143.57704162636992, 70.133903503444), 0.0, 0.0, 847.0, 'BTI', 'Airport', 'Barter Island LRRS', 2055.0, 'AK', 'North Slope Borough', '02185', '02')
# (188, (-164.65992736785373, 62.68004608146157), 0.0, 0.0, 848.0, 'AUK', 'Airport', 'Alakanuk', 3735.0, 'AK', 'Wade Hampton Census Area', '02270', '02')
# (189, (-164.49104309086593, 62.785186767955054), 0.0, 0.0, 849.0, 'ENM', 'Airport', 'Emmonak', 6780.0, 'AK', 'Wade Hampton Census Area', '02270', '02')
# (190, (-162.2700653077677, 64.61400604204528), 0.0, 0.0, 850.0, 'ELI', 'Airport', 'Elim', 2827.0, 'AK', 'Nome Census Area', '02180', '02')
# (191, (-163.03952026364922, 64.54343414297136), 0.0, 0.0, 851.0, 'GLV', 'Airport', 'Golovin', 1562.0, 'AK', 'Nome Census Area', '02180', '02')
# (192, (-163.41255187986533, 64.68919372590977), 0.0, 0.0, 852.0, 'WMO', 'Airport', 'White Mountain', 1790.0, 'AK', 'Nome Census Area', '02180', '02')
# (193, (-161.1519775388323, 65.98228454589514), 0.0, 0.0, 853.0, 'BVK', 'Airport', 'Buckland', 3153.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (194, (-159.98619079606834, 66.60002899154478), 0.0, 0.0, 854.0, 'WLK', 'Airport', 'Selawik', 5176.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (195, (-156.861053466844, 66.90917205824394), 0.0, 0.0, 855.0, 'OBU', 'Airport', 'Kobuk', 992.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (196, (-157.15051269510477, 66.88916778596462), 0.0, 0.0, 856.0, 'SHG', 'Airport', 'Shungnak', 2309.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (197, (-157.8536224369259, 67.1061019900149), 0.0, 0.0, 857.0, 'AFM', 'Airport', 'Ambler', 2423.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (198, (-148.4651641848792, 70.1947555541256), 0.0, 0.0, 858.0, 'SCC', 'Airport', 'Deadhorse', 12479.0, 'AK', 'North Slope Borough', '02185', '02')
# (199, (-165.4452514646833, 64.51219940228066), 0.0, 0.0, 859.0, 'OME', 'Airport', 'Nome', 56911.0, 'AK', 'Nome Census Area', '02180', '02')
# (200, (-162.76660156251208, 66.06820678681379), 0.0, 0.0, 860.0, 'DEE', 'Airport', 'Deering', 1473.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (201, (-160.43586730992837, 66.97937774618612), 0.0, 0.0, 861.0, 'IAN', 'Airport', 'Bob Baker Memorial', 3899.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (202, (-161.0277862553314, 66.82852935754386), 0.0, 0.0, 862.0, 'ORV', 'Airport', 'Robert (Bob) Curtis Memorial', 5266.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (203, (-162.5985565184685, 66.88467407245054), 0.0, 0.0, 863.0, 'OTZ', 'Airport', 'Ralph Wien Memorial', 59351.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (204, (-151.00555419886715, 70.20995330799883), 0.0, 0.0, 864.0, 'AQT', 'Airport', 'Nuiqsut', 1018.0, 'AK', 'North Slope Borough', '02185', '02')
# (205, (-170.49263000457103, 63.68639373818053), 0.0, 0.0, 865.0, 'SVA', 'Airport', 'Savoonga', 4271.0, 'AK', 'Nome Census Area', '02180', '02')
# (206, (-166.3360137941013, 65.24089813254284), 0.0, 0.0, 866.0, 'K54', 'Airport', 'Teller', 983.0, 'AK', 'Nome Census Area', '02180', '02')
# (207, (-166.46316528335112, 65.33135986336708), 0.0, 0.0, 867.0, 'KTS', 'Airport', 'Brevig Mission', 1463.0, 'AK', 'Nome Census Area', '02180', '02')
# (208, (-166.08955383284308, 66.24956512463086), 0.0, 0.0, 868.0, 'SHH', 'Airport', 'Shishmaref', 3866.0, 'AK', 'Nome Census Area', '02180', '02')
# (209, (-168.0991668701549, 65.6239395142972), 0.0, 0.0, 869.0, 'IWK', 'Airport', 'Wales', 1542.0, 'AK', 'Nome Census Area', '02180', '02')
# (210, (-162.97528076179768, 67.56208038350297), 0.0, 0.0, 870.0, 'WTK', 'Airport', 'Noatak', 4124.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (211, (-162.90295410195023, 68.03128814693048), 0.0, 0.0, 871.0, 'AED', 'Airport', 'Red Dog', 9316.0, 'AK', 'Northwest Arctic Borough', '02188', '02')
# (212, (-157.4357299804542, 70.46727752653669), 0.0, 0.0, 872.0, 'ATK', 'Airport', 'Atqasuk Edward Burnell Sr. Memorial', 2686.0, 'AK', 'North Slope Borough', '02185', '02')
# (213, (-171.73281860359566, 63.7667655945566), 0.0, 0.0, 874.0, 'GAM', 'Airport', 'Gambell', 4098.0, 'AK', 'Nome Census Area', '02180', '02')
# (214, (-166.79930114782968, 68.34877777117725), 0.0, 0.0, 875.0, 'PHO', 'Airport', 'Point Hope', 5533.0, 'AK', 'North Slope Borough', '02185', '02')
# (215, (-163.00534057600674, 69.73287200883618), 0.0, 0.0, 876.0, 'PIZ', 'Airport', 'Point Lay LRRS', 1962.0, 'AK', 'North Slope Borough', '02185', '02')
# (216, (-159.99475097677612, 70.63800048813209), 0.0, 0.0, 877.0, 'AWI', 'Airport', 'Wainwright', 3783.0, 'AK', 'North Slope Borough', '02185', '02')
# (217, (-156.76600646972278, 71.28544616670729), 0.0, 0.0, 878.0, 'BRW', 'Airport', 'Wiley Post-Will Rogers Memorial', 40751.0, 'AK', 'North Slope Borough', '02185', '02')
# (218, (-157.32719421384186, 59.44955444348284), 0.0, 0.0, 880.0, 'KNW', 'Airport', 'New Stuyahok', 2217.0, 'AK', 'Dillingham Census Area', '02070', '02')
# (219, (-149.9961853030093, 61.17432022060177), 0.0, 0.0, 881.0, 'ANC', 'Airport', 'Ted Stevens Anchorage International', 2536319.0, 'AK', 'Anchorage Borough', '02020', '02')
# (220, (-154.91096496576054, 59.753799438093665), 0.0, 0.0, 900.0, 'ILI', 'Airport', 'Iliamna', 13806.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (221, (-157.71583557145442, 64.87714385960152), 0.0, 0.0, 901.0, 'KYU', 'Airport', 'Koyukuk', 994.0, 'AK', 'Yukon-Koyukuk Census Area', '02290', '02')
cursor = arcpy.da.SearchCursor(fc,['NAME'])
for row in cursor:
#   File "<string>", line 1
#     for row in cursor:
#                      ^
# SyntaxError: unexpected EOF while parsing
for row in cursor:
    print('Airport name = ' + row[0] )
# Airport name = Hyder
# Airport name = Chignik Lagoon
# Airport name = Koyuk
# Airport name = Kivalina
# Airport name = Ketchikan Harbor
# Airport name = Metlakatla
# Airport name = Waterfall
# Airport name = Ketchikan
# Airport name = Kasaan
# Airport name = Hollis
# Airport name = Craig
# Airport name = Thorne Bay
# Airport name = Coffman Cove
# Airport name = Meyers Chuck
# Airport name = Klawock
# Airport name = Yes Bay Lodge
# Airport name = Wrangell
# Airport name = Petersburg James A. Johnson
# Airport name = Kake
# Airport name = Sitka Rocky Gutierrez
# Airport name = Angoon
# Airport name = Funter Bay
# Airport name = Tenakee
# Airport name = Hawk Inlet
# Airport name = Hoonah
# Airport name = Juneau International
# Airport name = Pelican
# Airport name = Elfin Cove
# Airport name = Excursion Inlet
# Airport name = Gustavus
# Airport name = Haines
# Airport name = Skagway
# Airport name = Yakutat
# Airport name = Icy Bay
# Airport name = Alitak
# Airport name = Akhiok
# Airport name = San Juan/Uganik Bay
# Airport name = Old Harbor
# Airport name = Larsen Bay
# Airport name = Trident Basin
# Airport name = Kodiak
# Airport name = Ouzinkie
# Airport name = Port Lions
# Airport name = Merle K. (Mudhole) Smith
# Airport name = Sand Point
# Airport name = Ivanof Bay
# Airport name = Perryville
# Airport name = Chignik Fisheries
# Airport name = Chignik Lake
# Airport name = Chignik
# Airport name = Karluk
# Airport name = Port Graham
# Airport name = Seldovia
# Airport name = English Bay
# Airport name = Homer
# Airport name = Seward
# Airport name = Girdwood
# Airport name = Valdez
# Airport name = Chitina
# Airport name = Gulkana
# Airport name = Tetlin
# Airport name = King Cove
# Airport name = Cold Bay
# Airport name = False Pass
# Airport name = Port Heiden
# Airport name = Pilot Point
# Airport name = Egegik
# Airport name = Lake Brooks
# Airport name = Levelock
# Airport name = King Salmon
# Airport name = South Naknek Nr 2
# Airport name = Tibbetts
# Airport name = Kulik Lake
# Airport name = Kokhanok
# Airport name = Pedro Bay
# Airport name = Igiugig
# Airport name = Nondalton
# Airport name = Port Alsworth
# Airport name = Soldotna
# Airport name = Kenai Municipal
# Airport name = Tyonek
# Airport name = Trading Bay Production
# Airport name = Beluga
# Airport name = Merrill Field
# Airport name = Lake Hood
# Airport name = Elmendorf Air Force Base
# Airport name = Palmer Municipal
# Airport name = Willow
# Airport name = Skelton
# Airport name = Tok
# Airport name = Eagle
# Airport name = Akutan
# Airport name = Unalaska
# Airport name = Ekuk
# Airport name = Clarks Point
# Airport name = Manokotak
# Airport name = Ekwok
# Airport name = Dillingham
# Airport name = Koliganek
# Airport name = Skwentna
# Airport name = Talkeetna
# Airport name = McKinley National Park
# Airport name = Platinum
# Airport name = Goodnews
# Airport name = Twin Hills
# Airport name = Togiak
# Airport name = Stony River 2
# Airport name = Sleetmute
# Airport name = Nikolai
# Airport name = Kantishna
# Airport name = Minchumina
# Airport name = Healy River
# Airport name = Eielson Air Force Base
# Airport name = Wainwright Army Air Field
# Airport name = Fairbanks International
# Airport name = Circle City
# Airport name = Chalkyitsik
# Airport name = Atka
# Airport name = Quinhagak
# Airport name = Eek
# Airport name = Kongiganak
# Airport name = Kwigillingok
# Airport name = Tuntutuliak
# Airport name = Akiak
# Airport name = Kwethluk
# Airport name = Tuluksak
# Airport name = Napaskiak
# Airport name = Akiachak
# Airport name = Napakiak
# Airport name = Bethel
# Airport name = Aniak
# Airport name = Kalskag
# Airport name = Red Devil
# Airport name = Crooked Creek
# Airport name = McGrath
# Airport name = Ralph M. Calhoun Memorial
# Airport name = Minto
# Airport name = Rampart
# Airport name = Stevens Village
# Airport name = Beaver
# Airport name = Birch Creek
# Airport name = Fort Yukon
# Airport name = Venetie
# Airport name = Adak Naval Air Facility
# Airport name = Saint George
# Airport name = Saint Paul Island
# Airport name = Newtok
# Airport name = Kipnuk
# Airport name = Chefornak
# Airport name = Nightmute
# Airport name = Toksook Bay
# Airport name = Tununak
# Airport name = Atmautluak
# Airport name = Nunapitchuk
# Airport name = Kasigluk
# Airport name = Russian Mission
# Airport name = Marshall
# Airport name = Pilot Station
# Airport name = Holy Cross
# Airport name = Shageluk
# Airport name = Anvik
# Airport name = Grayling
# Airport name = Edward G. Pitka Sr.
# Airport name = Ruby
# Airport name = Bettles
# Airport name = New Allakaket
# Airport name = Prospect Creek
# Airport name = Coldfoot
# Airport name = Arctic Village
# Airport name = Mekoryuk
# Airport name = Hooper Bay
# Airport name = Mountain Village
# Airport name = Chevak
# Airport name = Scammon Bay
# Airport name = Saint Mary's
# Airport name = Sheldon Point
# Airport name = Saint Michael
# Airport name = Stebbins
# Airport name = Unalakleet
# Airport name = Shaktoolik
# Airport name = Kaltag
# Airport name = Nulato
# Airport name = Huslia
# Airport name = Hughes
# Airport name = Anaktuvuk Pass
# Airport name = Galbraith Lake
# Airport name = Barter Island LRRS
# Airport name = Alakanuk
# Airport name = Emmonak
# Airport name = Elim
# Airport name = Golovin
# Airport name = White Mountain
# Airport name = Buckland
# Airport name = Selawik
# Airport name = Kobuk
# Airport name = Shungnak
# Airport name = Ambler
# Airport name = Deadhorse
# Airport name = Nome
# Airport name = Deering
# Airport name = Bob Baker Memorial
# Airport name = Robert (Bob) Curtis Memorial
# Airport name = Ralph Wien Memorial
# Airport name = Nuiqsut
# Airport name = Savoonga
# Airport name = Teller
# Airport name = Brevig Mission
# Airport name = Shishmaref
# Airport name = Wales
# Airport name = Noatak
# Airport name = Red Dog
# Airport name = Atqasuk Edward Burnell Sr. Memorial
# Airport name = Gambell
# Airport name = Point Hope
# Airport name = Point Lay LRRS
# Airport name = Wainwright
# Airport name = Wiley Post-Will Rogers Memorial
# Airport name = New Stuyahok
# Airport name = Ted Stevens Anchorage International
# Airport name = Iliamna
# Airport name = Koyukuk
cursor = arcpy.da.SearchCursor(fc,['NAME','TOT_ENP'])
for row in cursor:
    print('Airport name = ' + row[0] )
# Airport name = Hyder
# Airport name = Chignik Lagoon
# Airport name = Koyuk
# Airport name = Kivalina
# Airport name = Ketchikan Harbor
# Airport name = Metlakatla
# Airport name = Waterfall
# Airport name = Ketchikan
# Airport name = Kasaan
# Airport name = Hollis
# Airport name = Craig
# Airport name = Thorne Bay
# Airport name = Coffman Cove
# Airport name = Meyers Chuck
# Airport name = Klawock
# Airport name = Yes Bay Lodge
# Airport name = Wrangell
# Airport name = Petersburg James A. Johnson
# Airport name = Kake
# Airport name = Sitka Rocky Gutierrez
# Airport name = Angoon
# Airport name = Funter Bay
# Airport name = Tenakee
# Airport name = Hawk Inlet
# Airport name = Hoonah
# Airport name = Juneau International
# Airport name = Pelican
# Airport name = Elfin Cove
# Airport name = Excursion Inlet
# Airport name = Gustavus
# Airport name = Haines
# Airport name = Skagway
# Airport name = Yakutat
# Airport name = Icy Bay
# Airport name = Alitak
# Airport name = Akhiok
# Airport name = San Juan/Uganik Bay
# Airport name = Old Harbor
# Airport name = Larsen Bay
# Airport name = Trident Basin
# Airport name = Kodiak
# Airport name = Ouzinkie
# Airport name = Port Lions
# Airport name = Merle K. (Mudhole) Smith
# Airport name = Sand Point
# Airport name = Ivanof Bay
# Airport name = Perryville
# Airport name = Chignik Fisheries
# Airport name = Chignik Lake
# Airport name = Chignik
# Airport name = Karluk
# Airport name = Port Graham
# Airport name = Seldovia
# Airport name = English Bay
# Airport name = Homer
# Airport name = Seward
# Airport name = Girdwood
# Airport name = Valdez
# Airport name = Chitina
# Airport name = Gulkana
# Airport name = Tetlin
# Airport name = King Cove
# Airport name = Cold Bay
# Airport name = False Pass
# Airport name = Port Heiden
# Airport name = Pilot Point
# Airport name = Egegik
# Airport name = Lake Brooks
# Airport name = Levelock
# Airport name = King Salmon
# Airport name = South Naknek Nr 2
# Airport name = Tibbetts
# Airport name = Kulik Lake
# Airport name = Kokhanok
# Airport name = Pedro Bay
# Airport name = Igiugig
# Airport name = Nondalton
# Airport name = Port Alsworth
# Airport name = Soldotna
# Airport name = Kenai Municipal
# Airport name = Tyonek
# Airport name = Trading Bay Production
# Airport name = Beluga
# Airport name = Merrill Field
# Airport name = Lake Hood
# Airport name = Elmendorf Air Force Base
# Airport name = Palmer Municipal
# Airport name = Willow
# Airport name = Skelton
# Airport name = Tok
# Airport name = Eagle
# Airport name = Akutan
# Airport name = Unalaska
# Airport name = Ekuk
# Airport name = Clarks Point
# Airport name = Manokotak
# Airport name = Ekwok
# Airport name = Dillingham
# Airport name = Koliganek
# Airport name = Skwentna
# Airport name = Talkeetna
# Airport name = McKinley National Park
# Airport name = Platinum
# Airport name = Goodnews
# Airport name = Twin Hills
# Airport name = Togiak
# Airport name = Stony River 2
# Airport name = Sleetmute
# Airport name = Nikolai
# Airport name = Kantishna
# Airport name = Minchumina
# Airport name = Healy River
# Airport name = Eielson Air Force Base
# Airport name = Wainwright Army Air Field
# Airport name = Fairbanks International
# Airport name = Circle City
# Airport name = Chalkyitsik
# Airport name = Atka
# Airport name = Quinhagak
# Airport name = Eek
# Airport name = Kongiganak
# Airport name = Kwigillingok
# Airport name = Tuntutuliak
# Airport name = Akiak
# Airport name = Kwethluk
# Airport name = Tuluksak
# Airport name = Napaskiak
# Airport name = Akiachak
# Airport name = Napakiak
# Airport name = Bethel
# Airport name = Aniak
# Airport name = Kalskag
# Airport name = Red Devil
# Airport name = Crooked Creek
# Airport name = McGrath
# Airport name = Ralph M. Calhoun Memorial
# Airport name = Minto
# Airport name = Rampart
# Airport name = Stevens Village
# Airport name = Beaver
# Airport name = Birch Creek
# Airport name = Fort Yukon
# Airport name = Venetie
# Airport name = Adak Naval Air Facility
# Airport name = Saint George
# Airport name = Saint Paul Island
# Airport name = Newtok
# Airport name = Kipnuk
# Airport name = Chefornak
# Airport name = Nightmute
# Airport name = Toksook Bay
# Airport name = Tununak
# Airport name = Atmautluak
# Airport name = Nunapitchuk
# Airport name = Kasigluk
# Airport name = Russian Mission
# Airport name = Marshall
# Airport name = Pilot Station
# Airport name = Holy Cross
# Airport name = Shageluk
# Airport name = Anvik
# Airport name = Grayling
# Airport name = Edward G. Pitka Sr.
# Airport name = Ruby
# Airport name = Bettles
# Airport name = New Allakaket
# Airport name = Prospect Creek
# Airport name = Coldfoot
# Airport name = Arctic Village
# Airport name = Mekoryuk
# Airport name = Hooper Bay
# Airport name = Mountain Village
# Airport name = Chevak
# Airport name = Scammon Bay
# Airport name = Saint Mary's
# Airport name = Sheldon Point
# Airport name = Saint Michael
# Airport name = Stebbins
# Airport name = Unalakleet
# Airport name = Shaktoolik
# Airport name = Kaltag
# Airport name = Nulato
# Airport name = Huslia
# Airport name = Hughes
# Airport name = Anaktuvuk Pass
# Airport name = Galbraith Lake
# Airport name = Barter Island LRRS
# Airport name = Alakanuk
# Airport name = Emmonak
# Airport name = Elim
# Airport name = Golovin
# Airport name = White Mountain
# Airport name = Buckland
# Airport name = Selawik
# Airport name = Kobuk
# Airport name = Shungnak
# Airport name = Ambler
# Airport name = Deadhorse
# Airport name = Nome
# Airport name = Deering
# Airport name = Bob Baker Memorial
# Airport name = Robert (Bob) Curtis Memorial
# Airport name = Ralph Wien Memorial
# Airport name = Nuiqsut
# Airport name = Savoonga
# Airport name = Teller
# Airport name = Brevig Mission
# Airport name = Shishmaref
# Airport name = Wales
# Airport name = Noatak
# Airport name = Red Dog
# Airport name = Atqasuk Edward Burnell Sr. Memorial
# Airport name = Gambell
# Airport name = Point Hope
# Airport name = Point Lay LRRS
# Airport name = Wainwright
# Airport name = Wiley Post-Will Rogers Memorial
# Airport name = New Stuyahok
# Airport name = Ted Stevens Anchorage International
# Airport name = Iliamna
# Airport name = Koyukuk
for row in cursor:
    print('Airport name = ' + row[0], row[1] )
for row in cursor:
    print('Airport name = ' + row[0] + row[1])
for row in cursor:
    print('Airport name = ' + row)
cursor = arcpy.da.SearchCursor(fc,['NAME'],['TOT_ENP'])
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# TypeError: 'where_clause' is not a string
cursor = arcpy.da.SearchCursor(fc,'NAME','TOT_ENP')
for row in cursor:
    print('Airport name = ' + row[0] + row[1])
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# RuntimeError: An invalid SQL statement was used. [SELECT NAME, OBJECTID FROM airports WHERE TOT_ENP]
cursor = arcpy.da.SearchCursor(fc,['NAME','TOT_ENP'])
for row in cursor:
    print('Airport name = ' + row[0] + row[1])
# Traceback (most recent call last):
#   File "<string>", line 2, in <module>
# TypeError: must be str, not float
cursor = arcpy.da.SearchCursor(fc,['NAME',TOT_ENP])
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# NameError: name 'TOT_ENP' is not defined
cursor = arcpy.da.SearchCursor(fc,['NAME','TOT_ENP'])
for row in cursor:
    print('Airport name = ' + row[0] + float(row[1])
#   File "<string>", line 2
#     print('Airport name = ' + row[0] + float(row[1])
#                                                    ^
# SyntaxError: unexpected EOF while parsing
for row in cursor:
    print('Airport name = ' + row[0] + float(row[1]))
# Traceback (most recent call last):
#   File "<string>", line 2, in <module>
# TypeError: must be str, not float
cursor = arcpy.da.SearchCursor(fc,['*'])
for row in cursor:
    print('Airport name = ' + row[11])
# Airport name = 02201
# Airport name = 02164
# Airport name = 02180
# Airport name = 02188
# Airport name = 02130
# Airport name = 02201
# Airport name = 02201
# Airport name = 02130
# Airport name = 02201
# Airport name = 02201
# Airport name = 02201
# Airport name = 02201
# Airport name = 02201
# Airport name = 02201
# Airport name = 02201
# Airport name = 02201
# Airport name = 02280
# Airport name = 02280
# Airport name = 02280
# Airport name = 02220
# Airport name = 02232
# Airport name = 02232
# Airport name = 02232
# Airport name = 02232
# Airport name = 02232
# Airport name = 02110
# Airport name = 02232
# Airport name = 02232
# Airport name = 02232
# Airport name = 02232
# Airport name = 02100
# Airport name = 02232
# Airport name = 02282
# Airport name = 02261
# Airport name = 02150
# Airport name = 02150
# Airport name = 02150
# Airport name = 02150
# Airport name = 02150
# Airport name = 02150
# Airport name = 02150
# Airport name = 02150
# Airport name = 02150
# Airport name = 02261
# Airport name = 02013
# Airport name = 02164
# Airport name = 02164
# Airport name = 02164
# Airport name = 02164
# Airport name = 02164
# Airport name = 02150
# Airport name = 02122
# Airport name = 02122
# Airport name = 02122
# Airport name = 02122
# Airport name = 02122
# Airport name = 02020
# Airport name = 02261
# Airport name = 02261
# Airport name = 02261
# Airport name = 02240
# Airport name = 02013
# Airport name = 02013
# Airport name = 02013
# Airport name = 02164
# Airport name = 02164
# Airport name = 02164
# Airport name = 02164
# Airport name = 02164
# Airport name = 02060
# Airport name = 02060
# Airport name = 02060
# Airport name = 02164
# Airport name = 02164
# Airport name = 02164
# Airport name = 02164
# Airport name = 02164
# Airport name = 02164
# Airport name = 02122
# Airport name = 02122
# Airport name = 02122
# Airport name = 02122
# Airport name = 02122
# Airport name = 02020
# Airport name = 02020
# Airport name = 02020
# Airport name = 02170
# Airport name = 02170
# Airport name = 02170
# Airport name = 02240
# Airport name = 02240
# Airport name = 02013
# Airport name = 02016
# Airport name = 02070
# Airport name = 02070
# Airport name = 02070
# Airport name = 02070
# Airport name = 02070
# Airport name = 02070
# Airport name = 02170
# Airport name = 02170
# Airport name = 02068
# Airport name = 02050
# Airport name = 02050
# Airport name = 02070
# Airport name = 02070
# Airport name = 02050
# Airport name = 02050
# Airport name = 02290
# Airport name = 02068
# Airport name = 02290
# Airport name = 02068
# Airport name = 02090
# Airport name = 02090
# Airport name = 02090
# Airport name = 02290
# Airport name = 02290
# Airport name = 02016
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02016
# Airport name = 02016
# Airport name = 02016
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02050
# Airport name = 02270
# Airport name = 02270
# Airport name = 02270
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02050
# Airport name = 02270
# Airport name = 02270
# Airport name = 02270
# Airport name = 02270
# Airport name = 02270
# Airport name = 02270
# Airport name = 02180
# Airport name = 02180
# Airport name = 02180
# Airport name = 02180
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02290
# Airport name = 02185
# Airport name = 02185
# Airport name = 02185
# Airport name = 02270
# Airport name = 02270
# Airport name = 02180
# Airport name = 02180
# Airport name = 02180
# Airport name = 02188
# Airport name = 02188
# Airport name = 02188
# Airport name = 02188
# Airport name = 02188
# Airport name = 02185
# Airport name = 02180
# Airport name = 02188
# Airport name = 02188
# Airport name = 02188
# Airport name = 02188
# Airport name = 02185
# Airport name = 02180
# Airport name = 02180
# Airport name = 02180
# Airport name = 02180
# Airport name = 02180
# Airport name = 02188
# Airport name = 02188
# Airport name = 02185
# Airport name = 02180
# Airport name = 02185
# Airport name = 02185
# Airport name = 02185
# Airport name = 02185
# Airport name = 02070
# Airport name = 02020
# Airport name = 02164
# Airport name = 02290
cursor = arcpy.da.SearchCursor(fc,['NAME'])
for row in cursor:
    print('Airport name = ' + row[0])
# Airport name = Hyder
# Airport name = Chignik Lagoon
# Airport name = Koyuk
# Airport name = Kivalina
# Airport name = Ketchikan Harbor
# Airport name = Metlakatla
# Airport name = Waterfall
# Airport name = Ketchikan
# Airport name = Kasaan
# Airport name = Hollis
# Airport name = Craig
# Airport name = Thorne Bay
# Airport name = Coffman Cove
# Airport name = Meyers Chuck
# Airport name = Klawock
# Airport name = Yes Bay Lodge
# Airport name = Wrangell
# Airport name = Petersburg James A. Johnson
# Airport name = Kake
# Airport name = Sitka Rocky Gutierrez
# Airport name = Angoon
# Airport name = Funter Bay
# Airport name = Tenakee
# Airport name = Hawk Inlet
# Airport name = Hoonah
# Airport name = Juneau International
# Airport name = Pelican
# Airport name = Elfin Cove
# Airport name = Excursion Inlet
# Airport name = Gustavus
# Airport name = Haines
# Airport name = Skagway
# Airport name = Yakutat
# Airport name = Icy Bay
# Airport name = Alitak
# Airport name = Akhiok
# Airport name = San Juan/Uganik Bay
# Airport name = Old Harbor
# Airport name = Larsen Bay
# Airport name = Trident Basin
# Airport name = Kodiak
# Airport name = Ouzinkie
# Airport name = Port Lions
# Airport name = Merle K. (Mudhole) Smith
# Airport name = Sand Point
# Airport name = Ivanof Bay
# Airport name = Perryville
# Airport name = Chignik Fisheries
# Airport name = Chignik Lake
# Airport name = Chignik
# Airport name = Karluk
# Airport name = Port Graham
# Airport name = Seldovia
# Airport name = English Bay
# Airport name = Homer
# Airport name = Seward
# Airport name = Girdwood
# Airport name = Valdez
# Airport name = Chitina
# Airport name = Gulkana
# Airport name = Tetlin
# Airport name = King Cove
# Airport name = Cold Bay
# Airport name = False Pass
# Airport name = Port Heiden
# Airport name = Pilot Point
# Airport name = Egegik
# Airport name = Lake Brooks
# Airport name = Levelock
# Airport name = King Salmon
# Airport name = South Naknek Nr 2
# Airport name = Tibbetts
# Airport name = Kulik Lake
# Airport name = Kokhanok
# Airport name = Pedro Bay
# Airport name = Igiugig
# Airport name = Nondalton
# Airport name = Port Alsworth
# Airport name = Soldotna
# Airport name = Kenai Municipal
# Airport name = Tyonek
# Airport name = Trading Bay Production
# Airport name = Beluga
# Airport name = Merrill Field
# Airport name = Lake Hood
# Airport name = Elmendorf Air Force Base
# Airport name = Palmer Municipal
# Airport name = Willow
# Airport name = Skelton
# Airport name = Tok
# Airport name = Eagle
# Airport name = Akutan
# Airport name = Unalaska
# Airport name = Ekuk
# Airport name = Clarks Point
# Airport name = Manokotak
# Airport name = Ekwok
# Airport name = Dillingham
# Airport name = Koliganek
# Airport name = Skwentna
# Airport name = Talkeetna
# Airport name = McKinley National Park
# Airport name = Platinum
# Airport name = Goodnews
# Airport name = Twin Hills
# Airport name = Togiak
# Airport name = Stony River 2
# Airport name = Sleetmute
# Airport name = Nikolai
# Airport name = Kantishna
# Airport name = Minchumina
# Airport name = Healy River
# Airport name = Eielson Air Force Base
# Airport name = Wainwright Army Air Field
# Airport name = Fairbanks International
# Airport name = Circle City
# Airport name = Chalkyitsik
# Airport name = Atka
# Airport name = Quinhagak
# Airport name = Eek
# Airport name = Kongiganak
# Airport name = Kwigillingok
# Airport name = Tuntutuliak
# Airport name = Akiak
# Airport name = Kwethluk
# Airport name = Tuluksak
# Airport name = Napaskiak
# Airport name = Akiachak
# Airport name = Napakiak
# Airport name = Bethel
# Airport name = Aniak
# Airport name = Kalskag
# Airport name = Red Devil
# Airport name = Crooked Creek
# Airport name = McGrath
# Airport name = Ralph M. Calhoun Memorial
# Airport name = Minto
# Airport name = Rampart
# Airport name = Stevens Village
# Airport name = Beaver
# Airport name = Birch Creek
# Airport name = Fort Yukon
# Airport name = Venetie
# Airport name = Adak Naval Air Facility
# Airport name = Saint George
# Airport name = Saint Paul Island
# Airport name = Newtok
# Airport name = Kipnuk
# Airport name = Chefornak
# Airport name = Nightmute
# Airport name = Toksook Bay
# Airport name = Tununak
# Airport name = Atmautluak
# Airport name = Nunapitchuk
# Airport name = Kasigluk
# Airport name = Russian Mission
# Airport name = Marshall
# Airport name = Pilot Station
# Airport name = Holy Cross
# Airport name = Shageluk
# Airport name = Anvik
# Airport name = Grayling
# Airport name = Edward G. Pitka Sr.
# Airport name = Ruby
# Airport name = Bettles
# Airport name = New Allakaket
# Airport name = Prospect Creek
# Airport name = Coldfoot
# Airport name = Arctic Village
# Airport name = Mekoryuk
# Airport name = Hooper Bay
# Airport name = Mountain Village
# Airport name = Chevak
# Airport name = Scammon Bay
# Airport name = Saint Mary's
# Airport name = Sheldon Point
# Airport name = Saint Michael
# Airport name = Stebbins
# Airport name = Unalakleet
# Airport name = Shaktoolik
# Airport name = Kaltag
# Airport name = Nulato
# Airport name = Huslia
# Airport name = Hughes
# Airport name = Anaktuvuk Pass
# Airport name = Galbraith Lake
# Airport name = Barter Island LRRS
# Airport name = Alakanuk
# Airport name = Emmonak
# Airport name = Elim
# Airport name = Golovin
# Airport name = White Mountain
# Airport name = Buckland
# Airport name = Selawik
# Airport name = Kobuk
# Airport name = Shungnak
# Airport name = Ambler
# Airport name = Deadhorse
# Airport name = Nome
# Airport name = Deering
# Airport name = Bob Baker Memorial
# Airport name = Robert (Bob) Curtis Memorial
# Airport name = Ralph Wien Memorial
# Airport name = Nuiqsut
# Airport name = Savoonga
# Airport name = Teller
# Airport name = Brevig Mission
# Airport name = Shishmaref
# Airport name = Wales
# Airport name = Noatak
# Airport name = Red Dog
# Airport name = Atqasuk Edward Burnell Sr. Memorial
# Airport name = Gambell
# Airport name = Point Hope
# Airport name = Point Lay LRRS
# Airport name = Wainwright
# Airport name = Wiley Post-Will Rogers Memorial
# Airport name = New Stuyahok
# Airport name = Ted Stevens Anchorage International
# Airport name = Iliamna
# Airport name = Koyukuk
for row in cursor:
    print('Airport name = ' + row[0], row[11])
cursor = arcpy.da.SearchCursor(fc,['NAME']['TOT_ENP'])
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# TypeError: list indices must be integers or slices, not str
cursor = arcpy.da.SearchCursor(fc,['NAME','TOT_ENP'])
for row in cursor:
    print('Airport name = ' + row[0], row[11])
# Traceback (most recent call last):
#   File "<string>", line 2, in <module>
# IndexError: tuple index out of range
for row in cursor:
    print('Airport name = ' + row[0], row[1])
# Airport name = Chignik Lagoon 2697.0
# Airport name = Koyuk 2346.0
# Airport name = Kivalina 3313.0
# Airport name = Ketchikan Harbor 46644.0
# Airport name = Metlakatla 15387.0
# Airport name = Waterfall 2018.0
# Airport name = Ketchikan 132451.0
# Airport name = Kasaan 455.0
# Airport name = Hollis 4170.0
# Airport name = Craig 5898.0
# Airport name = Thorne Bay 5210.0
# Airport name = Coffman Cove 705.0
# Airport name = Meyers Chuck 341.0
# Airport name = Klawock 3900.0
# Airport name = Yes Bay Lodge 941.0
# Airport name = Wrangell 13895.0
# Airport name = Petersburg James A. Johnson 21047.0
# Airport name = Kake 3466.0
# Airport name = Sitka Rocky Gutierrez 68659.0
# Airport name = Angoon 2865.0
# Airport name = Funter Bay 303.0
# Airport name = Tenakee 1072.0
# Airport name = Hawk Inlet 1073.0
# Airport name = Hoonah 9126.0
# Airport name = Juneau International 377559.0
# Airport name = Pelican 1022.0
# Airport name = Elfin Cove 1325.0
# Airport name = Excursion Inlet 1972.0
# Airport name = Gustavus 11570.0
# Airport name = Haines 11060.0
# Airport name = Skagway 36554.0
# Airport name = Yakutat 14702.0
# Airport name = Icy Bay 455.0
# Airport name = Alitak 313.0
# Airport name = Akhiok 1037.0
# Airport name = San Juan/Uganik Bay 335.0
# Airport name = Old Harbor 1082.0
# Airport name = Larsen Bay 2855.0
# Airport name = Trident Basin 2625.0
# Airport name = Kodiak 80107.0
# Airport name = Ouzinkie 661.0
# Airport name = Port Lions 1499.0
# Airport name = Merle K. (Mudhole) Smith 20648.0
# Airport name = Sand Point 4366.0
# Airport name = Ivanof Bay 277.0
# Airport name = Perryville 1111.0
# Airport name = Chignik Fisheries 1416.0
# Airport name = Chignik Lake 635.0
# Airport name = Chignik 1819.0
# Airport name = Karluk 910.0
# Airport name = Port Graham 1481.0
# Airport name = Seldovia 5534.0
# Airport name = English Bay 1153.0
# Airport name = Homer 32859.0
# Airport name = Seward 1213.0
# Airport name = Girdwood 2420.0
# Airport name = Valdez 21536.0
# Airport name = Chitina 451.0
# Airport name = Gulkana 708.0
# Airport name = Tetlin 787.0
# Airport name = King Cove 2777.0
# Airport name = Cold Bay 9909.0
# Airport name = False Pass 498.0
# Airport name = Port Heiden 1694.0
# Airport name = Pilot Point 1037.0
# Airport name = Egegik 1879.0
# Airport name = Lake Brooks 5251.0
# Airport name = Levelock 1157.0
# Airport name = King Salmon 48743.0
# Airport name = South Naknek Nr 2 1176.0
# Airport name = Tibbetts 487.0
# Airport name = Kulik Lake 3178.0
# Airport name = Kokhanok 2283.0
# Airport name = Pedro Bay 676.0
# Airport name = Igiugig 1330.0
# Airport name = Nondalton 1845.0
# Airport name = Port Alsworth 282.0
# Airport name = Soldotna 2508.0
# Airport name = Kenai Municipal 106530.0
# Airport name = Tyonek 8780.0
# Airport name = Trading Bay Production 400.0
# Airport name = Beluga 2570.0
# Airport name = Merrill Field 2240.0
# Airport name = Lake Hood 26733.0
# Airport name = Elmendorf Air Force Base 2104.0
# Airport name = Palmer Municipal 683.0
# Airport name = Willow 1595.0
# Airport name = Skelton 300.0
# Airport name = Tok 1816.0
# Airport name = Eagle 483.0
# Airport name = Akutan 2313.0
# Airport name = Unalaska 31988.0
# Airport name = Ekuk 648.0
# Airport name = Clarks Point 2029.0
# Airport name = Manokotak 2855.0
# Airport name = Ekwok 973.0
# Airport name = Dillingham 45173.0
# Airport name = Koliganek 1855.0
# Airport name = Skwentna 287.0
# Airport name = Talkeetna 13589.0
# Airport name = McKinley National Park 725.0
# Airport name = Platinum 510.0
# Airport name = Goodnews 1596.0
# Airport name = Twin Hills 524.0
# Airport name = Togiak 3845.0
# Airport name = Stony River 2 347.0
# Airport name = Sleetmute 671.0
# Airport name = Nikolai 356.0
# Airport name = Kantishna 1556.0
# Airport name = Minchumina 254.0
# Airport name = Healy River 482.0
# Airport name = Eielson Air Force Base 1740.0
# Airport name = Wainwright Army Air Field 775.0
# Airport name = Fairbanks International 393381.0
# Airport name = Circle City 465.0
# Airport name = Chalkyitsik 1312.0
# Airport name = Atka 397.0
# Airport name = Quinhagak 1666.0
# Airport name = Eek 1408.0
# Airport name = Kongiganak 3349.0
# Airport name = Kwigillingok 3047.0
# Airport name = Tuntutuliak 3342.0
# Airport name = Akiak 1373.0
# Airport name = Kwethluk 2293.0
# Airport name = Tuluksak 2775.0
# Airport name = Napaskiak 748.0
# Airport name = Akiachak 2250.0
# Airport name = Napakiak 1236.0
# Airport name = Bethel 125885.0
# Airport name = Aniak 16471.0
# Airport name = Kalskag 4549.0
# Airport name = Red Devil 250.0
# Airport name = Crooked Creek 720.0
# Airport name = McGrath 4954.0
# Airport name = Ralph M. Calhoun Memorial 4653.0
# Airport name = Minto 393.0
# Airport name = Rampart 1087.0
# Airport name = Stevens Village 2212.0
# Airport name = Beaver 2676.0
# Airport name = Birch Creek 744.0
# Airport name = Fort Yukon 11392.0
# Airport name = Venetie 2274.0
# Airport name = Adak Naval Air Facility 2698.0
# Airport name = Saint George 1007.0
# Airport name = Saint Paul Island 4712.0
# Airport name = Newtok 1683.0
# Airport name = Kipnuk 4677.0
# Airport name = Chefornak 3049.0
# Airport name = Nightmute 1537.0
# Airport name = Toksook Bay 3938.0
# Airport name = Tununak 1826.0
# Airport name = Atmautluak 2065.0
# Airport name = Nunapitchuk 2502.0
# Airport name = Kasigluk 2439.0
# Airport name = Russian Mission 2470.0
# Airport name = Marshall 2662.0
# Airport name = Pilot Station 4703.0
# Airport name = Holy Cross 1510.0
# Airport name = Shageluk 788.0
# Airport name = Anvik 649.0
# Airport name = Grayling 1095.0
# Airport name = Edward G. Pitka Sr. 10027.0
# Airport name = Ruby 1941.0
# Airport name = Bettles 3900.0
# Airport name = New Allakaket 1901.0
# Airport name = Prospect Creek 2419.0
# Airport name = Coldfoot 631.0
# Airport name = Arctic Village 2296.0
# Airport name = Mekoryuk 1954.0
# Airport name = Hooper Bay 5319.0
# Airport name = Mountain Village 5523.0
# Airport name = Chevak 4404.0
# Airport name = Scammon Bay 2864.0
# Airport name = Saint Mary's 8281.0
# Airport name = Sheldon Point 1376.0
# Airport name = Saint Michael 2123.0
# Airport name = Stebbins 2407.0
# Airport name = Unalakleet 8467.0
# Airport name = Shaktoolik 1756.0
# Airport name = Kaltag 2192.0
# Airport name = Nulato 3529.0
# Airport name = Huslia 3443.0
# Airport name = Hughes 1095.0
# Airport name = Anaktuvuk Pass 3653.0
# Airport name = Galbraith Lake 1200.0
# Airport name = Barter Island LRRS 2055.0
# Airport name = Alakanuk 3735.0
# Airport name = Emmonak 6780.0
# Airport name = Elim 2827.0
# Airport name = Golovin 1562.0
# Airport name = White Mountain 1790.0
# Airport name = Buckland 3153.0
# Airport name = Selawik 5176.0
# Airport name = Kobuk 992.0
# Airport name = Shungnak 2309.0
# Airport name = Ambler 2423.0
# Airport name = Deadhorse 12479.0
# Airport name = Nome 56911.0
# Airport name = Deering 1473.0
# Airport name = Bob Baker Memorial 3899.0
# Airport name = Robert (Bob) Curtis Memorial 5266.0
# Airport name = Ralph Wien Memorial 59351.0
# Airport name = Nuiqsut 1018.0
# Airport name = Savoonga 4271.0
# Airport name = Teller 983.0
# Airport name = Brevig Mission 1463.0
# Airport name = Shishmaref 3866.0
# Airport name = Wales 1542.0
# Airport name = Noatak 4124.0
# Airport name = Red Dog 9316.0
# Airport name = Atqasuk Edward Burnell Sr. Memorial 2686.0
# Airport name = Gambell 4098.0
# Airport name = Point Hope 5533.0
# Airport name = Point Lay LRRS 1962.0
# Airport name = Wainwright 3783.0
# Airport name = Wiley Post-Will Rogers Memorial 40751.0
# Airport name = New Stuyahok 2217.0
# Airport name = Ted Stevens Anchorage International 2536319.0
# Airport name = Iliamna 13806.0
# Airport name = Koyukuk 994.0
for row in cursor:
    print('Airport name = ' + row[0] + ',' row[1])
#   File "<string>", line 2
#     print('Airport name = ' + row[0] + ',' row[1])
#                                              ^
# SyntaxError: invalid syntax
for row in cursor:
    print('Airport name = ' + row[0] + ',' + row[1])
for row in cursor:
    print('Airport name = ' + row[0], row[1])
cursor = arcpy.da.SearchCursor(fc,['NAME','TOT_ENP'])
for row in cursor:
    print('Airport name = ' + row[0], row[1])
# Airport name = Hyder 319.0
# Airport name = Chignik Lagoon 2697.0
# Airport name = Koyuk 2346.0
# Airport name = Kivalina 3313.0
# Airport name = Ketchikan Harbor 46644.0
# Airport name = Metlakatla 15387.0
# Airport name = Waterfall 2018.0
# Airport name = Ketchikan 132451.0
# Airport name = Kasaan 455.0
# Airport name = Hollis 4170.0
# Airport name = Craig 5898.0
# Airport name = Thorne Bay 5210.0
# Airport name = Coffman Cove 705.0
# Airport name = Meyers Chuck 341.0
# Airport name = Klawock 3900.0
# Airport name = Yes Bay Lodge 941.0
# Airport name = Wrangell 13895.0
# Airport name = Petersburg James A. Johnson 21047.0
# Airport name = Kake 3466.0
# Airport name = Sitka Rocky Gutierrez 68659.0
# Airport name = Angoon 2865.0
# Airport name = Funter Bay 303.0
# Airport name = Tenakee 1072.0
# Airport name = Hawk Inlet 1073.0
# Airport name = Hoonah 9126.0
# Airport name = Juneau International 377559.0
# Airport name = Pelican 1022.0
# Airport name = Elfin Cove 1325.0
# Airport name = Excursion Inlet 1972.0
# Airport name = Gustavus 11570.0
# Airport name = Haines 11060.0
# Airport name = Skagway 36554.0
# Airport name = Yakutat 14702.0
# Airport name = Icy Bay 455.0
# Airport name = Alitak 313.0
# Airport name = Akhiok 1037.0
# Airport name = San Juan/Uganik Bay 335.0
# Airport name = Old Harbor 1082.0
# Airport name = Larsen Bay 2855.0
# Airport name = Trident Basin 2625.0
# Airport name = Kodiak 80107.0
# Airport name = Ouzinkie 661.0
# Airport name = Port Lions 1499.0
# Airport name = Merle K. (Mudhole) Smith 20648.0
# Airport name = Sand Point 4366.0
# Airport name = Ivanof Bay 277.0
# Airport name = Perryville 1111.0
# Airport name = Chignik Fisheries 1416.0
# Airport name = Chignik Lake 635.0
# Airport name = Chignik 1819.0
# Airport name = Karluk 910.0
# Airport name = Port Graham 1481.0
# Airport name = Seldovia 5534.0
# Airport name = English Bay 1153.0
# Airport name = Homer 32859.0
# Airport name = Seward 1213.0
# Airport name = Girdwood 2420.0
# Airport name = Valdez 21536.0
# Airport name = Chitina 451.0
# Airport name = Gulkana 708.0
# Airport name = Tetlin 787.0
# Airport name = King Cove 2777.0
# Airport name = Cold Bay 9909.0
# Airport name = False Pass 498.0
# Airport name = Port Heiden 1694.0
# Airport name = Pilot Point 1037.0
# Airport name = Egegik 1879.0
# Airport name = Lake Brooks 5251.0
# Airport name = Levelock 1157.0
# Airport name = King Salmon 48743.0
# Airport name = South Naknek Nr 2 1176.0
# Airport name = Tibbetts 487.0
# Airport name = Kulik Lake 3178.0
# Airport name = Kokhanok 2283.0
# Airport name = Pedro Bay 676.0
# Airport name = Igiugig 1330.0
# Airport name = Nondalton 1845.0
# Airport name = Port Alsworth 282.0
# Airport name = Soldotna 2508.0
# Airport name = Kenai Municipal 106530.0
# Airport name = Tyonek 8780.0
# Airport name = Trading Bay Production 400.0
# Airport name = Beluga 2570.0
# Airport name = Merrill Field 2240.0
# Airport name = Lake Hood 26733.0
# Airport name = Elmendorf Air Force Base 2104.0
# Airport name = Palmer Municipal 683.0
# Airport name = Willow 1595.0
# Airport name = Skelton 300.0
# Airport name = Tok 1816.0
# Airport name = Eagle 483.0
# Airport name = Akutan 2313.0
# Airport name = Unalaska 31988.0
# Airport name = Ekuk 648.0
# Airport name = Clarks Point 2029.0
# Airport name = Manokotak 2855.0
# Airport name = Ekwok 973.0
# Airport name = Dillingham 45173.0
# Airport name = Koliganek 1855.0
# Airport name = Skwentna 287.0
# Airport name = Talkeetna 13589.0
# Airport name = McKinley National Park 725.0
# Airport name = Platinum 510.0
# Airport name = Goodnews 1596.0
# Airport name = Twin Hills 524.0
# Airport name = Togiak 3845.0
# Airport name = Stony River 2 347.0
# Airport name = Sleetmute 671.0
# Airport name = Nikolai 356.0
# Airport name = Kantishna 1556.0
# Airport name = Minchumina 254.0
# Airport name = Healy River 482.0
# Airport name = Eielson Air Force Base 1740.0
# Airport name = Wainwright Army Air Field 775.0
# Airport name = Fairbanks International 393381.0
# Airport name = Circle City 465.0
# Airport name = Chalkyitsik 1312.0
# Airport name = Atka 397.0
# Airport name = Quinhagak 1666.0
# Airport name = Eek 1408.0
# Airport name = Kongiganak 3349.0
# Airport name = Kwigillingok 3047.0
# Airport name = Tuntutuliak 3342.0
# Airport name = Akiak 1373.0
# Airport name = Kwethluk 2293.0
# Airport name = Tuluksak 2775.0
# Airport name = Napaskiak 748.0
# Airport name = Akiachak 2250.0
# Airport name = Napakiak 1236.0
# Airport name = Bethel 125885.0
# Airport name = Aniak 16471.0
# Airport name = Kalskag 4549.0
# Airport name = Red Devil 250.0
# Airport name = Crooked Creek 720.0
# Airport name = McGrath 4954.0
# Airport name = Ralph M. Calhoun Memorial 4653.0
# Airport name = Minto 393.0
# Airport name = Rampart 1087.0
# Airport name = Stevens Village 2212.0
# Airport name = Beaver 2676.0
# Airport name = Birch Creek 744.0
# Airport name = Fort Yukon 11392.0
# Airport name = Venetie 2274.0
# Airport name = Adak Naval Air Facility 2698.0
# Airport name = Saint George 1007.0
# Airport name = Saint Paul Island 4712.0
# Airport name = Newtok 1683.0
# Airport name = Kipnuk 4677.0
# Airport name = Chefornak 3049.0
# Airport name = Nightmute 1537.0
# Airport name = Toksook Bay 3938.0
# Airport name = Tununak 1826.0
# Airport name = Atmautluak 2065.0
# Airport name = Nunapitchuk 2502.0
# Airport name = Kasigluk 2439.0
# Airport name = Russian Mission 2470.0
# Airport name = Marshall 2662.0
# Airport name = Pilot Station 4703.0
# Airport name = Holy Cross 1510.0
# Airport name = Shageluk 788.0
# Airport name = Anvik 649.0
# Airport name = Grayling 1095.0
# Airport name = Edward G. Pitka Sr. 10027.0
# Airport name = Ruby 1941.0
# Airport name = Bettles 3900.0
# Airport name = New Allakaket 1901.0
# Airport name = Prospect Creek 2419.0
# Airport name = Coldfoot 631.0
# Airport name = Arctic Village 2296.0
# Airport name = Mekoryuk 1954.0
# Airport name = Hooper Bay 5319.0
# Airport name = Mountain Village 5523.0
# Airport name = Chevak 4404.0
# Airport name = Scammon Bay 2864.0
# Airport name = Saint Mary's 8281.0
# Airport name = Sheldon Point 1376.0
# Airport name = Saint Michael 2123.0
# Airport name = Stebbins 2407.0
# Airport name = Unalakleet 8467.0
# Airport name = Shaktoolik 1756.0
# Airport name = Kaltag 2192.0
# Airport name = Nulato 3529.0
# Airport name = Huslia 3443.0
# Airport name = Hughes 1095.0
# Airport name = Anaktuvuk Pass 3653.0
# Airport name = Galbraith Lake 1200.0
# Airport name = Barter Island LRRS 2055.0
# Airport name = Alakanuk 3735.0
# Airport name = Emmonak 6780.0
# Airport name = Elim 2827.0
# Airport name = Golovin 1562.0
# Airport name = White Mountain 1790.0
# Airport name = Buckland 3153.0
# Airport name = Selawik 5176.0
# Airport name = Kobuk 992.0
# Airport name = Shungnak 2309.0
# Airport name = Ambler 2423.0
# Airport name = Deadhorse 12479.0
# Airport name = Nome 56911.0
# Airport name = Deering 1473.0
# Airport name = Bob Baker Memorial 3899.0
# Airport name = Robert (Bob) Curtis Memorial 5266.0
# Airport name = Ralph Wien Memorial 59351.0
# Airport name = Nuiqsut 1018.0
# Airport name = Savoonga 4271.0
# Airport name = Teller 983.0
# Airport name = Brevig Mission 1463.0
# Airport name = Shishmaref 3866.0
# Airport name = Wales 1542.0
# Airport name = Noatak 4124.0
# Airport name = Red Dog 9316.0
# Airport name = Atqasuk Edward Burnell Sr. Memorial 2686.0
# Airport name = Gambell 4098.0
# Airport name = Point Hope 5533.0
# Airport name = Point Lay LRRS 1962.0
# Airport name = Wainwright 3783.0
# Airport name = Wiley Post-Will Rogers Memorial 40751.0
# Airport name = New Stuyahok 2217.0
# Airport name = Ted Stevens Anchorage International 2536319.0
# Airport name = Iliamna 13806.0
# Airport name = Koyukuk 994.0
cursor = arcpy.da.SearchCursor(fc,['NAME'],'TOT_ENP>100000')
for row in cursor:
    print(row)
# ('Ketchikan',)
# ('Juneau International',)
# ('Kenai Municipal',)
# ('Fairbanks International',)
# ('Bethel',)
# ('Ted Stevens Anchorage International',)
count = 0
for row in cursor:
    print(row)
    count += 1
print (count)
# 0
cursor = arcpy.da.SearchCursor(fc,['NAME'],'TOT_ENP>100000')
for row in cursor:
    print(row)
    count += 1
# ('Ketchikan',)
# ('Juneau International',)
# ('Kenai Municipal',)
# ('Fairbanks International',)
# ('Bethel',)
# ('Ted Stevens Anchorage International',)
print(count)
# 6
for row in cursor:
    print(row)
    count += 1
print(count)
# 6
for row in cursor:
    print(row)
    count += 1 
print(count)
# 6
cursor = arcpy.da.SearchCursor(fc,['NAME'],'TOT_ENP>100000')
for row in cursor:
    print(row)
    count += 1 
print(count)
# ('Ketchikan',)
# ('Juneau International',)
# ('Kenai Municipal',)
# ('Fairbanks International',)
# ('Bethel',)
# ('Ted Stevens Anchorage International',)
# 12
count = 0
for row in cursor:
    print(row)
    count += 1 
print(count)
# 0
cursor = arcpy.da.SearchCursor(fc,['NAME'],'TOT_ENP>100000')
for row in cursor:
    print(row)
    count += 1 
print(count)
# ('Ketchikan',)
# ('Juneau International',)
# ('Kenai Municipal',)
# ('Fairbanks International',)
# ('Bethel',)
# ('Ted Stevens Anchorage International',)
# 6
for row in cursor:
    print(row)
    count += 1 
print(count)
print('The sum is' + row)
# 6
# Traceback (most recent call last):
#   File "<string>", line 5, in <module>
# TypeError: must be str, not tuple
cursor = arcpy.da.SearchCursor(fc,['NAME', 'TOT_ENP'])
accum = 0
for row in cursor:
    print(row)
    count += 1
    accum += row[1]

print('the average is' + accum/count)
print(count)
print('The sum is' + accum)
# ('Hyder', 319.0)
# ('Chignik Lagoon', 2697.0)
# ('Koyuk', 2346.0)
# ('Kivalina', 3313.0)
# ('Ketchikan Harbor', 46644.0)
# ('Metlakatla', 15387.0)
# ('Waterfall', 2018.0)
# ('Ketchikan', 132451.0)
# ('Kasaan', 455.0)
# ('Hollis', 4170.0)
# ('Craig', 5898.0)
# ('Thorne Bay', 5210.0)
# ('Coffman Cove', 705.0)
# ('Meyers Chuck', 341.0)
# ('Klawock', 3900.0)
# ('Yes Bay Lodge', 941.0)
# ('Wrangell', 13895.0)
# ('Petersburg James A. Johnson', 21047.0)
# ('Kake', 3466.0)
# ('Sitka Rocky Gutierrez', 68659.0)
# ('Angoon', 2865.0)
# ('Funter Bay', 303.0)
# ('Tenakee', 1072.0)
# ('Hawk Inlet', 1073.0)
# ('Hoonah', 9126.0)
# ('Juneau International', 377559.0)
# ('Pelican', 1022.0)
# ('Elfin Cove', 1325.0)
# ('Excursion Inlet', 1972.0)
# ('Gustavus', 11570.0)
# ('Haines', 11060.0)
# ('Skagway', 36554.0)
# ('Yakutat', 14702.0)
# ('Icy Bay', 455.0)
# ('Alitak', 313.0)
# ('Akhiok', 1037.0)
# ('San Juan/Uganik Bay', 335.0)
# ('Old Harbor', 1082.0)
# ('Larsen Bay', 2855.0)
# ('Trident Basin', 2625.0)
# ('Kodiak', 80107.0)
# ('Ouzinkie', 661.0)
# ('Port Lions', 1499.0)
# ('Merle K. (Mudhole) Smith', 20648.0)
# ('Sand Point', 4366.0)
# ('Ivanof Bay', 277.0)
# ('Perryville', 1111.0)
# ('Chignik Fisheries', 1416.0)
# ('Chignik Lake', 635.0)
# ('Chignik', 1819.0)
# ('Karluk', 910.0)
# ('Port Graham', 1481.0)
# ('Seldovia', 5534.0)
# ('English Bay', 1153.0)
# ('Homer', 32859.0)
# ('Seward', 1213.0)
# ('Girdwood', 2420.0)
# ('Valdez', 21536.0)
# ('Chitina', 451.0)
# ('Gulkana', 708.0)
# ('Tetlin', 787.0)
# ('King Cove', 2777.0)
# ('Cold Bay', 9909.0)
# ('False Pass', 498.0)
# ('Port Heiden', 1694.0)
# ('Pilot Point', 1037.0)
# ('Egegik', 1879.0)
# ('Lake Brooks', 5251.0)
# ('Levelock', 1157.0)
# ('King Salmon', 48743.0)
# ('South Naknek Nr 2', 1176.0)
# ('Tibbetts', 487.0)
# ('Kulik Lake', 3178.0)
# ('Kokhanok', 2283.0)
# ('Pedro Bay', 676.0)
# ('Igiugig', 1330.0)
# ('Nondalton', 1845.0)
# ('Port Alsworth', 282.0)
# ('Soldotna', 2508.0)
# ('Kenai Municipal', 106530.0)
# ('Tyonek', 8780.0)
# ('Trading Bay Production', 400.0)
# ('Beluga', 2570.0)
# ('Merrill Field', 2240.0)
# ('Lake Hood', 26733.0)
# ('Elmendorf Air Force Base', 2104.0)
# ('Palmer Municipal', 683.0)
# ('Willow', 1595.0)
# ('Skelton', 300.0)
# ('Tok', 1816.0)
# ('Eagle', 483.0)
# ('Akutan', 2313.0)
# ('Unalaska', 31988.0)
# ('Ekuk', 648.0)
# ('Clarks Point', 2029.0)
# ('Manokotak', 2855.0)
# ('Ekwok', 973.0)
# ('Dillingham', 45173.0)
# ('Koliganek', 1855.0)
# ('Skwentna', 287.0)
# ('Talkeetna', 13589.0)
# ('McKinley National Park', 725.0)
# ('Platinum', 510.0)
# ('Goodnews', 1596.0)
# ('Twin Hills', 524.0)
# ('Togiak', 3845.0)
# ('Stony River 2', 347.0)
# ('Sleetmute', 671.0)
# ('Nikolai', 356.0)
# ('Kantishna', 1556.0)
# ('Minchumina', 254.0)
# ('Healy River', 482.0)
# ('Eielson Air Force Base', 1740.0)
# ('Wainwright Army Air Field', 775.0)
# ('Fairbanks International', 393381.0)
# ('Circle City', 465.0)
# ('Chalkyitsik', 1312.0)
# ('Atka', 397.0)
# ('Quinhagak', 1666.0)
# ('Eek', 1408.0)
# ('Kongiganak', 3349.0)
# ('Kwigillingok', 3047.0)
# ('Tuntutuliak', 3342.0)
# ('Akiak', 1373.0)
# ('Kwethluk', 2293.0)
# ('Tuluksak', 2775.0)
# ('Napaskiak', 748.0)
# ('Akiachak', 2250.0)
# ('Napakiak', 1236.0)
# ('Bethel', 125885.0)
# ('Aniak', 16471.0)
# ('Kalskag', 4549.0)
# ('Red Devil', 250.0)
# ('Crooked Creek', 720.0)
# ('McGrath', 4954.0)
# ('Ralph M. Calhoun Memorial', 4653.0)
# ('Minto', 393.0)
# ('Rampart', 1087.0)
# ('Stevens Village', 2212.0)
# ('Beaver', 2676.0)
# ('Birch Creek', 744.0)
# ('Fort Yukon', 11392.0)
# ('Venetie', 2274.0)
# ('Adak Naval Air Facility', 2698.0)
# ('Saint George', 1007.0)
# ('Saint Paul Island', 4712.0)
# ('Newtok', 1683.0)
# ('Kipnuk', 4677.0)
# ('Chefornak', 3049.0)
# ('Nightmute', 1537.0)
# ('Toksook Bay', 3938.0)
# ('Tununak', 1826.0)
# ('Atmautluak', 2065.0)
# ('Nunapitchuk', 2502.0)
# ('Kasigluk', 2439.0)
# ('Russian Mission', 2470.0)
# ('Marshall', 2662.0)
# ('Pilot Station', 4703.0)
# ('Holy Cross', 1510.0)
# ('Shageluk', 788.0)
# ('Anvik', 649.0)
# ('Grayling', 1095.0)
# ('Edward G. Pitka Sr.', 10027.0)
# ('Ruby', 1941.0)
# ('Bettles', 3900.0)
# ('New Allakaket', 1901.0)
# ('Prospect Creek', 2419.0)
# ('Coldfoot', 631.0)
# ('Arctic Village', 2296.0)
# ('Mekoryuk', 1954.0)
# ('Hooper Bay', 5319.0)
# ('Mountain Village', 5523.0)
# ('Chevak', 4404.0)
# ('Scammon Bay', 2864.0)
# ("Saint Mary's", 8281.0)
# ('Sheldon Point', 1376.0)
# ('Saint Michael', 2123.0)
# ('Stebbins', 2407.0)
# ('Unalakleet', 8467.0)
# ('Shaktoolik', 1756.0)
# ('Kaltag', 2192.0)
# ('Nulato', 3529.0)
# ('Huslia', 3443.0)
# ('Hughes', 1095.0)
# ('Anaktuvuk Pass', 3653.0)
# ('Galbraith Lake', 1200.0)
# ('Barter Island LRRS', 2055.0)
# ('Alakanuk', 3735.0)
# ('Emmonak', 6780.0)
# ('Elim', 2827.0)
# ('Golovin', 1562.0)
# ('White Mountain', 1790.0)
# ('Buckland', 3153.0)
# ('Selawik', 5176.0)
# ('Kobuk', 992.0)
# ('Shungnak', 2309.0)
# ('Ambler', 2423.0)
# ('Deadhorse', 12479.0)
# ('Nome', 56911.0)
# ('Deering', 1473.0)
# ('Bob Baker Memorial', 3899.0)
# ('Robert (Bob) Curtis Memorial', 5266.0)
# ('Ralph Wien Memorial', 59351.0)
# ('Nuiqsut', 1018.0)
# ('Savoonga', 4271.0)
# ('Teller', 983.0)
# ('Brevig Mission', 1463.0)
# ('Shishmaref', 3866.0)
# ('Wales', 1542.0)
# ('Noatak', 4124.0)
# ('Red Dog', 9316.0)
# ('Atqasuk Edward Burnell Sr. Memorial', 2686.0)
# ('Gambell', 4098.0)
# ('Point Hope', 5533.0)
# ('Point Lay LRRS', 1962.0)
# ('Wainwright', 3783.0)
# ('Wiley Post-Will Rogers Memorial', 40751.0)
# ('New Stuyahok', 2217.0)
# ('Ted Stevens Anchorage International', 2536319.0)
# ('Iliamna', 13806.0)
# ('Koyukuk', 994.0)
# Traceback (most recent call last):
#   File "<string>", line 6, in <module>
# TypeError: must be str, not float
for row in cursor:
    
    count += 1
    accum += row[1]

print('the average is' + accum/count)
print(count)
print('The sum is' + accum)
# Traceback (most recent call last):
#   File "<string>", line 6, in <module>
# TypeError: must be str, not float
count = 0
accum = 0
for row in cursor:
    print(row)
    count += 1
    accum += row[1]

print('the average is' + accum/count)
print(count)
print('The sum is' + accum)
# Traceback (most recent call last):
#   File "<string>", line 6, in <module>
# ZeroDivisionError: division by zero
cursor = arcpy.da.SearchCursor(fc,['NAME', 'TOT_ENP'])
for row in cursor:
    print(row)
    count += 1
    accum += row[1]

print('the average is' + accum/count)
print(count)
print('The sum is' + accum)
# ('Hyder', 319.0)
# ('Chignik Lagoon', 2697.0)
# ('Koyuk', 2346.0)
# ('Kivalina', 3313.0)
# ('Ketchikan Harbor', 46644.0)
# ('Metlakatla', 15387.0)
# ('Waterfall', 2018.0)
# ('Ketchikan', 132451.0)
# ('Kasaan', 455.0)
# ('Hollis', 4170.0)
# ('Craig', 5898.0)
# ('Thorne Bay', 5210.0)
# ('Coffman Cove', 705.0)
# ('Meyers Chuck', 341.0)
# ('Klawock', 3900.0)
# ('Yes Bay Lodge', 941.0)
# ('Wrangell', 13895.0)
# ('Petersburg James A. Johnson', 21047.0)
# ('Kake', 3466.0)
# ('Sitka Rocky Gutierrez', 68659.0)
# ('Angoon', 2865.0)
# ('Funter Bay', 303.0)
# ('Tenakee', 1072.0)
# ('Hawk Inlet', 1073.0)
# ('Hoonah', 9126.0)
# ('Juneau International', 377559.0)
# ('Pelican', 1022.0)
# ('Elfin Cove', 1325.0)
# ('Excursion Inlet', 1972.0)
# ('Gustavus', 11570.0)
# ('Haines', 11060.0)
# ('Skagway', 36554.0)
# ('Yakutat', 14702.0)
# ('Icy Bay', 455.0)
# ('Alitak', 313.0)
# ('Akhiok', 1037.0)
# ('San Juan/Uganik Bay', 335.0)
# ('Old Harbor', 1082.0)
# ('Larsen Bay', 2855.0)
# ('Trident Basin', 2625.0)
# ('Kodiak', 80107.0)
# ('Ouzinkie', 661.0)
# ('Port Lions', 1499.0)
# ('Merle K. (Mudhole) Smith', 20648.0)
# ('Sand Point', 4366.0)
# ('Ivanof Bay', 277.0)
# ('Perryville', 1111.0)
# ('Chignik Fisheries', 1416.0)
# ('Chignik Lake', 635.0)
# ('Chignik', 1819.0)
# ('Karluk', 910.0)
# ('Port Graham', 1481.0)
# ('Seldovia', 5534.0)
# ('English Bay', 1153.0)
# ('Homer', 32859.0)
# ('Seward', 1213.0)
# ('Girdwood', 2420.0)
# ('Valdez', 21536.0)
# ('Chitina', 451.0)
# ('Gulkana', 708.0)
# ('Tetlin', 787.0)
# ('King Cove', 2777.0)
# ('Cold Bay', 9909.0)
# ('False Pass', 498.0)
# ('Port Heiden', 1694.0)
# ('Pilot Point', 1037.0)
# ('Egegik', 1879.0)
# ('Lake Brooks', 5251.0)
# ('Levelock', 1157.0)
# ('King Salmon', 48743.0)
# ('South Naknek Nr 2', 1176.0)
# ('Tibbetts', 487.0)
# ('Kulik Lake', 3178.0)
# ('Kokhanok', 2283.0)
# ('Pedro Bay', 676.0)
# ('Igiugig', 1330.0)
# ('Nondalton', 1845.0)
# ('Port Alsworth', 282.0)
# ('Soldotna', 2508.0)
# ('Kenai Municipal', 106530.0)
# ('Tyonek', 8780.0)
# ('Trading Bay Production', 400.0)
# ('Beluga', 2570.0)
# ('Merrill Field', 2240.0)
# ('Lake Hood', 26733.0)
# ('Elmendorf Air Force Base', 2104.0)
# ('Palmer Municipal', 683.0)
# ('Willow', 1595.0)
# ('Skelton', 300.0)
# ('Tok', 1816.0)
# ('Eagle', 483.0)
# ('Akutan', 2313.0)
# ('Unalaska', 31988.0)
# ('Ekuk', 648.0)
# ('Clarks Point', 2029.0)
# ('Manokotak', 2855.0)
# ('Ekwok', 973.0)
# ('Dillingham', 45173.0)
# ('Koliganek', 1855.0)
# ('Skwentna', 287.0)
# ('Talkeetna', 13589.0)
# ('McKinley National Park', 725.0)
# ('Platinum', 510.0)
# ('Goodnews', 1596.0)
# ('Twin Hills', 524.0)
# ('Togiak', 3845.0)
# ('Stony River 2', 347.0)
# ('Sleetmute', 671.0)
# ('Nikolai', 356.0)
# ('Kantishna', 1556.0)
# ('Minchumina', 254.0)
# ('Healy River', 482.0)
# ('Eielson Air Force Base', 1740.0)
# ('Wainwright Army Air Field', 775.0)
# ('Fairbanks International', 393381.0)
# ('Circle City', 465.0)
# ('Chalkyitsik', 1312.0)
# ('Atka', 397.0)
# ('Quinhagak', 1666.0)
# ('Eek', 1408.0)
# ('Kongiganak', 3349.0)
# ('Kwigillingok', 3047.0)
# ('Tuntutuliak', 3342.0)
# ('Akiak', 1373.0)
# ('Kwethluk', 2293.0)
# ('Tuluksak', 2775.0)
# ('Napaskiak', 748.0)
# ('Akiachak', 2250.0)
# ('Napakiak', 1236.0)
# ('Bethel', 125885.0)
# ('Aniak', 16471.0)
# ('Kalskag', 4549.0)
# ('Red Devil', 250.0)
# ('Crooked Creek', 720.0)
# ('McGrath', 4954.0)
# ('Ralph M. Calhoun Memorial', 4653.0)
# ('Minto', 393.0)
# ('Rampart', 1087.0)
# ('Stevens Village', 2212.0)
# ('Beaver', 2676.0)
# ('Birch Creek', 744.0)
# ('Fort Yukon', 11392.0)
# ('Venetie', 2274.0)
# ('Adak Naval Air Facility', 2698.0)
# ('Saint George', 1007.0)
# ('Saint Paul Island', 4712.0)
# ('Newtok', 1683.0)
# ('Kipnuk', 4677.0)
# ('Chefornak', 3049.0)
# ('Nightmute', 1537.0)
# ('Toksook Bay', 3938.0)
# ('Tununak', 1826.0)
# ('Atmautluak', 2065.0)
# ('Nunapitchuk', 2502.0)
# ('Kasigluk', 2439.0)
# ('Russian Mission', 2470.0)
# ('Marshall', 2662.0)
# ('Pilot Station', 4703.0)
# ('Holy Cross', 1510.0)
# ('Shageluk', 788.0)
# ('Anvik', 649.0)
# ('Grayling', 1095.0)
# ('Edward G. Pitka Sr.', 10027.0)
# ('Ruby', 1941.0)
# ('Bettles', 3900.0)
# ('New Allakaket', 1901.0)
# ('Prospect Creek', 2419.0)
# ('Coldfoot', 631.0)
# ('Arctic Village', 2296.0)
# ('Mekoryuk', 1954.0)
# ('Hooper Bay', 5319.0)
# ('Mountain Village', 5523.0)
# ('Chevak', 4404.0)
# ('Scammon Bay', 2864.0)
# ("Saint Mary's", 8281.0)
# ('Sheldon Point', 1376.0)
# ('Saint Michael', 2123.0)
# ('Stebbins', 2407.0)
# ('Unalakleet', 8467.0)
# ('Shaktoolik', 1756.0)
# ('Kaltag', 2192.0)
# ('Nulato', 3529.0)
# ('Huslia', 3443.0)
# ('Hughes', 1095.0)
# ('Anaktuvuk Pass', 3653.0)
# ('Galbraith Lake', 1200.0)
# ('Barter Island LRRS', 2055.0)
# ('Alakanuk', 3735.0)
# ('Emmonak', 6780.0)
# ('Elim', 2827.0)
# ('Golovin', 1562.0)
# ('White Mountain', 1790.0)
# ('Buckland', 3153.0)
# ('Selawik', 5176.0)
# ('Kobuk', 992.0)
# ('Shungnak', 2309.0)
# ('Ambler', 2423.0)
# ('Deadhorse', 12479.0)
# ('Nome', 56911.0)
# ('Deering', 1473.0)
# ('Bob Baker Memorial', 3899.0)
# ('Robert (Bob) Curtis Memorial', 5266.0)
# ('Ralph Wien Memorial', 59351.0)
# ('Nuiqsut', 1018.0)
# ('Savoonga', 4271.0)
# ('Teller', 983.0)
# ('Brevig Mission', 1463.0)
# ('Shishmaref', 3866.0)
# ('Wales', 1542.0)
# ('Noatak', 4124.0)
# ('Red Dog', 9316.0)
# ('Atqasuk Edward Burnell Sr. Memorial', 2686.0)
# ('Gambell', 4098.0)
# ('Point Hope', 5533.0)
# ('Point Lay LRRS', 1962.0)
# ('Wainwright', 3783.0)
# ('Wiley Post-Will Rogers Memorial', 40751.0)
# ('New Stuyahok', 2217.0)
# ('Ted Stevens Anchorage International', 2536319.0)
# ('Iliamna', 13806.0)
# ('Koyukuk', 994.0)
# Traceback (most recent call last):
#   File "<string>", line 6, in <module>
# TypeError: must be str, not float
for row in cursor:
    count += 1
    accum += row[1]

print('the average is' + accum/count)
print(count)
print('The sum is' + accum)
# Traceback (most recent call last):
#   File "<string>", line 5, in <module>
# TypeError: must be str, not float
cursor = arcpy.da.SearchCursor(fc,['NAME'],'FEATURE = Seaplane Base')
for row in cursor:
    print(row)
    i +=1
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# RuntimeError: An invalid SQL statement was used. [SELECT NAME, OBJECTID FROM airports WHERE FEATURE = Seaplane Base]
cursor = arcpy.da.SearchCursor(fc,['NAME'],'FEATURE = 'Seaplane Base'')
#   File "<string>", line 1
#     cursor = arcpy.da.SearchCursor(fc,['NAME'],'FEATURE = 'Seaplane Base'')
#                                                                   ^
# SyntaxError: invalid syntax
cursor = arcpy.da.SearchCursor(fc,['NAME'],'FEATURE = "Seaplane Base"')
for row in cursor:
    print(row)
    i +=1
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# RuntimeError: An expected Field was not found or could not be retrieved properly. [airports]
for row in cursor:
    print(row)
    count +=1
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# RuntimeError: An expected Field was not found or could not be retrieved properly. [airports]
for row in cursor:
    print(row)
    count +=1 
print(count)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# RuntimeError: An expected Field was not found or could not be retrieved properly. [airports]
cursor = arcpy.da.SearchCursor(fc,['*'],'FEATURE = "Seaplane Base"')
for row in cursor:
    print(row)
    count +=1 
print(count)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# RuntimeError: An expected Field was not found or could not be retrieved properly. [airports]
cursor = arcpy.da.SearchCursor(fc,['*'],"FEATURE = 'Seaplane Base'")
for row in cursor:
    print(row)
    count +=1 
print(count)
# (1, (-130.01252746616962, 55.904338836668046), 0.0, 0.0, 5.0, '4Z7', 'Seaplane Base', 'Hyder', 319.0, ' ', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (5, (-131.68510436997065, 55.34780883790762), 0.0, 0.0, 10.0, '5KE', 'Seaplane Base', 'Ketchikan Harbor', 46644.0, 'AK', 'Ketchikan Gateway Borough', '02130', '02')
# (6, (-131.57806396458028, 55.13104629555016), 0.0, 0.0, 666.0, 'MTM', 'Seaplane Base', 'Metlakatla', 15387.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (7, (-133.24333190904036, 55.29632186925892), 0.0, 0.0, 667.0, 'KWF', 'Seaplane Base', 'Waterfall', 2018.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (9, (-132.39752197266085, 55.537414550641074), 0.0, 0.0, 669.0, 'KXA', 'Seaplane Base', 'Kasaan', 455.0, ' ', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (10, (-132.6460876461279, 55.48158645644986), 0.0, 0.0, 670.0, 'HYL', 'Seaplane Base', 'Hollis', 4170.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (11, (-133.14779663041014, 55.47883224491221), 0.0, 0.0, 671.0, 'CGA', 'Seaplane Base', 'Craig', 5898.0, ' ', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (12, (-132.53668212897702, 55.687961578264265), 0.0, 0.0, 672.0, 'KTB', 'Seaplane Base', 'Thorne Bay', 5210.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (13, (-132.84196472179445, 56.00324249274689), 0.0, 0.0, 673.0, 'KCC', 'Seaplane Base', 'Coffman Cove', 705.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (14, (-132.25502014156626, 55.739635467402934), 0.0, 0.0, 674.0, '84K', 'Seaplane Base', 'Meyers Chuck', 341.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (16, (-131.80113220238917, 55.9163017273429), 0.0, 0.0, 676.0, '78K', 'Seaplane Base', 'Yes Bay Lodge', 941.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (19, (-133.94561767581507, 56.972995757848025), 0.0, 0.0, 679.0, 'KAE', 'Seaplane Base', 'Kake', 3466.0, 'AK', 'Wrangell-Petersburg Census Area', '02280', '02')
# (21, (-134.58509826677158, 57.503555298238496), 0.0, 0.0, 681.0, 'AGN', 'Seaplane Base', 'Angoon', 2865.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (22, (-134.89790344209013, 58.254386901634234), 0.0, 0.0, 682.0, 'FNR', 'Seaplane Base', 'Funter Bay', 303.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (23, (-135.21844482396943, 57.779659271258424), 0.0, 0.0, 683.0, 'TKE', 'Seaplane Base', 'Tenakee', 1072.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (24, (-134.7559509276931, 58.127441406595665), 0.0, 0.0, 684.0, 'HWI', 'Seaplane Base', 'Hawk Inlet', 1073.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (27, (-136.23626708985427, 57.955173492462734), 0.0, 0.0, 687.0, 'PEC', 'Seaplane Base', 'Pelican', 1022.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (28, (-136.34739685018445, 58.19518280014614), 0.0, 0.0, 688.0, 'ELV', 'Seaplane Base', 'Elfin Cove', 1325.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (29, (-135.44903564427955, 58.42049789426244), 0.0, 0.0, 689.0, 'EXI', 'Seaplane Base', 'Excursion Inlet', 1972.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (35, (-154.24784851060025, 56.899486541670626), 0.0, 0.0, 695.0, 'ALZ', 'Seaplane Base', 'Alitak', 313.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (37, (-153.32060241696794, 57.73037338252561), 0.0, 0.0, 697.0, 'WSJ', 'Seaplane Base', 'San Juan/Uganik Bay', 335.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (40, (-152.39138793940185, 57.78083419774009), 0.0, 0.0, 700.0, 'T44', 'Seaplane Base', 'Trident Basin', 2625.0, ' ', 'Kodiak Island Borough', '02150', '02')
# (46, (-159.48866271950888, 55.897533416733836), 0.0, 0.0, 706.0, 'KIB', 'Seaplane Base', 'Ivanof Bay', 277.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (68, (-155.77738952630557, 58.55484390232431), 0.0, 0.0, 728.0, '5Z9', 'Seaplane Base', 'Lake Brooks', 5251.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (85, (-149.9719390869193, 61.18000412029397), 0.0, 0.0, 745.0, 'LHD', 'Seaplane Base', 'Lake Hood', 26733.0, 'AK', 'Anchorage Borough', '02020', '02')
# (92, (-165.78530883823228, 54.13246536298618), 0.0, 0.0, 752.0, 'KQA', 'Seaplane Base', 'Akutan', 2313.0, ' ', 'Aleutians East Borough', '02013', '02')
# (128, (-161.43507385227645, 60.90786361691244), 0.0, 0.0, 788.0, 'KKI', 'Seaplane Base', 'Akiachak', 2250.0, 'AK', 'Bethel Census Area', '02050', '02')
# (147, (-164.65621948284283, 60.92365264895062), 0.0, 0.0, 807.0, 'WWT', 'Seaplane Base', 'Newtok', 1683.0, 'AK', 'Bethel Census Area', '02050', '02')
# 249
count = 0
for row in cursor:
    print(row)
    count +=1 
print(count)
# 0
cursor = arcpy.da.SearchCursor(fc,['*'],"FEATURE = 'Seaplane Base'")
for row in cursor:
    print(row)
    count +=1 
print(count)
# (1, (-130.01252746616962, 55.904338836668046), 0.0, 0.0, 5.0, '4Z7', 'Seaplane Base', 'Hyder', 319.0, ' ', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (5, (-131.68510436997065, 55.34780883790762), 0.0, 0.0, 10.0, '5KE', 'Seaplane Base', 'Ketchikan Harbor', 46644.0, 'AK', 'Ketchikan Gateway Borough', '02130', '02')
# (6, (-131.57806396458028, 55.13104629555016), 0.0, 0.0, 666.0, 'MTM', 'Seaplane Base', 'Metlakatla', 15387.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (7, (-133.24333190904036, 55.29632186925892), 0.0, 0.0, 667.0, 'KWF', 'Seaplane Base', 'Waterfall', 2018.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (9, (-132.39752197266085, 55.537414550641074), 0.0, 0.0, 669.0, 'KXA', 'Seaplane Base', 'Kasaan', 455.0, ' ', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (10, (-132.6460876461279, 55.48158645644986), 0.0, 0.0, 670.0, 'HYL', 'Seaplane Base', 'Hollis', 4170.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (11, (-133.14779663041014, 55.47883224491221), 0.0, 0.0, 671.0, 'CGA', 'Seaplane Base', 'Craig', 5898.0, ' ', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (12, (-132.53668212897702, 55.687961578264265), 0.0, 0.0, 672.0, 'KTB', 'Seaplane Base', 'Thorne Bay', 5210.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (13, (-132.84196472179445, 56.00324249274689), 0.0, 0.0, 673.0, 'KCC', 'Seaplane Base', 'Coffman Cove', 705.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (14, (-132.25502014156626, 55.739635467402934), 0.0, 0.0, 674.0, '84K', 'Seaplane Base', 'Meyers Chuck', 341.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (16, (-131.80113220238917, 55.9163017273429), 0.0, 0.0, 676.0, '78K', 'Seaplane Base', 'Yes Bay Lodge', 941.0, 'AK', 'Prince of Wales-Outer Ketchikan Census Area', '02201', '02')
# (19, (-133.94561767581507, 56.972995757848025), 0.0, 0.0, 679.0, 'KAE', 'Seaplane Base', 'Kake', 3466.0, 'AK', 'Wrangell-Petersburg Census Area', '02280', '02')
# (21, (-134.58509826677158, 57.503555298238496), 0.0, 0.0, 681.0, 'AGN', 'Seaplane Base', 'Angoon', 2865.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (22, (-134.89790344209013, 58.254386901634234), 0.0, 0.0, 682.0, 'FNR', 'Seaplane Base', 'Funter Bay', 303.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (23, (-135.21844482396943, 57.779659271258424), 0.0, 0.0, 683.0, 'TKE', 'Seaplane Base', 'Tenakee', 1072.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (24, (-134.7559509276931, 58.127441406595665), 0.0, 0.0, 684.0, 'HWI', 'Seaplane Base', 'Hawk Inlet', 1073.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (27, (-136.23626708985427, 57.955173492462734), 0.0, 0.0, 687.0, 'PEC', 'Seaplane Base', 'Pelican', 1022.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (28, (-136.34739685018445, 58.19518280014614), 0.0, 0.0, 688.0, 'ELV', 'Seaplane Base', 'Elfin Cove', 1325.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (29, (-135.44903564427955, 58.42049789426244), 0.0, 0.0, 689.0, 'EXI', 'Seaplane Base', 'Excursion Inlet', 1972.0, 'AK', 'Skagway-Hoonah-Angoon Census Area', '02232', '02')
# (35, (-154.24784851060025, 56.899486541670626), 0.0, 0.0, 695.0, 'ALZ', 'Seaplane Base', 'Alitak', 313.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (37, (-153.32060241696794, 57.73037338252561), 0.0, 0.0, 697.0, 'WSJ', 'Seaplane Base', 'San Juan/Uganik Bay', 335.0, 'AK', 'Kodiak Island Borough', '02150', '02')
# (40, (-152.39138793940185, 57.78083419774009), 0.0, 0.0, 700.0, 'T44', 'Seaplane Base', 'Trident Basin', 2625.0, ' ', 'Kodiak Island Borough', '02150', '02')
# (46, (-159.48866271950888, 55.897533416733836), 0.0, 0.0, 706.0, 'KIB', 'Seaplane Base', 'Ivanof Bay', 277.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (68, (-155.77738952630557, 58.55484390232431), 0.0, 0.0, 728.0, '5Z9', 'Seaplane Base', 'Lake Brooks', 5251.0, 'AK', 'Lake and Peninsula Borough', '02164', '02')
# (85, (-149.9719390869193, 61.18000412029397), 0.0, 0.0, 745.0, 'LHD', 'Seaplane Base', 'Lake Hood', 26733.0, 'AK', 'Anchorage Borough', '02020', '02')
# (92, (-165.78530883823228, 54.13246536298618), 0.0, 0.0, 752.0, 'KQA', 'Seaplane Base', 'Akutan', 2313.0, ' ', 'Aleutians East Borough', '02013', '02')
# (128, (-161.43507385227645, 60.90786361691244), 0.0, 0.0, 788.0, 'KKI', 'Seaplane Base', 'Akiachak', 2250.0, 'AK', 'Bethel Census Area', '02050', '02')
# (147, (-164.65621948284283, 60.92365264895062), 0.0, 0.0, 807.0, 'WWT', 'Seaplane Base', 'Newtok', 1683.0, 'AK', 'Bethel Census Area', '02050', '02')
# 28
accum = 0
count = 0
cursor = arcpy.da.SearchCursor(fc,['NAME'])
cursor = arcpy.da.SearchCursor(fc,['*'])
cursor = arcpy.da.SearchCursor(fc,['*','TOTAL_ENP'])
for row in cursor:
    accum += row[1]
    count += 1
print("the average is ", accum/num, " and the total enplanement is " accum)
#   File "<string>", line 4
#     print("the average is ", accum/num, " and the total enplanement is " accum)
#                                                                              ^
# SyntaxError: invalid syntax
for row in cursor:
    accum += row[1]
    count += 1
print("the average is ", accum/num, " and the total enplanement is " + accum)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# RuntimeError: Cannot find field 'TOTAL_ENP'
cursor = arcpy.da.SearchCursor(fc,['*','TOT_ENP'])
for row in cursor:
    accum += row[1]
    count += 1
print("the average is ", accum/num, " and the total enplanement is " + accum)
# Traceback (most recent call last):
#   File "<string>", line 2, in <module>
# TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
accum = 0
count = 0
for row in cursor:
    accum += row[1]
    count += 1
print("the average is ", accum/num, " and the total enplanement is " + accum)
# Traceback (most recent call last):
#   File "<string>", line 2, in <module>
# TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
cursor = arcpy.da.SearchCursor(fc,['*','TOT_ENP'])
for row in cursor:
    accum += row[1]
    count += 1
print("the average is ", accum/num, " and the total enplanement is " + accum)
# Traceback (most recent call last):
#   File "<string>", line 2, in <module>
# TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
for row in cursor:
    accum += row[0]
    count += 1
print("the average is ", accum/num, " and the total enplanement is " + accum)
# Traceback (most recent call last):
#   File "<string>", line 4, in <module>
# NameError: name 'num' is not defined
for row in cursor:
    accum += row[1]
    count += 1
print("the average is ", accum/count, " and the total enplanement is " + accum)
# Traceback (most recent call last):
#   File "<string>", line 4, in <module>
# TypeError: must be str, not int
for row in cursor:
    accum += row[1]
    count += 1
print("the average is " + accum/count + " and the total enplanement is " + accum)
# Traceback (most recent call last):
#   File "<string>", line 4, in <module>
# TypeError: must be str, not float
cursor = arcpy.da.SearchCursor(fc, ['feature'])
values = [row[0] for row in cursor]
values
# ['Seaplane Base', 'Airport', 'Airport', 'Airport', 'Seaplane Base', 'Seaplane Base', 'Seaplane Base', 'Airport', 'Seaplane Base', 'Seaplane Base', 'Seaplane Base', 'Seaplane Base', 'Seaplane Base', 'Seaplane Base', 'Airport', 'Seaplane Base', 'Airport', 'Airport', 'Seaplane Base', 'Airport', 'Seaplane Base', 'Seaplane Base', 'Seaplane Base', 'Seaplane Base', 'Airport', 'Airport', 'Seaplane Base', 'Seaplane Base', 'Seaplane Base', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Seaplane Base', 'Airport', 'Seaplane Base', 'Airport', 'Airport', 'Seaplane Base', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Seaplane Base', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Seaplane Base', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Seaplane Base', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Seaplane Base', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Seaplane Base', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Seaplane Base', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport', 'Airport']
unique = set(values)
unique
# {'Airport', 'Seaplane Base'}
set([row[0] for row in cursor])
# set()
cursor = arcpy.da.SearchCursor(fc, ['feature'])
set([row[0] for row in cursor])
# {'Airport', 'Seaplane Base'}
cursor = arcpy.da.UpdateCursor(fc,['STATE'], "STATE ,. 'AK'")
for row in cursor:
    row[0] = 'AK'
    cursor.updateRow(row)
del row
del cursor
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# RuntimeError: An invalid SQL statement was used. [SELECT STATE, OBJECTID FROM airports WHERE STATE ,. 'AK']
cursor = arcpy.da.UpdateCursor(fc,['STATE'], "STATE <> 'AK'")
for row in cursor:
    row[0] = 'AK'
    cursor.updateRow(row)
del row
del cursor
cursor = arcpy.da.UpdateCursor(fc,['STATE'], "TOT_ENP < 50000")
for row in cursor:
    cursor.deleteRow(row)
del row
del cursor
# Traceback (most recent call last):
#   File "<string>", line 2, in <module>
# TypeError: deleteRow() takes no arguments (1 given)
for row in cursor:
    cursor.deleteRow(row[0])
del row
del cursor
# Traceback (most recent call last):
#   File "<string>", line 2, in <module>
# TypeError: deleteRow() takes no arguments (1 given)
for row in cursor:
    cursor.deleteRow()
del row
del cursor
cursor = arcpy.da.UpdateCursor('airports_1',['STATE'], "TOT_ENP < 50000")
for row in cursor:
    cursor.deleteRow()
del row
del cursor
fc2 = "airports2"
cursor = arcpy.da.InsertCursor(fc2, ['NAME'])
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# RuntimeError: cannot open 'airports2'
fc2 = "airports_1"
cursor = arcpy.da.InsertCursor(fc2, ['NAME'])
cursor.insertRow(['New Airport'])
# 222
cursor = arcpy.da.UpdateCursor('airports_1',['STATE'], "TOT_ENP < 50000")
cursor = arcpy.da.UpdateCursor('airports_1',['STATE'], "TOT_ENP < 50000")
for row in cursor:
    cursor.deleteRow()
del row
del cursor
def delaprts():
    fc = arcpy.CopyFeatures_namagement('airports', 'airports2')
    cursor = arcpy.da.UpdateCursor(fc, ['TOT_ENP'],'TOT_ENP < 50000')
    for row in cursor:
        cursor.deleteRow()
    del cursor
    del row
delaprts()
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
#   File "<string>", line 2, in delaprts
# AttributeError: module 'arcpy' has no attribute 'CopyFeatures_namagement'
def delaprts():
    fc = arcpy.CopyFeatures_management('airports', 'airports2')
    cursor = arcpy.da.UpdateCursor(fc, ['TOT_ENP'],'TOT_ENP < 50000')
    for row in cursor:
        cursor.deleteRow()
    del cursor
    del row
delaprts()