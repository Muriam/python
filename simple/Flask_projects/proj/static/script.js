function time()
{
    var date = new Date();          // получение текущей даты
    var time = date.getHours();     // получение текущего времени в часах

    if (time > 5 && time < 11)      // если время от 5 до 11
        alert('Доброе утро!');
    else if (time > 11 && time < 18)
        alert('Добрый день!');
    else if (time > 18 && time < 23)
        alert('Добрый вечер!');
    else
        alert('Спи давай');
}