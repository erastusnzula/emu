const collapseToggle = document.getElementById("collapse-bars");
const closeNavItems = document.getElementById("close");
const navItems = document.getElementById("nav-items");

if(collapseToggle){
    collapseToggle.addEventListener('click', ()=>{
        navItems.classList.add("active");
    })
}

if(closeNavItems){
    closeNavItems.addEventListener("click", ()=>{
        navItems.classList.remove("active");
    })
}