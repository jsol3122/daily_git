const clockTitle = document.querySelector(".js-clock");

function dayCheck() {
  const today = new Date();
  const xmas = new Date("2021-12-24");

  const day = Math.floor((xmas - today) / (1000 * 60 * 60 * 24));
  const hours = String(
    Math.floor(((xmas - today) / (1000 * 60 * 60)) % 24)
  ).padStart(2, "0");
  const minutes = String(
    Math.floor(((xmas - today) % (1000 * 60 * 60)) / (1000 * 60))
  ).padStart(2, "0");
  const seconds = String(Math.floor(((xmas - today) / 1000) % 60)).padStart(
    2,
    "0"
  );

  clockTitle.innerHTML = `${day}d ${hours}h ${minutes}m ${seconds}s`;
}

dayCheck();
setInterval(dayCheck, 1000);
