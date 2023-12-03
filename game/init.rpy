# Вы можете расположить сценарий своей игры в этом файле.
define config.end_splash_transition = Dissolve(1.0)
# Определение персонажей игры.
define m = Character("Мама", color="313447")
define e = Character("Егор", color="1B9753")
define i = Character("Ирина", color="8378C8")
define a = Character("Александра Владимировна", color="ff0000")

# Backgrounds
image room = "bg/room_in_day.jpg"
image school = "bg/school.jpg"
# image black = "bg/black.jpg"
image episode_1 = "bg/episode_1.jpg"
image kitchen = "bg/kitchen.jpg"
image food = "bg/food.jpg"
image koridor = "bg/korifor.jpg"
image street = "bg/street.jpg"
image phone = "bg/phone.jpg"
image streetDog = "bg/street_with_dog.jpg"
image episode_end = "bg/episode_end.jpg"
image street_with_tree = "bg/street_with_tree.jpg"
image fall_dog = "bg/fall_dog.jpg"
image vorota = "bg/vorota.jpg"
image tolpa = "bg/tolpa.jpg"
image tolpa_no = "bg/tolpa_no.jpg"
image dvor = "bg/school_dvor.jpg"
image classroom = "bg/classroom.jpg"

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
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Переменные:
$ score_ecaterina = 0
$ score_blondinka = 0
$ score_friend = 0
$ bad_condition = 0
$ good_condition = 0

# Спрайты главной героини со светлыми волосами (Имя?)
image person_1 = "characters/person_1/pers_1.png"

# Спрайты подруги дества
image friend_default = "characters/person_2/friend.png"
image friend_smile = "characters/person_2/friend_smile.png"
image friend_blush = "characters/person_2/friend_blush.png"

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
