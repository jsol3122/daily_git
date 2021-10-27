const playBtn = document.querySelector("#playBtn");
const userInput = document.querySelector("#insertNumber");
const machineInput = document.querySelector("#randomNumber");
const result = document.querySelector("#result");
const hidden = document.querySelectorAll(".hidden");

function gameStart() {
  const maxNumber = document.querySelector("#maxNumber").value;
  const randomNumber = Math.ceil(Math.random() * maxNumber);
  const userNumber = document.querySelector("#userNumber").value;
  userInput.innerHTML = userNumber;
  machineInput.innerHTML = randomNumber;
  if (userNumber == randomNumber) {
    result.innerHTML = "You won!";
  } else if (userNumber != randomNumber) {
    result.innerHTML = "You lost!";
  }
  hidden[0].classList.remove("hidden");
  hidden[1].classList.remove("hidden");
}

playBtn.addEventListener("click", gameStart);
