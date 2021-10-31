const clock = document.querySelector('#clock p');
const day = document.querySelector('.date');
const list_date = document.querySelector('.todo-cmp__header p');

function getClock(){
    const d = new Date();
    const hours = String(d.getHours()).padStart(2, "0");
    const minutes = String(d.getMinutes()).padStart(2, "0");
    const seconds = String(d.getSeconds()).padStart(2, "0");

    const days = [
        'Sun',
        'Mon',
        'Tue',
        'Wed',
        'Thu',
        'Fri',
        'Sat'
    ]
    const date = d.getDate();
    const months = {
        0: 'January',
        1: 'February',
        2: 'March',
        3: 'April',
        4: 'May',
        5: 'June',
        6: 'July',
        7: 'August',
        8: 'September',
        9: 'October',
        10: 'November',
        11: 'December'
    }
    const year = d.getFullYear();

    const monthName = months[d.getMonth()]
    const dayName = days[d.getDay()]

    clock.innerText = `${hours}:${minutes}:${seconds}`;
    day.innerText = `${dayName}, ${date} ${monthName} ${year}`
    list_date.innerText = `${monthName} ${date}, ${year}` 
}
getClock();
setInterval(getClock, 1000);

