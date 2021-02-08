let button = document.querySelectorAll('.button1');
console.log(button)
let mymodal = document.querySelector('.mymodal');
let closebutton = document.querySelector('.closemodal');

function modalopen(){
	mymodal.style.display = 'block';
}

for (i=0; i < button.length; i++){
button[i].addEventListener('click',modalopen);
}

function closemodal(){
mymodal.style.display = 'none';
}
closebutton.onclick = closemodal;