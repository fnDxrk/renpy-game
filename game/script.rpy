define a = Character('Хан', color="000DD0")

init python:
    def calcRes(arr):
        return arr.count(True)

label start:
    play music ["music.mp3"] loop volume 0.3
    scene b4
    show h1 with dissolve
    a "Привет! Меня зовут Хан!" 
    a "В этой игре я тебе расскажу, как нужно себя веcти на уроке, а также как правильно сидеть за партой!"
    a "После обучения ты можешь пройти тест на проверку знаний, если ты конечно не против."
    hide h1 with dissolve

label behavior:
    scene bg
    show h1 with dissolve
    a "Сперва ты узнаешь, как нужно правильно ввести себя на уроке."
    hide h1 with dissolve
    scene 1
    show h1 at right with dissolve
    a "1.Перед началом урока учащиеся должны подготовить и выложить на парту: учебник, тетрадь, дневник и пенал."
    scene 2
    show h1 at right with dissolve
    a "2.По звонку учащиеся должны занять места за партами."
    scene 3
    show h1 at left with dissolve
    a "3.Вежливость и уважение к другим людям обязательны на уроке."
    scene 4
    show h1 at right with dissolve
    a "4.Во время урока нужно вести себя спокойно: не кричать, не перебивать учителя и не заниматься посторонними делами."
    scene 5
    show h1 at right with dissolve
    a "5.Если хочется ответить на вопрос учителя или задать свой вопрос, то поднимите руку и дождитесь обращения учителя."
    scene 6
    show h1 at left with dissolve
    a "6.Если во время урока вам нужно выйти из класса, поднимите руку и дождитесь обращения учителя."
    scene 7
    show h1 at left with dissolve
    a "7.Если ваш одноклассник отвечает на вопрос, то нельзя его перебивать."
    scene 8
    show h1 at right with dissolve
    a "8.Если вас вызывают отвечать, то говорите громко и чётко, выражайте свои мысли полными предложениями."
    scene 9
    show h1 at right with dissolve
    a "9.В тетрадях и в дневнике пишите разборчиво и аккуратно."
    scene 10
    show h1 at left with dissolve
    a "10.Когда учитель или другой взрослый входит в класс, учащиеся встают, приветствуя его."
    scene 11
    show h1 at right with dissolve
    a "11.Не пользуйтесь во время урока мобильным телефоном."
    scene 12
    show h1 at left with dissolve
    a "12.Услышав звонок, возвещающий об окончании урока, не вскакивайте с места. Покидать класс можно только с разрешения учителя."

label posture:
    scene bg
    show h1 with dissolve
    a "А теперь давай узнаем, как нужно правильно сидеть за партой, чтобы спина всегда оставалась ровной и красивой."
    hide h1
    scene 01
    show h1 with dissolve
    a "1.При нормальной осанке у школьника плечи расположены горизонтально, лопатки прижаты к спине."
    a "2.Спина должна быть под углом в 90 градусов и прикасаться к спинке стула."
    a "3.Правая и левая половины туловища при осмотре спереди и сзади симметричны."
    a "4.Шея ровная, не вытянута вперёд и не наклона вниз."
    a "5.Локти должны находиться на парте."
    a "6.Ноги стоят на полу всей поверхностью стоп."
    hide h1 with dissolve


label test0:
    scene b3
    show h3 with dissolve
    a "Ты прошёл обучение!"
    hide h3
    show h1 at right with dissolve
    menu:   
        a "Желаешь пройти тест по пройденному материалу?"
        "Да":
            hide h1 
            show h2 with dissolve
            a "Хорошо, тогда приступим."
            jump test
        "Нет":
            hide h1 with dissolve
            show h1 with dissolve
            a "Тогда я с тобой прощаюсь."
            hide h1 
            show h2
            a "До скорой встречи!"
            return
label test:    
    
    scene bg
    show h1 at right with dissolve
    menu:
        a "Что ты должен подготовить на парте перед уроком?"

        "Учебник, тетрадь, дневник и пенал":
            $ question0 = 1
        "Дневник, телефон, наушники":
            $ question0 = 0
        "Бейсбольную биту, мяч, перчатку":
            $ question0 = 0
    
    if question0 == 1:
        $ results[0] = True

    menu:
        a "Как себя нужно вести во время урока?"

        "Кричать, бегать по классу":
            $ question1 = 0
        "Рисовать в тетрадке":
            $ question1 = 0
        "Быть спокойным, слушать учителя и выполнять задания":
            $ question1 = 1
    
    if question1 == 1:
        $ results[1] = True

    menu:
        a "Что нужно сделать, чтобы ответить на вопрос учителя?"

        "Поднять руку и ждать разрешения учителя":
            $ question2 = 1
        "Выкрикнуть ответ":
            $ question2 = 0
    
    if question2 == 1:
        $ results[2] = True

    menu:
        a "Где должны находится локти, когда сидишь за партой?"

        "На воздухе":
            $ question3 = 0
        "На парте":
            $ question3 = 1
        "На стуле":
            $ question3 = 0
    
    if question3 == 1:
        $ results[3] = True

    menu:
        a "Под каким углом должна находится спина относительно стула?"

        "45 градусов":
            $ question4 = 0
        "90 градусов":
            $ question4 = 1
        "60 градусов":
            $ question4 = 0
    
    if question4 == 1:
        $ results[4] = True

    menu:
        a "Что нужно сделать, когда заходит учитель в класс?"

        "Ничего не делать":
            $ question5 = 0
        "Встать и поприветствовать его":
            $ question5 = 1
    
    if question5 == 1:
        $ results[5] = True

    menu:
        a "В тетрадях и дневнике нужно ..."

        "Красиво и разборчиво писать":
            $ question6 = 1
        "Рисовать каракули":
            $ question6 = 0
