const header = document.querySelector('.header')
const list = document.querySelectorAll('.menu__item')
const logoIMG = document.querySelector('.logo_IMG')


window.addEventListener('scroll', ()=> {
    const offsetY = window.pageYOffset;
    if (offsetY > 0){
        header.classList.add('onScroll')
        list.forEach(item => {
            item.classList.add('color-black')   
        });
        logoIMG.src='/img/logo-dark.png'
        
    }else{
        header.classList.remove('onScroll')
        list.forEach(item => {
            item.classList.remove('color-black')   
        });
        logoIMG.src='/img/logo.png'

    }
})