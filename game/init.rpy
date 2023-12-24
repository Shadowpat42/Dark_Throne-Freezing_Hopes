# Вы можете расположить сценарий своей игры в этом файле.
define config.end_splash_transition = Dissolve(1.0)
# Определение персонажей игры.
define m = Character("Мама", color="313447")
define e = Character("Егор", color="1B9753")
define i = Character("Ирина", color="8378C8")
define a = Character("Александра Владимировна", color="ff0000")
define d = Character("Даша")
define k = Character("Катя")

# Backgrounds:

# Фоны дома ГГ:
image room_in_day = "bg/room_in_day.jpg"
image room_in_night = "bg/room_in_night.jpg"
image kitchen = "bg/kitchen.jpg"
image kitchen_dark = "bg/kitchen_dark.jpg"
image food = "bg/food.jpg"
image food_2 = "bg/food_2.jpg"
image koridor = "bg/korifor.jpg"
image koridor_dark = "bg/koridor_dark.jpg"
image cake = "bg/cake.jpg"
image piece_of_cake = "bg/piece_of_cake.jpg"

# Фоны с улицей возле дома:
image street = "bg/street.jpg"
image streetDog = "bg/street_with_dog.jpg"
image fall_dog = "bg/fall_dog.jpg"

# Фон телефона со временем
image phone = "bg/phone.jpg"

# Фоны школы (наружние и внутренние):
image hall = "bg/hall.jpg"
image street_with_tree = "bg/street_with_tree.jpg"
image road_to_school = "bg/road_to_school.jpg"
image vorota = "bg/vorota.jpg"
image dvor = "bg/school_dvor.jpg"
image classroom = "bg/classroom.jpg"

# Фоны дома Ирины
image house = "bg/house.jpg"
image prohojaya = "bg/prohojaya.jpg"
image kitchen_Irina = "bg/kitchen_Irina.jpg"
image food_Irina = "bg/food_Irina.jpg"
image kitchen_Irina_1 = "bg/kitchen_Irina_1.jpg"
image kitchen_Irina_2 = "bg/kitchen_Irina_2.jpg"
image kitchen_Irina_3 = "bg/kitchen_Irina_3.jpg"
image kitchen_Irina_4 = "bg/kitchen_Irina_4.jpg"


# Фоны магазина (наружние и внутренние)
image shoping_1 = "bg/shoping_1.jpg"
image shoping_2 = "bg/shoping_2.jpg"
image shoping_3 = "bg/shoping_3.jpg"
image kassa = "bg/kassa.jpg"
image ShopStreet = "bg/ShopStreet.jpg"
image road2 = "bg/road2.jpg"

# Фоны для учительской
image office = "bg/office.jpg"
image teacher_in_office = "bg/teacher_in_office.jpg"
image  directions = "bg/directions.png"

# Фоны эпизодов:
image episode_1 = "bg/episode_1.jpg"
image episode_2 = "bg/episode_2.jpg"
image episode_3 = "bg/episode_3.jpg"
image episode_end = "bg/episode_end.jpg"

# Questions:
image questions = "bg/questions.jpg"
image question_1 = "bg/question_1.jpg"
image question_2 = "bg/question_2.jpg"
image question_3 = "bg/question_3.jpg"
image question_4 = "bg/question_4.jpg"
image question_5 = "bg/question_5.jpg"
image question_6 = "bg/question_6.jpg"

# intro
image black = "intro/black.png"
image first = "intro/first.png"
image center_text = "intro/center_text.png"
image loader0 = "intro/loader (0).png"
image loader1 = "intro/loader (1).png"
image loader2 = "intro/loader (2).png"
image loader3 = "intro/loader (3).png"
image loader4 = "intro/loader (4).png"
image loader5 = "intro/loader (5).png"
image loader6 = "intro/loader (6).png"
image loader7 = "intro/loader (7).png"
image loader8 = "intro/loader (8).png"
image loader9 = "intro/loader (9).png"
image loader10 = "intro/loader (10).png"
image loader11 = "intro/loader (11).png"


# Переменные (пока не используются)
$ score_ecaterina = 0
$ score_blondinka = 0
$ score_friend = 0
$ bad_condition = 0
$ good_condition = 0

# Спрайты главной героини со светлыми волосами (Даша)
image person_1 = "characters/person_1/pers_1.png"

# Спрайты подруги дества (Ирина)
image friend_default = "characters/person_2/friend.png"
image friend_smile = "characters/person_2/friend_smile.png"
image friend_blush = "characters/person_2/friend_blush.png"

# Спрайты главного героя:
image egor = "characters/main_hero/egor.png"

# Спрайты матери главного героя
image mother = "characters/mother/mother.png"

# Спрайты учителя
image teacher = "characters/teacher/teacher.png"
image teacher_smile = "characters/teacher/teacher_smile.png"
image teacher_smile_2 = "characters/teacher/teacher_smile_2.png"
image teacher_surprised = "characters/teacher/teacher_surprised.png"

# Заставка перед входом
label splashscreen:
    scene black
    pause(0.5)
    scene first with fade
    pause(4)
    scene black
    show center_text:
        xalign 0.5
        yalign 0.5
    with dissolve
    pause
    show loader0:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader1:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader2:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader3:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader4:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader5:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader6:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader7:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader8:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader9:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader10:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader11:
        xalign 0.95
        yalign 0.95
    pause(2)
