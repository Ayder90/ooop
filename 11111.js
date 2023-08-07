let first_text = document.querySelector('.first_text')
first_text.innerHTML = first_text.textContent.replace(/\S/g, '<span>$&</span>')
first_text.addEventListener('mouseover', function(event){
    if (event.target.tagName != 'SPAN') return
    event.target.classList.add('active')
})