const menuBurger = document.querySelector('.menuBurger')
const btnBurger = document.querySelector('.btnBurger')
const mobileContent = document.querySelector('.mobileContent')
const main = document.querySelector('main')
const footer = document.querySelector('footer')
const menu = document.getElementById('menu');   

menuBurger.onclick = () =>
{
    btnBurger.classList.toggle('close')
    mobileContent.classList.toggle('hide')
    main.classList.toggle('hide');
    footer.classList.toggle('hide');
}

// fixed
const scrollTop = 230;        
window.addEventListener('scroll', function (event) {
    let scrolled = window.pageYOffset || document.documentElement.scrollTop;
    if (scrolled > scrollTop) {
        menu.classList.add('menuFixed');
        menu.style.top = Math.min(-scrollTop + scrolled - 80, 0) + 'px';
       
    } else {
        menu.classList.remove('menuFixed');
        menu.style.top = 0 + 'px';
    }
});   