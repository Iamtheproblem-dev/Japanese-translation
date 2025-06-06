const delay = ms => new Promise(res => setTimeout(res, ms));
const input_textarea = document.getElementById('input_text');
const output_textarea = document.getElementById('output_text');
async function upload(select){

    var msg = new FormData

    const radio = document.querySelector('input[name="option"]:checked');
    if (radio == null){
        let button = document.getElementById('upload')
        let inner = button.innerHTML
        button.innerHTML = '<h3>select an option</h3>';
        button.disabled = true;
        
        await delay(2000);
        button.innerHTML = inner;
        button.disabled = false;

    }else{

       
    msg['option'] = radio.id;  
    msg['text'] = input_textarea.value;
    msg['select?'] = select
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
function clear_input(){
    input_textarea.value = '';
}