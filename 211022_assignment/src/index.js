const default_length = window.innerWidth;
const body = document.body.classList;
const changeOrange = "changeOrange";
const changeBlue = "changeBlue";

function resizeEvent() {
  if (window.innerWidth > default_length + 200) {
    body.add(changeOrange);
    if (body.contains(changeBlue)) {
      body.remove(changeBlue);
    }
  } else if (window.innerWidth < default_length - 200) {
    body.add(changeBlue);
    if (body.contains(changeOrange)) {
      body.remove(changeOrange);
    }
  } else {
    body.remove(changeBlue);
    body.remove(changeOrange);
  }
}

window.addEventListener("resize", resizeEvent);
