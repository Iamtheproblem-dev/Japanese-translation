
function upload(){
    const textarea = document.getElementById('input_text');
    msg = JSON.stringify({ 'text': textarea.value })
    fetch('/change', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: msg
    }).then(response => response.text())
    .then(response =>{
        textarea.value = response; 
    })
}