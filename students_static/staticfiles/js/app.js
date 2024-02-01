let change_bg = document.querySelectorAll("#change_bg")
for (let i = 0; i < change_bg.length; i++) {
    
    change_bg[i].style.cssText = `background-color:${change_bg[i].textContent} !important;
    padding:0px 10px;
    border:1px solid light${change_bg[i].textContent} !important;
    border-radius:10px;
    color:black;
    font-weight:600;`
if(change_bg[i].textContent.length == 36){
    change_bg[i].textContent = 'Good'
}
if(change_bg[i].textContent.length == 35){
    change_bg[i].textContent = 'The Best'
    change_bg[i].style.cssText += `box-shadow:0px 0px 20px green;`
}
if(change_bg[i].textContent.length == 33){
    change_bg[i].textContent = 'Not Bad'
}
}
let to_bottom = document.querySelector('.to_bottom')
let search_box = document.querySelector('.search_box')
to_bottom.addEventListener('click' , ()=>{
    search_box.style.cssText = `trnsform:translateY(-0px)`
})

let payment = document.querySelector('#payment')
let wrapper = document.querySelector('.wrapper')
let left = document.querySelector('.left')
let bottom = document.querySelector('.bottom')
let age = document.querySelector('#age')
let lvl = document.querySelector('.lvl')
let right = document.querySelector('.right')
payment.addEventListener('click' , ()=>{
    wrapper.style.cssText = `transform:translate(150px)`;
    left.style.cssText = `transform:translate(0px)`
})
age.addEventListener('click' , ()=>{
    wrapper.style.cssText = `transform:translateY(150px)`
    bottom.style.cssText = `transform:translateY(0px)`
})
lvl.addEventListener('click' , ()=>{
    wrapper.style.cssText = `transform:translateX(-150px)`
    right.style.cssText = `transform:translateY(0px)`
})