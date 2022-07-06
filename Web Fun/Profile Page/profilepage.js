function changeName(){
    var user = document.getElementById('main-user')
    user.innerText="Jane Doe";
}

var requests = 4

function removeRequest(el){
    console.log(el.parentElement);
    el.parentElement.remove();
    requests++;
    console.log(requests);
    document.querySelector('#connections').innerText = requests;
}



/*
    const acceptIcons = document.querySelectorAll(".accept-icons")
    acceptIcons.forEach(el=>{
    el.addEventListener("click", event=>{
        event.target.parentElement.remove()
    })
    })
//} */
