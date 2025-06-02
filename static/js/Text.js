
function upload(){
    const input_textarea = document.getElementById('input_text');
    const output_textarea = document.getElementById('output_text');
    var msg = new FormData

    const radio = document.querySelector('input[name="option"]:checked');
    if (radio == null){
        let button = document.getElementById('upload')
        button.innerHTML = 'select an option';

    }else{

       
    msg['option'] = radio.id;  
    msg['text'] = input_textarea.value;
    msg['select_start'] = input_textarea.selectionStart
    msg['select_end'] = input_textarea.selectionEnd

    
    fetch('/change', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(msg)
    }).then(response => response.text())
    .then(response =>{
        output_textarea.innerHTML = response;
    })} 
}