krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]

print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])
print(len(krediler)) # length

krediler[0] = "Çabuk kredi"
print(krediler)

# print(krediler[5])

for kredi in krediler:
    print("<option>" + kredi + "<option>")

for i in range(len(krediler)):
    print(krediler[i])

for i in range(3, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)
