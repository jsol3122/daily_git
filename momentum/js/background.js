const images = [
    "duck.jfif", "rabbit.jfif", "cat.jfif"
];
const img = document.querySelector('#bgImg');

const chosenImage = images[Math.floor(Math.random()*images.length)]

document.body.style.background = 'white';
img.src =  `img/${chosenImage}`;


