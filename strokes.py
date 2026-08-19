from decimal import Decimal, ROUND_HALF_UP

PLAYERS = [("Matt",2.7), ("Josh",14.5), ("Michael",12.4), ("Jon",12.5)]
TEAM_A, TEAM_B = ("Matt","Josh"), ("Michael","Jon")

# rating / slope for men, straight off the printed cards. par 72 everywhere.
COURSES = [
    ("The River",      "Thu", {"Green":(72.1,139), "White":(70.3,132)}),
    ("The Irish",      "Fri", {"Green":(72.0,137), "White":(70.3,133)}),
    ("The Straits",    "Sat", {"Green":(71.9,141), "White":(70.4,137)}),
    ("Meadow Valleys", "Sun", {"Green":(71.5,136), "White":(70.3,132)}),
]

def ch(index, cr, slope, par=72):
    """World Handicap System course handicap, rounded half up."""
    raw = Decimal(str(index)) * Decimal(slope) / Decimal(113) + (Decimal(str(cr)) - Decimal(par))
    return int(raw.quantize(Decimal('1'), rounding=ROUND_HALF_UP))

for tee in ("Green", "White"):
    print(f'\n{"="*74}\n  {tee.upper()} TEES\n{"="*74}')
    print(f'{"Course":<16}{"Day":<5}' + "".join(f'{n:>9}' for n,_ in PLAYERS)
          + f'{"us":>7}{"them":>7}{"swing":>8}')
    print("-"*74)
    for name, day, tees in COURSES:
        cr, sl = tees[tee]
        chs = {n: ch(i, cr, sl) for n, i in PLAYERS}
        low = min(chs.values())                     # low man plays off scratch
        strokes = {n: v - low for n, v in chs.items()}
        us   = sum(strokes[n] for n in TEAM_A)
        them = sum(strokes[n] for n in TEAM_B)
        print(f'{name:<16}{day:<5}' + "".join(f'{strokes[n]:>9}' for n,_ in PLAYERS)
              + f'{us:>7}{them:>7}{them-us:>+8}')
    print("-"*74)
    print("  course handicaps before subtracting the low man:")
    for name, day, tees in COURSES:
        cr, sl = tees[tee]
        print(f'    {name:<16}' + "  ".join(f'{n} {ch(i,cr,sl)}' for n,i in PLAYERS))