#        "":
#            $ question6 = 0
    
    if question6 == 1:
        $ results[6] = True

    menu:
        a "Что нужно сделать, чтобы выйти из класса?"

        "Просто выйти":
            $ question7 = 0
        "Спросить учителя":
            $ question7 = 1
    
    if question7 == 1:
        $ results[7] = True

    menu:
        a "При нормальной осанке у школьника плечи расположены ..."

        "Вертикально":
            $ question8 = 0
        "Горизонтально":
            $ question8 = 1
    
    if question8 == 1:
        $ results[8] = True

    menu:
        a "Что нужно сделать, когда прозвенит звонок?"

        "Выйти из класса":
            $ question9 = 0
        "Ждать разрешения учителя":
            $ question9 = 1
        "Начать кричать: \"Ура!\" ":
            $ question9 = 0
    
    if question9 == 1:
        $ results[9] = True



label result:
    scene b4
    show h3 with dissolve
    a "Поздравляю, ты завершил тест!"
    hide h3
    show h1
    with dissolve
    a "А теперь узнаем твой результат."
    $ answer = int(calcRes(results))
    hide h3
    show h
    with dissolve
    a "Ты ответил ..."
    with dissolve
    hide h1
    if answer == 1:
        show h with dissolve
        a "Ты ответил на 1 правильный вопрос из 10."
        a "Твоя оценка — 2"
        a "К сожалению, ты получил плохую отметку за этот тест..."
        hide h
        show h1 at right with dissolve
        menu:
            a "Хочешь перепройти тест ещё раз?"
            "Да":
                menu:
                    a "Хочешь повторить изученный материал или сразу начать с теста?"
                    "Повторить изученный материал":
                        jump repeat
                    "Начать с теста":
                        jump test
            "Нет":
                hide h1 
                show h1 with dissolve                
                a "Тогда я с тобой прощаюсь."
                hide h1
                show h2
                a "До скорой встречи!"
                return
    if 0 <= answer < 4:
        show h with dissolve
        a "Ты ответил на [answer] правильных вопросов из 10."
        a "Твоя оценка — 2!"
        a "К сожалению, ты получил плохую отметку за этот тест..."
        hide h with dissolve
        show h1 at right with dissolve
        menu:
            a "Хочешь перепройти тест ещё раз?"
            "Да":
                menu:
                    a "Хочешь повторить изученный материал или сразу начать с теста?"
                    "Повторить изученный материал":
                        jump repeat
                    "Начать с теста":
                        jump test
            "Нет":
                hide h1 with dissolve
                show h1 with dissolve
                a "Тогда я с тобой прощаюсь."
                hide h1
                show h2
                a "До скорой встречи!"
                return
    
    if 4 <= answer < 6:
        show h1 with dissolve
        a "Ты ответил на [answer] правильных вопросов из 10."
        a "Твоя оценка — 3!"
        a "Ты получил удовлетворительную отметку за тест."
        hide h
        hide h1
        show h1 at right with dissolve
        menu:
            a "Хочешь перепройти тест ещё раз?"
            "Да":
                menu:
                    a "Хочешь повторить изученный материал или сразу начать с теста?"
                    "Повторить изученный материал":
                        jump repeat
                    "Начать с теста":
                        jump test
            "Нет":
                a "Тогда я с тобой прощаюсь."
                hide h1
                show h2
                a "До скорой встречи!"
                return

    if 6 <= answer < 8:
        show h2 with dissolve
        a "Ты ответил на [answer] правильных вопросов из 10."
        a "Твоя оценка — 4!"
        a "Ты получил хорошую отметку за тест!"
        hide h
        hide h2 with dissolve

    if 8 <= answer <= 10:
        show h3 with dissolve
        a "Ты ответил на [answer] правильных вопросов из 10."
        a "Твоя оценка — 5!"
        a "Ты получил отличную отметку за тест!"
        hide h
        hide h3 with dissolve
    
    show h1 with dissolve
    a "А теперь, я с тобой прощаюсь."
    hide h1
    show h3 
    a "До скорой встречи!"
    