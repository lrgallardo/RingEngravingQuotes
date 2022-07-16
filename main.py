#define quote function
#if ring is solid gold, base cost is 100
#10 USD per the length of the engraving
def ring_quote(engraving, solid_gold):
  q = solid_gold * (100 + 10 * len(engraving))
  return(q)

quote1 = ring_quote("It's my life, it's now or never!", True)

quote2 = ring_quote("LRGE & CLGS", True)

print("The cost is $",quote1)
print("The cost is $",quote2)