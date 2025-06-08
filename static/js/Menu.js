const hamburger = document.getElementsByClassName('Hamburger')[0];
const dropDown  = document.getElementsByClassName('nav')[0];
dropDown.classList.toggle('closed');
hamburger.addEventListener('click',(e)=>{
    dropDown.classList.toggle('open');
    dropDown.classList.toggle('.closed');
});
const Cross = document.getElementsByClassName('Cross')[0];
Cross.addEventListener('click',(e)=>{
    dropDown.classList.toggle('open');
    dropDown.classList.toggle('closed');

});
function go(location){
    window.location.href = location;
}

