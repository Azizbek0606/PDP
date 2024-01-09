// menu button method
let menu_btn = document.querySelectorAll(".menu_btn");
let nav = document.querySelector("nav");

for (let i = 0; i < menu_btn.length; i++) {
    menu_btn[i].addEventListener('click', () => {
        nav.classList.toggle('active_nav')
    })
}
// menu button method ended

// site inducator method

window.onscroll = function () { myFunction() };
function myFunction() {
    let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrolled = (winScroll / height) * 100;
    document.getElementById("myBar").style.width = scrolled + "%";
    document.getElementById("myBar").textContent = Math.round(scrolled) + "%";
    if (Math.round(winScroll) < 2) {
        document.getElementById("myBar").textContent = "";
    }
}
// site inducator method ended

// modal all methods
let subtitle = document.querySelector('.subtitle');
let modal = document.querySelector('.first_modal_wrapper');
// open modal
function get_modal(str) {
    subtitle.textContent = str;
    modal.classList.add('active_modal')
}
// close modal
function remove_modal() {
    modal.classList.remove('active_modal')
}
// close modal and cteate new message
function create_party() {
    remove_modal()
    let elem_p = document.createElement('p');
    elem_p.classList.add('alert_p');
    elem_p.textContent = "Your party has been created"
    document.body.append(elem_p)
}
// all modal methods ended

// music band card hover effect creator
let band_card = document.querySelectorAll('.band_card');
for (let i = 0; i < band_card.length; i++) {
    band_card[i].addEventListener('mouseover', () => {
        for (let k = 0; k < band_card.length; k++) {
            band_card[k].classList.remove("active_band_card");
        }
        band_card[i].classList.add("active_band_card");
    })
}
// music band card hover effect creator