from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.create_terms('P01, P02, P03, P04, P05, P06, P07, P08, G001, G002, G003, G004, G005, G006,'
                       ' G007, G008, G009, G010, G011, G012, G013, G014, G015, G016, G017, G018, G019,'
                       ' G020, G021, G022, G023, X')
P01(X) <= G001(X) & G002(X) & G003(X) & G004(X)
P02(X) <= G001(X) & G002(X) & G005(X) & G006(X)
P03(X) <= G007(X) & G008(X)
P04(X) <= G009(X) & G010(X) & G011(X) & G012(X)
P05(X) <= G014(X) & G015(X) & G016(X) & G017(X)
P06(X) <= G010(X) & G015(X) & G016(X) & G017(X) & G018(X) & G019(X)
P07(X) <= G010(X) & G019(X) & G020(X) & G021(X)
P08(X) <= G001(X) & G010(X) & G019(X) & G022(X) & G023(X)

+G009("Selim")
+G010("flo")
+G011("loic")
+G012("eric")
+G009("flo")
+G011("flo")
+G012("flo")
+G010("Selim")
+G011("Selim")
+G012("Selim")

query = 'P04(X)'
answers = pyDatalog.ask(query).answers
print(answers)