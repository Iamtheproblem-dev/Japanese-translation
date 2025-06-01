
function upload(){
    const textarea = document.getElementById('input_text');
    var msg = new FormData

    const radio = document.querySelector('input[name="option"]:checked');
    if (radio == null){
        let button = document.getElementById('upload')
        button.innerHTML = 'select an option';

    }else{

       
    msg['option'] = radio.id;  
    msg['text'] = textarea.value;
    
    fetch('/change', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(msg)
    }).then(response => response.text())
    .then(response =>{
        textarea.value = response; 
    })} 
}