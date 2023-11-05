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

const messagesClose = document.getElementById("messages-close-icon")
const messages = document.getElementById("notification-messages")

const closeMessages = ()=>{
    messages.style.display='none'
}
if(messages){
    setInterval(closeNotification, 5000)
}

function closeNotification(){
    messages.style.display='none'
}


console.log(90)