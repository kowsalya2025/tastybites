let slides = document.querySelectorAll(".slide")
let dots = document.querySelectorAll(".dot")

let index = 0

function showSlide(){

slides.forEach((slide)=>{
slide.classList.remove("active")
})

dots.forEach((dot)=>{
dot.classList.remove("active")
})

slides[index].classList.add("active")
dots[index].classList.add("active")

index++

if(index == slides.length){
index = 0
}

}

setInterval(showSlide,4000)