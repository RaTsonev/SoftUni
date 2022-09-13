skumriq = float(input())
caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

palamud = (skumriq + skumriq*0.6)*kg_palamud
safrid = (caca + caca*0.8)*kg_safrid
midi = kg_midi*7.5
final_price = palamud + safrid + midi
print(f"{final_price:.2f}")