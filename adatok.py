class data:



    # Kik legyenek a támadók
    #attackers = [False, False, False, False, False]
    attackers = [True, True, True, True, True]

    # Milyen százalékban hajtsanak végre támadást
    miss_labeling = [0,0,0,0,0]
    #miss_labeling = [90, 90, 90, 90, 90]

    #noise = [0,0,0,0,0]
    noise = [90, 90, 50, 10, 10]

    #-------------------------------------------------------------------------------------------------------------------
    #INNENTŐL MÉG SEMMI SEM HASZNÁLHATÓ
    #-------------------------------------------------------------------------------------------------------------------

    #Még nem használható
    to_lie = [0,0,0,0,0]

    data_are_correct = None
    # Hova legyenek kiírva az eredmények
    results_path = 'eredmenyek.txt'
    # A kísérlet paraméterei
    number_users = 5

    #Még nem használható
    secure_aggregation = False  # A false azt jelenti, hogy minden tanítási kombinációt minden teszt kombinációval végignéz
    # True esetén: Tanítási koalíciók: 1. Mindenki benne van, 2. Mindenki kivétel a teszelő, 3. Csak a tesztelő
    # True esetén: Tesztelési koalíciók: 1. Mindenki benne van, 2. Csak 1 résztvevő van benne

    # Melyik résztvevőnek milyen százalékban oszoljanak el az adatai a számok között [0,1,2,3,4,5,6,7,8,9]
    user_labels_percents = [
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    ]

    # Hány képet kapjon a résztvevő
    user_images_count = [
        200,
        200,
        200,
        200,
        200
    ]


    #Ezeket az init függvénynek kell kitöltenie a beállítások szerint
    train_groups_in_binary = []
    actual_train_group_in_binary = []

    test_groups_in_binary = []
    actual_test_group_in_binary = []

    actual_user=0


def init():
    #Adatok ellenőrzése
    data.data_are_correct = is_data_correct()
    if not data.data_are_correct != False:  #Ha nem helyesek az adatok visszatérünk
        return

    if data.secure_aggregation:
        for i in range(1, 2 ** data.number_users - 1):
            binary = numberToBinary(i)
            sum_of_binary = sum(binary)  # Hány résztvevő van a koalícióban
            if sum_of_binary == 1 or sum_of_binary == data.number_users:  # Mindenki és külön csak az 1 résztvevősök
                data.train_groups_in_binary.append(binary)
                data.test_groups_in_binary.append(binary)

            # A tanításnál azt is meg kell nézni amikor a tesztelő nincs benne
            if sum_of_binary == data.number_users - 1:
                data.train_groups_in_binary.append(binary)

    else:
        for i in range(1, 2 ** data.number_users - 1):
            binary = numberToBinary(i)
            data.train_groups_in_binary.append(binary)
            data.test_groups_in_binary.append(binary)

    data.actual_test_group_in_binary =  data.test_groups_in_binary[0]
    data.actual_train_group_in_binary = data.train_groups_in_binary[0]


# Adatok ellenőrzése (Ne tanítás közben derüljön ki, hogy valamit nem jól adtunk meg.
def is_data_correct():
    check_these_data = [data.attackers, data.miss_labeling, data.noise, data.user_labels_percents,
                         data.user_images_count]
    for i in check_these_data:
        if check_data(i) == False:
            return False
    for i in data.user_labels_percents:
        if len(i) < 10 and sum(i)!=100:
            print("Error: Percents are not 10 long or sum not 100: "+i)
            return False
    return True


def check_data(list):
    for i in list:
        if len(i) < data.number_users:
            print("Error with data: " + i)
            return False
    return True


def numberToBinary(number):
    x = []
    a = "{0:b}".format(number)
    for j in a:
        x.append(int(j))
    for j in range(len(x), data.number_users):
        x.insert(0, 0)
    return x