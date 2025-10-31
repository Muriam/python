function time()
{
    let date = new Date();          // получение текущей даты
    let time = date.getHours();     // получение текущего времени в часах

    if (time > 5 && time < 11)      // если время от 5 до 11
        document.write('Доброе утро!');
    else if (time > 11 && time < 18)
        document.write('Добрый день!');
    else if (time > 18 && time < 23)
        document.write('Добрый вечер!');
    else
        document.write('Спи давай');
}


