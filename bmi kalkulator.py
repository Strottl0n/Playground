def bmi():
    return waga / (wzrost ** 2)


def main():
    calculated_bmi = bmi()
    if calculated_bmi <= 0.0018:
        print(f"BMI ({calculated_bmi:.4f} {waga_jednostka} / {wzrost_jednostka}^2) wskazuje na niedowagę. Proponowałbym skonsultować się z lekarzem, gdyż może mieć to poważny skutek na zdrowiu.")
    elif 0.0018 < calculated_bmi < 0.0024:
        print(f"BMI ({calculated_bmi:.4f} {waga_jednostka} / {wzrost_jednostka}^2) wskazuje na normalną. :)")
    elif 0.0024 <= calculated_bmi < 0.0029:
        print(f"BMI ({calculated_bmi:.4f} {waga_jednostka} / {wzrost_jednostka}^2) wskazuje na nadwagę. Jednak nie musi to oznaczać potrzeby schudnięcia. Masa mięśniowa została wliczona w ogólną masę, przez co, dla osoby ćwiczącej może to być powodem takiego wyniku.")
    elif 0.0029 <= calculated_bmi < 0.0034:
        print(f"BMI ({calculated_bmi:.4f} {waga_jednostka} / {wzrost_jednostka}^2) wskazuje na otyłość stopnia I. Nie jest to jeszcze poważny problem, jednak nie należy go zignorować. Dieta i ćwiczenia są zalecane.")
    elif 0.0034 <= calculated_bmi < 0.0039:
        print(f"BMI ({calculated_bmi:.4f} {waga_jednostka} / {wzrost_jednostka}^2) wskazuje na otyłość II stopnia. Jest to już poważny problem. Konsultacja z lekarzem jest zalecana.")
    else:
        print(f"BMI ({calculated_bmi:.4f} {waga_jednostka} / {wzrost_jednostka}^2) wskazuje na otyłość III stopnia. Jest to punkt, w którym tłuszcz może zagrażać życiu bądź zdrowiu.")

while True:
    bmi_wartosc = []

    while True:
        wzrost_jednostka = input("Jakiej jednostki wzrostu chcesz użyć? ")
        waga_jednostka = input("Jakiej jednostki wagi chcesz użyć? ")
        if wzrost_jednostka == 'cm' and waga_jednostka == 'kg':
            break
        elif wzrost_jednostka == 'ft' and waga_jednostka == 'lb':
            break
        else:
            print("Podano albo niewłaściwe jednostki albo pomieszano system imperialny z metrycznym.")

    while True:
        try:
            wzrost = int(input(f"Podaj swój wzrost ({wzrost_jednostka}): "))
            waga = int(input(f"Podaj swoją wagę ({waga_jednostka}): "))
            if wzrost_jednostka == 'cm' and 60 < wzrost < 272:
                break
            elif wzrost_jednostka == 'ft' and 2 < wzrost < 9:
                break
            elif waga_jednostka == 'kg' and 45.7 < waga < 275:
                break
            elif waga_jednostka == 'lb' and 100 < waga < 607:
                break
            else:
                print("Podana waga / wzrost są prawdopodobnie błędne. Przepraszam jeśli tak nie jest, ale założyłem pewne limity górne i dolne")
        except ValueError:
            print("Podano nie właściwą wartość / wartości.")

    main()


