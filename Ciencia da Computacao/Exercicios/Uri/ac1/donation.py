donation = []

while True:
    askDonation = float(input())
    if(askDonation == -1.0):
        break
    donation.append(askDonation)

vc = sum(donation)
valor = sum(donation) * 2.50

print(f'VC$ {vc:.2f}')
print(f'R$ {valor:.2f}')