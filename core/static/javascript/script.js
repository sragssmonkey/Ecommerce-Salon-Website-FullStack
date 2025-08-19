const main = document.querySelector("#main");
const brand=document.querySelector("#brand");
const photo=document.querySelector("#photos");

window.addEventListener("load", () => {
  setTimeout(() => {
    const left = document.querySelectorAll(".left");
    const right = document.querySelectorAll(".right");

    let index = 0;

    const interval = setInterval(() => {
      // Hide previous elements
      if (index > 0) {
        left[index - 1].style.opacity = "0";
        right[index - 1].style.opacity = "0";
      }

      // Show current elements
      if (index < left.length && index < right.length) {
        left[index].style.transition = "opacity 1s ease";
        right[index].style.transition = "opacity 1s ease";
        left[index].style.opacity = "1";
        right[index].style.opacity = "1";
        index++;
      } else {
        clearInterval(interval);
        
        // Add final headline after all transitions
        const newname = document.createElement("h1");
        newname.innerHTML = "THE BANG THEORY";
        newname.classList.add("font-mono", "text-white", "text-4xl", "text-center", "mt-8","w-full","absolute");


        main.appendChild(newname);
      }
    }, 2000);
  }, 1000);
});


